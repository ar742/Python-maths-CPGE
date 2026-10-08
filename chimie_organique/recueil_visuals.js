'use strict';
function drawDipoles(ctx,w,h,s){
  const left={l:20,r:w*.44,t:75,b:h-75};
  if(s.molecule)drawMolecule(ctx,s.molecule,left);
  label(ctx,'Positions des groupes NO₂',25,32,CHEM.green,14);
  label(ctx,`Isomère ${s.isomer} · angle ${fmt(s.angle_deg)}°`,25,h-35,CHEM.muted,12);
  const vectors=s.vectors||[],points=vectors.flatMap(q=>[q.start,q.end]),xs=points.map(p=>p[0]),ys=points.map(p=>p[1]);
  const amplitude=Math.max(1,...xs.map(Math.abs),...ys.map(Math.abs),s.mu0||1),box={l:w*.50,r:w-40,t:75,b:h-95};
  const scale=Math.min((box.r-box.l)/(2.3*amplitude),(box.b-box.t)/(2.3*amplitude)),cx=(box.l+box.r)/2,cy=(box.t+box.b)/2;
  const X=x=>cx+x*scale,Y=y=>cy-y*scale;
  line(ctx,[[box.l,cy],[box.r,cy]],CHEM.line,1);line(ctx,[[cx,box.t],[cx,box.b]],CHEM.line,1);
  for(const q of vectors){const color=q.role==='resultant'?CHEM.violet:q.role==='component'?CHEM.line:CHEM.green;
    if(Math.hypot(q.end[0]-q.start[0],q.end[1]-q.start[1])<1e-10)continue;
    if(q.role==='component')line(ctx,[[X(q.start[0]),Y(q.start[1])],[X(q.end[0]),Y(q.end[1])]],color,1.5,true);
    else arrow(ctx,X(q.start[0]),Y(q.start[1]),X(q.end[0]),Y(q.end[1]),color,q.role==='resultant'?3:2);
  }
  label(ctx,'Somme des deux vecteurs de groupe',box.l,32,CHEM.green,14);
  label(ctx,`|μ| = ${fmt(s.magnitude)} ${s.unit||'D'}`,box.l,h-49,CHEM.violet,18);
  label(ctx,`μ₀ = ${fmt(s.mu0)} D · modèle de groupes identiques`,box.l,h-26,CHEM.muted,11);
  label(ctx,'Vert : groupes · violet : résultante',box.l,h-10,CHEM.muted,10);
  if(Math.abs(s.magnitude)<1e-9)label(ctx,'Compensation',cx+10,cy+25,CHEM.violet,12);
}
function drawE2Newman(ctx,w,h,s){
  const cx=w*.30,cy=h*.49,r=Math.min(48,w*.065),ray=Math.min(94,w*.13),angles=[-Math.PI/2,Math.PI/6,5*Math.PI/6],theta=(s.angle||0)*Math.PI/180;
  ctx.strokeStyle=CHEM.red;ctx.lineWidth=2.3;ctx.beginPath();ctx.arc(cx,cy,r,0,2*Math.PI);ctx.stroke();
  for(let i=0;i<3;i++){const a=angles[i]+theta;line(ctx,[[cx+r*Math.cos(a),cy+r*Math.sin(a)],[cx+ray*Math.cos(a),cy+ray*Math.sin(a)]],CHEM.red,2.3);label(ctx,s.back[i],cx+(ray+23)*Math.cos(a),cy+(ray+23)*Math.sin(a),CHEM.red,13,'center');}
  for(let i=0;i<3;i++){const a=angles[i];line(ctx,[[cx,cy],[cx+ray*.86*Math.cos(a),cy+ray*.86*Math.sin(a)]],CHEM.green,2.6);label(ctx,s.front[i],cx+(ray+19)*Math.cos(a),cy+(ray+19)*Math.sin(a),CHEM.green,13,'center');}
  dot(ctx,cx,cy,5,CHEM.green);label(ctx,'Regard C3 → C4',22,31,CHEM.green,15);label(ctx,`Configuration : ${s.configuration}`,22,53,CHEM.muted,12);
  if(s.product){drawMolecule(ctx,s.product,{l:w*.59,r:w-30,t:115,b:h-105});label(ctx,`Produit ${s.product_configuration}`,w*.60,88,CHEM.green,17);}
  else wrap(ctx,'Cette conformation ne permet pas l’élimination anti C3=C4.',w*.60,120,w*.33,CHEM.red,15,22);
  wrap(ctx,`Br/Hβ : ${fmt(s.angle)}° · ${s.reactive?'anti-périplanaires':'tourner autour de C3–C4'}`,25,h-64,w-50,s.reactive?CHEM.green:CHEM.red,13,19);
  wrap(ctx,'C3 avant : vert · C4 arrière : corail · Et = CH₂CH₃',25,h-22,w-50,CHEM.muted,11,15);
}
