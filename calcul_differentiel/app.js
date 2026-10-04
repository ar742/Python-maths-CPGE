'use strict';
const $=id=>document.getElementById(id);
const palette={green:'#23745c',gold:'#c79432',rose:'#b66375',mint:'#8dc9ac',ink:'#17363d'};
const labs={
 jacobiennes:{title:'Une jacobienne transforme les directions',source:'TP · COORDONNÉES · PRIORITÉ',intro:'Voir le changement de coordonnées, son orientation et l’approximation affine locale.',lesson:1,
 controls:[['mode','Coordonnées',[['spherique','Sphériques (ρ, θ, φ)'],['cylindrique','Cylindriques (ρ, θ, z)'],['polaire','Polaires (ρ, θ)']],'spherique'],['r','Rayon ρ',0,3,.05,2],['theta','Azimut θ (degrés)',-180,180,1,35],['phi','Colatitude φ (degrés)',0,180,1,65],['z','Altitude z (cylindrique)',-2,2,.05,.5],['h','Taille de la face paramétrique',.01,.4,.01,.2]],
 presets:[['Pôle : carte singulière',{phi:0}],['Carte régulière',{r:2,phi:65}],['Polaire',{mode:'polaire'}]]},
 elliptique:{title:'L’intégrale change avec la mesure',source:'TP · INTÉGRALE ELLIPTIQUE · PRIORITÉ',intro:'Transformer un quart de disque, retrouver le facteur de mesure et corriger le calcul du recueil.',lesson:2,
 controls:[['a','Demi-axe a',.2,5,.1,3],['b','Demi-axe b',.2,5,.1,2],['alpha','Coefficient α de x³',0,5,.1,3],['beta','Coefficient β de y²',0,5,.1,1],['order','Nœuds par variable',2,64,1,12]],
 presets:[['TP du recueil',{a:3,b:2,alpha:3,beta:1}],['Ellipticité marquée',{a:4,b:.5}],['Disque unité',{a:1,b:1}]]},
 taylor:{title:'La fonction, sa tangente et sa courbure',source:'DIFFÉRENTIELLE · TAYLOR · EXERCICE 1',intro:'Comparer les restes et apprendre à classer un point critique avec les bonnes hypothèses.',lesson:4,
 controls:[['mode','Fonction',[['lisse','sin x cos y + 0,2(x²+y²)'],['cubique','Polynôme de l’exercice 1'],['pathologie','Dérivées directionnelles sans continuité']],'lisse'],['x','Point de base : x',-3,3,.01,.5],['y','Point de base : y',-3,3,.01,.3],['angle','Direction (degrés)',-180,180,1,40],['h','Étendue de la coupe',.05,1.5,.05,.8]],
 presets:[['Selle (−2,−2)',{mode:'cubique',x:-2,y:-2}],['Selle (2/3,−2/3)',{mode:'cubique',x:2/3,y:-2/3}],['Origine dégénérée',{mode:'cubique',x:0,y:0}],['Chemin courbe',{mode:'pathologie'}]]},
 matrices:{title:'Différencier le déterminant et l’inverse',source:'TP · APPLICATIONS MATRICIELLES · PRIORITÉ',intro:'Suivre une droite A+tH et comprendre le rôle de l’inversibilité et de l’ordre des facteurs.',lesson:5,
 controls:[['a','A₁₁',-3,3,.05,1],['b','A₁₂',-3,3,.05,.6],['c','A₂₁',-3,3,.05,-.2],['d','A₂₂',-3,3,.05,1.5]],
 presets:[['À l’identité',{a:1,b:0,c:0,d:1}],['Matrice singulière',{a:1,b:0,c:0,d:0}],['Presque singulière',{a:1,b:0,c:0,d:.05}]]},
 optimisation:{title:'Du gradient aux valeurs propres',source:'TP · QUADRATIQUES · RAYLEIGH · NEWTON',intro:'Relier la géométrie des niveaux, la vitesse de descente et la précision du quotient de Rayleigh.',lesson:7,
 controls:[['mode','Expérience',[['quadratique','Descente et Newton'],['rayleigh','Quotient de Rayleigh']],'quadratique'],['lambda1','Première valeur propre',.2,5,.1,1],['lambda2','Seconde valeur propre',.2,10,.1,4],['rotation','Rotation des axes (degrés)',-90,90,1,30],['angle','Direction pour Rayleigh (degrés)',-180,180,1,65],['x','Départ x (descente)',-3,3,.1,-1.5],['y','Départ y (descente)',-3,3,.1,2],['factor','Facteur du pas αλmax',.1,2.5,.05,.8],['steps','Itérations',0,50,1,25]],
 presets:[['Descente stable',{mode:'quadratique',factor:.8}],['Pas trop grand',{mode:'quadratique',factor:2.3}],['Rayleigh',{mode:'rayleigh'}]]},
 lie:{title:'Le tangent engendre une transformation',source:'TXT · ALGÈBRES DE LIE · PRIORITÉ',intro:'Passer de la contrainte du groupe à son espace tangent, puis observer rotations et commutateurs.',lesson:8,
 controls:[['group','Groupe de matrices',[['SO','SO : rotations'],['SL','SL : déterminant 1'],['GL','GL : matrices inversibles']],'SO'],['n','Dimension',2,3,1,3],['a','Paramètre diagonal',-2,2,.1,.8],['b','Paramètre de cisaillement',-2,2,.1,1],['c','Second paramètre',-2,2,.1,.6],['t','Temps t',-2,2,.05,1]],
 presets:[['Rotations 3D',{group:'SO',n:3}],['SO(2) : crochet nul',{group:'SO',n:2}],['Volume conservé',{group:'SL',n:3}],['Volume variable',{group:'GL',n:3}]]},
 gaussienne:{title:'Une intégrale révèle moyenne et covariance',source:'TXT · GAUSSIENNE ÉTENDUE · PRIORITÉ',intro:'Décentrer et tourner une gaussienne, calculer son intégrale et interpréter ses dérivées.',lesson:10,
 controls:[['n','Dimension n',2,8,1,3],['lambda1','Précision du premier axe',.2,5,.1,.7],['lambda2','Précision du second axe',.2,5,.1,2],['gamma','Précision des axes suivants',.2,5,.1,1],['rotation','Rotation des axes (degrés)',-90,90,1,35],['b1','Terme linéaire B₁',-3,3,.1,1],['b2','Terme linéaire B₂',-3,3,.1,-.5],['order','Nœuds de quadrature / variable',4,80,1,32]],
 presets:[['Centrée',{b1:0,b2:0}],['Exemple calculable',{n:2,lambda1:2,lambda2:3,rotation:0,b1:2,b2:-3}],['Forte anisotropie',{lambda1:.2,lambda2:5,rotation:45,order:80}]]},
 green_fubini:{title:'Intégrer : orientation et hypothèses',source:'EXERCICES 2 & 7 · GREEN · FUBINI',intro:'Vérifier une circulation par deux méthodes, puis voir pourquoi on ne peut pas toujours permuter les intégrales.',lesson:12,
 controls:[['mode','Expérience',[['green','Green : frontière et domaine'],['fubini','Fubini : singularité et coupures']],'green'],['orientation','Sens (Green)',[['1','Orientation positive'],['-1','Orientation négative']],'1'],['logx','log₁₀ εx (Fubini)',-6,0,.1,-2],['logy','log₁₀ εy (Fubini)',-6,0,.1,-2]],
 presets:[['Green positif',{mode:'green',orientation:'1'}],['Coupure symétrique',{mode:'fubini',logx:-4,logy:-4}],['Coupures inégales',{mode:'fubini',logx:-2,logy:-5}]]}
};
let current='jacobiennes',token,lessons=[],exercises=[],latest,serial=0,timer,lessonIndex=1;
const state = Object.fromEntries(Object.entries(labs).map(([id,l])=>[id,Object.fromEntries(l.controls.map(c=>[c[0],Array.isArray(c[2])?c[3]:c[5]]))]));
const fmt = v => v===null?'—':typeof v==='boolean'?(v?'Oui':'Non'):typeof v==='string'?v:Number.isInteger(v)?String(v):Math.abs(v)<.0001&&v!==0?v.toExponential(3):Number(v.toPrecision(6)).toLocaleString('fr-FR',{maximumFractionDigits:6});
function elem(tag,text,cls){const e=document.createElement(tag);if(text!==undefined)e.textContent=text;if(cls)e.className=cls;return e;}
function constrain(){}
function activeLesson(){
 if(current==='taylor'&&state.taylor.mode==='pathologie')return 0;
 if(current==='green_fubini'&&state.green_fubini.mode==='fubini')return 13;
 return labs[current].lesson;
}
function syncTheory(){const index=activeLesson();$('theory-text').innerHTML=lessons[index].html;$('open-lesson').onclick=()=>showCourse(index);}
function irrelevant(key){
 const s=state[current];
 if(current==='jacobiennes')return key==='phi'&&s.mode!=='spherique'||key==='z'&&s.mode!=='cylindrique';
 if(current==='taylor')return s.mode==='pathologie'&&['x','y','h'].includes(key);
 if(current==='optimisation')return s.mode==='rayleigh'?['x','y','factor','steps'].includes(key):key==='angle';
 if(current==='lie')return s.group==='SO'&&key==='a';
 if(current==='gaussienne')return s.n===2&&key==='gamma';
 if(current==='green_fubini')return s.mode==='green'?['logx','logy'].includes(key):key==='orientation';
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
   if(['mode','group','n'].includes(key)){document.querySelectorAll('#controls input,#controls select').forEach(e=>e.disabled=irrelevant(e.id.replace('param-','')));syncTheory();}
   $('export').disabled=true;++serial;
   clearTimeout(timer);timer=setTimeout(update,140);
  };box.append(l,input);$('controls').append(box);
 }
}
async function update(){
 const id=++serial;const data={lab:current,...state[current]};if(current==='green_fubini')data.orientation=Number(data.orientation);
 $('status').textContent='Calcul de l’expérience…';$('export').disabled=true;
 try{
  const response=await fetch('/api',{method:'POST',headers:{'Content-Type':'application/json','X-Differentiel-Token':token},body:JSON.stringify(data)});
  const result=await response.json();if(id!==serial)return;if(!response.ok)throw Error(result.error);
  latest=result;$('error').hidden=true;renderResult(result);$('status').textContent='Calcul terminé · résultats exacts et diagnostics numériques disponibles';$('export').disabled=false;
 }catch(e){if(id!==serial)return;$('error').hidden=false;$('error').textContent=e.message;$('status').textContent='Vérifiez les paramètres avant de recommencer.';}
}
function renderResult(r){
 $('metrics').replaceChildren();for(const m of r.metrics){const e=elem('div',undefined,'metric');e.append(elem('span',m.label),elem('b',fmt(m.value)),elem('small',m.note));$('metrics').append(e);}
 $('plots').replaceChildren();for(const data of r.charts){const f=elem('section',undefined,'figure');f.append(elem('h3',data.title));const canvas=elem('canvas');canvas.setAttribute('role','img');canvas.setAttribute('aria-label',data.title+' : '+data.series.filter(s=>!s.label.startsWith('Trajectoire')).map(s=>s.label).join(', '));f.append(canvas);
  const legend=elem('div',undefined,'legend');const seen=new Set();for(const s of data.series){const label=s.label;if(seen.has(label))continue;seen.add(label);const item=elem('span');item.append(elem('i',undefined,s.color),document.createTextNode(label));legend.append(item);}f.append(legend);$('plots').append(f);canvas._data=data;
 }
 document.querySelectorAll('#plots canvas').forEach(c=>draw(c,c._data));
 $('details').replaceChildren();for(const note of r.notes)$('details').append(elem('p',note));
 const details=elem('details');details.append(elem('summary','Consulter les matrices et les valeurs'));const table=elem('table'),head=elem('thead'),tr=elem('tr');for(const v of r.table.headers)tr.append(elem('th',v));head.append(tr);table.append(head);const body=elem('tbody');for(const row of r.table.rows){const line=elem('tr');for(const v of row)line.append(elem('td',fmt(v)));body.append(line);}table.append(body);details.append(table);$('details').append(details);
}
function draw(canvas,data){
 const width=canvas.clientWidth,height=canvas.clientHeight;if(!width)return;
 const dpr=window.devicePixelRatio||1;canvas.width=Math.round(width*dpr);canvas.height=Math.round(height*dpr);
 const ctx=canvas.getContext('2d');ctx.scale(dpr,dpr);const pad={l:68,r:20,t:20,b:48},w=width-pad.l-pad.r,h=height-pad.t-pad.b;
 const tx=x=>data.logx?Math.log10(Math.max(x,1e-16)):x,ty=y=>data.logy?Math.log10(Math.max(y,1e-16)):y;
 const xs=data.series.flatMap(s=>s.x.map(tx)),ys=data.series.flatMap(s=>s.y.map(ty));
 let xmin=Math.min(...xs),xmax=Math.max(...xs),ymin=Math.min(...ys),ymax=Math.max(...ys);
 if(xmax-xmin<1e-12){xmin-=.5;xmax+=.5;}if(ymax-ymin<1e-12){ymin-=.5;ymax+=.5;}
 let dx=(xmax-xmin)*.04,dy=(ymax-ymin)*.08;xmin-=dx;xmax+=dx;ymin-=dy;ymax+=dy;
 if(data.equal){const units=Math.max((xmax-xmin)/w,(ymax-ymin)/h),cx=(xmin+xmax)/2,cy=(ymin+ymax)/2;xmin=cx-units*w/2;xmax=cx+units*w/2;ymin=cy-units*h/2;ymax=cy+units*h/2;}
 const X=x=>pad.l+(tx(x)-xmin)/(xmax-xmin)*w,Y=y=>pad.t+h-(ty(y)-ymin)/(ymax-ymin)*h;
 const tick=(v,log)=>log?'10^'+Number(v.toFixed(1)):Math.abs(v)>=1000||Math.abs(v)<.001&&v!==0?v.toExponential(1):v.toLocaleString('fr-FR',{maximumFractionDigits:2});
 ctx.font='11px Segoe UI, sans-serif';ctx.fillStyle='#627477';ctx.textAlign='right';
 for(let i=0;i<=4;i++){const y=ymin+(ymax-ymin)*i/4,pos=pad.t+h-h*i/4;ctx.strokeStyle='#edf0e9';ctx.beginPath();ctx.moveTo(pad.l,pos);ctx.lineTo(pad.l+w,pos);ctx.stroke();ctx.fillText(tick(y,data.logy),pad.l-9,pos+4);}
 ctx.textAlign='center';for(let i=0;i<=4;i++){const x=xmin+(xmax-xmin)*i/4;ctx.fillText(tick(x,data.logx),pad.l+w*i/4,pad.t+h+18);}
 ctx.fillText(data.xlabel,pad.l+w/2,height-7);ctx.save();ctx.translate(14,pad.t+h/2);ctx.rotate(-Math.PI/2);ctx.fillText(data.ylabel,0,0);ctx.restore();
 ctx.save();ctx.beginPath();ctx.rect(pad.l,pad.t,w,h);ctx.clip();
 for(const s of data.series){ctx.strokeStyle=ctx.fillStyle=palette[s.color]||palette.green;ctx.lineWidth=s.color==='mint'?1:2;ctx.globalAlpha=s.color==='mint'?.7:1;
  if(s.kind==='dots'){s.x.forEach((x,i)=>{ctx.beginPath();ctx.arc(X(x),Y(s.y[i]),4,0,2*Math.PI);ctx.fill();});}
  else{ctx.beginPath();s.x.forEach((x,i)=>{if(!i)ctx.moveTo(X(x),Y(s.y[i]));else ctx.lineTo(X(x),Y(s.y[i]));});ctx.stroke();}
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
$('export').onclick=()=>{if(!latest)return;const a=elem('a');a.href='/api/export/'+latest.export_id;a.download=`differentiel-${latest.lab}.json`;document.body.append(a);a.click();a.remove();};
let resizeTimer;window.addEventListener('resize',()=>{clearTimeout(resizeTimer);resizeTimer=setTimeout(()=>document.querySelectorAll('canvas').forEach(c=>draw(c,c._data)),100);});
(async()=>{try{const r=await fetch('/api/bootstrap');if(!r.ok)throw Error('Le serveur Python ne répond pas.');const bootstrap=await r.json();token=bootstrap.token;lessons=bootstrap.lessons;exercises=bootstrap.exercises;
 const names={jacobiennes:'Jacobiennes',elliptique:'Intégrale elliptique',taylor:'Différentielle & Taylor',matrices:'Matrices',optimisation:'Rayleigh & Newton',lie:'Algèbres de Lie',gaussienne:'Gaussienne étendue',green_fubini:'Green & Fubini',course:'Cours & exercices'};
 for(const [id,name]of Object.entries(names)){const b=elem('button',name);b.dataset.lab=id;b.onclick=()=>id==='course'?showCourse():showLab(id);$('tabs').append(b);}prepareCourse(bootstrap.sources);showLab('jacobiennes');
}catch(e){$('error').hidden=false;$('error').textContent=e.message;$('status').textContent='Lancez le programme Python pour ouvrir l’atelier.';}})();
