'use strict';
const $ = id => document.getElementById(id);
const palette = {green:'#23745c',gold:'#c79432',rose:'#b66375',mint:'#8dc9ac',ink:'#17363d'};
const labs = {
 polarisation:{title:'La moyenne tient, la population se sépare',source:'EXERCICE 6 · PRIORITÉ',intro:'Suivre un processus qui conserve son espérance tout en concentrant sa loi près de 0 et de 1.',lesson:6,
 controls:[['c','État initial c',.01,.99,.01,.35],['lambda','Intensité λ',.01,.99,.01,.25],['steps','Nombre d’étapes',0,500,1,100],['epsilon','Zone centrale : ε',.01,.49,.01,.1]],
 presets:[['Polarisation rapide',{lambda:.6,steps:80}],['Polarisation lente',{lambda:.08,steps:200}],['Départ symétrique',{c:.5}]]},
 extremes:{title:'Le maximum approche la frontière',source:'EXERCICE 7 · PRIORITÉ',intro:'Comprendre les statistiques d’ordre et la vitesse de convergence, puis corriger le biais d’un maximum.',lesson:8,
 controls:[['mode','Variable observée',[['max','Maximum'],['min','Minimum'],['ordre','k-ième valeur'],['ecart','Écart n(1−Mₙ/θ)']],'max'],['n','Taille de l’échantillon n',1,300,1,20],['k','Rang k (mode k-ième)',1,300,1,5],['theta','Borne θ de l’intervalle',.1,10,.1,1]],
 presets:[['Maximum',{mode:'max',n:20}],['Vitesse exponentielle',{mode:'ecart',n:100}],['Rang médian',{mode:'ordre',n:31,k:16}]]},
 arcsinus:{title:'Un cosinus fait émerger la loi arcsinus',source:'EXERCICE 8 · PRIORITÉ · SPECTRE DÉTERMINISTE',intro:'Relier une somme de Riemann, un changement de variable et le spectre de la matrice d’un chemin.',lesson:10,
 controls:[['n','Dimension / nombre de valeurs',2,300,1,60],['mode','Indice du mode propre',1,300,1,3],['power','Ordre du moment étudié',1,10,1,4]],
 presets:[['Petit spectre',{n:12,mode:3}],['Vers la limite',{n:200,mode:3}],['Moment d’ordre 2',{power:2}]]},
 wigner:{title:'Des matrices aléatoires au demi-cercle',source:'EXERCICE 8 · APPROFONDISSEMENT · WIGNER',intro:'Comparer plusieurs modèles d’entrées et retrouver les moments de Catalan, sans confondre les deux lois spectrales.',lesson:11,
 controls:[['n','Dimension n',8,180,1,80],['matrices','Matrices indépendantes',1,8,1,3],['law','Loi des entrées',[['gauss','Normale N(0,1)'],['signes','Signes ±1 équiprobables'],['uniforme','Uniforme [−√3,√3]']],'gauss']],
 presets:[['Signes aléatoires',{law:'signes'}],['Entrées uniformes',{law:'uniforme'}],['Plus de matrices',{matrices:8,n:100}]]},
 urne:{title:'La remise change la loi',source:'EXERCICE 4 · FONDATIONS',intro:'Comparer tirages avec et sans remise : même espérance, variance différente, indépendance à justifier.',lesson:0,
 controls:[['red','Boules rouges R',1,100,1,10],['blue','Boules bleues B',1,100,1,10],['draws','Boules tirées d',1,200,1,10]],
 presets:[['Exercice 4',{red:10,blue:10,draws:10}],['Toute l’urne',{red:10,blue:10,draws:20}],['Faible prélèvement',{red:100,blue:100,draws:10}]]},
 fluctuations:{title:'Observer la loi, maîtriser l’écart',source:'TP · EXERCICE 5 · GRANDS NOMBRES',intro:'Passer d’une marche aléatoire à une loi binomiale, puis confronter les fluctuations aux bornes théoriques.',lesson:4,
 controls:[['n','Taille d’un bloc n',1,1000,1,100],['p','Probabilité de succès p',0,1,.01,.5],['epsilon','Tolérance ε',.001,1,.001,.1]],
 presets:[['Marche du TP',{n:20,p:.5}],['Événement rare',{n:100,p:.02}],['Grands nombres',{n:1000,p:.5,epsilon:.05}]]}
};
let current='polarisation', token, lessons=[], exercises=[], latest, serial=0, timer, lessonIndex=6;
const state = Object.fromEntries(Object.entries(labs).map(([id,l])=>[id,Object.fromEntries(l.controls.map(c=>[c[0],Array.isArray(c[2])?c[3]:c[5]]))]));
const fmt = v => v===null?'—':typeof v==='string'?v:Number.isInteger(v)?String(v):Math.abs(v)<.0001&&v!==0?v.toExponential(3):Number(v.toPrecision(6)).toLocaleString('fr-FR',{maximumFractionDigits:6});
function elem(tag,text,cls){const e=document.createElement(tag);if(text!==undefined)e.textContent=text;if(cls)e.className=cls;return e;}
function constrain(){
 if(current==='urne')state.urne.draws=Math.min(state.urne.draws,state.urne.red+state.urne.blue);
 if(current==='extremes')state.extremes.k=Math.min(state.extremes.k,state.extremes.n);
 if(current==='arcsinus')state.arcsinus.mode=Math.min(state.arcsinus.mode,state.arcsinus.n);
}
function showLab(id,params={}){
 current=id;Object.assign(state[id],params);constrain();
 $('course').hidden=true;$('laboratory').hidden=false;
 document.querySelectorAll('#tabs button').forEach(b=>b.classList.toggle('active',b.dataset.lab===id));
 const lab=labs[id];$('lab-title').textContent=lab.title;$('lab-source').textContent=lab.source;$('lab-intro').textContent=lab.intro;
 $('reps').disabled=id==='wigner';$('seed-note').textContent=id==='wigner'?'La répétition porte ici sur les matrices indépendantes, et non sur les valeurs propres.':'Une même graine et les mêmes paramètres reproduisent l’expérience dans une même version de NumPy.';
 $('presets').replaceChildren();
 for(const [name,p] of lab.presets){const b=elem('button',name);b.onclick=()=>showLab(id,p);$('presets').append(b);}
 renderControls();$('theory-text').innerHTML=lessons[lab.lesson].html;
 $('open-lesson').onclick=()=>showCourse(lab.lesson);update();
}
function renderControls(){
 $('controls').replaceChildren();
 for(const c of labs[current].controls){
  const [key,label]=c, box=elem('div',undefined,'control'), l=elem('label',label), out=elem('output',fmt(state[current][key]));
  const input=elem(Array.isArray(c[2])?'select':'input');input.id='param-'+key;l.htmlFor=input.id;
  if(Array.isArray(c[2])){for(const [value,name]of c[2]){const o=elem('option',name);o.value=value;input.append(o);}input.value=state[current][key];}
  else{input.type='range';input.min=c[2];input.max=c[3];input.step=c[4];if(key==='draws')input.max=state.urne.red+state.urne.blue;if(key==='k')input.max=state.extremes.n;if(key==='mode'&&current==='arcsinus')input.max=state.arcsinus.n;input.value=state[current][key];l.append(out);}
  input.oninput=()=>{state[current][key]=Array.isArray(c[2])?input.value:Number(input.value);out.textContent=fmt(state[current][key]);constrain();
   if(['red','blue','n'].includes(key)){for(const dep of ['draws','k','mode']){const e=$('param-'+dep);if(e&&e.type==='range'){e.max=dep==='draws'?state.urne.red+state.urne.blue:state[current].n;e.value=state[current][dep];e.previousElementSibling.querySelector('output').textContent=fmt(state[current][dep]);}}}
   clearTimeout(timer);timer=setTimeout(update,140);
  };box.append(l,input);$('controls').append(box);
 }
}
async function update(){
 const id=++serial;const data={lab:current,...state[current],seed:Number($('seed').value),reps:Number($('reps').value)};
 $('status').textContent='Calcul de l’expérience…';$('export').disabled=true;
 try{
  const response=await fetch('/api',{method:'POST',headers:{'Content-Type':'application/json','X-Probabilites-Token':token},body:JSON.stringify(data)});
  const result=await response.json();if(id!==serial)return;if(!response.ok)throw Error(result.error);
  latest=result;$('error').hidden=true;renderResult(result);$('status').textContent=`Expérience calculée · graine ${result.seed} · ${current==='wigner'?state.wigner.matrices+' matrices indépendantes':result.reps.toLocaleString('fr-FR')+' répétitions'}`;$('export').disabled=false;
 }catch(e){if(id!==serial)return;$('error').hidden=false;$('error').textContent=e.message;$('status').textContent='Vérifiez les paramètres avant de recommencer.';}
}
function renderResult(r){
 $('metrics').replaceChildren();for(const m of r.metrics){const e=elem('div',undefined,'metric');e.append(elem('span',m.label),elem('b',fmt(m.value)),elem('small',m.note));$('metrics').append(e);}
 $('plots').replaceChildren();for(const data of r.charts){const f=elem('section',undefined,'figure');f.append(elem('h3',data.title));const canvas=elem('canvas');canvas.setAttribute('role','img');canvas.setAttribute('aria-label',data.title+' : '+data.series.filter(s=>!s.label.startsWith('Trajectoire')).map(s=>s.label).join(', '));f.append(canvas);
  const legend=elem('div',undefined,'legend');const seen=new Set();for(const s of data.series){const label=s.label.startsWith('Trajectoire')?'Trajectoires':s.label;if(seen.has(label))continue;seen.add(label);const item=elem('span');item.append(elem('i',undefined,s.color),document.createTextNode(label));legend.append(item);}f.append(legend);$('plots').append(f);draw(canvas,data);canvas._data=data;
 }
 $('details').replaceChildren();for(const note of r.notes)$('details').append(elem('p',note));
 const details=elem('details');details.append(elem('summary','Consulter les valeurs et les moments'));const table=elem('table'),head=elem('thead'),tr=elem('tr');for(const v of r.table.headers)tr.append(elem('th',v));head.append(tr);table.append(head);const body=elem('tbody');for(const row of r.table.rows){const line=elem('tr');for(const v of row)line.append(elem('td',fmt(v)));body.append(line);}table.append(body);details.append(table);$('details').append(details);
}
function draw(canvas, data){
 const width=canvas.clientWidth,height=canvas.clientHeight;if(!width)return;const dpr=window.devicePixelRatio||1;canvas.width=Math.round(width*dpr);canvas.height=Math.round(height*dpr);const ctx=canvas.getContext('2d');ctx.scale(dpr,dpr);const pad={l:58,r:20,t:20,b:48},w=width-pad.l-pad.r,h=height-pad.t-pad.b;
 const xs=data.series.flatMap(s=>s.x),ys=data.series.flatMap(s=>s.y),xmin=data.xlim?data.xlim[0]:Math.min(...xs),xmax=data.xlim?data.xlim[1]:Math.max(...xs);
 const ymin=data.ylim?data.ylim[0]:Math.min(0,...ys),ymax=data.ylim?data.ylim[1]:Math.max(...ys)*1.1||1;
 const X=x=>pad.l+(x-xmin)/(xmax-xmin||1)*w,Y=y=>pad.t+h-(y-ymin)/(ymax-ymin||1)*h;
 ctx.font='11px Segoe UI, sans-serif';ctx.fillStyle='#627477';ctx.textAlign='right';
 for(let i=0;i<=4;i++){const y=ymin+(ymax-ymin)*i/4;ctx.strokeStyle='#edf0e9';ctx.beginPath();ctx.moveTo(pad.l,Y(y));ctx.lineTo(pad.l+w,Y(y));ctx.stroke();ctx.fillText(y.toLocaleString('fr-FR',{maximumFractionDigits:3}),pad.l-9,Y(y)+4);}
 ctx.textAlign='center';for(let i=0;i<=4;i++){const x=xmin+(xmax-xmin)*i/4;ctx.fillText(x.toLocaleString('fr-FR',{maximumFractionDigits:2}),X(x),pad.t+h+18);}
 ctx.fillText(data.xlabel,pad.l+w/2,height-7);ctx.save();ctx.translate(14,pad.t+h/2);ctx.rotate(-Math.PI/2);ctx.fillText(data.ylabel,0,0);ctx.restore();
 ctx.save();ctx.beginPath();ctx.rect(pad.l,pad.t,w,h);ctx.clip();
 for(const s of data.series){ctx.strokeStyle=ctx.fillStyle=palette[s.color]||palette.green;ctx.lineWidth=s.color==='mint'?1:2;ctx.globalAlpha=s.color==='mint'?.65:1;
  if(s.kind==='bars'){const bw=Math.max(2,w/s.x.length*.8);s.x.forEach((x,i)=>ctx.fillRect(X(x)-bw/2,Y(s.y[i]),bw,Y(0)-Y(s.y[i])));}
  else if(s.kind==='dots'||s.kind==='stems'){s.x.forEach((x,i)=>{if(s.kind==='stems'){ctx.beginPath();ctx.moveTo(X(x),Y(0));ctx.lineTo(X(x),Y(s.y[i]));ctx.stroke();}ctx.beginPath();ctx.arc(X(x),Y(s.y[i]),s.kind==='stems'?4:2.4,0,2*Math.PI);ctx.fill();});}
  else{ctx.beginPath();s.x.forEach((x,i)=>{if(!i)ctx.moveTo(X(x),Y(s.y[i]));else{if(s.kind==='step')ctx.lineTo(X(x),Y(s.y[i-1]));ctx.lineTo(X(x),Y(s.y[i]));}});ctx.stroke();}
 }ctx.restore();
}
function showCourse(index=lessonIndex){++serial;lessonIndex=index;$('course').hidden=false;$('laboratory').hidden=true;$('status').textContent='Cours et exercices corrigés';document.querySelectorAll('#tabs button').forEach(b=>b.classList.toggle('active',b.dataset.lab==='course'));
 $('lesson-list').replaceChildren();lessons.forEach((l,i)=>{const b=elem('button',l.title,i===index?'active':'');b.onclick=()=>showCourse(i);$('lesson-list').append(b);});
 const l=lessons[index];$('lesson').innerHTML='';$('lesson').append(elem('span',l.level,'badge'),elem('h2',l.title));const content=elem('div');content.innerHTML=l.html;$('lesson').append(content);const b=elem('button','Ouvrir le laboratoire associé');b.onclick=()=>showLab(l.lab);$('lesson').append(b);
}
function prepareCourse(sources){
 $('exercises').replaceChildren();for(const e of exercises){const card=elem('div',undefined,'exercise');card.append(elem('span',e.level,'badge'),elem('h3',e.title),elem('p',e.question));const detail=elem('details');detail.append(elem('summary','Déplier la correction'),elem('p',e.answer));card.append(detail);const b=elem('button','Expérimenter');b.onclick=()=>{showLab(e.lab,e.params);$('tabs').scrollIntoView({behavior:'smooth',block:'start'});};card.append(b);$('exercises').append(card);}
 $('sources').replaceChildren();for(const text of sources)$('sources').append(elem('p',text));
}
$('reps').onchange=update;$('seed').onchange=update;$('reroll').onclick=()=>{$('seed').value=(Number($('seed').value)+1)>>>0;update();};
$('export').onclick=()=>{if(!latest)return;const a=elem('a');a.href='/api/export/'+latest.export_id;a.download=`probabilites-${latest.lab}-${latest.seed}.json`;document.body.append(a);a.click();a.remove();};
let resizeTimer;window.addEventListener('resize',()=>{clearTimeout(resizeTimer);resizeTimer=setTimeout(()=>document.querySelectorAll('canvas').forEach(c=>draw(c,c._data)),100);});
(async()=>{try{const r=await fetch('/api/bootstrap');if(!r.ok)throw Error('Le serveur Python ne répond pas.');const bootstrap=await r.json();token=bootstrap.token;lessons=bootstrap.lessons;exercises=bootstrap.exercises;
 const names={polarisation:'6 · Polarisation',extremes:'7 · Extrêmes',arcsinus:'8 · Arcsinus',wigner:'8 · Wigner',urne:'Urnes & dépendance',fluctuations:'Fréquences & fluctuations',course:'Cours & exercices'};
 for(const [id,name]of Object.entries(names)){const b=elem('button',name);b.dataset.lab=id;b.onclick=()=>id==='course'?showCourse():showLab(id);$('tabs').append(b);}prepareCourse(bootstrap.sources);showLab('polarisation');
}catch(e){$('error').hidden=false;$('error').textContent=e.message;$('status').textContent='Lancez le programme Python pour ouvrir l’atelier.';}})();
