'use strict';
const $=id=>document.getElementById(id);
const palette={green:'#23745c',gold:'#c79432',rose:'#b66375',mint:'#8dc9ac',ink:'#17363d'};
const labs={"maxwell": {"title": "Des vitesses microscopiques à la pression", "source": "TP PRIORITAIRE · MAXWELL · EFFUSION", "intro": "Comparer vitesses moyennes, pression, fuite d’un gaz et échange entre deux compartiments thermostatés.", "controls": [["mode", "Expérience", [["vitesses", "Distribution des vitesses"], ["pression", "Pression cinétique"], ["effusion", "Fuite par un petit trou"], ["paroi", "Échanges par une paroi poreuse"]], "vitesses"], ["temperature", "Température T₁ (K)", 1, 3000, 1, 300], ["molar_mass", "Masse molaire M (g/mol)", 1, 200, 1, 28], ["log_density", "log₁₀ densité n (m⁻³)", 15, 28, 0.1, 25], ["volume_litre", "Volume V₁ (L)", 0.001, 100, 0.001, 1], ["hole_mm2", "Surface du trou S (mm²)", 1e-06, 10, 0.02, 0.01, "log"], ["time_ratio", "Temps t / τ", 0, 8, 0.05, 1], ["temperature2", "Température T₂ (K)", 1, 3000, 1, 600], ["volume2_litre", "Volume V₂ (L)", 0.001, 100, 0.001, 1], ["fraction_initial", "Fraction initiale N₁ / Ntotal", 0, 1, 0.01, 0.5]], "presets": [["Azote à 300 K", {"mode": "vitesses", "temperature": 300, "molar_mass": 28}], ["Pression et température", {"mode": "pression"}], ["Une constante de temps", {"mode": "effusion", "time_ratio": 1}], ["Paroi : températures inégales", {"mode": "paroi", "temperature": 300, "temperature2": 600, "fraction_initial": 0.5}]]}, "canonique": {"title": "Deux niveaux : populations et fluctuations", "source": "EXERCICE 2 · MICROCANONIQUE ET CANONIQUE", "intro": "Comparer microcanonique et canonique, puis relier température, énergie moyenne et fluctuations.", "controls": [["mode", "Spectre", [["deux", "Deux niveaux 0 et ε"], ["trois", "Trois niveaux dégénérés"]], "deux"], ["temperature", "Température T (K)", 1, 3000, 1, 300], ["epsilon_mev", "Écart ε entre niveaux (meV)", 0.1, 250, 0.1, 25], ["degeneracy", "Dégénérescence du niveau ε", 1, 30, 1, 4], ["particles", "Nombre de sites N", 1, 100000, 1, 100], ["fraction", "Fraction excitée (microcanonique)", 0, 1, 0.01, 0.25]], "presets": [["Deux niveaux", {"mode": "deux", "temperature": 300, "epsilon_mev": 25}], ["Entropie maximale", {"mode": "deux", "fraction": 0.5}], ["Trois niveaux", {"mode": "trois", "degeneracy": 4}]]}, "gaz": {"title": "Les niveaux d’un cube deviennent un gaz", "source": "PONT AVEC PQ · BOÎTE · LIMITE CLASSIQUE", "intro": "Sommer les niveaux de la boîte, contrôler la troncature et comparer à la partition classique.", "controls": [["temperature", "Température T (K)", 1, 3000, 1, 300], ["side_nm", "Côté du cube L (nm)", 0.2, 20, 0.1, 3], ["mass_ratio", "Masse m / mₑ", 0.1, 5, 0.1, 1], ["cutoff", "Nombre de niveaux 1D conservés", 4, 100, 1, 36], ["log_density", "log₁₀ densité n (m⁻³)", 15, 28, 0.1, 23]], "presets": [["Confinement quantique", {"temperature": 10, "side_nm": 1}], ["Limite classique", {"temperature": 1500, "side_nm": 10, "cutoff": 100}], ["Troncature à contrôler", {"temperature": 3000, "side_nm": 20, "cutoff": 4}]]}, "oscillateur": {"title": "Quantification et équipartition", "source": "PONT AVEC PQ · OSCILLATEUR THERMIQUE", "intro": "Comparer l’oscillateur quantique à son approximation classique, puis compter les termes quadratiques du recueil.", "controls": [["temperature", "Température T (K)", 0.5, 3000, 0.5, 300], ["frequency_thz", "Fréquence ν (THz)", 0.05, 50, 0.05, 5], ["confinement", "Termes quadratiques supplémentaires r", 0, 6, 1, 1]], "presets": [["État presque fondamental", {"temperature": 5}], ["Équipartition", {"temperature": 1500, "frequency_thz": 1}]]}, "spins": {"title": "Spins, saturation et loi de Curie", "source": "PARAMAGNÉTISME · DEUX NIVEAUX", "intro": "Suivre l’aimantation de spins indépendants et la compétition entre champ et agitation thermique.", "controls": [["temperature", "Température T (K)", 0.1, 500, 0.1, 5], ["field", "Champ magnétique B (T)", -10, 10, 0.1, 2], ["magnetic_moment", "Moment magnétique μ / μB", 0.01, 3, 0.01, 1]], "presets": [["Régime de Curie", {"temperature": 100, "field": 1}], ["Saturation", {"temperature": 0.2, "field": 8}], ["Champ nul", {"field": 0}]]}, "planck": {"title": "Le rayonnement échappe à la catastrophe", "source": "CORPS NOIR · PLANCK · WIEN", "intro": "Explorer le spectre par longueur d’onde, son maximum et sa limite classique de Rayleigh–Jeans.", "controls": [["temperature", "Température T (K)", 100, 10000, 10, 5800], ["wavelength_um", "Longueur d’onde choisie λ (µm)", 0.05, 200, 0.05, 0.5]], "presets": [["Température solaire", {"temperature": 5800, "wavelength_um": 0.5}], ["Objet à 300 K", {"temperature": 300, "wavelength_um": 10}], ["Corps chaud", {"temperature": 1500, "wavelength_um": 2}]]}, "occupations": {"title": "Bosons, fermions et limite diluée", "source": "TP · ÉNERGIE DE FERMI · CONDENSATION BOSE", "intro": "Passer des fonctions d’occupation à la densité fixée : gaz électronique, atomes bosoniques et limite diluée.", "controls": [["mode", "Gaz ou comparaison", [["fermi", "Gaz électronique : Fermi"], ["bose", "Gaz atomique : Bose"], ["comparaison", "Comparer FD, BE et MB"]], "fermi"], ["temperature", "T (K) · échelle logarithmique", 1e-08, 3000, 0.02, 300, "log"], ["log_density", "log₁₀ densité n (m⁻³)", 15, 30, 0.1, 28], ["mass_atom_u", "Masse atomique Bose (u)", 1, 250, 1, 87], ["mu_ratio", "Potentiel μ / (kBT) · comparaison", -8, -0.01, 0.01, -2], ["energy_ratio", "Énergie ε / (kBT) · comparaison", 0, 12, 0.05, 1]], "presets": [["Fermi électronique", {"mode": "fermi", "temperature": 300, "log_density": 28}], ["Bose : condensat", {"mode": "bose", "temperature": 1e-07, "log_density": 20, "mass_atom_u": 87}], ["Bose au-dessus de Tc", {"mode": "bose", "temperature": 1e-06, "log_density": 20, "mass_atom_u": 87}], ["Limite diluée", {"mode": "comparaison", "mu_ratio": -6, "temperature": 300}]]}, "ising": {"title": "De la chaîne d’Ising au réseau d’Onsager", "source": "EXERCICE 5 · ISING 1D · ONSAGER–YANG 2D", "intro": "Calculer la chaîne périodique exactement, puis observer des domaines magnétiques sur un réseau carré simulé.", "controls": [["mode", "Modèle", [["chaine", "Chaîne périodique : calcul exact"], ["carre", "Carré 2D : simulation et Onsager"]], "chaine"], ["theta", "Température réduite θ = kBT/J", 0.2, 8, 0.01, 2.3], ["N", "Nombre de spins de la chaîne", 3, 100, 1, 20], ["level", "Nombre de paires de parois n", 0, 10, 1, 1], ["size", "Côté du carré (nombre pair)", 8, 24, 2, 16], ["burnin", "Balayages de préparation", 50, 1000, 10, 200], ["sweeps", "Balayages après préparation", 300, 5000, 100, 1200], ["stride", "Espacement des mesures", 1, 20, 1, 5], ["initial", "État initial du carré", [["aleatoire", "Spins aléatoires"], ["plus", "Tous les spins +1"]], "aleatoire"], ["seed", "Graine aléatoire reproductible", 0, 9999999, 1, 742]], "presets": [["Chaîne froide", {"mode": "chaine", "theta": 0.5}], ["Près de Tc en 2D", {"mode": "carre", "theta": 2.269185314, "size": 16, "burnin": 500, "sweeps": 2000}], ["Domaines à bas T", {"mode": "carre", "theta": 1.5, "initial": "plus"}], ["Désordre thermique", {"mode": "carre", "theta": 4}]]}};
let current='maxwell',token,lessons=[],exercises=[],latest,serial=0,timer,lessonIndex=1;
const state = Object.fromEntries(Object.entries(labs).map(([id,l])=>[id,Object.fromEntries(l.controls.map(c=>[c[0],Array.isArray(c[2])?c[3]:c[5]]))]));
const fmt = v => v===null?'—':typeof v==='boolean'?(v?'Oui':'Non'):typeof v==='string'?v:Number.isInteger(v)?String(v):Math.abs(v)<.0001&&v!==0?v.toExponential(3):Number(v.toPrecision(6)).toLocaleString('fr-FR',{maximumFractionDigits:6});
function elem(tag,text,cls){const e=document.createElement(tag);if(text!==undefined)e.textContent=text;if(cls)e.className=cls;return e;}
function constrain(){
 if(current==='ising'){state.ising.level=Math.min(state.ising.level,Math.floor(state.ising.N/2));labs.ising.controls.find(c=>c[0]==='level')[3]=Math.floor(state.ising.N/2);}
 if(current==='boite'){const s=state.boite,min=s.boundary==='parois'?1:-4,max=s.boundary==='parois'?6:4;for(const key of ['nx','ny','nz']){s[key]=Math.max(min,Math.min(max,Math.round(s[key])));const c=labs.boite.controls.find(c=>c[0]===key);c[2]=min;c[3]=max;}}
}
function activeLesson(){if(current==='ising')return state.ising.mode==='carre'?15:14;if(current==='occupations')return {fermi:9,bose:10,comparaison:8}[state.occupations.mode];if(current==='maxwell')return {vitesses:5,pression:5,effusion:6,paroi:7}[state.maxwell.mode];if(current==='canonique')return 2;const i=lessons.findIndex(l=>l.lab===current);return Math.max(0,i);}
function syncTheory(){const index=activeLesson();$('theory-text').innerHTML=lessons[index].html;$('open-lesson').onclick=()=>showCourse(index);}
function irrelevant(key){
 const s=state[current];
 if(current==='canonique')return s.mode==='deux'?key==='degeneracy':['particles','fraction'].includes(key);
 if(current==='maxwell'){
  if(s.mode==='vitesses')return !['mode','temperature','molar_mass'].includes(key);
  if(s.mode==='pression')return !['mode','temperature','molar_mass','log_density'].includes(key);
  if(s.mode==='effusion')return ['temperature2','volume2_litre','fraction_initial'].includes(key);
 }
 if(current==='occupations')return s.mode==='comparaison'?['log_density','mass_atom_u'].includes(key):['mu_ratio','energy_ratio'].includes(key)||key==='mass_atom_u'&&s.mode==='fermi';
 if(current==='ising')return s.mode==='chaine'?['size','burnin','sweeps','stride','initial','seed'].includes(key):['N','level'].includes(key);
 return false;
}
function showLab(id,params={}){
 current=id;Object.assign(state[id],params);constrain();
 $('course').hidden=true;$('laboratory').hidden=false;
 document.querySelectorAll('#tabs button').forEach(b=>b.classList.toggle('active',b.dataset.lab===id));
 const lab=labs[id];$('lab-title').textContent=lab.title;$('lab-source').textContent=lab.source;$('lab-intro').textContent=lab.intro;
 $('presets').replaceChildren();
 for(const [name,p] of lab.presets){const b=elem('button',name);b.onclick=()=>showLab(id,p);$('presets').append(b);}
 renderControls();syncTheory();update();
}
function renderControls(){
 $('controls').replaceChildren();
 for(const c of labs[current].controls){
  const [key,label]=c, box=elem('div',undefined,'control'), l=elem('label',label), out=elem('output',fmt(state[current][key]));
  const input=elem(Array.isArray(c[2])?'select':'input');input.id='param-'+key;l.htmlFor=input.id;
  if(Array.isArray(c[2])){for(const [value,name]of c[2]){const o=elem('option',name);o.value=value;input.append(o);}input.value=state[current][key];}
  else{input.type='range';const logarithmic=c[6]==='log';input.min=logarithmic?Math.log10(c[2]):c[2];input.max=logarithmic?Math.log10(c[3]):c[3];input.step=c[4];input.value=logarithmic?Math.log10(state[current][key]):state[current][key];l.append(out);}
  input.disabled=irrelevant(key);
  input.oninput=()=>{state[current][key]=Array.isArray(c[2])?input.value:(c[6]==='log'?10**Number(input.value):Number(input.value));out.textContent=fmt(state[current][key]);constrain();
   if(['mode','boundary','gate','state','N'].includes(key)){renderControls();document.querySelectorAll('#controls input,#controls select').forEach(e=>e.disabled=irrelevant(e.id.replace('param-','')));syncTheory();}
   $('export').disabled=true;$('status').textContent='Calcul des nouveaux paramètres…';++serial;
   clearTimeout(timer);timer=setTimeout(update,140);
  };box.append(l,input);$('controls').append(box);
 }
}
async function update(){
 const id=++serial;const data={lab:current,...state[current]};
 $('status').textContent='Calcul de l’expérience…';$('export').disabled=true;
 try{
  const response=await fetch('/api',{method:'POST',headers:{'Content-Type':'application/json','X-Statistique-Token':token},body:JSON.stringify(data)});
  const result=await response.json();if(id!==serial)return;if(!response.ok)throw Error(result.error);
  latest=result;$('error').hidden=true;renderResult(result);$('status').textContent='Expérience calculée · unités et hypothèses précisées sous les graphiques';$('export').disabled=false;
 }catch(e){if(id!==serial)return;$('error').hidden=false;$('error').textContent=e.message;$('status').textContent='Vérifiez les paramètres avant de recommencer.';}
}
function renderResult(r){
 $('metrics').replaceChildren();for(const m of r.metrics){const e=elem('div',undefined,'metric');e.append(elem('span',m.label),elem('b',fmt(m.value)),elem('small',m.note));$('metrics').append(e);}
 $('plots').replaceChildren();renderCircuit(r);for(const data of r.charts){data.series=data.series||[];const f=elem('section',undefined,'figure');f.append(elem('h3',data.title));const canvas=elem('canvas');canvas.setAttribute('role','img');canvas.setAttribute('aria-label',data.title+' : '+[...new Set(data.series.map(s=>s.label))].join(', '));f.append(canvas);
  const legend=elem('div',undefined,'legend');const seen=new Set();for(const s of (data.sceneBloch?data.sceneBloch.vectors:data.series)){const label=s.label;if(seen.has(label))continue;seen.add(label);const item=elem('span');item.append(elem('i',undefined,s.color),document.createTextNode(label));legend.append(item);}f.append(legend);$('plots').append(f);canvas._data=data;
 }
 document.querySelectorAll('#plots canvas').forEach(c=>draw(c,c._data));
 $('details').replaceChildren();for(const note of r.notes)$('details').append(elem('p',note));
 const details=elem('details');details.append(elem('summary','Consulter les populations et les grandeurs physiques'));const table=elem('table'),head=elem('thead'),tr=elem('tr');for(const v of r.table.headers)tr.append(elem('th',v));head.append(tr);table.append(head);const body=elem('tbody');for(const row of r.table.rows){const line=elem('tr');for(const v of row)line.append(elem('td',fmt(v)));body.append(line);}table.append(body);details.append(table);$('details').append(details);
}
function draw(canvas,data){
 if(data.sceneBloch){drawBloch(canvas,data);return;}
 if(data.grid){drawGrid(canvas,data);return;}
 const width=canvas.clientWidth,height=canvas.clientHeight;if(!width)return;
 const dpr=window.devicePixelRatio||1;canvas.width=Math.round(width*dpr);canvas.height=Math.round(height*dpr);
 const ctx=canvas.getContext('2d');ctx.scale(dpr,dpr);const pad={l:68,r:20,t:20,b:48},w=width-pad.l-pad.r,h=height-pad.t-pad.b;
 const tx=x=>data.logx?Math.log10(Math.max(x,Number.MIN_VALUE)):x,ty=y=>data.logy?Math.log10(Math.max(y,Number.MIN_VALUE)):y;
 const xs=data.series.flatMap(s=>s.x.map(tx)),ys=data.series.flatMap(s=>s.y.map(ty));
 let xmin=Math.min(...xs),xmax=Math.max(...xs),ymin=Math.min(...ys),ymax=Math.max(...ys);
 const expand=(lo,hi)=>{const scale=Math.max(Math.abs(lo),Math.abs(hi));return hi-lo<=Number.EPSILON*16*(scale||1)?[lo-(scale||1)*.05,hi+(scale||1)*.05]:[lo,hi];};
 [xmin,xmax]=expand(xmin,xmax);[ymin,ymax]=expand(ymin,ymax);
 if(data.series.some(s=>['bars','stems'].includes(s.kind))){xmin-=.5;xmax+=.5;ymin=Math.min(0,ymin);}
 let dx=(xmax-xmin)*.04,dy=(ymax-ymin)*.08;xmin-=dx;xmax+=dx;ymin-=dy;ymax+=dy;
 if(/^Probabilité$|^P\(/.test(data.ylabel)){ymin=0;ymax=1;}
 if(data.equal){const units=Math.max((xmax-xmin)/w,(ymax-ymin)/h),cx=(xmin+xmax)/2,cy=(ymin+ymax)/2;xmin=cx-units*w/2;xmax=cx+units*w/2;ymin=cy-units*h/2;ymax=cy+units*h/2;}
 const X=x=>pad.l+(tx(x)-xmin)/(xmax-xmin)*w,Y=y=>pad.t+h-(ty(y)-ymin)/(ymax-ymin)*h;
 const tick=(v,log)=>log?'10^'+Number(v.toFixed(1)):Math.abs(v)>=1000||Math.abs(v)<.001&&v!==0?v.toExponential(1):v.toLocaleString('fr-FR',{maximumSignificantDigits:3});
 ctx.font='11px Segoe UI, sans-serif';ctx.fillStyle='#627477';ctx.textAlign='right';
 for(let i=0;i<=4;i++){const y=ymin+(ymax-ymin)*i/4,pos=pad.t+h-h*i/4;ctx.strokeStyle='#edf0e9';ctx.beginPath();ctx.moveTo(pad.l,pos);ctx.lineTo(pad.l+w,pos);ctx.stroke();ctx.fillText(tick(y,data.logy),pad.l-9,pos+4);}
 ctx.textAlign='center';for(let i=0;i<=4;i++){const x=xmin+(xmax-xmin)*i/4;ctx.fillText(tick(x,data.logx),pad.l+w*i/4,pad.t+h+18);}
 ctx.fillText(data.xlabel,pad.l+w/2,height-7);ctx.save();ctx.translate(14,pad.t+h/2);ctx.rotate(-Math.PI/2);ctx.fillText(data.ylabel,0,0);ctx.restore();
 ctx.save();ctx.beginPath();ctx.rect(pad.l,pad.t,w,h);ctx.clip();
 for(const s of data.series){ctx.strokeStyle=ctx.fillStyle=palette[s.color]||palette.green;ctx.lineWidth=s.color==='mint'?1:2;ctx.globalAlpha=s.color==='mint'?.7:1;
  if(s.kind==='bars'){const bw=Math.min(35,w/(s.x.length+2)*.6);s.x.forEach((x,i)=>{ctx.fillRect(X(x)-bw/2,Math.min(Y(0),Y(s.y[i])),bw,Math.abs(Y(s.y[i])-Y(0)));});}
  else if(s.kind==='stems'){s.x.forEach((x,i)=>{ctx.beginPath();ctx.moveTo(X(x),Y(0));ctx.lineTo(X(x),Y(s.y[i]));ctx.stroke();ctx.beginPath();ctx.arc(X(x),Y(s.y[i]),3,0,2*Math.PI);ctx.fill();});}
  else if(s.kind==='dots'){s.x.forEach((x,i)=>{ctx.beginPath();ctx.arc(X(x),Y(s.y[i]),4,0,2*Math.PI);ctx.fill();});}
  else{ctx.beginPath();s.x.forEach((x,i)=>{if(!i)ctx.moveTo(X(x),Y(s.y[i]));else{if(s.kind==='step')ctx.lineTo(X(x),Y(s.y[i-1]));ctx.lineTo(X(x),Y(s.y[i]));}});ctx.stroke();}
 }ctx.restore();
}
function showCourse(index=lessonIndex){++serial;lessonIndex=index;$('course').hidden=false;$('laboratory').hidden=true;$('status').textContent='Cours et exercices corrigés';document.querySelectorAll('#tabs button').forEach(b=>b.classList.toggle('active',b.dataset.lab==='course'));
 $('lesson-list').replaceChildren();lessons.forEach((l,i)=>{const b=elem('button',l.title,i===index?'active':'');b.onclick=()=>showCourse(i);$('lesson-list').append(b);});
 const l=lessons[index];$('lesson').innerHTML='';$('lesson').append(elem('span',l.level,'badge'),elem('h2',l.title));const content=elem('div');content.innerHTML=l.html;$('lesson').append(content);const b=elem('button','Ouvrir le laboratoire associé');b.onclick=()=>showLab(l.lab);$('lesson').append(b);
}
function prepareCourse(sources){
 $('exercises').replaceChildren();for(const e of exercises){const card=elem('div',undefined,'exercise');card.append(elem('span',e.level,'badge'),elem('h3',e.title),elem('p',e.question));const detail=elem('details');detail.append(elem('summary','Déplier la correction'),elem('p',e.answer));card.append(detail);const b=elem('button','Expérimenter');b.onclick=()=>{showLab(e.lab,e.params);$('tabs').scrollIntoView({behavior:'smooth',block:'start'});};card.append(b);$('exercises').append(card);}
 $('sources').replaceChildren();for(const text of sources){const p=elem('p');const parts=text.split(/(https?:\/\/[^\s<>]+)/g);for(const part of parts){if(/^https?:/.test(part)){const a=elem('a',part);a.href=part;a.target='_blank';a.rel='noopener';p.append(a);}else p.append(document.createTextNode(part));}$('sources').append(p);}
}
$('export').onclick=()=>{if(!latest)return;const a=elem('a');a.href='/api/export/'+latest.export_id;a.download=`statistique-${latest.lab}.json`;document.body.append(a);a.click();a.remove();};
let resizeTimer;window.addEventListener('resize',()=>{clearTimeout(resizeTimer);resizeTimer=setTimeout(()=>document.querySelectorAll('canvas').forEach(c=>draw(c,c._data)),100);});
(async()=>{try{const r=await fetch('/api/bootstrap');if(!r.ok)throw Error('Le serveur Python ne répond pas.');const bootstrap=await r.json();token=bootstrap.token;lessons=bootstrap.lessons;exercises=bootstrap.exercises;
 const names={"maxwell": "Maxwell & Effusion", "canonique": "Deux niveaux", "gaz": "Gaz dans un cube", "oscillateur": "Oscillateur thermique", "spins": "Spins & Curie", "planck": "Corps noir", "occupations": "Fermi & Bose", "ising": "Ising & Onsager", "course": "Cours & exercices"};
 for(const [id,name]of Object.entries(names)){const b=elem('button',name);b.dataset.lab=id;b.onclick=()=>id==='course'?showCourse():showLab(id);$('tabs').append(b);}prepareCourse(bootstrap.sources);showLab('maxwell');
}catch(e){$('error').hidden=false;$('error').textContent=e.message;$('status').textContent='Lancez le programme Python pour ouvrir l’atelier.';}})();


function drawBloch(canvas,data){
 const width=canvas.clientWidth,height=canvas.clientHeight;if(!width)return;const dpr=window.devicePixelRatio||1;canvas.width=Math.round(width*dpr);canvas.height=Math.round(height*dpr);const c=canvas.getContext('2d');c.scale(dpr,dpr);
 const view=canvas._rotate||(canvas._rotate={yaw:.55,pitch:.25}),scene=data.sceneBloch,scale=Math.min(width*.34,height*.37),cx=width/2,cy=height/2+2;
 const project=p=>{const x=p[0]*Math.cos(view.yaw)+p[1]*Math.sin(view.yaw),y=-p[0]*Math.sin(view.yaw)+p[1]*Math.cos(view.yaw);return [cx+scale*x,cy-scale*(p[2]*Math.cos(view.pitch)-y*Math.sin(view.pitch))];};
 c.strokeStyle='#dedfd4';c.fillStyle='#f8faf5';c.beginPath();c.arc(cx,cy,scale,0,2*Math.PI);c.fill();c.stroke();
 for(const path of scene.paths||[]){c.strokeStyle=palette[path.color]||palette.mint;c.lineWidth=path.color==='mint'?.9:2;c.beginPath();path.points.forEach((p,i)=>{const [x,y]=project(p);if(!i)c.moveTo(x,y);else c.lineTo(x,y);});c.stroke();}
 c.font='12px Segoe UI, sans-serif';for(const [j,label]of [[0,'x'],[1,'y'],[2,'z · |0⟩']]){const p=[0,0,0];p[j]=1.12;const [x,y]=project(p);c.strokeStyle='#9caaa7';c.setLineDash([3,3]);c.beginPath();c.moveTo(cx,cy);c.lineTo(x,y);c.stroke();c.setLineDash([]);c.fillStyle='#627477';c.fillText(label,x+4,y-4);}
 for(const v of scene.vectors||[]){const [x,y]=project(v.point),dx=x-cx,dy=y-cy,ang=Math.atan2(dy,dx);c.strokeStyle=c.fillStyle=palette[v.color]||palette.green;c.lineWidth=2.5;c.beginPath();c.moveTo(cx,cy);c.lineTo(x,y);c.stroke();c.beginPath();c.arc(x,y,4,0,2*Math.PI);c.fill();if(Math.hypot(dx,dy)>10){c.beginPath();c.moveTo(x,y);c.lineTo(x-10*Math.cos(ang-.35),y-10*Math.sin(ang-.35));c.lineTo(x-10*Math.cos(ang+.35),y-10*Math.sin(ang+.35));c.closePath();c.fill();}}
 c.fillStyle='#627477';c.font='11px Segoe UI, sans-serif';c.textAlign='center';c.fillText('Glisser pour faire tourner la vue · z = +1 : |0⟩ ; z = −1 : |1⟩',cx,height-12);
 if(!canvas._dragReady){canvas._dragReady=true;let drag;canvas.onpointerdown=e=>{drag=[e.clientX,e.clientY];canvas.setPointerCapture(e.pointerId);};canvas.onpointermove=e=>{if(!drag)return;view.yaw+=(e.clientX-drag[0])*.012;view.pitch=Math.max(-1.4,Math.min(1.4,view.pitch+(e.clientY-drag[1])*.012));drag=[e.clientX,e.clientY];drawBloch(canvas,data);};canvas.onpointerup=canvas.onpointercancel=()=>{drag=null;};}
}
function drawGrid(canvas,data){
 const width=canvas.clientWidth,height=canvas.clientHeight;if(!width)return;const dpr=window.devicePixelRatio||1;canvas.width=Math.round(width*dpr);canvas.height=Math.round(height*dpr);const c=canvas.getContext('2d');c.scale(dpr,dpr);
 const {x,y,z}=data.grid,p={l:62,r:18,t:18,b:49};let w=width-p.l-p.r,h=height-p.t-p.b;if(data.equal){const size=Math.min(w,h);p.l+=(w-size)/2;w=h=size;}const vals=z.flat(),lo=data.grid.vmin??Math.min(...vals),hi=data.grid.vmax??Math.max(...vals),nx=x.length,ny=y.length;
 // Chaque cellule représente un échantillon de la densité, avec axe y croissant vers le haut.
 for(let j=0;j<ny;j++)for(let i=0;i<nx;i++){const u=(z[j][i]-lo)/(hi-lo||1);c.fillStyle=`rgb(${Math.round(245-212*u)},${Math.round(246-130*u)},${Math.round(238-146*u)})`;c.fillRect(p.l+i*w/nx,p.t+(ny-j-1)*h/ny,w/nx+.5,h/ny+.5);}
 c.font='11px Segoe UI, sans-serif';c.fillStyle='#627477';for(let i=0;i<=4;i++){c.textAlign='center';c.fillText(fmt(x[0]+(x[nx-1]-x[0])*i/4),p.l+w*i/4,p.t+h+19);c.textAlign='right';c.fillText(fmt(y[0]+(y[ny-1]-y[0])*i/4),p.l-7,p.t+h-h*i/4+4);}
 c.textAlign='center';c.fillText(data.xlabel,p.l+w/2,height-7);c.save();c.translate(13,p.t+h/2);c.rotate(-Math.PI/2);c.fillText(data.ylabel,0,0);c.restore();
 c.fillStyle='#17363d';c.textAlign='right';c.fillText('Clair : '+fmt(lo)+' · vert : '+fmt(hi),width-18,12);
}
function renderCircuit(r){
 const box=$('circuit');box.hidden=r.lab!=='circuits';if(box.hidden)return;
 const bell=state.circuits.mode==='bell',n=state.circuits.iterations;
 const gate=(x,y,label)=>`<rect x="${x-22}" y="${y-18}" width="44" height="36" rx="5" fill="#edf4ec" stroke="#23745c"/><text x="${x}" y="${y+5}" text-anchor="middle" font-size="15" fill="#17363d">${label}</text>`;
 let svg='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 115" role="img" aria-label="Circuit quantique à deux qubits"><g font-family="Segoe UI, sans-serif"><path d="M65 35H650M65 85H650" stroke="#627477"/><text x="5" y="40" fill="#17363d">q₀ |0⟩</text><text x="5" y="90" fill="#17363d">q₁ |0⟩</text>';
 if(bell){svg+=gate(150,35,'H')+'<path d="M320 35V85" stroke="#17363d" stroke-width="2"/><circle cx="320" cy="35" r="5" fill="#17363d"/><circle cx="320" cy="85" r="15" fill="white" stroke="#17363d" stroke-width="2"/><path d="M308 85H332M320 73V97" stroke="#17363d"/><text x="440" y="58" font-size="16" fill="#23745c">(|00⟩ + |11⟩) / √2</text>';}
 else{svg+=gate(115,35,'H')+gate(115,85,'H');for(let i=0;i<n;i++){const x=190+110*i;svg+=`<rect x="${x-23}" y="16" width="46" height="89" rx="5" fill="#fff8e8" stroke="#c79432"/><text x="${x}" y="66" text-anchor="middle" fill="#17363d">O</text><rect x="${x+28}" y="16" width="46" height="89" rx="5" fill="#edf4ec" stroke="#23745c"/><text x="${x+51}" y="66" text-anchor="middle" fill="#17363d">D</text>`;}}
 svg+='</g></svg>';box.innerHTML=svg;box.append(elem('p',bell?'H sur q₀, puis CNOT avec q₀ comme contrôle et q₁ comme cible. Ordre des bases : |q₀q₁⟩.':'Préparation uniforme, oracle O qui inverse le signe de la cible, puis diffusion D = 2|s⟩⟨s| − I. Chaque paire O, D compte pour une itération.'));
}
