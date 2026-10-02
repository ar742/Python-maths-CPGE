/* Interface et dessin uniquement. Les permutations et les recherches sont en Python. */
"use strict";
const $ = (selector) => document.querySelector(selector);
const esc = (value) => String(value).replace(/[&<>"']/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));
let boot, current, history = [], route = "cours", lessonIndex = 0;
let running = false, paused = false, animating = false, queue = [], queueIndex = 0, queueOrigin = "manual";
let solution = null, analysis = null, comparison = null, exerciseFilter = "Tous";
let yaw = -0.62, pitch = 0.48, transient = null, figureCount = 0;

async function api(data) {
  const response = await fetch("/api", {method:"POST", headers:{"Content-Type":"application/json", "X-Rubik-Token":boot.token}, body:JSON.stringify(data)});
  let result;
  try { result = await response.json(); } catch { throw new Error("Réponse illisible du programme Python. Vérifiez sa fenêtre de lancement."); }
  if (!response.ok) throw new Error(result.error || "Le calcul a échoué.");
  return result;
}

function notify(message, success = false) {
  const notice = $("#notice");
  notice.className = success ? "success" : "";
  notice.innerHTML = `<span>${esc(message)}</span><button aria-label="Fermer le message">✕</button>`;
  notice.hidden = false;
  notice.querySelector("button").onclick = () => notice.hidden = true;
}

function guarded(fn) {
  return async (...args) => { try { await fn(...args); } catch (error) { notify(error.message); } };
}

function save() {
  try { localStorage.setItem("rubik-groupes-v1", JSON.stringify({state:current.state, history, lessonIndex})); } catch { /* La navigation privée peut interdire le stockage. */ }
}

function project(vector, y = yaw, p = pitch) {
  const [x0, y0, z0] = vector;
  const x = Math.cos(y)*x0 + Math.sin(y)*z0;
  const z = -Math.sin(y)*x0 + Math.cos(y)*z0;
  return [x, Math.cos(p)*y0-Math.sin(p)*z, Math.sin(p)*y0+Math.cos(p)*z];
}

function rotateVector(vector, axis, angle) {
  const [x,y,z] = vector, c = Math.cos(angle), s = Math.sin(angle);
  if (axis === 0) return [x, c*y-s*z, s*y+c*z];
  if (axis === 1) return [c*x+s*z, y, -s*x+c*z];
  return [c*x-s*y, s*x+c*y, z];
}

function cubeMarkup(info, opts = {}) {
  const width = opts.width || 420, height = opts.height || 300;
  const scale = Math.min(width/6.2, height/5.25), cy = height/2-5, cx = width/2;
  const viewYaw = opts.yaw ?? yaw, viewPitch = opts.pitch ?? pitch;
  const labelled = opts.labels ?? $("#show-labels").checked;
  const changed = opts.changed ?? $("#show-changed").checked;
  const motion = opts.motion || null, marked = new Set(opts.marked || []);
  const toScreen = vector => {
    const [x,y,z] = project(vector, viewYaw, viewPitch);
    return [cx+x*scale, cy-y*scale, z];
  };
  const tiles = [];
  for (let i = 0; i < 54; i++) {
    let [position, normal] = boot.geometry[i];
    let center = position.map((v,j) => v + normal[j]*0.505);
    const axes = [0,1,2].filter(j => normal[j] === 0);
    let vertices = [[-1,-1],[1,-1],[1,1],[-1,1]].map(([a,b]) => center.map((v,j) => v+(j===axes[0]?a*0.459:0)+(j===axes[1]?b*0.459:0)));
    if (motion && position[motion.axis] === motion.layer) {
      center = rotateVector(center, motion.axis, motion.angle);
      vertices = vertices.map(v => rotateVector(v, motion.axis, motion.angle));
      normal = rotateVector(normal, motion.axis, motion.angle);
    }
    const cameraNormal = project(normal, viewYaw, viewPitch);
    if (cameraNormal[2] <= 0.005) continue;
    const screen = toScreen(center), polygon = vertices.map(v => toScreen(v).slice(0,2).map(n=>n.toFixed(2)).join(",")).join(" ");
    const identity = info.state[i], homeFace = boot.faces[Math.floor(identity/9)];
    const isChanged = identity !== i;
    const highlighted = marked.has(i) || changed && isChanged;
    const label = labelled ? `${homeFace}${identity%9+1}` : i%9 === 4 ? boot.faces[Math.floor(i/9)] : "";
    const font = labelled ? scale*0.21 : scale*0.28;
    const outline = highlighted ? "#bd9335" : "#203744";
    const fill = boot.colors[homeFace];
    const ink = "#143340";
    const html = `<g><polygon points="${polygon}" fill="${fill}" stroke="${outline}" stroke-width="${highlighted?2.7:1.6}" stroke-linejoin="round"/>${label ? `<text x="${screen[0].toFixed(2)}" y="${(screen[1]+font*.34).toFixed(2)}" font-family="Segoe UI,Arial,sans-serif" font-size="${font.toFixed(2)}" font-weight="600" text-anchor="middle" fill="${ink}">${label}</text>`:""}</g>`;
    tiles.push({depth:screen[2], html});
  }
  tiles.sort((a,b)=>a.depth-b.depth);
  // Silhouette noire du cube, y compris les espaces entre les stickers.
  const corners = [];
  for (const x of [-1.51,1.51]) for (const y of [-1.51,1.51]) for (const z of [-1.51,1.51]) corners.push(toScreen([x,y,z]));
  const points = corners.map(v => [v[0],v[1]]).sort((a,b)=>a[0]-b[0] || a[1]-b[1]);
  const cross = (o,a,b) => (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0]);
  const lower=[], upper=[];
  for (const pt of points) { while(lower.length>=2 && cross(lower.at(-2),lower.at(-1),pt)<=0) lower.pop(); lower.push(pt); }
  for (const pt of [...points].reverse()) { while(upper.length>=2 && cross(upper.at(-2),upper.at(-1),pt)<=0) upper.pop(); upper.push(pt); }
  const hull = lower.slice(0,-1).concat(upper.slice(0,-1)).map(v=>v.map(n=>n.toFixed(2)).join(",")).join(" ");
  return `<ellipse cx="${cx}" cy="${height*.89}" rx="${scale*1.7}" ry="${scale*.17}" fill="#dbe5de" opacity=".75"/><polygon points="${hull}" fill="#203744" stroke="#203744" stroke-width="2"/>${tiles.map(t=>t.html).join("")}`;
}

function drawCube() { $("#cube-svg").innerHTML = cubeMarkup(current, {motion:transient}); }

function netMarkup(info, marked = []) {
  const positions = {U:[1,0], L:[0,1], F:[1,1], R:[2,1], B:[3,1], D:[1,2]}, highlights = new Set(marked);
  const tile=25, gap=15, baseX=30, baseY=22;
  let html = "";
  for(let f=0;f<6;f++) {
    const face=boot.faces[f], [gx,gy]=positions[face], x=baseX+gx*(tile*3+gap), y=baseY+gy*(tile*3+gap);
    for(let r=0;r<3;r++) for(let c=0;c<3;c++) {
      const i=f*9+r*3+c, id=info.state[i], color=boot.colors[boot.faces[Math.floor(id/9)]], altered=$("#show-changed").checked && id!==i || highlights.has(i);
      html += `<rect x="${x+c*tile}" y="${y+r*tile}" width="${tile-2}" height="${tile-2}" rx="2" fill="${color}" stroke="${altered?'#bd9335':'#344c58'}" stroke-width="${altered?2:0.9}"/>`;
      if($("#show-labels").checked || r===1 && c===1) {
        const label=r===1 && c===1 ? face : `${boot.faces[Math.floor(id/9)]}${id%9+1}`;
        html+=`<text x="${x+c*tile+11.5}" y="${y+r*tile+15}" font-family="Segoe UI,Arial,sans-serif" font-size="${label.length===1?11:8}" text-anchor="middle" fill="#183040" font-weight="600">${label}</text>`;
      }
    }
  }
  html += '<text x="309" y="284" font-family="Segoe UI,Arial,sans-serif" font-size="10" fill="#76877f">U : haut · F : devant</text><text x="309" y="298" font-family="Segoe UI,Arial,sans-serif" font-size="10" fill="#76877f">R : droite · B : derrière</text>';
  return html;
}

function updateState() {
  drawCube(); $("#net-svg").innerHTML=netMarkup(current);
  $("#state-badge").textContent=current.solved?"Résolu":"Mélangé";
  $("#state-badge").classList.toggle("mixed",!current.solved);
  $("#correct-corners").textContent=`${8-current.corners_changed}/8`;
  $("#correct-edges").textContent=`${12-current.edges_changed}/12`;
  $("#in-h").textContent=current.in_h?"Oui":"Non";
  const rows=(names, perm, orientations)=>names.map((name,i)=>`<tr><td>${name}</td><td>${names[perm[i]]}</td><td>${orientations[i]}</td></tr>`).join("");
  $("#state-details").innerHTML=`<p><b>Coins :</b> ${esc(current.corner_cycle_text)}</p><p><b>Arêtes :</b> ${esc(current.edge_cycle_text)}</p><p>Ces cycles décrivent les positions. L'ordre complet de la transformation depuis le cube résolu vaut <b>${current.order}</b>.</p><div class="invariants">Σ co mod 3 = ${current.corner_sum} · Σ eo mod 2 = ${current.edge_sum}<br>Parité coins : ${current.corner_parity?'impaire':'paire'} · arêtes : ${current.edge_parity?'impaire':'paire'}</div><table class="piece-table"><thead><tr><th>Place de coin</th><th>Pièce présente</th><th>Twist co</th></tr></thead><tbody>${rows(boot.corners,current.cp,current.co)}</tbody></table><table class="piece-table"><thead><tr><th>Place d'arête</th><th>Pièce présente</th><th>Flip eo</th></tr></thead><tbody>${rows(boot.edges,current.ep,current.eo)}</tbody></table>`;
  $("#history-text").textContent=history===null?"Historique inconnu · recherche à partir de l'état requise.":history.join(" ") || "e (aucun mouvement)";
  $("#export-state").value=current.facelets.match(/.{9}/g).join("\n");
  updateLocks(); save(); updateSolution();
}

function updateLocks() {
  document.querySelectorAll("#moves button,#play-sequence,#reset-cube,#undo,[data-mutation]").forEach(b=>b.disabled=running);
  $("#undo").disabled=running || history===null || history.length===0;
  $("#pause").disabled=!(running && (queue.length>queueIndex || paused || animating));
  $("#pause").textContent=paused?"Reprendre":"Pause";
  const historyButton=$("#solve-history"); if(historyButton) historyButton.disabled=running || history===null;
  const completeButton=$("#solve-complete"); if(completeButton) completeButton.disabled=running || !boot.complete_solver;
  document.querySelectorAll("#solution-play,#solution-step").forEach(b=>b.disabled=running || !solution || solution.cursor>=solution.moves.length);
}

async function animate(token) {
  const settings={U:[1,1],R:[0,1],F:[2,1],D:[1,-1],L:[0,-1],B:[2,-1]};
  const [axis,layer]=settings[token[0]];
  const turns=token.endsWith("2")?2:token.endsWith("'")?-1:1;
  const duration=token.endsWith("2")?460:350, total=-layer*turns*Math.PI/2;
  animating=true;
  await new Promise(resolve=>{
    const start=performance.now();
    function frame(now) {
      const t=Math.min((now-start)/duration,1), eased=t*t*(3-2*t);
      transient={axis,layer,angle:total*eased}; drawCube();
      if(t<1) requestAnimationFrame(frame); else resolve();
    }
    requestAnimationFrame(frame);
  });
  transient=null; animating=false;
}

async function nextGesture() {
  if(paused || animating) return;
  if(queueIndex>=queue.length) {
    running=false; queue=[]; updateLocks();
    $("#playback-status").textContent=current.solved?"Cube résolu. Les trois invariants sont respectés.":"Séquence terminée.";
    return;
  }
  const step=queue[queueIndex];
  $("#playback-status").textContent=`${step.token} · geste ${queueIndex+1} / ${queue.length}`;
  await animate(step.token);
  current=step.info;
  if(queueOrigin==="undo") history.pop();
  else if(history!==null) {
    history.push(step.token);
    if(history.length>1000) { history=null; notify("L'historique a atteint 1 000 gestes. Le cube reste utilisable par recherche à partir de son état."); }
  }
  if(queueOrigin==="solution" && solution) solution.cursor++;
  queueIndex++; updateState();
  if(paused) { $("#playback-status").textContent=`Pause · ${queueIndex} / ${queue.length} gestes effectués.`; return; }
  // Laisser le navigateur afficher la nouvelle configuration avant le geste suivant.
  setTimeout(()=>guarded(nextGesture)(),90);
}

async function play(sequence, origin="manual") {
  if(running) return;
  // Un cube résolu reconstitue une origine connue même après un import ou
  // une résolution sans historique ; les gestes suivants sont enregistrables.
  if(history===null && current.solved) history=[];
  running=true; paused=false; updateLocks();
  try {
    const timeline=await api({action:"timeline",state:current.state,sequence});
    if(origin!=="solution") { solution=null; updateSolution(); }
    queue=timeline.steps; queueIndex=0; queueOrigin=origin; updateLocks();
    if(!queue.length) { running=false; updateLocks(); $("#playback-status").textContent="Mot vide : transformation identité."; return; }
    await nextGesture();
  } catch(error) { running=false; updateLocks(); throw error; }
}

function drawChapters() {
  $("#lesson-list").innerHTML=boot.lessons.map((l,i)=>`<button class="chapter ${i===lessonIndex && route==='cours'?'active':''}" data-lesson="${i}"><span class="number">${String(i+1).padStart(2,'0')}</span><span>${esc(l.title)}<small>${esc(l.level)}</small></span></button>`).join("");
  document.querySelectorAll("[data-lesson]").forEach(b=>b.onclick=()=>{lessonIndex=Number(b.dataset.lesson);setRoute("cours");save();});
}

function setRoute(next) {
  route=next;
  document.querySelectorAll("[data-route]").forEach(b=>b.classList.toggle("active",b.dataset.route===route));
  drawChapters();
  if(route==="cours") renderLesson();
  else if(route==="labo") renderLab();
  else if(route==="resolution") renderResolution();
  else renderExercises();
  updateLocks();
}

function renderLesson() {
  const lesson=boot.lessons[lessonIndex];
  $("#content").innerHTML=`<article class="lesson card"><span class="pill">${esc(lesson.level)}</span><h2>${esc(lesson.title)}</h2><p class="subtitle">${esc(lesson.subtitle)}</p><div class="formula">${esc(lesson.formula)}</div><div class="lesson-body">${lesson.html}</div><div class="demo-box"><p class="eyebrow">L'EXPÉRIENCE À FAIRE</p><p class="tiny">Départ : cube résolu. La séquence sera animée.</p><code>${esc(lesson.demo)}</code><button id="lesson-demo" data-mutation>${esc(lesson.demo_label)} →</button><button id="lesson-lab" class="text-button">Analyser cette manœuvre au laboratoire</button></div><div class="lesson-nav"><button id="prev-lesson" ${lessonIndex===0?'disabled':''}>← Précédent</button><button id="next-lesson" ${lessonIndex===boot.lessons.length-1?'disabled':''}>Suivant →</button></div></article>`;
  $("#lesson-demo").onclick=guarded(async()=>{if(running)return;current=boot.identity;history=[];solution=null;updateState();$("#sequence").value=lesson.demo;await play(lesson.demo);});
  $("#lesson-lab").onclick=guarded(async()=>{setRoute("labo");$("#lab-sequence").value=lesson.demo;await analyseSequence();});
  $("#prev-lesson").onclick=()=>{lessonIndex--;setRoute("cours");save();};
  $("#next-lesson").onclick=()=>{lessonIndex++;setRoute("cours");save();};
}

function cycleFigure(cycles, labels, title) {
  if(!cycles.length) return `<div class="alert-inline">${esc(title)} : toutes les positions sont fixes. Vérifiez aussi les orientations.</div>`;
  const width=360, rowHeight=106, height=cycles.length*rowHeight+26, marker=`arrow-${++figureCount}`;
  let html=`<svg viewBox="0 0 ${width} ${height}" role="img" aria-label="${esc(title)}"><defs><marker id="${marker}" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><path d="M0 0 L6 3 L0 6 Z" fill="#3b806b"/></marker></defs><text x="15" y="20" font-size="11" font-family="Segoe UI,Arial,sans-serif" fill="#61756b">${esc(title)}</text>`;
  cycles.forEach((cycle,row)=>{
    const startY=row*rowHeight+44, xStep=(width-50)/Math.max(cycle.length,3);
    const positions=cycle.map((_,i)=>[25+xStep*(i+.5),startY+26]);
    for(let i=0;i<positions.length;i++) {
      const [x,y]=positions[i], [nx,ny]=positions[(i+1)%positions.length];
      if(i<positions.length-1) html+=`<path d="M${x+17} ${y} L${nx-19} ${ny}" stroke="#3b806b" fill="none" stroke-width="1.4" marker-end="url(#${marker})"/>`;
      else html+=`<path d="M${x} ${y+18} C${x} ${y+53}, ${nx} ${ny+53}, ${nx} ${ny+18}" stroke="#3b806b" fill="none" stroke-width="1.4" marker-end="url(#${marker})"/>`;
      html+=`<circle cx="${x}" cy="${y}" r="17" fill="#e4eee7" stroke="#9fc1ad"/><text x="${x}" y="${y+4}" font-size="10" font-weight="500" text-anchor="middle" fill="#205a48" font-family="Segoe UI,Arial,sans-serif">${esc(labels[cycle[i]])}</text>`;
    }
  });
  return `<div class="cycle-figure">${html}</svg></div>`;
}

function analysisMarkup(result) {
  return `<div class="metric-row"><div><strong>${result.order}</strong><span>ordre complet</span></div><div><strong>${result.corners_changed}</strong><span>coins affectés</span></div><div><strong>${result.edges_changed}</strong><span>arêtes affectées</span></div></div><p><b>Inverse :</b> <code>${esc(result.inverse||'e')}</code></p><p><b>Réduction locale :</b> <code>${esc(result.reduced||'e')}</code></p>${cycleFigure(result.corner_cycles,boot.corners,'Cycles des coins · positions')}${cycleFigure(result.edge_cycles,boot.edges,'Cycles des arêtes · positions')}<p class="tiny">Les orientations ne figurent pas dans ces deux diagrammes. L'ordre complet est calculé sur toutes les facettes.</p><details><summary>Cycles des facettes (calcul exact de l'ordre)</summary><p>${esc(result.sticker_cycles)}</p></details><div class="button-row"><button id="analysis-demo" data-mutation>Jouer depuis le cube résolu</button></div>`;
}

async function analyseSequence() {
  analysis=await api({action:"analyse",sequence:$("#lab-sequence").value});
  $("#analysis-result").innerHTML=analysisMarkup(analysis);
  $("#analysis-demo").onclick=guarded(async()=>{if(running)return;current=boot.identity;history=[];solution=null;updateState();await play(analysis.sequence);});
  updateLocks();
}

function renderLab() {
  $("#content").innerHTML=`<section class="section-card card"><p class="eyebrow">LABORATOIRE · 01</p><h2>Lire une transformation</h2><p class="subtitle">Son inverse, ses cycles, son ordre exact.</p><label class="field" for="presets">Une manœuvre à explorer</label><select id="presets" class="wide"><option value="">Séquence personnalisée</option>${boot.presets.map(p=>`<option value="${esc(p.sequence)}">${esc(p.name)}</option>`).join('')}</select><label class="field" for="lab-sequence">Mot dans les générateurs du cube</label><input class="wide" id="lab-sequence" value="${esc(analysis?.sequence||"R U R' U'")}" spellcheck="false"><div class="button-row"><button class="primary" id="analyse">Calculer l'effet</button></div><div id="analysis-result" class="result"></div></section><section class="section-card card"><p class="eyebrow">LABORATOIRE · 02</p><h2>Comparer et construire</h2><p class="subtitle">AB et BA, le commutateur et la conjugaison.</p><label class="field" for="factor-a">A · premier facteur / réglage</label><input class="wide" id="factor-a" value="R" spellcheck="false"><label class="field" for="factor-b">B · second facteur / manœuvre</label><input class="wide" id="factor-b" value="U" spellcheck="false"><div class="button-row"><button class="primary" id="compare">Comparer AB et BA</button><button id="three-corners-preset">Exemple : trois coins</button></div><div id="comparison-result" class="result"></div></section>`;
  $("#analyse").onclick=guarded(analyseSequence);
  $("#presets").onchange=guarded(async(e)=>{if(e.target.value){$("#lab-sequence").value=e.target.value;await analyseSequence();}});
  $("#compare").onclick=guarded(compareFactors);
  $("#three-corners-preset").onclick=guarded(async()=>{$("#factor-a").value="R U R'";$("#factor-b").value="D";await compareFactors();});
  if(analysis) { $("#analysis-result").innerHTML=analysisMarkup(analysis);$("#analysis-demo").onclick=guarded(async()=>{if(running)return;current=boot.identity;history=[];solution=null;updateState();await play(analysis.sequence);}); }
}

async function compareFactors() {
  comparison=await api({action:"compare",a:$("#factor-a").value,b:$("#factor-b").value});
  const result=comparison;
  $("#comparison-result").innerHTML=`<div class="result-equation">${result.commute?'AB = BA · ces deux éléments commutent.':`AB ≠ BA · ${result.difference.length} facettes diffèrent.`}</div><div class="compare-grid"><div><p>AB</p><svg viewBox="0 0 210 165" role="img" aria-label="Résultat AB">${cubeMarkup(result.ab,{width:210,height:165,yaw:-.62,pitch:.48,labels:false,changed:false,marked:result.difference})}</svg></div><div><p>BA</p><svg viewBox="0 0 210 165" role="img" aria-label="Résultat BA">${cubeMarkup(result.ba,{width:210,height:165,yaw:-.62,pitch:.48,labels:false,changed:false,marked:result.difference})}</svg></div></div><p class="tiny">Les contours dorés marquent les positions différentes. Certaines peuvent se trouver sur les faces cachées.</p><h3>[A, B] = A B A⁻¹ B⁻¹</h3><p><code>${esc(result.commutator_sequence||'e')}</code></p><p>${result.commutator.corners_changed} coins et ${result.commutator.edges_changed} arêtes affectés · ordre ${result.commutator.order}.</p>${cycleFigure(result.commutator.corner_cycles,boot.corners,'Commutateur · cycles des coins')}<div class="button-row"><button id="play-commutator" data-mutation>Jouer le commutateur</button></div><h3>A B A⁻¹ · le conjugué de B</h3><p><code>${esc(result.conjugate_sequence||'e')}</code></p><p>Ordre ${result.conjugate.order} · ${result.conjugate.corners_changed} coins et ${result.conjugate.edges_changed} arêtes affectés.</p><div class="button-row"><button id="play-conjugate" data-mutation>Jouer le conjugué</button></div>`;
  const demo=async(sequence)=>{if(running)return;current=boot.identity;history=[];solution=null;updateState();await play(sequence);};
  $("#play-commutator").onclick=guarded(()=>demo(result.commutator_sequence));
  $("#play-conjugate").onclick=guarded(()=>demo(result.conjugate_sequence));
  updateLocks();
}

function renderResolution() {
  $("#content").innerHTML=`<section class="section-card card"><p class="eyebrow">RÉSOLUTION · EXPÉRIMENTER</p><h2>Du mélange au mot solution</h2><p class="subtitle">Trois méthodes, avec leurs hypothèses explicites.</p><div class="button-row"><button id="mix-short" data-mutation>Mélange court · 4 gestes</button><button id="mix-long" data-mutation>Mélange · 20 gestes</button><button id="challenge" data-mutation>Défi : trois coins</button></div><p class="tiny">Un mélange repart du cube résolu. Le défi crée l'inverse du commutateur de trois coins ; utilisez ensuite la manœuvre de la leçon 5 pour le corriger.</p><div class="button-row"><button id="forget-history" data-mutation>Oublier l'historique</button></div><h3>1 · L'inverse de l'historique</h3><p class="tiny">Toujours disponible pour un mélange dont tous les gestes sont connus. La réduction est locale, sans garantie de minimalité.</p><button id="solve-history" data-mutation>Construire l'inverse</button><h3>2 · Chercher sans l'historique</h3><p class="tiny">Recherche en largeur bidirectionnelle depuis l'état. Solution minimale en HTM si elle est trouvée ; borne maximale : six gestes.</p><label class="field" for="search-depth">Borne de recherche</label><select id="search-depth"><option value="4">4 HTM</option><option value="5">5 HTM</option><option value="6" selected>6 HTM</option></select><div class="button-row"><button id="solve-short" class="primary" data-mutation>Chercher une solution courte</button></div><h3>3 · Solveur général optionnel</h3><p class="tiny">${boot.complete_solver?'Module kociemba détecté. Les solutions sont vérifiées par le moteur local.':'Pour les états généraux sans historique : installer le module optionnel kociemba. Les instructions figurent dans LISEZ_MOI.md.'}</p><button id="solve-complete" data-mutation>Résoudre par deux phases</button><div id="solution-result" class="result"></div></section><section class="section-card card"><p class="eyebrow">RÉSOLUTION · IMPORTER</p><h2>Tester une configuration</h2><p class="subtitle">54 lettres, par faces U, R, F, D, L, B, de gauche à droite et de haut en bas sur chaque face vue de l'extérieur.</p><label class="field" for="import-state">État en notation URFDLB</label><textarea id="import-state" rows="6" spellcheck="false">${boot.identity.facelets.match(/.{9}/g).join('\n')}</textarea><p class="tiny">Les lettres désignent les couleurs des centres correspondants, quelle que soit la marque du cube. Le patron à droite fournit le repère exact.</p><div class="button-row"><button id="import-button" data-mutation>Vérifier et importer</button><button id="use-current">Copier l'état courant ici</button></div><h3>Trois états impossibles</h3><div class="button-row"><button data-impossible="twist">Un coin tourné</button><button data-impossible="flip">Une arête retournée</button><button data-impossible="parity">Deux arêtes échangées</button></div><div id="impossible-result" class="result"></div></section>`;
  $("#mix-short").onclick=guarded(()=>mix(4));$("#mix-long").onclick=guarded(()=>mix(20));
  $("#challenge").onclick=guarded(async()=>{if(running)return;running=true;updateLocks();let result;try{result=await api({action:"analyse",sequence:"R U R' D R U' R' D'"});}finally{running=false;updateLocks();}current=boot.identity;history=[];solution=null;updateState();await play(result.inverse);});
  $("#forget-history").onclick=()=>{if(running)return;history=null;solution=null;updateState();notify("Historique oublié. Les recherches utiliseront uniquement la configuration du cube.",true);};
  $("#solve-history").onclick=guarded(()=>solve("history"));$("#solve-short").onclick=guarded(()=>solve("short"));$("#solve-complete").onclick=guarded(()=>solve("complete"));
  $("#import-button").onclick=guarded(async()=>{if(running)return;running=true;updateLocks();try{const imported=await api({action:"import",facelets:$("#import-state").value});current=imported;history=current.solved?[]:null;solution=null;updateState();notify("Configuration légale importée. Les pièces et les trois invariants ont été vérifiés.",true);}finally{running=false;updateLocks();}});
  $("#use-current").onclick=()=>$("#import-state").value=current.facelets.match(/.{9}/g).join("\n");
  document.querySelectorAll("[data-impossible]").forEach(b=>b.onclick=guarded(async()=>{const result=await api({action:"impossible",kind:b.dataset.impossible});$("#impossible-result").innerHTML=`<div class="alert-inline">${esc(result.reason)}<br><small>Exemple théorique uniquement : le cube courant est conservé.</small></div><p class="tiny">Σ co = ${result.preview.corner_sum} mod 3 · Σ eo = ${result.preview.edge_sum} mod 2 · parités : ${result.preview.corner_parity} / ${result.preview.edge_parity}</p>`;}));
  updateSolution();updateLocks();
}

async function mix(length) {
  if(running)return;
  // Le tirage des mots est aussi effectué côté Python dans l'analyse de l'API.
  running=true;updateLocks();let result;
  try{result=await api({action:"scramble",length});}finally{running=false;updateLocks();}
  current=boot.identity;history=[];solution=null;updateState();$("#sequence").value=result.sequence;
  await play(result.sequence);
}

async function solve(mode) {
  if(running)return;
  running=true;updateLocks();$("#playback-status").textContent="Recherche en cours dans le moteur Python…";
  try {
    const result=await api({action:"solve",state:current.state,mode,history:history?.join(" ")||"",depth:Number($("#search-depth").value)});
    solution={...result,cursor:0};updateSolution();
    $("#playback-status").textContent=result.moves.length?"Solution vérifiée. Jouez-la pas à pas ou en entier.":"Le cube est déjà résolu.";
  } finally {running=false;updateLocks();}
}

function updateSolution() {
  const target=$("#solution-result");if(!target)return;
  if(!solution){target.innerHTML="";return;}
  target.innerHTML=`<div class="result-equation">${esc(solution.method)}<br>${solution.moves.length} HTM · solution vérifiée${solution.optimal?' · longueur minimale':''}</div>${solution.visited?`<p class="tiny">${solution.visited.toLocaleString('fr-FR')} états visités · ${solution.seconds} s.</p>`:''}<div class="step-list">${solution.moves.map((token,i)=>`<span class="${i<solution.cursor?'done':i===solution.cursor?'current':''}">${esc(token)}</span>`).join('')||'<span>e</span>'}</div><p class="tiny">${solution.cursor} / ${solution.moves.length} gestes exécutés.</p><div class="button-row"><button id="solution-step" data-mutation>Geste suivant</button><button id="solution-play" class="primary" data-mutation>Jouer la suite</button></div>`;
  $("#solution-step").onclick=guarded(()=>play(solution.moves[solution.cursor]||"","solution"));
  $("#solution-play").onclick=guarded(()=>play(solution.moves.slice(solution.cursor).join(" "),"solution"));
  updateLocks();
}

function renderExercises() {
  const exercises=boot.exercises.filter(e=>exerciseFilter==='Tous' || e.level.startsWith(exerciseFilter));
  $("#content").innerHTML=`<section class="section-card card"><p class="eyebrow">S'ENTRAÎNER</p><h2>Du geste à la preuve</h2><p class="subtitle">Douze exercices progressifs. Essayez une démonstration avant d'ouvrir la correction.</p><div class="exercises-filter">${['Tous','Sup','Spé'].map(filter=>`<button data-filter="${filter}" class="${filter===exerciseFilter?'active':''}">${filter}</button>`).join('')}</div>${exercises.map((e,i)=>`<article class="exercise"><span class="pill">${esc(e.level)}</span><h3>${esc(e.title)}</h3><p>${esc(e.question)}</p><details><summary>Afficher la correction</summary><p>${esc(e.answer)}</p></details><button data-exercise="${i}" data-mutation>Illustrer sur le cube →</button></article>`).join('')}</section>`;
  document.querySelectorAll("[data-filter]").forEach(b=>b.onclick=()=>{exerciseFilter=b.dataset.filter;renderExercises();updateLocks();});
  document.querySelectorAll("[data-exercise]").forEach(b=>b.onclick=guarded(async()=>{if(running)return;current=boot.identity;history=[];solution=null;updateState();await play(exercises[Number(b.dataset.exercise)].demo);}));
  updateLocks();
}

async function initialize() {
  const response=await fetch("/api/bootstrap");
  if(!response.ok)throw new Error("Le programme Python local ne répond pas.");
  boot=await response.json();current=boot.identity;
  try {
    const saved=JSON.parse(localStorage.getItem("rubik-groupes-v1"));
    if(saved){current=await api({action:"apply",state:saved.state,sequence:""});history=Array.isArray(saved.history)?saved.history:null;lessonIndex=Math.max(0,Math.min(boot.lessons.length-1,Number(saved.lessonIndex)||0));}
  } catch { current=boot.identity;history=[]; }
  $("#moves").innerHTML=["","'","2"].map(suffix=>boot.faces.split("").map(face=>`<button data-move="${face+suffix}" title="${face+suffix}">${face+suffix}</button>`).join('')).join('');
  document.querySelectorAll("[data-move]").forEach(b=>b.onclick=guarded(()=>play(b.dataset.move)));
  document.querySelectorAll("[data-route]").forEach(b=>b.onclick=()=>setRoute(b.dataset.route));
  $("#play-sequence").onclick=guarded(()=>play($("#sequence").value));
  $("#sequence").onkeydown=e=>{if(e.key==='Enter')guarded(()=>play($("#sequence").value))();};
  $("#reset-cube").onclick=()=>{if(running)return;current=boot.identity;history=[];solution=null;updateState();$("#playback-status").textContent="Cube réinitialisé.";};
  $("#undo").onclick=guarded(()=>{if(running || !history?.length)return;const t=history.at(-1), inverse=t.endsWith('2')?t:t.endsWith("'")?t[0]:t+"'";return play(inverse,"undo");});
  $("#pause").onclick=guarded(async()=>{paused=!paused;updateLocks();if(!paused && !animating)await nextGesture();});
  $("#show-labels").onchange=updateState;$("#show-changed").onchange=updateState;
  $("#camera-reset").onclick=()=>{yaw=-.62;pitch=.48;drawCube();};
  $("#copy-state").onclick=guarded(async()=>{await navigator.clipboard.writeText(current.facelets);notify("État du cube copié (54 lettres URFDLB).",true);});
  $("#sources-content").innerHTML=boot.sources.map(s=>`<p><a href="${esc(s.url)}" target="_blank" rel="noopener noreferrer">${esc(s.title)} ↗</a><small>${esc(s.description)}</small></p>`).join('')+'<small>Les liens externes demandent une connexion. Le cours et le simulateur sont autonomes.</small>';
  $("#sources-btn").onclick=()=>$("#sources-dialog").showModal();$("#close-dialog").onclick=()=>$("#sources-dialog").close();
  let drag=null;
  $("#cube-stage").onpointerdown=e=>{drag=[e.clientX,e.clientY,yaw,pitch];$("#cube-stage").setPointerCapture(e.pointerId);};
  $("#cube-stage").onpointermove=e=>{if(!drag)return;yaw=drag[2]+(e.clientX-drag[0])*.009;pitch=Math.max(-1.35,Math.min(1.35,drag[3]+(e.clientY-drag[1])*.007));drawCube();};
  $("#cube-stage").onpointerup=()=>drag=null;$("#cube-stage").onpointercancel=()=>drag=null;
  setRoute('cours');updateState();
}

initialize().catch(error=>{$("#content").innerHTML=`<section class="section-card card"><h2>Connexion au programme Python</h2><p>${esc(error.message)}</p><p>Relancez le fichier Lancer_Rubik.cmd puis ouvrez l'adresse affichée.</p></section>`;});
