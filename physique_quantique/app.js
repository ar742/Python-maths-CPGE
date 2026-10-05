'use strict';
const $=id=>document.getElementById(id);
const palette={green:'#23745c',gold:'#c79432',rose:'#b66375',mint:'#8dc9ac',ink:'#17363d'};
const labs={"boite": {"title": "Une particule dans un volume cubique", "source": "TP · SPECTRE · SUPERPOSITION", "intro": "Changer les dimensions et les nombres quantiques, lire les dégénérescences et observer l’évolution d’une superposition.", "controls": [["boundary", "Conditions aux limites", [["parois", "Parois infinies : ψ = 0"], ["periodique", "Périodiques : onde plane"]], "parois"], ["L_nm", "Côté L (nm)", 0.2, 5, 0.1, 1], ["nx", "Nombre quantique nₓ", 1, 6, 1, 1], ["ny", "Nombre quantique nᵧ", 1, 6, 1, 1], ["nz", "Nombre quantique n_z", 1, 6, 1, 1], ["mix", "Poids du second état", 0, 1, 0.05, 0], ["phase", "Phase relative (degrés)", -180, 180, 5, 0], ["time", "Temps τ = t E_L / ℏ", 0, 8, 0.05, 0]], "presets": [["Fondamental", {"boundary": "parois", "nx": 1, "ny": 1, "nz": 1, "mix": 0}], ["Dégénérescence", {"nx": 2, "ny": 1, "nz": 1}], ["Superposition", {"boundary": "parois", "nx": 1, "ny": 1, "nz": 1, "mix": 0.5}], ["Onde plane", {"boundary": "periodique", "nx": 1, "ny": 0, "nz": 0, "mix": 0}]]}, "heisenberg": {"title": "L’incertitude révèle les échelles classiques", "source": "TP · HEISENBERG · GAUSSIENNE", "intro": "Étudier une gaussienne, distinguer diffraction et écart type, puis retrouver les échelles de l’atome et de l’oscillateur.", "controls": [["mode", "Expérience", [["gaussienne", "Paquet gaussien libre"], ["fente", "Fente : diffraction"], ["estimations", "Atome, boîte et oscillateur"]], "gaussienne"], ["sigma", "Écart type initial σ (réduit)", 0.2, 2, 0.05, 1], ["chirp", "Corrélation initiale c", -3, 3, 0.1, 0], ["time", "Temps t (ℏ = m = 1)", 0, 6, 0.05, 0], ["p0", "Impulsion moyenne p₀", -3, 3, 0.1, 0], ["width", "Largeur de fente a (µm)", 0.2, 4, 0.1, 1], ["wavelength_nm", "Longueur d’onde λ (nm)", 380, 780, 10, 550], ["omega", "Pulsation ω (réduite)", 0.2, 3, 0.1, 1]], "presets": [["Borne saturée", {"mode": "gaussienne", "chirp": 0, "time": 0}], ["Paquet qui s’étale", {"mode": "gaussienne", "time": 4}], ["Diffraction", {"mode": "fente"}], ["Énergies minimales", {"mode": "estimations"}]]}, "diffusion": {"title": "Réflexion, pénétration et effet tunnel", "source": "EXERCICES 1–2 · MARCHE ET BARRIÈRE", "intro": "Comparer les courants, raccorder ψ et ψ′ et explorer la transmission sous ou au-dessus de la barrière.", "controls": [["mode", "Potentiel", [["barriere", "Barrière finie"], ["marche", "Marche semi-infinie"]], "barriere"], ["energy", "Énergie E (ℏ = m = 1)", 0.1, 4, 0.05, 1], ["height", "Hauteur V₀", 0, 4, 0.05, 2], ["width", "Largeur a", 0.05, 4, 0.05, 1]], "presets": [["Tunnel V₀ = 2E", {"mode": "barriere", "energy": 1, "height": 2, "width": 1}], ["Sommet de barrière", {"mode": "barriere", "energy": 2, "height": 2}], ["Marche infranchissable", {"mode": "marche", "energy": 1, "height": 2}], ["Résonance", {"mode": "barriere", "energy": 3, "height": 1, "width": 1.57}]]}, "oscillateur": {"title": "Du spectre quantique à l’oscillation classique", "source": "EXTENSION · HERMITE · ÉTAT COHÉRENT", "intro": "Reconnaître les fonctions propres, l’énergie de point zéro et une moyenne qui suit la trajectoire classique.", "controls": [["mode", "État", [["stationnaire", "État propre |n⟩"], ["coherent", "État cohérent |α⟩"]], "stationnaire"], ["n", "Niveau n", 0, 10, 1, 0], ["alpha", "Amplitude |α|", 0, 3, 0.1, 1.5], ["phase", "Phase de α (degrés)", -180, 180, 5, 0], ["time", "Temps ωt", 0, 12, 0.1, 0]], "presets": [["Fondamental", {"mode": "stationnaire", "n": 0}], ["Trois nœuds", {"mode": "stationnaire", "n": 3}], ["Moyenne classique", {"mode": "coherent", "alpha": 2}]]}, "intrication": {"title": "Deux photons, une corrélation quantique", "source": "TP · BELL · CHSH", "intro": "Calculer les probabilités conjointes et les marges, puis comparer un état de Bell à un mélange classique.", "controls": [["state", "Préparation", [["werner", "État de Bell + bruit blanc"], ["classique", "Mélange classique HH / VV"]], "werner"], ["visibility", "Poids p de l’état de Bell", 0, 1, 0.01, 1], ["a", "Analyseur A : a (degrés)", -180, 180, 0.5, 0], ["a2", "Analyseur A : a′ (degrés)", -180, 180, 0.5, 45], ["b", "Analyseur B : b (degrés)", -180, 180, 0.5, 22.5], ["b2", "Analyseur B : b′ (degrés)", -180, 180, 0.5, -22.5]], "presets": [["CHSH optimal", {"state": "werner", "visibility": 1, "a": 0, "a2": 45, "b": 22.5, "b2": -22.5}], ["Intriqué sans violation ici", {"state": "werner", "visibility": 0.5}], ["Corrélation classique", {"state": "classique"}]]}, "josephson": {"title": "La phase commande le courant", "source": "EXERCICE 3 · JOSEPHSON · SQUID", "intro": "Relier tension et fréquence, puis observer la modulation du courant critique d’un SQUID idéal.", "controls": [["mode", "Système", [["squid", "SQUID : deux jonctions"], ["jonction", "Jonction Josephson"]], "squid"], ["I1", "Courant critique I₁ (µA)", 0.1, 30, 0.1, 10], ["I2", "Courant critique I₂ (µA)", 0.1, 30, 0.1, 10], ["flux", "Flux Φ / Φ₀", -2, 2, 0.01, 0], ["voltage_uV", "Tension V (µV)", 0, 10, 0.1, 1], ["phase", "Phase moyenne δ (degrés)", -180, 180, 5, 0]], "presets": [["SQUID symétrique", {"mode": "squid", "I1": 10, "I2": 10, "flux": 0}], ["Demi-quantum de flux", {"mode": "squid", "flux": 0.5}], ["SQUID asymétrique", {"mode": "squid", "I1": 10, "I2": 5}], ["Josephson alternatif", {"mode": "jonction", "voltage_uV": 1}]]}, "rabi": {"title": "Piloter une transition par résonance", "source": "EXERCICE 4 · RMN · IMPULSIONS", "intro": "Explorer les oscillations dans le repère tournant et retrouver les fréquences physiques d’un proton.", "controls": [["omega", "Couplage Ω (réduit)", 0.1, 4, 0.05, 1], ["detuning", "Désaccord Δ (réduit)", -4, 4, 0.05, 0], ["time", "Temps t (réduit)", 0, 15, 0.01, 3.141592653589793], ["B0", "Champ statique B₀ (T)", 0.1, 7, 0.1, 1], ["B1_uT", "Champ circulaire B₁ (µT)", 1, 100, 1, 10]], "presets": [["Impulsion π", {"omega": 1, "detuning": 0, "time": 3.141592653589793}], ["Impulsion π/2", {"omega": 1, "detuning": 0, "time": 1.5707963267948966}], ["Hors résonance", {"detuning": 2}]]}, "bloch": {"title": "Un qubit sur la sphère de Bloch", "source": "INFORMATIQUE QUANTIQUE · ÉTATS ET PORTES", "intro": "Faire varier l’état, appliquer une porte et mesurer selon un axe choisi ; suivre pureté et probabilités.", "controls": [["theta", "Colatitude θ (degrés)", 0, 180, 5, 60], ["phi", "Azimut φ (degrés)", -180, 180, 5, 30], ["purity", "Longueur du vecteur r", 0, 1, 0.05, 1], ["gate", "Porte", [["identite", "Identité"], ["H", "Hadamard H"], ["X", "Pauli X"], ["Rx", "Rotation Rx"], ["Ry", "Rotation Ry"], ["Rz", "Rotation Rz"]], "identite"], ["angle", "Angle de rotation α (degrés)", -360, 360, 5, 90], ["axis_theta", "Axe de mesure : θ (degrés)", 0, 180, 5, 0], ["axis_phi", "Axe de mesure : φ (degrés)", -180, 180, 5, 0]], "presets": [["|0⟩", {"theta": 0, "phi": 0, "purity": 1, "gate": "identite"}], ["Superposition |+⟩", {"theta": 90, "phi": 0, "purity": 1, "gate": "identite"}], ["Hadamard |0⟩", {"theta": 0, "purity": 1, "gate": "H"}], ["État mélangé I/2", {"purity": 0, "gate": "identite"}]]}, "circuits": {"title": "Construire Bell, puis chercher avec Grover", "source": "INFORMATIQUE QUANTIQUE · DEUX QUBITS", "intro": "Lire un circuit, suivre les amplitudes et constater qu’une itération retrouve une cible parmi quatre états.", "controls": [["mode", "Circuit", [["bell", "Préparation d’une paire de Bell"], ["grover", "Recherche de Grover (4 états)"]], "bell"], ["marked", "Indice de la cible", 0, 3, 1, 3], ["iterations", "Itérations de Grover", 0, 4, 1, 1]], "presets": [["Bell", {"mode": "bell"}], ["Grover : une itération", {"mode": "grover", "iterations": 1}], ["Trop d’itérations", {"mode": "grover", "iterations": 2}]]}};
let current='boite',token,lessons=[],exercises=[],latest,serial=0,timer,lessonIndex=1;
const state = Object.fromEntries(Object.entries(labs).map(([id,l])=>[id,Object.fromEntries(l.controls.map(c=>[c[0],Array.isArray(c[2])?c[3]:c[5]]))]));
const fmt = v => v===null?'—':typeof v==='boolean'?(v?'Oui':'Non'):typeof v==='string'?v:Number.isInteger(v)?String(v):Math.abs(v)<.0001&&v!==0?v.toExponential(3):Number(v.toPrecision(6)).toLocaleString('fr-FR',{maximumFractionDigits:6});
function elem(tag,text,cls){const e=document.createElement(tag);if(text!==undefined)e.textContent=text;if(cls)e.className=cls;return e;}
function constrain(){
 if(current==='boite'){const s=state.boite,min=s.boundary==='parois'?1:-4,max=s.boundary==='parois'?6:4;for(const key of ['nx','ny','nz']){s[key]=Math.max(min,Math.min(max,Math.round(s[key])));const c=labs.boite.controls.find(c=>c[0]===key);c[2]=min;c[3]=max;}}
}
function activeLesson(){const i=lessons.findIndex(l=>l.lab===current);return Math.max(0,i);}
function syncTheory(){const index=activeLesson();$('theory-text').innerHTML=lessons[index].html;$('open-lesson').onclick=()=>showCourse(index);}
function irrelevant(key){
 const s=state[current];
 if(current==='heisenberg')return s.mode==='gaussienne'?['width','wavelength_nm','omega'].includes(key):s.mode==='fente'?['sigma','chirp','time','p0','omega'].includes(key):['sigma','chirp','time','p0','width','wavelength_nm'].includes(key);
 if(current==='diffusion')return s.mode==='marche'&&key==='width';
 if(current==='oscillateur'&&'mode' in s)return s.mode==='stationnaire'?['alpha','phase','time'].includes(key):key==='n';
 if(current==='intrication')return s.state==='classique'&&key==='visibility';
 if(current==='josephson')return s.mode==='squid'?key==='voltage_uV':['I2','flux'].includes(key);
 if(current==='bloch')return key==='angle'&&!['Rx','Ry','Rz'].includes(s.gate);
 if(current==='circuits')return s.mode==='bell'&&['marked','iterations'].includes(key);
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
  else{input.type='range';input.min=c[2];input.max=c[3];input.step=c[4];input.value=state[current][key];l.append(out);}
  input.disabled=irrelevant(key);
  input.oninput=()=>{state[current][key]=Array.isArray(c[2])?input.value:Number(input.value);out.textContent=fmt(state[current][key]);constrain();
   if(['mode','boundary','gate','state'].includes(key)){renderControls();document.querySelectorAll('#controls input,#controls select').forEach(e=>e.disabled=irrelevant(e.id.replace('param-','')));syncTheory();}
   $('export').disabled=true;$('status').textContent='Calcul des nouveaux paramètres…';++serial;
   clearTimeout(timer);timer=setTimeout(update,140);
  };box.append(l,input);$('controls').append(box);
 }
}
async function update(){
 const id=++serial;const data={lab:current,...state[current]};
 $('status').textContent='Calcul de l’expérience…';$('export').disabled=true;
 try{
  const response=await fetch('/api',{method:'POST',headers:{'Content-Type':'application/json','X-Quantique-Token':token},body:JSON.stringify(data)});
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
 const details=elem('details');details.append(elem('summary','Consulter les amplitudes, probabilités et valeurs'));const table=elem('table'),head=elem('thead'),tr=elem('tr');for(const v of r.table.headers)tr.append(elem('th',v));head.append(tr);table.append(head);const body=elem('tbody');for(const row of r.table.rows){const line=elem('tr');for(const v of row)line.append(elem('td',fmt(v)));body.append(line);}table.append(body);details.append(table);$('details').append(details);
}
function draw(canvas,data){
 if(data.sceneBloch){drawBloch(canvas,data);return;}
 if(data.grid){drawGrid(canvas,data);return;}
 const width=canvas.clientWidth,height=canvas.clientHeight;if(!width)return;
 const dpr=window.devicePixelRatio||1;canvas.width=Math.round(width*dpr);canvas.height=Math.round(height*dpr);
 const ctx=canvas.getContext('2d');ctx.scale(dpr,dpr);const pad={l:68,r:20,t:20,b:48},w=width-pad.l-pad.r,h=height-pad.t-pad.b;
 const tx=x=>data.logx?Math.log10(Math.max(x,1e-16)):x,ty=y=>data.logy?Math.log10(Math.max(y,1e-16)):y;
 const xs=data.series.flatMap(s=>s.x.map(tx)),ys=data.series.flatMap(s=>s.y.map(ty));
 let xmin=Math.min(...xs),xmax=Math.max(...xs),ymin=Math.min(...ys),ymax=Math.max(...ys);
 if(xmax-xmin<1e-12){xmin-=.5;xmax+=.5;}if(ymax-ymin<1e-12){ymin-=.5;ymax+=.5;}
 if(data.series.some(s=>['bars','stems'].includes(s.kind))){xmin-=.5;xmax+=.5;ymin=Math.min(0,ymin);}
 let dx=(xmax-xmin)*.04,dy=(ymax-ymin)*.08;xmin-=dx;xmax+=dx;ymin-=dy;ymax+=dy;
 if(/^Probabilité$|^P\(/.test(data.ylabel)){ymin=0;ymax=1;}
 if(data.equal){const units=Math.max((xmax-xmin)/w,(ymax-ymin)/h),cx=(xmin+xmax)/2,cy=(ymin+ymax)/2;xmin=cx-units*w/2;xmax=cx+units*w/2;ymin=cy-units*h/2;ymax=cy+units*h/2;}
 const X=x=>pad.l+(tx(x)-xmin)/(xmax-xmin)*w,Y=y=>pad.t+h-(ty(y)-ymin)/(ymax-ymin)*h;
 const tick=(v,log)=>log?'10^'+Number(v.toFixed(1)):Math.abs(v)>=1000||Math.abs(v)<.001&&v!==0?v.toExponential(1):v.toLocaleString('fr-FR',{maximumFractionDigits:2});
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
$('export').onclick=()=>{if(!latest)return;const a=elem('a');a.href='/api/export/'+latest.export_id;a.download=`quantique-${latest.lab}.json`;document.body.append(a);a.click();a.remove();};
let resizeTimer;window.addEventListener('resize',()=>{clearTimeout(resizeTimer);resizeTimer=setTimeout(()=>document.querySelectorAll('canvas').forEach(c=>draw(c,c._data)),100);});
(async()=>{try{const r=await fetch('/api/bootstrap');if(!r.ok)throw Error('Le serveur Python ne répond pas.');const bootstrap=await r.json();token=bootstrap.token;lessons=bootstrap.lessons;exercises=bootstrap.exercises;
 const names={"boite": "Boîte cubique", "heisenberg": "Heisenberg", "diffusion": "Marche & tunnel", "oscillateur": "Oscillateur", "intrication": "Intrication", "josephson": "Josephson & SQUID", "rabi": "RMN & Rabi", "bloch": "Sphère de Bloch", "circuits": "Circuits quantiques", "course": "Cours & exercices"};
 for(const [id,name]of Object.entries(names)){const b=elem('button',name);b.dataset.lab=id;b.onclick=()=>id==='course'?showCourse():showLab(id);$('tabs').append(b);}prepareCourse(bootstrap.sources);showLab('boite');
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
 const {x,y,z}=data.grid,p={l:62,r:18,t:18,b:49};let w=width-p.l-p.r,h=height-p.t-p.b;if(data.equal){const size=Math.min(w,h);p.l+=(w-size)/2;w=h=size;}const vals=z.flat(),lo=Math.min(...vals),hi=Math.max(...vals),nx=x.length,ny=y.length;
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
