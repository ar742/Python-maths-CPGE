"""Exemples exacts derrière les représentations finies d’ensembles infinis."""
from __future__ import annotations
import math
from decimal import Decimal,ROUND_FLOOR
from fractions import Fraction
import numpy as np
from commun import metric as m,series as s,chart as c,scene,result

def pack(metrics,charts,title,description,steps,assumptions,kind='geometry',**data):
    return result(metrics,charts,scene(kind,title,description,**data),steps,assumptions)

def path_(label,x,y,**kw):
    return dict(label=label,points=np.column_stack((x,y)),**kw)

def circle(r=1,n=241):
    theta=np.linspace(0,2*np.pi,n)
    return r*np.cos(theta),r*np.sin(theta)

def rational_enumeration(H):
    return [Fraction(p,q) for h in range(1,H+1) for q in range(1,h+1)
            for p in sorted(set([h-q,q-h])) if math.gcd(abs(p),q)==1]

def denombrer_rationnels(p):
    H,x=int(p['H']),p['target'];fractions=rational_enumeration(H)
    values=np.array([float(f) for f in fractions]);nearest=fractions[int(np.argmin(abs(values-x)))]
    heights=np.arange(1,H+1);counts=[len(rational_enumeration(h)) for h in heights]
    best=[min(abs(float(v)-x) for v in rational_enumeration(h)) for h in heights]
    pts=[dict(x=f.numerator,y=f.denominator,label=str(f),colorIndex=0) for f in fractions]
    return pack([m('Fractions distinctes dans le préfixe',len(fractions)),m('Plus proche fraction du préfixe',str(nearest)),m('Écart à la cible',abs(float(nearest)-x)),m('Cardinal de ℚ','ℵ₀ (preuve par énumération)')],
      [c('Le préfixe fini grandit','Hauteur |p|+q','Nombre de fractions',s('Fractions irréductibles',heights,counts)),c('Approcher un réel avec ce préfixe','Hauteur |p|+q','Meilleur écart observé',s('Distance au préfixe',heights,best))],
      'Des couples entiers aux rationnels','Un point représente une écriture irréductible p/q ; les signes et zéro sont inclus.',
      ['Classer les couples (p,q), q≥1, par hauteur |p|+q.','Garder gcd(|p|,q)=1 : chaque rationnel apparaît une fois.','Chaque étage est fini et tout rationnel finit par apparaître : ℚ est dénombrable.','Pour tout ε>0, choisir q>1/ε puis p=floor(qx), donc |x−p/q|<ε.'],
      ['Les points visibles constituent un préfixe fini ; les deux preuves utilisent tous les étages.','Cardinalité et densité sont deux propriétés différentes ; une partie finie de ℝ n’est jamais dense dans ℝ.'],points=pts,bounds=[-H,H,0,H+1],x_label='p',y_label='q')

def diagonale_cantor(p):
    N,seed=int(p['N']),int(p['seed']);table=np.random.default_rng(seed).integers(0,2,(N,N));anti=1-np.diag(table)
    weights=3.**(-np.arange(1,N+1));rows=2*table@weights;value=float(2*anti@weights)
    prefix=np.cumsum(2*anti*weights)
    return pack([m('Différences garanties',N),m('Préfixe ternaire diagonal',value),m('Largeur du cylindre restant',3.**(-N)),m('Cardinal de {0,1}^ℕ','Indénombrable')],
      [c('Réels associés aux lignes affichées','Numéro de ligne','Σ 2bⱼ/3ʲ',dict(s('Préfixes des lignes',np.arange(1,N+1),rows),style='dots')),c('Le préfixe diagonal se construit','Rang j','Somme ternaire partielle',s('Préfixe diagonal',np.arange(1,N+1),prefix))],
      'La ligne absente est construite','La case diagonale est changée : aᵢ=1−bᵢᵢ. Le tableau fini montre les premiers rangs de la preuve infinie.',
      ['Supposer qu’une liste indexée par ℕ contient toutes les suites binaires.','La suite aᵢ=1−bᵢᵢ diffère de la ligne i au moins au rang i.','La suite a n’apparaît donc dans aucune ligne de la liste infinie.','L’application b↦Σ2bⱼ/3ʲ est injective : au premier chiffre différent, la différence dominante dépasse la queue.'],
      ['Le tableau visible est fini ; l’indénombrabilité est prouvée par l’argument quantifié pour toutes les lignes.','Les chiffres ternaires sont 0 et 2 ; l’injection est justifiée même aux extrémités qui admettent une autre écriture avec un chiffre 1.'],kind='diagonal',matrix=table,anti=anti)

def cantor_intervals(level):
    intervals=[(0.,1.)];levels=[intervals]
    for _ in range(level):
        intervals=[v for a,b in intervals for v in [(a,a+(b-a)/3),(b-(b-a)/3,b)]]
        levels.append(intervals)
    return levels

def ensemble_cantor(p):
    k=int(p['level']);levels=cantor_intervals(k);chosen=int(p['address'])%2**k;a,b=levels[-1][chosen]
    ranks=np.arange(k+1)
    return pack([m('Segments à l’étape k',2**k),m('Longueur de chaque segment',3.**(-k)),m('Longueur totale à l’étape k',(2/3)**k),m('Adresse retenue',chosen),m('Cardinal du compact limite','2^ℵ₀')],
      [c('Des segments toujours plus petits','Étape k','Longueur',s('Longueur totale (2/3)^k',ranks,(2/3.)**ranks),s('Longueur individuelle 3^−k',ranks,3.**(-ranks))),c('Nombre de composantes des étapes finies','Étape k','Nombre de segments',s('2^k',ranks,2.**ranks))],
      'Retirer sans faire disparaître','Chaque ligne est une étape Kₖ. Le compact K est l’intersection de toutes les lignes, et non la dernière image.',
      ['Kₖ est une union finie de segments : fermé, borné et compact.','Les Kₖ sont emboîtés, contiennent 0 et 1 ; K=∩Kₖ est compact non vide.','Deux points distincts finissent dans des segments séparés : aucune partie connexe de K n’a deux points.','Chaque suite de chiffres 0 et 2 code un point de K : indénombrable, mais sans intervalle non trivial.'],
      ['Une étape finie contient encore des intervalles et est déjà indénombrable ; 2^k compte ses segments, pas ses points.','Au-delà : la dimension de Hausdorff du compact limite vaut log(2)/log(3).'],kind='cantor',levels=levels,selected=chosen,address_interval=[a,b])

def rationnels_irrationnels(p):
    x=p['target'];N=int(p['N']);xd=Decimal(str(x));indices=np.arange(1,N+1)
    q=[Fraction(int((xd*10**int(n)).to_integral_value(rounding=ROUND_FLOOR)),10**int(n)) for n in indices]
    qr=np.array([float(v) for v in q]);irr=qr+np.sqrt(2.)/10.**indices
    scale=10.**(-indices)
    return pack([m('Cible x',x),m('Dernier rationnel qₙ',str(q[-1])),m('Borne de l’erreur rationnelle',10.**(-N)),m('Borne de l’erreur irrationnelle',np.sqrt(2)*10.**(-N)),m('Intersection ℚ∩(ℝ∖ℚ)','Vide')],
      [c('Deux approximations de la même cible','Rang n','Valeur',s('qₙ rationnel',indices,qr),s('qₙ+√2/10ⁿ irrationnel',indices,irr),s('Cible x',indices,np.full(N,x))),c('Les bornes certifiées rétrécissent','Rang n','Borne absolue',s('10^−n',indices,scale),s('√2·10^−n',indices,np.sqrt(2)*scale),y_scale='log')],
      'Densité sans intersection','À chaque rang, un point rationnel et un point irrationnel approchent la même cible.',
      ['0≤x−qₙ<10^−n, par définition de la partie entière, même si x<0.','qₙ+√2/10ⁿ est irrationnel : autrement √2 serait rationnel.','Les deux suites convergent vers x. Comme la cible x est arbitraire, ℚ et ℝ∖ℚ sont denses dans ℝ.','Deux parties denses peuvent être disjointes. L’exercice 8 ajoute l’ouverture de l’une d’elles pour assurer une intersection dense.'],
      ['Les rationnels sont calculés exactement à partir de la valeur décimale du contrôle ; les tracés utilisent ensuite des flottants.','Les deux ensembles ont intérieur vide et adhérence ℝ. La densité de leur intersection n’est pas déduite de leurs seules densités.'],kind='density',rationals=qr,irrationals=irr,target=x)

def sinus_topologue(p):
    turns,y0=int(p['turns']),p['height'];u=np.linspace(1,2*np.pi*turns,min(640,turns*16+60));x=1/u;y=np.sin(u)
    n=np.arange(1,9);xn=1/(2*np.pi*n+np.arcsin(y0))
    return pack([m('Compact limite S','Oui'),m('Connexe','Oui, adhérence d’une courbe connexe'),m('Connexe par arcs','Non'),m('Distance horizontale du dernier témoin',xn[-1])],
      [c('Oscillations et segment d’adhérence','x','y',s('Courbe tronquée visible',x,y),s('Segment limite x=0',[0,0],[-1,1]),dict(s('Points tendant vers (0,y₀)',xn,np.full(len(n),y0)),style='dots')),c('Construire un point adhérent','Rang n','Abscisse xₙ',s('1/(2πn+arcsin y₀)',n,xn))],
      'Une connexité qui résiste aux chemins','La courbe oscillante s’approche de chaque hauteur du segment vertical. Aucun lien artificiel n’est tracé entre eux.',
      ['La courbe Γ est l’image continue de ]0,1] : elle est connexe.','Pour y₀∈[−1,1], choisir xₙ=1/(2πn+arcsin y₀) ; (xₙ,sin(1/xₙ))→(0,y₀).','S est exactement l’adhérence de Γ, donc connexe ; fermé et borné dans ℝ², donc compact.','Un chemin quittant le segment aurait une abscisse positive tendant vers 0 : les oscillations forcées de son ordonnée contredisent sa continuité.'],
      ['La courbe dessinée est tronquée ; ses propriétés ne sont pas celles de S, ensemble limite défini avec toutes les oscillations.','Exemple au-delà : connexe par arcs implique connexe ; la réciproque échoue même pour un compact de ℝ².'],paths=[path_('Courbe visible',x,y,colorIndex=0),path_('Segment d’adhérence',[0,0],[-1,1],colorIndex=1)],points=[dict(x=0,y=y0,label='Point adhérent',colorIndex=1)],bounds=[-.05,1.05,-1.2,1.2])

def rotations4(offset=0.):
    Q=np.eye(4)
    for i,j,angle in [(0,1,.43),(1,2,.68),(2,3,.31),(0,3,.52),(0,2,.29),(1,3,.37)]:
        G=np.eye(4);a=angle+offset;G[i,i]=G[j,j]=np.cos(a);G[i,j]=-np.sin(a);G[j,i]=np.sin(a);Q=Q@G
    return Q

Q4,R4=rotations4(),rotations4(.17)

def gl_composantes(p):
    real=p['field']=='real';t=p['t'];theta=np.deg2rad(p['angle']);lam=t if real else np.exp(1j*theta)
    A=Q4@np.diag([lam,1,2,3])@R4;det=6*lam;singular=np.linalg.svd(A,compute_uv=False)
    u=np.linspace(-2,2,241) if real else np.linspace(0,2*np.pi,241)
    z=6*u if real else 6*np.exp(1j*u)
    sign='Singulière' if real and t==0 else ('Positive' if t>0 else 'Négative') if real else 'Chemin complexe inversible'
    return pack([m('Déterminant : partie réelle',float(np.real(det))),m('Déterminant : partie imaginaire',float(np.imag(det))),m('Distance de Frobenius aux singulières',float(singular[-1])),m('État de la famille',sign),m('Dimension réelle de M₄(ℝ)',16)],
      [c('Le déterminant le long du chemin','t' if real else 'θ / rad','Partie du déterminant',s('Partie réelle',u,np.real(z)),s('Partie imaginaire',u,np.imag(z))),c('Valeurs singulières de A','Indice décroissant','σⱼ',dict(s('Valeurs singulières',np.arange(1,5),singular),style='stems'))],
      'Matrices denses et orientation','La matrice 4×4 est affichée en partie réelle ; les deux rotations fixes ont déterminant 1.',
      ['det A=det Q·λ·1·2·3·det R=6λ.','GL₄(ℝ)=det⁻¹(ℝ∖{0}) est ouvert ; le signe continu ne change pas le long d’un chemin inversible.','Pour la famille réelle, t=0 est la seule singularité. Pour λ=eⁱᶿ, |det A|=6 reste constant.','La plus petite valeur singulière mesure la distance de Frobenius à l’ensemble des matrices singulières (Eckart–Young).'],
      ['A est une matrice 4×4 ; l’affichage ne remplace pas le critère déterminant. Les valeurs singulières sont calculées numériquement.','GL₄⁺(ℝ) signifie det>0 ; SL₄(ℝ) signifie det=1. Ce sont des ensembles distincts.'],kind='matrix',matrix=A.real,imaginary=A.imag,matrix_label='Partie réelle de A',labels=['1','2','3','4'])

def orthogonal_compact(p):
    a=np.deg2rad(p['angle']);D=np.eye(4)
    for i,j,v in [(0,1,a),(2,3,.7*a)]:D[i,i]=D[j,j]=np.cos(v);D[i,j]=-np.sin(v);D[j,i]=np.sin(v)
    if p['orientation']=='negative':D[:,0]*=-1
    O=Q4@D@R4;T=p['T'];SL=Q4@np.diag([np.exp(T),np.exp(-T),1,1])@R4
    t=np.linspace(0,max(1,T),201)
    return pack([m('Erreur d’orthogonalité ‖OᵀO−I‖F',float(np.linalg.norm(O.T@O-np.eye(4)))),m('Déterminant de O',round(float(np.linalg.det(O)))),m('Norme de Frobenius de O',float(np.linalg.norm(O))),m('Norme de Frobenius dans SL₄',float(np.linalg.norm(SL))),m('Déterminant dans SL₄',float(np.linalg.det(SL)))],
      [c('Borné orthogonal, étirement spécial linéaire','t','Norme de Frobenius',s('O₄ : norme constante 2',t,np.full(len(t),2.)),s('SL₄ : √(e²ᵗ+e⁻²ᵗ+2)',t,np.sqrt(np.exp(2*t)+np.exp(-2*t)+2))),c('Deux spectra singuliers','Indice','Valeur singulière',dict(s('O',np.arange(1,5),np.linalg.svd(O,compute_uv=False)),style='dots'),dict(s('SL',np.arange(1,5),np.linalg.svd(SL,compute_uv=False)),style='dots'))],
      'La dimension finie rend la borne décisive','O₄ est fermé et toutes ses matrices ont norme de Frobenius 2 ; la famille de SL₄ s’étire sans borne.',
      ['O₄={O:OᵀO=I}, image réciproque d’un fermé par une application continue.','‖O‖F²=tr(OᵀO)=4 ; O₄ est donc fermé borné dans ℝ¹⁶, et compact.','SL₄={A:det A=1} est fermé. La famille affichée a norme au moins eᵗ : elle n’est pas bornée.','Les composantes det=±1 de O₄ sont fermées et ouvertes relativement à O₄.'],
      ['Les matrices affichées sont denses de taille 4×4 ; Q et R sont fixées dans SO₄.','La non-compacité de SL₄ résulte d’une famille pour tous t≥0, et non de la seule plage numérique visible.'],kind='matrix',matrix=O,secondary_matrix=SL,matrix_label='O, matrice orthogonale',labels=['1','2','3','4'])

def point_fixe(p):
    N,x0=int(p['N']),p['x0'];is_cos=p['family']=='cos';q=math.sin(1) if is_cos else abs(p['q']);f=math.cos if is_cos else lambda x:p['q']*x+.7
    seq=[x0]
    for _ in range(N):seq.append(f(seq[-1]))
    u=np.linspace(0,1,301) if is_cos else np.linspace(min(seq)-1,max(seq)+1,301)
    star=.7390851332151607 if is_cos else .7/(1-p['q']) if p['q']!=1 else None
    metrics=[m('Constante de Lipschitz q',q),m('Contraction démontrée',q<1),m('Dernier itéré',seq[-1])]
    if star is not None:metrics.append(m('Écart au point fixe de référence',abs(seq[-1]-star)))
    if q<1:metrics.append(m('Borne a posteriori',q*abs(seq[-1]-seq[-2])/(1-q)))
    else:metrics.append(m('Borne de Banach','Non applicable'))
    xs,ys=[],[]
    for a,b in zip(seq[:-1],seq[1:]):xs.extend([a,a,b]);ys.extend([a,b,b])
    charts=[c('Le graphe et les escaliers de l’itération','x','y',s('f(x)',u,[f(float(v)) for v in u]),s('y=x',u,u),s('Itération',xs,ys)),c('Suivre les valeurs','Rang n','xₙ',s('Itérés',np.arange(N+1),seq))]
    return pack(metrics,charts,'Des marches vers une équation','Les escaliers représentent xₙ₊₁=f(xₙ), avec une borne d’erreur seulement dans le régime contractant.',
      ['cos([0,1])⊂[0,1] et |cos′|≤sin(1)<1 : la restriction est une contraction.','Le segment fermé [0,1] est complet ; ℝ est complet pour l’application affine.','Si q<1, Banach assure un unique point fixe et la convergence de toute itération.','‖xₙ−x*‖≤q/(1−q)·‖xₙ−xₙ₋₁‖ ; sans contraction, le théorème ne conclut pas.'],
      ['Pour cos, le point fixe de référence est une approximation numérique ; la borne a posteriori est indépendante de cette référence.','Pour l’affine qx+0,7, q=1 n’a pas de point fixe ; |q|≥1 n’exclut pas un départ exactement stationnaire lorsque le point fixe existe.'],kind='iteration')

def cassini_paths(b):
    paths=[]
    if b<=1:
        alpha=.5*np.arcsin(min(1,b*b));theta=np.linspace(-alpha,alpha,161)
        disc=np.maximum(0,b**4-np.sin(2*theta)**2);outer=np.sqrt(np.maximum(0,np.cos(2*theta)+np.sqrt(disc)));inner=np.sqrt(np.maximum(0,np.cos(2*theta)-np.sqrt(disc)))
        if b==1:outer[[0,-1]]=0;inner[:]=0
        for sign in (1,-1):
            x=np.r_[outer*np.cos(theta),inner[::-1]*np.cos(theta[::-1])]*sign
            y=np.r_[outer*np.sin(theta),inner[::-1]*np.sin(theta[::-1])]*sign
            paths.append(path_('Ovale droit' if sign==1 else 'Ovale gauche',x,y,closed=True,fill=True,colorIndex=0 if sign==1 else 1))
    else:
        theta=np.linspace(0,2*np.pi,361);r=np.sqrt(np.cos(2*theta)+np.sqrt(b**4-np.sin(2*theta)**2))
        paths=[path_('Frontière unique',r*np.cos(theta),r*np.sin(theta),closed=True,fill=True,colorIndex=0)]
    return paths

def chemins_niveaux(p):
    b=p['b'];closed=p['closed']=='yes';components=2 if b<1 or b==1 and not closed else 1
    x=np.linspace(-2.2,2.2,601);f=(x*x-1)**2;paths=cassini_paths(b)
    for path in paths:path['dashed']=not closed
    return pack([m('Composantes connexes',components),m('Convexe','Non pour b≤1 ; au-delà à étudier séparément' if b<=1 else 'La connexité n’assure pas la convexité'),m('Ouvert de ℝ²',not closed),m('Compact',closed),m('L’origine appartient au sous-niveau',b>1 or b==1 and closed)],
      [c('Lire le passage sur l’axe réel','x','F(x,0)',s('F(x,0)=(x²−1)²',x,f),s('Niveau b⁴',x,np.full(len(x),b**4)))],
      'Deux lobes et un point décisif','F est continue ; le sous-niveau est ouvert avec <, fermé avec ≤. La frontière est calculée en coordonnées polaires.',
      ['F=(x²+y²)²−2(x²−y²)+1. F(0,y)=(y²+1)²≥1.','Si b<1, l’axe x=0 est exclu et sépare les deux lobes en ouverts relatifs non vides.','À b=1, le fermé contient l’origine : les deux lobes s’y rejoignent par arcs. Le sous-niveau strict l’exclut et garde deux composantes.','Pour b>1, les rayons depuis l’origine restent dans le sous-niveau ; il est étoilé et connexe par arcs.'],
      ['F(x,y)=((x−1)²+y²)((x+1)²+y²), foyers fixés (±1,0), b>0.','Les propriétés sont analytiques ; les polygones de bord sont seulement des approximations de dessin. Tous ces ensembles sont bornés ; les sous-niveaux stricts ne sont pas fermés.'],paths=paths,points=[dict(x=-1,y=0,label='Foyer −1',colorIndex=2),dict(x=1,y=0,label='Foyer +1',colorIndex=2),dict(x=0,y=0,label='Contact',colorIndex=1)],bounds=[-2.2,2.2,-1.8,1.8])

def homeomorphisme(p):
    n=int(p['n']);is_circle=p['family']=='circle';k=np.arange(2,n+1)
    if is_circle:
        theta=2*np.pi-1/k;distance=2*np.sin(1/(2*k));x,y=circle();probe=2*np.pi-1/n
        charts=[c('Au cercle, les images convergent vers 1','Rang n','Distance à 1',s('|eⁱᵗⁿ−1|=2sin(1/(2n))',k,distance)),c('L’inverse reste loin de 0','Rang n','tₙ / rad',s('2π−1/n',k,theta))]
        paths=[path_('Cercle',x,y,colorIndex=0)];points=[dict(x=1,y=0,label='1 = image de 0',colorIndex=1),dict(x=np.cos(probe),y=np.sin(probe),label='Image de tₙ',colorIndex=2)]
        metrics=[m('Bijection continue','Oui'),m('Domaine compact','Non'),m('Inverse continu','Non à 1'),m('Distance des images à 1',float(distance[-1]))]
        bounds=[-1.3,1.3,-1.3,1.3]
    else:
        t=np.linspace(-1,1,241);value=p['t'];charts=[c('Les trois coordonnées de l’injection','t','Coordonnée',s('x=t',t,t),s('y=t²',t,t*t),s('z=t³',t,t**3))]
        paths=[path_('Projection (t,t²)',t,t*t,colorIndex=0)];points=[dict(x=value,y=value*value,label='Point du segment',colorIndex=1)];bounds=[-1.3,1.3,-.15,1.3]
        metrics=[m('Domaine compact','Oui : [−1,1]'),m('Injection continue','Oui'),m('Inverse sur l’image','Projection première coordonnée'),m('Constante de Lipschitz de l’inverse',1)]
    return pack(metrics,charts,'Une couture ou un compact','La projection plane de la courbe cubique sert de repère ; l’application étudiée est bien à valeurs dans ℝ³.' if not is_circle else 'Les images se rapprochent, mais leurs antécédents tendent vers 2π, hors du domaine.',
      ['f:[0,2π[→S¹ est une bijection continue. Pour tₙ=2π−1/n, f(tₙ)→f(0), tandis que tₙ ne tend pas vers 0.','Une injection continue d’un compact dans un espace métrique est un homéomorphisme sur son image.','Pour g(t)=(t,t²,t³), la première coordonnée donne explicitement l’inverse continu.','Les hypothèses compact et injectif sont distinctes : sur [0,2π], l’enroulement n’est plus injectif.'],
      ['L’intervalle [0,2π[ est muni de sa topologie relative dans ℝ ; le cercle de celle induite par ℝ².','Les distances seules ne prouvent pas un homéomorphisme : on vérifie bijectivité et continuité dans les deux sens.'],paths=paths,points=points,bounds=bounds)

MODELS={name:globals()[name] for name in ['denombrer_rationnels','diagonale_cantor','ensemble_cantor','rationnels_irrationnels','sinus_topologue','gl_composantes','orthogonal_compact','point_fixe','chemins_niveaux','homeomorphisme']}
def calculate(lab_id,p):return MODELS[lab_id](p)
