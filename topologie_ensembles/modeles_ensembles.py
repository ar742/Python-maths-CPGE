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
    return pack([m('Fractions distinctes dans la liste affichée',len(fractions)),m('Fraction affichée la plus proche de x',str(nearest)),m('Écart à la cible',abs(float(nearest)-x)),m('Ensemble ℚ','Dénombrable : ses éléments peuvent être listés')],
      [c('La liste de fractions s’allonge','Limite de |p|+q','Nombre de fractions',s('Fractions irréductibles',heights,counts)),c('Chercher une fraction plus proche de x','Limite de |p|+q','Meilleur écart observé',s('Distance à la liste affichée',heights,best))],
      'Des couples entiers aux rationnels','Un point représente une écriture irréductible p/q ; les signes et zéro sont inclus.',
      ['Ranger les fractions p/q par valeurs croissantes de |p|+q, avec q≥1. À chaque valeur, il n’y a qu’un nombre fini de couples à examiner.','Garder les fractions irréductibles, c’est-à-dire PGCD(|p|,q)=1 : chaque rationnel apparaît une seule fois.','Tout rationnel est rencontré à une étape finie. La liste infinie contient donc exactement ℚ : c’est le sens de dénombrable.','Pour approcher n’importe quel réel x à ε près, choisir q>1/ε, puis p=⌊qx⌋ (partie entière). On obtient |x−p/q|<ε : c’est la densité de ℚ dans ℝ.'],
      ['Le dessin montre une liste finie. La dénombrabilité et la densité s’établissent en considérant toutes les étapes de la construction.','MPSI : densité des rationnels. MP : dénombrabilité de ℚ ; la démonstration est non exigible. Une liste finie ne peut pas être dense dans tout ℝ.'],points=pts,bounds=[-H,H,0,H+1],x_label='p',y_label='q')

def diagonale_cantor(p):
    N,seed=int(p['N']),int(p['seed']);table=np.random.default_rng(seed).integers(0,2,(N,N));anti=1-np.diag(table)
    weights=3.**(-np.arange(1,N+1));rows=2*table@weights;value=float(2*anti@weights)
    prefix=np.cumsum(2*anti*weights)
    return pack([m('Lignes distinguées par la diagonale',N),m('Somme obtenue avec les N premiers chiffres',value),m('Longueur de l’intervalle des valeurs encore possibles',3.**(-N)),m('Ensemble des suites de zéros et de uns','Indénombrable : aucune liste ne les contient toutes')],
      [c('Réels approchés par les lignes du tableau','Numéro de ligne','Σ 2bⱼ/3ʲ',dict(s('Sommes des N premiers chiffres',np.arange(1,N+1),rows),style='dots')),c('Construire le réel associé à la nouvelle ligne','Rang j','Somme des j premiers termes',s('Somme pour la nouvelle ligne',np.arange(1,N+1),prefix))],
      'Changer un chiffre de chaque ligne','La ligne du bas reprend les chiffres de la diagonale en remplaçant 0 par 1 et 1 par 0 : aᵢ=1−bᵢᵢ.',
      ['Raisonner par l’absurde : supposer qu’une liste numérotée par ℕ contient toutes les suites de zéros et de uns.','Construire aᵢ=1−bᵢᵢ. Au rang i, a diffère de la ligne i : cette ligne ne peut donc pas être a.','Cela vaut pour chaque ligne de la liste infinie. La suite a a été oubliée, ce qui contredit l’hypothèse.','Associer à b le réel Σ2bⱼ/3ʲ (écriture en base 3). Deux suites différentes donnent deux réels différents : l’écart au premier chiffre différent dépasse la somme maximale des écarts suivants.'],
      ['Le tableau fini permet de comprendre la construction ; la démonstration concerne une infinité de lignes et de chiffres. En MP, la non-dénombrabilité de ℝ est au programme, mais sa démonstration n’est pas exigible.','Écrire les réels en base 3 avec les chiffres 0 et 2 évite l’ambiguïté des écritures binaires. La comparaison des sommes prouve directement que l’application est injective.'],kind='diagonal',matrix=table,anti=anti)

def cantor_intervals(level):
    intervals=[(0.,1.)];levels=[intervals]
    for _ in range(level):
        intervals=[v for a,b in intervals for v in [(a,a+(b-a)/3),(b-(b-a)/3,b)]]
        levels.append(intervals)
    return levels

def ensemble_cantor(p):
    k=int(p['level']);levels=cantor_intervals(k);chosen=int(p['address'])%2**k;a,b=levels[-1][chosen]
    ranks=np.arange(k+1)
    return pack([m('Segments à l’étape k',2**k),m('Longueur de chaque segment',3.**(-k)),m('Longueur totale à l’étape k',(2/3)**k),m('Numéro du segment sélectionné (à partir de 0)',chosen),m('Ensemble de Cantor','Indénombrable : autant de points que ℝ')],
      [c('Des segments toujours plus petits','Étape k','Longueur',s('Longueur totale (2/3)^k',ranks,(2/3.)**ranks),s('Longueur individuelle 3^−k',ranks,3.**(-ranks))),c('Nombre de composantes des étapes finies','Étape k','Nombre de segments',s('2^k',ranks,2.**ranks))],
      'Les points qui ne sont jamais retirés','La ligne k représente les segments encore présents après k étapes. L’ensemble de Cantor est l’intersection de toutes les étapes : il faut rester dans chaque ligne pour lui appartenir.',
      ['À une étape fixée, Kₖ est une réunion finie de segments fermés. Il est fermé et borné dans ℝ, donc compact par le critère de MP.','Les Kₖ contiennent toujours 0 et 1 et sont inclus les uns dans les autres. Leur intersection est fermée et bornée, donc compacte et non vide.','Deux points distincts de l’ensemble final sont séparés par un intervalle retiré. Aucun chemin continu à valeurs dans ℝ ne peut les relier sans traverser cet intervalle : utiliser le théorème des valeurs intermédiaires.','Les écritures en base 3 utilisant seulement 0 et 2 donnent encore une infinité indénombrable de points. L’ensemble ne contient pourtant aucun intervalle de longueur positive.'],
      ['Ce prolongement réutilise compacité et valeurs intermédiaires. Une étape finie est déjà indénombrable : 2^k compte les segments, jamais leurs points.','Le numéro choisi sélectionne un des 2^k segments, en revenant au début si nécessaire. Prolongement plus avancé : la dimension de Hausdorff (une notion de dimension fractale) vaut log(2)/log(3).'],kind='cantor',levels=levels,selected=chosen,address_interval=[a,b])

def rationnels_irrationnels(p):
    x=p['target'];N=int(p['N']);xd=Decimal(str(x));indices=np.arange(1,N+1)
    q=[Fraction(int((xd*10**int(n)).to_integral_value(rounding=ROUND_FLOOR)),10**int(n)) for n in indices]
    qr=np.array([float(v) for v in q]);irr=qr+np.sqrt(2.)/10.**indices
    scale=10.**(-indices)
    return pack([m('Cible x',x),m('Dernier rationnel qₙ',str(q[-1])),m('Borne de l’erreur rationnelle',10.**(-N)),m('Borne de l’erreur irrationnelle',np.sqrt(2)*10.**(-N)),m('Intersection ℚ∩(ℝ∖ℚ)','Vide')],
      [c('Deux approximations de la même cible','Rang n','Valeur',s('qₙ rationnel',indices,qr),s('qₙ+√2/10ⁿ irrationnel',indices,irr),s('Cible x',indices,np.full(N,x))),c('Les majorations d’erreur tendent vers zéro','Rang n','Majoration de |approximation−x|',s('10^−n',indices,scale),s('√2·10^−n',indices,np.sqrt(2)*scale),y_scale='log')],
      'Deux façons d’approcher le même réel','À chaque rang, on choisit un rationnel et un irrationnel. Tous deux se rapprochent du réel x ; ils restent dans deux ensembles disjoints.',
      ['Poser qₙ=⌊10ⁿx⌋/10ⁿ, où ⌊·⌋ est la partie entière : qₙ est une approximation décimale par défaut et 0≤x−qₙ<10^−n, même pour x négatif.','Ajouter √2/10ⁿ à qₙ donne un irrationnel. Sinon, en soustrayant qₙ et en multipliant par 10ⁿ, on conclurait à tort que √2 est rationnel.','Les erreurs tendent vers zéro, donc les deux suites convergent vers x. La construction marche pour tout réel x : ℚ et ℝ∖ℚ sont denses dans ℝ.','L’intersection de ces deux ensembles est vide. Pour obtenir une intersection dense dans l’exercice 8 du recueil, il faut aussi que l’un des deux ensembles soit ouvert.'],
      ['MPSI : approximations décimales et densité. MP : caractérisation de l’adhérence par les suites. Les fractions sont calculées exactement à partir du nombre entré ; l’écran affiche des approximations numériques.','Tout intervalle ouvert contient des éléments des deux ensembles. Ils ont donc tous deux pour adhérence ℝ, mais un intérieur vide : aucun intervalle ouvert ne peut être entièrement contenu dans l’un d’eux.'],kind='density',rationals=qr,irrationals=irr,target=x)

def sinus_topologue(p):
    turns,y0=int(p['turns']),p['height'];u=np.linspace(1,2*np.pi*turns,min(640,turns*16+60));x=1/u;y=np.sin(u)
    n=np.arange(1,9);xn=1/(2*np.pi*n+np.arcsin(y0))
    return pack([m('Ensemble S compact','Oui : fermé et borné dans ℝ²'),m('Ensemble S connexe (prolongement)','Oui : adhérence d’une courbe connexe'),m('Ensemble S connexe par arcs','Non : aucun chemin dans S ne relie l’axe au graphe'),m('Abscisse du dernier point approchant (0,y₀)',xn[-1])],
      [c('Oscillations et segment d’adhérence','x','y',s('Courbe tronquée visible',x,y),s('Segment limite x=0',[0,0],[-1,1]),dict(s('Points tendant vers (0,y₀)',xn,np.full(len(n),y0)),style='dots')),c('Construire un point adhérent','Rang n','Abscisse xₙ',s('1/(2πn+arcsin y₀)',n,xn))],
      'Ajouter tous les points limites du graphe','Quand x se rapproche de zéro, le graphe approche chaque point du segment vertical. La possibilité d’approcher un point par une suite ne donne pas un chemin continu jusqu’à lui.',
      ['Le graphe Γ est parcouru continûment par x↦(x,sin(1/x)), pour 0<x≤1 : il est connexe par arcs.','Pour approcher (0,y₀), prendre xₙ=1/(2πn+arcsin y₀). Alors xₙ→0 et sin(1/xₙ)=y₀ : on obtient une suite du graphe convergeant vers le point voulu.','Ajouter le segment vertical donne exactement l’adhérence S de Γ. S est fermé et borné dans ℝ², donc compact. En prolongement, l’adhérence d’un ensemble connexe est connexe.','Un chemin allant du segment au graphe devrait avoir une abscisse positive se rapprochant de zéro. Le théorème des valeurs intermédiaires imposerait à son ordonnée des oscillations de −1 à 1, incompatibles avec sa continuité au point de départ du graphe.'],
      ['Seules certaines oscillations sont dessinées. L’ensemble S étudié contient le graphe entier et le segment vertical : sa compacité ne résulte pas de l’apparence du dessin.','MP : chemin continu, connexité par arcs, adhérence séquentielle, fermé et borné. La connexité générale, définie par l’absence de séparation en deux ouverts relatifs non vides, est expliquée ici en prolongement.'],paths=[path_('Courbe visible',x,y,colorIndex=0),path_('Points limites sur l’axe vertical',[0,0],[-1,1],colorIndex=1)],points=[dict(x=0,y=y0,label='Point adhérent',colorIndex=1)],bounds=[-.05,1.05,-1.2,1.2])

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
    sign='Non inversible : déterminant nul' if real and t==0 else ('Déterminant positif' if t>0 else 'Déterminant négatif') if real else 'Matrice complexe inversible'
    return pack([m('Déterminant : partie réelle',float(np.real(det))),m('Déterminant : partie imaginaire',float(np.imag(det))),m('Distance aux matrices non inversibles (norme de Frobenius)',float(singular[-1])),m('Situation de la matrice affichée',sign),m('Pour comparaison : dimension réelle de M₄(ℝ)',16)],
      [c('Le déterminant le long du chemin','t' if real else 'θ / rad','Partie du déterminant',s('Partie réelle',u,np.real(z)),s('Partie imaginaire',u,np.imag(z))),c('Valeurs singulières de A','Indice décroissant','σⱼ',dict(s('Valeurs singulières',np.arange(1,5),singular),style='stems'))],
      'Suivre l’inversibilité par le déterminant','Q et R sont deux matrices de rotation fixées de déterminant 1. Elles rendent A non diagonale sans changer det A=6λ. Pour une matrice complexe, les parties réelle et imaginaire sont affichées séparément si nécessaire.',
      ['Utiliser det(AB)=det A·det B : det A=det Q·λ·1·2·3·det R=6λ. Ainsi A est inversible exactement quand λ≠0.','La fonction déterminant est continue. L’ensemble GL₄(ℝ) est l’image réciproque de l’ouvert ℝ∖{0}, donc un ouvert : c’est une technique du cours de MP.','Sur un chemin de matrices réelles inversibles, le déterminant ne peut pas passer du positif au négatif : le théorème des valeurs intermédiaires imposerait un zéro. Avec λ=eⁱᶿ, le module |det A|=6 reste au contraire constant.','L’indicateur de distance utilise la plus petite valeur singulière, racine carrée de la plus petite valeur propre de A* A (A* est la transposée conjuguée). Le théorème d’Eckart–Young justifiant cette distance est un prolongement numérique.'],
      ['MPSI : déterminant et nombres complexes. MP : continuité d’une application polynomiale et image réciproque d’un ouvert. La norme de Frobenius est √(Σ|aᵢⱼ|²), soit la norme euclidienne des 16 coefficients.','GL₄⁺(ℝ) désigne det>0 ; SL₄(ℝ) désigne det=1. Passer de 1 à −1 sur le cercle complexe compare deux matrices complexes inversibles, sans attribuer un signe au déterminant complexe.'],kind='matrix',matrix=A.real,imaginary=A.imag,matrix_label='Partie réelle de A',labels=['1','2','3','4'])

def orthogonal_compact(p):
    a=np.deg2rad(p['angle']);D=np.eye(4)
    for i,j,v in [(0,1,a),(2,3,.7*a)]:D[i,i]=D[j,j]=np.cos(v);D[i,j]=-np.sin(v);D[j,i]=np.sin(v)
    if p['orientation']=='negative':D[:,0]*=-1
    O=Q4@D@R4;T=p['T'];SL=Q4@np.diag([np.exp(T),np.exp(-T),1,1])@R4
    t=np.linspace(0,max(1,T),201)
    return pack([m('Erreur d’orthogonalité ‖OᵀO−I‖F',float(np.linalg.norm(O.T@O-np.eye(4)))),m('Déterminant de O',round(float(np.linalg.det(O)))),m('Norme de Frobenius de O',float(np.linalg.norm(O))),m('Norme de Frobenius dans SL₄',float(np.linalg.norm(SL))),m('Déterminant dans SL₄',float(np.linalg.det(SL)))],
      [c('Norme constante dans O₄, norme croissante dans SL₄','t','Norme de Frobenius',s('O₄ : norme constante 2',t,np.full(len(t),2.)),s('SL₄ : √(e²ᵗ+e⁻²ᵗ+2)',t,np.sqrt(np.exp(2*t)+np.exp(-2*t)+2))),c('Comparer les facteurs d’étirement des deux matrices','Indice','Valeur singulière',dict(s('O : matrice orthogonale',np.arange(1,5),np.linalg.svd(O,compute_uv=False)),style='dots'),dict(s('A : matrice de déterminant 1',np.arange(1,5),np.linalg.svd(SL,compute_uv=False)),style='dots'))],
      'Vérifier séparément fermé et borné','La matrice O conserve les longueurs. La matrice A de déterminant 1 peut allonger certaines directions et en raccourcir d’autres. Dans l’espace des matrices 4×4, la compacité exige à la fois fermeture et bornitude.',
      ['O₄ est défini par OᵀO=I. Puisque O↦OᵀO est continue, l’image réciproque du fermé {I} est fermée : O₄ est fermé.','‖O‖F²=tr(OᵀO)=4 : toutes les matrices de O₄ ont une norme de Frobenius égale à 2. Cet ensemble est fermé et borné dans un espace de dimension 16, donc compact.','SL₄ est fermé car le déterminant est continu et {1} est fermé. Pourtant A(t)=Q diag(eᵗ,e⁻ᵗ,1,1)R vérifie det A(t)=1 et ‖A(t)‖F≥eᵗ : SL₄ n’est pas borné, donc pas compact.','Dans O₄, les deux ensembles de déterminants +1 et −1 sont ouverts et fermés relatifs. Cela compare le signe du déterminant et la notion d’ouvert relatif du cours.'],
      ['Q et R sont deux matrices orthogonales fixées de déterminant 1. La norme de Frobenius √(Σaᵢⱼ²) permet de regarder la matrice comme un vecteur de ℝ¹⁶. Les valeurs singulières sont les racines carrées des valeurs propres de AᵀA ; leur lecture comme facteurs d’étirement prolonge le cours.','Pour prouver que SL₄ n’est pas borné, considérer la formule pour tous les réels t≥0, même si le curseur n’en affiche qu’une plage finie.'],kind='matrix',matrix=O,secondary_matrix=SL,matrix_label='O, matrice orthogonale',labels=['1','2','3','4'])

def point_fixe(p):
    N,x0=int(p['N']),p['x0'];is_cos=p['family']=='cos';q=math.sin(1) if is_cos else abs(p['q']);f=math.cos if is_cos else lambda x:p['q']*x+.7
    seq=[x0]
    for _ in range(N):seq.append(f(seq[-1]))
    u=np.linspace(0,1,301) if is_cos else np.linspace(min(seq)-1,max(seq)+1,301)
    star=.7390851332151607 if is_cos else .7/(1-p['q']) if p['q']!=1 else None
    metrics=[m('Facteur L majorant la variation de f',q),m('Contraction : facteur L strictement inférieur à 1',q<1),m('Dernier terme xₙ calculé',seq[-1])]
    if star is not None:metrics.append(m('Écart au point fixe de référence',abs(seq[-1]-star)))
    if q<1:metrics.append(m('Majoration de l’erreur par les deux derniers termes',q*abs(seq[-1]-seq[-2])/(1-q)))
    else:metrics.append(m('Majoration par contraction','Non applicable : L≥1'))
    xs,ys=[],[]
    for a,b in zip(seq[:-1],seq[1:]):xs.extend([a,a,b]);ys.extend([a,b,b])
    charts=[c('Construire xₙ₊₁ à l’aide du graphe et de y=x','x','y',s('f(x)',u,[f(float(v)) for v in u]),s('y=x',u,u),s('Construction des termes',xs,ys)),c('Suivre les termes de la suite','Rang n','xₙ',s('Termes xₙ',np.arange(N+1),seq))]
    return pack(metrics,charts,'Chercher une limite ℓ vérifiant f(ℓ)=ℓ','Partir de x₀, lire f(x₀) sur le graphe, puis recommencer. Les traits verticaux et horizontaux représentent cette construction de la suite récurrente.',
      ['cos envoie [0,1] dans [0,1] : chaque terme y reste. L’inégalité des accroissements finis donne |cos(x)−cos(y)|≤sin(1)|x−y| sur ce segment.','Noter L le facteur de cette majoration : L=sin(1) pour cos et L=|q| pour l’application affine. Si L<1, f réduit les distances : on parle de contraction.','En prolongement, le théorème de Banach assure une unique solution x* de f(x*)=x* et la convergence des suites calculées. Il utilise la complétude, propriété selon laquelle toute suite de Cauchy converge dans le domaine ; ces notions générales sont hors programme MPSI/MP.','Pour L<1, |xₙ−x*|≤L/(1−L)·|xₙ−xₙ₋₁| : les deux derniers termes suffisent à majorer l’erreur. Pour une suite affine, on peut aussi étudier directement xₙ−x*=qⁿ(x₀−x*), méthode de MPSI.'],
      ['Le coefficient q peut être négatif ; le facteur de contraction est |q|. Pour cos, la valeur de référence est approchée numériquement, mais la majoration de l’erreur ne dépend pas de cette référence.','Pour f(x)=qx+0,7, q=1 ne donne aucun point fixe. Si |q|≥1, le théorème de contraction ne s’applique pas ; un départ exactement au point fixe, lorsqu’il existe, reste néanmoins constant.'],kind='iteration')

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
    return pack([m('Régions reliées par arcs (composantes)',components),m('Convexe','Non pour b≤1 ; pour b>1, question à étudier séparément' if b<=1 else 'Pouvoir relier par arcs ne suffit pas à être convexe'),m('Ouvert de ℝ²',not closed),m('Compact',closed),m('L’origine appartient à l’ensemble',b>1 or b==1 and closed)],
      [c('Lire le passage sur l’axe réel','x','F(x,0)',s('F(x,0)=(x²−1)²',x,f),s('Niveau b⁴',x,np.full(len(x),b**4)))],
      'Inclure le point de contact pour pouvoir passer','On appelle ici sous-niveau l’ensemble où F est inférieure à la valeur b⁴. Puisque F est continue, l’inégalité < donne un ouvert et l’inégalité ≤ un fermé.',
      ['Sur l’axe vertical, F(0,y)=(y²+1)²≥1. Si b<1, aucun point de cet axe ne peut appartenir à la région étudiée.','Un chemin entre les régions gauche et droite devrait traverser x=0, par le théorème des valeurs intermédiaires appliqué à son abscisse. Il est donc impossible lorsque b<1.','À b=1, l’inégalité ≤ inclut (0,0) : on peut passer d’une région à l’autre par ce point. L’inégalité < l’exclut, et les deux régions restent séparées.','Pour b>1, chaque point se relie à l’origine par un segment inclus dans l’ensemble : on dit que l’ensemble est étoilé par rapport à l’origine. Relier deux points en passant par zéro prouve la connexité par arcs.'],
      ['Les points (−1,0) et (1,0) sont les foyers. F est le produit des carrés des distances à ces deux points. Les frontières calculées correspondent aux ovales de Cassini.','MP : valeurs intermédiaires, images réciproques d’ouverts ou de fermés, parties étoilées et connexité par arcs. Tous les ensembles proposés sont bornés ; avec ≤, ils sont aussi fermés, donc compacts. Les contours dessinés sont approchés, les conclusions reposent sur les inégalités.'],paths=paths,points=[dict(x=-1,y=0,label='Foyer −1',colorIndex=2),dict(x=1,y=0,label='Foyer +1',colorIndex=2),dict(x=0,y=0,label='Contact',colorIndex=1)],bounds=[-2.2,2.2,-1.8,1.8])

def homeomorphisme(p):
    n=int(p['n']);is_circle=p['family']=='circle';k=np.arange(2,n+1)
    if is_circle:
        theta=2*np.pi-1/k;distance=2*np.sin(1/(2*k));x,y=circle();probe=2*np.pi-1/n
        charts=[c('Les points du cercle convergent vers 1=f(0)','Rang n','Distance à 1',s('|eⁱᵗⁿ−1|=2sin(1/(2n))',k,distance)),c('Leurs antécédents tendent vers 2π, et non vers 0','Rang n','tₙ / rad',s('2π−1/n',k,theta))]
        paths=[path_('Cercle',x,y,colorIndex=0)];points=[dict(x=1,y=0,label='1 = image de 0',colorIndex=1),dict(x=np.cos(probe),y=np.sin(probe),label='Image de tₙ',colorIndex=2)]
        metrics=[m('Bijection continue','Oui : un angle unique pour chaque point du cercle'),m('Domaine compact','Non : [0,2π[ n’est pas fermé dans ℝ'),m('Réciproque continue','Non au point 1=f(0)'),m('Distance des images à 1',float(distance[-1]))]
        bounds=[-1.3,1.3,-1.3,1.3]
    else:
        t=np.linspace(-1,1,241);value=p['t'];charts=[c('Les trois coordonnées de l’injection','t','Coordonnée',s('x=t',t,t),s('y=t²',t,t*t),s('z=t³',t,t**3))]
        paths=[path_('Projection (t,t²)',t,t*t,colorIndex=0)];points=[dict(x=value,y=value*value,label='Point du segment',colorIndex=1)];bounds=[-1.3,1.3,-.15,1.3]
        metrics=[m('Domaine compact','Oui : [−1,1]'),m('Injection continue','Oui : deux t différents donnent deux points différents'),m('Réciproque sur l’image','Lire la première coordonnée x=t'),m('Constante de Lipschitz de la réciproque',1)]
    return pack(metrics,charts,'Retrouver continûment l’antécédent ?','Le dessin montre seulement les coordonnées (t,t²) de la courbe. L’application étudiée est g(t)=(t,t²,t³) dans ℝ³ ; le graphique donne ses trois coordonnées.' if not is_circle else 'Les points f(tₙ) se rapprochent de 1=f(0), mais les angles tₙ tendent vers 2π et non vers 0. La réciproque ne respecte donc pas cette limite.',
      ['Pour f(t)=eⁱᵗ sur [0,2π[, chaque point du cercle possède un seul antécédent. Cependant tₙ=2π−1/n vérifie f(tₙ)→f(0), sans que tₙ→0 : la caractérisation séquentielle prouve la discontinuité de la réciproque.',
       'Dans un espace normé, une application continue injective sur un compact possède une réciproque continue sur son image. Ce résultat prolonge le cours : les fermés du compact ont des images compactes, donc fermées.',
       'Pour g(t)=(t,t²,t³), retrouver t revient à lire la première coordonnée. On voit directement que la réciproque est continue, et même 1-lipschitzienne pour la norme euclidienne.',
       'Ajouter 2π au domaine de f rend celui-ci compact, mais f(0)=f(2π) : l’application perd son injectivité. Il faut vérifier séparément les hypothèses compact et injectif.'],
      ['MPSI : angles, nombres complexes, bijections et suites. MP : continuité séquentielle, images de compacts et fermés relatifs. Un homéomorphisme est une bijection continue dont la réciproque est aussi continue.','Pour [0,2π[ et pour le cercle, les voisinages sont ceux de l’espace ambiant limités à l’ensemble considéré : il s’agit des voisinages relatifs du cours de MP.'],paths=paths,points=points,bounds=bounds)

MODELS={name:globals()[name] for name in ['denombrer_rationnels','diagonale_cantor','ensemble_cantor','rationnels_irrationnels','sinus_topologue','gl_composantes','orthogonal_compact','point_fixe','chemins_niveaux','homeomorphisme']}
def calculate(lab_id,p):return MODELS[lab_id](p)
