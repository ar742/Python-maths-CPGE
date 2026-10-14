"""Calculs exacts lorsqu’ils sont disponibles, expériences complexes contrôlées."""
from __future__ import annotations
import math
import numpy as np
import sympy as sp
from commun import metric, chart, series, table, result, plane_scene, field_scene, point, formula, exact

Z = sp.Symbol('Z')

def ctext(z, digits=7):
    z=complex(z); a=0 if abs(z.real)<1e-13 else z.real; b=0 if abs(z.imag)<1e-13 else z.imag
    if b==0: return f'{a:.{digits}g}'
    return f'{a:.{digits}g} {"+" if b>=0 else "−"} {abs(b):.{digits}g}i'

def polynomial_text(c):
    return ' + '.join(f'({ctext(a)})Z^{len(c)-i-1}' if len(c)-i-1>0 else f'({ctext(a)})' for i,a in enumerate(c) if abs(a)>1e-13)

def box(points, extra=0.5):
    z=np.asarray(points,dtype=complex); lo=min(z.real.min(),z.imag.min()); hi=max(z.real.max(),z.imag.max())
    # A square preserves angles and circles in the complex plane.
    center=(lo+hi)/2; half=max(.6,(hi-lo)/2+extra)
    return [float(center-half),float(center+half),float(center-half),float(center+half)]

def roots_table(roots,title='Racines calculées'):
    return table(title,['k','Re(αₖ)','Im(αₖ)','|αₖ|'],[[k+1,float(z.real),float(z.imag),float(abs(z))] for k,z in enumerate(roots)])

def six_coefficients(p):
    return np.array([1,0,complex(p['ar'],p['ai']),0,1+1j,complex(p['br'],p['bi']),.5-.8j],complex)

def cauchy_radius(c):
    """Unique positive zero of r^n−sum |c_k/c_n|r^k; bisection monotone h."""
    a=np.abs(np.asarray(c,dtype=complex)[1:]/c[0]); n=len(a)
    if not np.any(a): return 0.
    lo=0.; hi=1+max(a)
    for _ in range(90):
        mid=(lo+hi)/2
        h=1-sum(a[j]/mid**(j+1) for j in range(n))
        if h>=0: hi=mid
        else: lo=mid
    return (lo+hi)/2

def cayley_tangentes(p):
    n=int(p['n']); ks=np.array([k for k in range(2*n) if k!=n]); roots=1j*np.tan(ks*np.pi/(2*n))
    roots[np.abs(roots)<1e-13]=0
    coefficients=[2*math.comb(2*n,j) if j%2 else 0 for j in range(1,2*n+1)]
    poly=sp.Poly((Z+1)**(2*n)-(Z-1)**(2*n),Z).as_expr().expand()
    imag=roots.imag; tangent_product=float((-1)**(n-1)); top=max(1.4,float(np.max(np.abs(imag)))+.3)
    w=np.exp(2j*np.pi*ks/(2*n))
    pts=[point(z,f'α{k}=i tan({k}π/{2*n})',0) for k,z in zip(ks,roots)]
    pts += [point(z,f'w{k}',1) for k,z in zip(ks,w)]
    return result([metric('Degré de Pₙ',2*n-1),metric('Coefficient dominant',4*n),metric('Somme des tangentes',0),metric('Produit des tangentes non nulles',int(tangent_product))],
        [chart('Tangentes finies : le terme k=n est exclu','Indice k','tan(kπ/(2n))',series('Tangentes',ks,imag),style='bars'),chart('Coefficients du polynôme Pₙ','Puissance de Z','Coefficient',series('Développement binomial',np.arange(0,2*n),coefficients[::-1]),style='bars')],
        plane_scene('Du cercle des wₖ à la droite des racines αₖ',pts,circles=[dict(x=0,y=0,r=1,label='|w|=1')],paths=[dict(label='Re(α)=0',x=[0,0],y=[-top,top])],bounds=[-top,top,-top,top],description='Les points wₖ sont les racines 2n-ièmes de l’unité; αₖ=(wₖ−1)/(wₖ+1). Le point wₙ=−1 n’a pas d’image finie.'),
        ['Poser w=(1+z)/(1−z). Pour w≠−1, z=(w−1)/(w+1)=i tan(kπ/(2n)).','Le terme de degré 2n s’annule dans Pₙ; celui de degré 2n−1 vaut 4n.',f'Pₙ(Z)={formula(poly)}. La factorisation est 4n∏(Z−αₖ), pour 0≤k<2n et k≠n.','Le coefficient de Z^{2n−2} est nul : la somme des tangentes vaut 0. Le coefficient de Z vaut 4n : le produit des racines non nulles vaut 1.'],
        ['n est un entier au moins égal à 2 dans ce laboratoire. Toutes les quantités sont sans unité.','k=n est exclu : tan(π/2) n’existe pas. Le produit omet aussi k=0, dont la tangente est nulle.'],
        table('Le changement de variable',['k','wₖ','αₖ'],[[int(k),ctext(a),ctext(b)] for k,a,b in zip(ks,w,roots)]))

def geometrique_affine(p):
    n=int(p['n']); c=complex(p['cx'],p['cy']); r=float(p['r']); k=np.arange(1,n+1)
    roots=c+r*np.exp(2j*np.pi*k/(n+1)); coeff=np.poly(roots)/r**n
    cx=exact(p['cx'])+sp.I*exact(p['cy']); rx=exact(r)
    value_c=sum(((Z-cx)/rx)**j for j in range(n+1)).expand()
    product=complex(np.prod(roots)); theta=np.linspace(0,2*np.pi,361); circle=c+r*np.exp(1j*theta)
    y=np.linspace(-2.2,2.2,301); line=c+r*y; val=np.polyval(coeff,line)
    return result([metric('Degré',n),metric('Coefficient dominant',r**(-n)),metric('Pₙ(c+r)',n+1),metric('Produit des racines',ctext(product))],
        [chart('Somme géométrique sur la droite z=c+rt','t réel','Valeur complexe',series('Re(Pₙ)',y,val.real),series('Im(Pₙ)',y,val.imag))],
        plane_scene('n racines sur le cercle; un point exclu',points=[point(z,f'α{k}',0) for k,z in zip(k,roots)]+[point(c,'Centre c',2),point(c+r,'c+r : pas une racine',1)],circles=[dict(x=c.real,y=c.imag,r=r,label='|z−c|=r')],bounds=box(np.r_[circle]),description='Les racines sont c+r exp(2ikπ/(n+1)), avec 1≤k≤n. Le point correspondant à k=0 est exclu.'),
        [f'Poser t=(Z−c)/r et Pₙ=1+t+⋯+t^n. Ici Pₙ(Z)={formula(value_c)}.','L’identité (1−t)Pₙ=1−t^{n+1} évite de résoudre un polynôme degré par degré.','t=1 donne Pₙ=n+1 : ce point n’est pas une racine. Les autres racines de l’unité donnent exactement n racines simples.',f'Pₙ(Z)=r^(−n)∏(Z−αₖ). Le coefficient dominant est {r**(-n):.7g}; le produit des racines est (−1)^n r^n Pₙ(0).'],
        ['c est un centre complexe et r>0 un rayon réel; toutes les quantités sont sans unité.','Le réglage c=−1, r=2 retrouve exactement l’exercice 5 de M17. Avec Im(c)≠0, les coefficients deviennent complexes.'],roots_table(roots))

def racines_coefficients(p):
    c=six_coefficients(p); roots=np.roots(c); rho=cauchy_radius(c); maximum=max(abs(roots)); lower=(2**(1/6)-1)*rho
    residual=np.abs(np.polyval(c,roots)); x=np.linspace(.1,max(1,rho*1.35),250); q=x**6-sum(abs(c[-1-j])*x**j for j in range(6))
    return result([metric('Rayon maximal des racines',float(maximum)),metric('Borne supérieure ρ de Cauchy',rho),metric('Borne inférieure (2¹/⁶−1)ρ',lower),metric('Résidu maximal |P(α)|',float(max(residual)))],
        [chart('L’équation réelle qui détermine ρ','Rayon r','Q(r)',series('Q(r)=r⁶−Σ|aₖ|rᵏ',x,q)),chart('Six racines calculées et leurs résidus','Indice de racine','|P(α)|',series('Résidu numérique',np.arange(1,7),residual),style='bars')],
        plane_scene('Un polynôme à coefficients réellement complexes',points=[point(z,f'α{k+1}',0) for k,z in enumerate(roots)],circles=[dict(x=0,y=0,r=rho,label='Borne de Cauchy ρ'),dict(x=0,y=0,r=lower,label='Borne inférieure du rayon maximal')],bounds=[-rho*1.12,rho*1.12,-rho*1.12,rho*1.12],description='Le grand disque contient les six racines. Le petit rayon borne le plus grand module; il ne borne pas chaque racine inférieurement.'),
        [f'P(Z)=Z⁶+aZ⁴+(1+i)Z²+bZ+(0,5−0,8i), avec a={ctext(c[2])} et b={ctext(c[5])}.','Q(r)=r⁶−Σₖ₌₀⁵|aₖ|rᵏ. La fonction Q(r)/r⁶ est strictement croissante sur r>0, de −∞ à 1 : elle a un unique zéro ρ.','Si P(α)=0, l’inégalité triangulaire donne |α|⁶≤Σ|aₖ||α|ᵏ, donc |α|≤ρ.','En notant M=max|αₖ|, Viète donne |aₖ|≤binom(6,k)M^{6−k}. On obtient ρ⁶≤(ρ+M)⁶−ρ⁶, donc M≥(2^{1/6}−1)ρ.'],
        ['Le polynôme est unitaire de degré 6 et possède des termes complexes fixes; il n’est jamais imposé réel.','Les racines affichées sont calculées numériquement. Les deux bornes reposent sur une preuve; un petit résidu ne mesure pas à lui seul l’erreur sur une racine multiple.'],roots_table(roots))

def rouche_disque(p):
    a=complex(p['ar'],p['ai']); b=complex(p['br'],p['bi']); R=p['r']; c=np.array([1,0,0,a,0,b]); roots=np.roots(c)
    magnitudes={5:R**5,2:abs(a)*R**2,0:abs(b)}; dominant=max(magnitudes,key=magnitudes.get); remainder=sum(magnitudes.values())-magnitudes[dominant]
    margin=magnitudes[dominant]-remainder; certified=margin>1e-12*max(1,sum(magnitudes.values()))
    numerical=int(sum(abs(z)<R-1e-8 for z in roots)); on_boundary=int(sum(abs(abs(z)-R)<=1e-8 for z in roots))
    theta=np.linspace(0,2*np.pi,481); z=R*np.exp(1j*theta); power={5:1,2:a,0:b}[dominant]; f=power*z**dominant; g=np.polyval(c,z)-f
    span=max(R,max(abs(roots)))*1.12
    return result([metric('Certificat sur le disque ouvert',f'{dominant} racines' if certified else 'Le critère ne conclut pas'),metric('Marge suffisante |f|−majorant(g)',float(margin)),metric('Comptage numérique à l’intérieur',numerical),metric('Racines proches de la frontière',on_boundary)],
        [chart('Une condition vérifiée sur tout le cercle','θ (rad)','Module',series('|f(Reⁱθ)|',theta,np.abs(f)),series('|g(Reⁱθ)| échantillonné',theta,np.abs(g)),series('Majorant uniforme de |g|',theta,np.full(len(theta),remainder)))],
        plane_scene('Racines de Z⁵+aZ²+b et disque de rayon R',points=[point(z,f'α{k+1}',0 if abs(z)<R else 1) for k,z in enumerate(roots)],circles=[dict(x=0,y=0,r=R,label='|z|=R')],bounds=[-span,span,-span,span],description='Le certificat utilise un majorant analytique sur le cercle entier. Les points calculés et la courbe échantillonnée servent à observer le résultat.'),
        [f'P(Z)=Z⁵+({ctext(a)})Z²+({ctext(b)}). Comparer les modules R⁵, |a|R² et |b|.',f'Choisir f(Z)=({ctext(power)})Z^{dominant}, g=P−f. Le majorant uniforme des autres termes vaut {remainder:.7g}.',f'La marge suffisante vaut {margin:.7g}. '+(f'Elle est strictement positive : le théorème de Rouché donne exactement {dominant} racines dans |z|<R, comptées avec multiplicité.' if certified else 'Elle n’est pas strictement positive : ce critère ne fournit aucun comptage. Cela ne contredit pas le calcul numérique.'),'Le théorème compare f et f+g lorsque |g|<|f| en tout point du cercle; vérifier une seule valeur de θ ne suffit pas.'],
        ['R>0; les coefficients a et b sont complexes. Les polynômes sont holomorphes sur le disque et son bord.','Rouché relève d’un prolongement d’analyse complexe. Une égalité de modules ne fournit pas le certificat strict utilisé ici.'],roots_table(roots))

def convex_hull(z):
    pairs=sorted(set((float(v.real),float(v.imag)) for v in z))
    def cross(o,a,b): return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
    low=[]; high=[]
    for a in pairs:
        while len(low)>=2 and cross(low[-2],low[-1],a)<=0: low.pop()
        low.append(a)
    for a in reversed(pairs):
        while len(high)>=2 and cross(high[-2],high[-1],a)<=0: high.pop()
        high.append(a)
    return np.array([complex(x,y) for x,y in low[:-1]+high[:-1]])

def gauss_lucas(p):
    roots=np.array([-2-1j,-1+2j,1.5+1.4j,2-.9j,complex(p['x'],p['y'])]); c=np.poly(roots); derivative=np.roots(np.polyder(c)); derivative=derivative[np.lexsort((derivative.imag,derivative.real))]
    hull=convex_hull(roots); j=int(p['j'])-1; beta=derivative[j]; distances=np.abs(beta-roots)
    if min(distances)>1e-8:
        weights=1/distances**2; weights/=sum(weights); barycenter=np.dot(weights,roots); bary_error=abs(barycenter-beta)
    else:
        weights=np.zeros(5); weights[np.argmin(distances)]=1; bary_error=0.
    outside=[]
    for z in derivative:
        outside.append(max(-((v2-v1).conjugate()*(z-v1)).imag/abs(v2-v1) for v1,v2 in zip(hull,np.roll(hull,-1))))
    return result([metric('Degré de P / de P′','5 / 4'),metric('Écart maximal hors du polygone',max(0.,float(max(outside)))),metric('Erreur du barycentre positif',float(bary_error)),metric('Racine β examinée',ctext(beta))],
        [chart('Les poids du barycentre de β','Indice de racine de P','Poids positif',series('λₖ : somme égale à 1',np.arange(1,6),weights),style='bars')],
        plane_scene('Racines de P, de P′ et enveloppe convexe',points=[point(z,f'α{k+1}',0) for k,z in enumerate(roots)]+[point(z,f'β{k+1}',1) for k,z in enumerate(derivative)],paths=[dict(label=f'β{j+1} vers α{k+1}',x=[beta.real,z.real],y=[beta.imag,z.imag]) for k,z in enumerate(roots)],polygons=[dict(label='Enveloppe convexe des αₖ',x=hull.real,y=hull.imag)],bounds=box(roots),description='Les racines αₖ déterminent P=∏(Z−αₖ), sans symétrie de conjugaison imposée. Les βₖ sont les racines de sa dérivée.'),
        ['Former P(Z)=∏ₖ₌₁⁵(Z−αₖ), puis calculer P′ et ses quatre racines.',f'Ici P(Z)={polynomial_text(c)}.','Pour P(β)≠0, P′(β)/P(β)=Σ1/(β−αₖ)=0. Après conjugaison, β est le barycentre des αₖ avec des poids proportionnels à 1/|β−αₖ|².','Ces poids sont positifs : β appartient à l’enveloppe convexe. Si P(β)=0, β est déjà une racine multiple de P et appartient aussi à cette enveloppe.'],
        ['Les racines peuvent se confondre; les multiplicité sont conservées dans le produit.','Le théorème de Gauss–Lucas est un prolongement accompagné. Le barycentre fournit une preuve; le dessin seul ne la remplace pas.'],table('Barycentre de la racine β examinée',['k','αₖ','Poids λₖ'],[[k+1,ctext(z),float(w)] for k,(z,w) in enumerate(zip(roots,weights))]))

def reciproque_conjugue(p):
    rho=float(p['rho']); mobile=rho*np.exp(1j*np.deg2rad(p['theta'])); roots=np.array([mobile,1.7+.4j,-.8+1.3j,-1.2-.9j,.3-1.6j]); c=(1+.4j)*np.poly(roots); star=np.conjugate(c[::-1]); trimmed=np.trim_zeros(star,'f'); mapped=np.array([1/np.conj(z) for z in roots if abs(z)>1e-14]); actual=np.roots(trimmed)
    paths=[dict(label=f'α{k+1} → 1/conj(α{k+1})',x=[z.real,(1/np.conj(z)).real],y=[z.imag,(1/np.conj(z)).imag]) for k,z in enumerate(roots) if abs(z)>1e-14]
    inverse_error=max([min(abs(z-actual)) for z in mapped]) if len(mapped) else 0
    pts=[point(z,f'α{k+1}',0) for k,z in enumerate(roots)]+[point(1/np.conj(z),f'α*{k+1}',1) for k,z in enumerate(roots) if abs(z)>1e-14]
    return result([metric('Degré de P',5),metric('Degré effectif de P*',len(trimmed)-1),metric('Racines finies de P*',len(mapped)),metric('Écart de correspondance numérique',float(inverse_error))],
        [chart('Inverser le module sans changer l’argument','Indice de racine non nulle','Module',series('|α|',[k+1 for k,z in enumerate(roots) if abs(z)>1e-14],[abs(z) for z in roots if abs(z)>1e-14]),series('1/|α|',[k+1 for k,z in enumerate(roots) if abs(z)>1e-14],[1/abs(z) for z in roots if abs(z)>1e-14]),style='bars')],
        plane_scene('Racines et images dans le cercle unité',points=pts,paths=paths,circles=[dict(x=0,y=0,r=1,label='|z|=1')],bounds=box(np.r_[roots,mapped]),description='Chaque segment relie une racine non nulle et son image sur le même rayon. Une racine nulle n’a pas d’image finie.'),
        ['Fixer le degré ambiant n=5. Si P(Z)=ΣaₖZᵏ, définir P*(Z)=Σconj(aₙ₋ₖ)Zᵏ.',f'P*(Z)={polynomial_text(trimmed)}. Pour z≠0 : P*(z)=z⁵ conj(P(1/conj(z))).','Toute racine α≠0 donne la racine 1/conj(α). Les modules s’inversent; les arguments restent égaux.',('Une racine nulle fait perdre un degré à P*. Le double retournement du vecteur de six coefficients retrouve P; avec le degré effectif 4 au second retournement, on retrouve seulement P/Z.' if rho==0 else 'Le terme constant est non nul : P* garde le degré 5 et (P*)*=P avec la convention de degré usuelle.')],
        ['P a cinq racines données et un coefficient dominant 1+0,4i. Le symbole * désigne ici le réciproque conjugué.','Pour des coefficients réels, cette définition devient le réciproque usuel; pour des coefficients complexes, la conjugaison est essentielle.'],table('Coefficients avant et après retournement',['Puissance k','Coefficient de P','Coefficient de P*'],[[k,ctext(c[5-k]),ctext(star[5-k])] for k in range(6)]))

def newton_sums(c,m):
    n=len(c)-1; a=np.asarray(c,dtype=complex)/c[0]; sums=[]
    for k in range(1,m+1):
        value=-sum(a[j]*sums[k-j-1] for j in range(1,min(k,n+1)))
        if k<=n: value-=k*a[k]
        sums.append(value)
    return np.array(sums)

def viete_newton(p):
    c=six_coefficients(p); roots=np.roots(c); m=int(p['m']); powers=np.arange(1,9); sums=newton_sums(c,8); direct=np.array([sum(roots**k) for k in powers]); product=np.prod(roots)
    return result([metric(f'Somme s{m}',ctext(sums[m-1])),metric('Somme des racines s₁',ctext(sums[0])),metric('Produit des six racines',ctext(c[-1])),metric('Écart maximal, sommes calculées',float(max(abs(sums-direct))))],
        [chart('Sommes de puissances : parties réelle et imaginaire','Puissance k','sₖ',series('Re(sₖ), identités de Newton',powers,sums.real),series('Im(sₖ), identités de Newton',powers,sums.imag),style='bars')],
        plane_scene('Six racines et leur centre de gravité',points=[point(z,f'α{k+1}',0) for k,z in enumerate(roots)]+[point(sum(roots)/6,'Moyenne des racines',1)],bounds=box(roots),description='Le coefficient de Z⁵ est nul : la moyenne des six racines vaut zéro, même lorsque les racines ne sont pas symétriques.'),
        [f'P(Z)=Z⁶+aZ⁴+(1+i)Z²+bZ+(0,5−0,8i), avec a={ctext(c[2])} et b={ctext(c[5])}.','Écrire P=Z⁶+c₁Z⁵+⋯+c₆ et sₖ=Σαⱼᵏ. Pour 1≤k≤6 : sₖ+c₁sₖ₋₁+⋯+cₖ₋₁s₁+kcₖ=0.','Pour k>6 : sₖ+c₁sₖ₋₁+⋯+c₆sₖ₋₆=0. Ces relations fonctionnent sur ℂ comme sur ℝ.','Viète donne Σαⱼ=−c₁=0 et ∏αⱼ=c₆=0,5−0,8i. Les sommes sont calculées à partir des coefficients puis comparées aux racines numériques.'],
        ['Les six racines sont comptées avec multiplicité. Toutes les grandeurs sont sans unité.','Les identités de Newton sont exactes; les deux évaluations flottantes peuvent différer légèrement.'],table('Coefficients ou racines : deux voies',['k','Newton à partir des coefficients','Somme directe sur les racines','Écart'],[[int(k),ctext(a),ctext(b),float(abs(a-b))] for k,a,b in zip(powers,sums,direct)]))

def newton_family(name):
    if name=='carre': return .3+.4j+np.exp(2j*np.pi*np.arange(4)/4)
    return np.array([-1.5-.8j,-.3+1.4j,1.5+.5j,.3-1.5j])

def newton_bassins(p):
    roots=newton_family(p['family']); c=np.poly(roots); dc=np.polyder(c); n=int(p['grid']); it=int(p['iterations']); span=float(p['zoom']); axis=np.linspace(-span,span,n); xx,yy=np.meshgrid(axis,axis); z=xx+1j*yy; active=np.ones(z.shape,dtype=bool); singular=np.zeros(z.shape,dtype=bool)
    for _ in range(it):
        f=np.polyval(c,z); d=np.polyval(dc,z); close=np.min(abs(z[...,None]-roots),axis=2)<1e-6
        bad=active & ((abs(d)<1e-13)|(abs(z)>1e6)); singular|=bad; active &= ~bad & ~close
        if not np.any(active): break
        z[active]-=f[active]/d[active]
    dist=abs(z[...,None]-roots); classes=np.argmin(dist,axis=2); classes[np.min(dist,axis=2)>=1e-6]=4; classes[singular]=4
    selected=complex(p['x0'],p['y0']); orbit=[selected]; residuals=[float(abs(np.polyval(c,selected)))]; stopped=False
    for _ in range(it):
        value=np.polyval(c,selected); derivative=np.polyval(dc,selected)
        if abs(value)<1e-13: break
        if abs(derivative)<1e-13 or abs(selected)>1e4: stopped=True; break
        selected-=value/derivative; orbit.append(selected); residuals.append(float(abs(np.polyval(c,selected))))
    counts=[int(np.sum(classes==k)) for k in range(5)]; orbit=np.array(orbit)
    scene=field_scene('Bassins numériques de Newton pour un polynôme complexe',axis,axis,classes,points=[point(z,f'α{k+1}',k) for k,z in enumerate(roots)],paths=[dict(label='Orbite du point choisi',x=orbit.real,y=orbit.imag)],levels=[],categorical=True,labels=['Racine α₁','Racine α₂','Racine α₃','Racine α₄','Non classé'],description='Chaque couleur indique une racine atteinte à 10⁻⁶ près. Gris : aucune racine classée après le nombre fixé d’itérations, ou dérivée trop petite. Le maillage ne prouve pas la forme exacte des frontières.')
    scene['xLabel']='Re(z₀)'; scene['yLabel']='Im(z₀)'
    return result([metric('Points classés après les itérations',100*(1-counts[-1]/(n*n)),'%'),metric('Points non classés',counts[-1]),metric('Arrêt de l’orbite suivie','Dérivée nulle ou excursion' if stopped else ('Racine atteinte' if min(abs(selected-roots))<1e-6 else 'Limite d’itérations')),metric('Dernier |P(zₖ)| de l’orbite',residuals[-1])],
        [chart('Convergence de l’orbite suivie','Itération k','|P(zₖ)|',series('Résidu (plancher graphique 10⁻¹⁶)',np.arange(len(residuals)),np.maximum(1e-16,residuals)),y_scale='log')],
        scene,
        [f'P(Z)={polynomial_text(c)}. Les racines sont fixées avant le calcul des bassins.','La méthode de Newton est zₖ₊₁=zₖ−P(zₖ)/P′(zₖ). Elle exige P′(zₖ)≠0.','Pour chaque point du maillage, on effectue au plus N itérations et on cherche une racine à distance inférieure à 10⁻⁶.','Une racine simple attire localement les points proches avec convergence quadratique. Un dessin fini ne classe pas tous les points du plan et ne démontre pas une convergence globale.'],
        ['Les coefficients sont complexes et les quatre racines simples. Newton dans le plan complexe est un prolongement numérique accompagné.','Les points non classés constituent une cinquième catégorie explicite; ils ne sont jamais forcés dans un bassin.'],table('Comptage sur le maillage',['Catégorie','Nombre de points'],[[f'α{k+1}' if k<4 else 'Non classé',v] for k,v in enumerate(counts)]))

def conditionnement_racines(p):
    delta=float(p['delta']); epsilon=10.**int(p['exponent']); phi=np.deg2rad(p['theta']); eta=epsilon*np.exp(1j*phi); center=.2+.3j; fixed=np.array([-2+.4j,1.7+1.3j,1-1.9j]); square=np.sqrt(delta**2+eta+0j); initial=np.array([center+delta,center-delta]); changed=np.array([center+square,center-square]); c=np.polymul(np.array([1,-2*center,center**2-delta**2-eta]),np.poly(fixed)); numerical=np.roots(c); analytic=np.r_[changed,fixed]
    shift=min(max(abs(changed-initial)),max(abs(changed-initial[::-1]))); numeric_error=max(min(abs(z-numerical)) for z in analytic)
    eps=np.logspace(-12,-2,121); d=np.sqrt(delta**2+eps*np.exp(1j*phi)); moves=np.minimum(abs(d-delta),abs(d+delta)); cur=[series('Déplacement exact de la paire',eps,np.maximum(1e-16,moves))]
    if delta>0: cur.append(series('Premier ordre ε/(2δ)',eps,eps/(2*delta)))
    else: cur.append(series('√ε pour la racine double',eps,np.sqrt(eps)))
    scale=max(.01,delta,abs(square))*1.6
    return result([metric('Déplacement exact de chaque racine',float(shift)),metric('Estimation ε/(2δ)',epsilon/(2*delta) if delta>0 else 'Non définie : racine double'),metric('Rapport ε/δ²',epsilon/delta**2 if delta>0 else 'Non défini'),metric('Écart des racines numériques',float(numeric_error))],
        [chart('Loi linéaire ou loi racine carrée ?','Module ε de la perturbation','Déplacement',*cur,x_scale='log',y_scale='log')],
        plane_scene('Vue agrandie de la paire qui se sépare',points=[point(z,f'α{k+1} avant',0) for k,z in enumerate(initial)]+[point(z,f'α{k+1} après',1) for k,z in enumerate(changed)],paths=[dict(label='Déplacement de la racine',x=[initial[k].real,changed[k].real],y=[initial[k].imag,changed[k].imag]) for k in range(2)],bounds=[center.real-scale,center.real+scale,center.imag-scale,center.imag+scale],description='Les trois autres racines du polynôme de degré 5 restent fixes, hors de ce cadrage. La perturbation agit dans le facteur quadratique; son argument peut être non nul.'),
        ['Poser c=0,2+0,3i et Q(Z)=(Z−(−2+0,4i))(Z−(1,7+1,3i))(Z−(1−1,9i)). Pδ=[(Z−c)²−δ²]Q(Z).',f'La perturbation est η=εe^(iφ)={ctext(eta)}. Pδ,η=[(Z−c)²−δ²−η]Q(Z). Les deux racines mobiles sont exactement c±√(δ²+η).','Si δ>0 et |η|≪δ², √(δ²+η)=δ+η/(2δ)+O(|η|²/δ³). La sensibilité croît donc lorsque δ diminue.','Si δ=0, la racine double se sépare de √|η|. Le premier ordre en η n’est plus valable; un résidu très petit peut alors masquer une erreur notable sur une racine.'],
        ['La perturbation du polynôme est −ηQ(Z), et non une constante ajoutée à Pδ.','La formule exacte sur le facteur quadratique sert de référence indépendante au calcul flottant de degré 5.'],table('Formule exacte et calcul numérique',['Racine exacte','Racine numérique la plus proche','Écart'],[[ctext(z),ctext(numerical[np.argmin(abs(numerical-z))]),float(min(abs(numerical-z)))] for z in analytic]))

def recurrence_coefficients(n,lam=1):
    if n==0: return np.array([1.],complex)
    a=np.array([1.],complex); b=np.array([2*lam,0],complex)
    for _ in range(n-1): a,b=b,np.polyadd(-lam*np.polymul([1,0],b),-a)
    return b

def recurrence_value(n,t):
    if n==0: return 1+0j
    a=1+0j; b=2*t
    for _ in range(n-1): a,b=b,-t*b-a
    return b

def characteristic_value(n,t):
    discriminant=t*t-4; rplus=(-t+np.sqrt(discriminant+0j))/2; rminus=(-t-np.sqrt(discriminant+0j))/2
    if abs(rplus-rminus)<1e-12: return (1-5*n)*rplus**n, [rplus,rminus], True
    A=(2*t-rminus)/(rplus-rminus); B=1-A
    return A*rplus**n+B*rminus**n,[rplus,rminus],False

def recurrence_complexe(p):
    n=int(p['n']); lam=np.exp(1j*np.deg2rad(p['theta'])); z=complex(p['x'],p['y']); t=lam*z; c=recurrence_coefficients(n,lam); roots=np.roots(c); value=recurrence_value(n,t); closed,characteristic,double=characteristic_value(n,t); indices=np.arange(n+1); values=np.array([recurrence_value(k,t) for k in indices]); x=np.linspace(-2.5,2.5,251); real_line=np.polyval(c,x)
    return result([metric('Degré',n),metric('Pₙ(z) par récurrence',ctext(value)),metric('Racines caractéristiques','Double' if double else 'Distinctes'),metric('Écart relatif, formule fermée',float(abs(closed-value)/max(1,abs(value))))],
        [chart('Pₙ sur l’axe réel : coefficients complexes','x réel','Pₙ(x)',series('Re(Pₙ(x))',x,real_line.real),series('Im(Pₙ(x))',x,real_line.imag)),chart('Valeurs successives au point z choisi','Rang k','Pₖ(z)',series('Partie réelle',indices,values.real),series('Partie imaginaire',indices,values.imag))],
        plane_scene('Racines du polynôme Pₙ',points=[point(a,f'α{k+1}',0) for k,a in enumerate(roots)],bounds=box(roots),description='La phase de λ fait tourner les racines : Pₙ,λ(Z)=Pₙ,1(λZ). Cette famille conserve exactement les données initiales de l’exercice 6.'),
        ['λ=e^(iθ), P₀=1, P₁=2λZ et Pₖ₊₂+λZPₖ₊₁+Pₖ=0. Le réglage λ=1 retrouve la fiche.',f'Au point z={ctext(z)}, poser t=λz={ctext(t)}. L’équation caractéristique est r²+tr+1=0.',('Les racines sont confondues : r=−t/2 et Pₙ(z)=(1−5n)rⁿ. La forme Arⁿ+Brⁿ ne comporte plus deux solutions indépendantes.' if double else f'Les racines sont r₊={ctext(characteristic[0])}, r₋={ctext(characteristic[1])}. Pₙ=Ar₊ⁿ+Br₋ⁿ, avec A=(2t−r₋)/(r₊−r₋) et B=1−A.'),'Le calcul direct par récurrence évite la division par r₊−r₋ au voisinage d’une racine double. Les valeurs initiales fixent la famille : elles ne sont pas celles des Tchebychev usuels.'],
        ['n est un entier et z, λ sont complexes sans unité. Ici |λ|=1.','La récurrence définit un polynôme même quand la formule caractéristique change de forme. La représentation graphique n’est pas une preuve de factorisation.'],roots_table(roots))

COMPUTE={name:globals()[name] for name in ['cayley_tangentes','geometrique_affine','racines_coefficients','rouche_disque','gauss_lucas','reciproque_conjugue','viete_newton','newton_bassins','conditionnement_racines','recurrence_complexe']}
