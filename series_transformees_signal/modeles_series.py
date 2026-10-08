"""Calculs indépendants du rendu : convergence, sommes et intégrales.

Les maxima et les aires qui décident des théorèmes sont calculés
analytiquement. Les quadratures de Gauss ne servent qu'aux modèles pour
lesquels on affiche explicitement une valeur numérique.
"""
from __future__ import annotations
import math
from functools import lru_cache
import numpy as np
from commun import chart, metric, result, scene, series


@lru_cache(maxsize=4)
def _gauss(order):
    return np.polynomial.legendre.leggauss(order)


def _grid_peak(n, stop=1.0, count=401):
    return np.unique(np.r_[np.linspace(0,stop,count),np.linspace(0,min(stop,6/n),181),1/n])


def boundary_norm(n, delta=0.0):
    """Norme exacte de nx/(1+n²x²) sur [δ,1], n≥1."""
    return 0.5 if delta <= 1/n else n*delta/(1+(n*delta)**2)


def stable_tp99(u):
    """Évite la soustraction de deux nombres proches de 1."""
    u=np.asarray(u,dtype=float)
    value=np.cos(u)-1/np.sqrt(1+u*u)
    mask=np.abs(u)<0.04
    z=u[mask]**2
    polynomial=np.zeros_like(z)
    for k in range(9,1,-1):
        coefficient=(-1)**k*(1/math.factorial(2*k)-math.comb(2*k,k)/4**k)
        polynomial=polynomial*z+coefficient
    value[mask]=z*z*polynomial
    return value


def arcsin_coefficients(terms):
    coefficients=np.ones(terms)
    for k in range(1,terms): coefficients[k]=coefficients[k-1]*(2*k)/(2*k+1)
    return coefficients


def binomial_coefficients(alpha,terms):
    coefficients=np.ones(terms)
    for k in range(1,terms): coefficients[k]=coefficients[k-1]*(alpha+k-1)/k
    return coefficients


def coefficient_log_ratio(n):
    """log((1+2/n²)ⁿ³/e²ⁿ), avec annulation numérique contrôlée."""
    n=np.asarray(n,dtype=float)
    values=n**3*np.log1p(2/n**2)-2*n
    mask=n>=20
    selected=n[mask]
    values[mask]=sum((-1)**(k+1)*2**k/(k*selected**(2*k-3)) for k in range(2,10))
    return values


def poisson_scaled_sum(x,last=None):
    """S(x)/exp(e²x) ; x≥0. La troncature automatique est bien après le pic."""
    lam=math.exp(2)*x
    if not lam:return 0.0
    end=int(math.ceil(lam+16*math.sqrt(lam+1)+70)) if last is None else int(last)
    ns=np.arange(2,end+1,dtype=float)
    if len(ns)==0:return 0.0
    logarithms=ns*math.log(lam)-np.array([math.lgamma(t+1) for t in ns])-lam
    return float(np.exp(logarithms+coefficient_log_ratio(ns)).sum())


def elliptic_ratio(k,terms=None):
    """I(k)/π, I intégrée sur [0,π]."""
    if terms is not None:
        coefficients=np.ones(terms)
        for n in range(1,terms):coefficients[n]=coefficients[n-1]*((2*n-1)/(2*n))**2
        return float(np.polynomial.polynomial.polyval(k*k,coefficients))
    points,weights=_gauss(160)
    t=(points+1)*math.pi/4
    return float(np.dot(weights,1/np.sqrt(1-k*k*np.sin(t)**2))/2)


def sinh_integrand(t):
    t=np.asarray(t,dtype=float)
    values=np.ones_like(t)
    nonzero=t!=0
    values[nonzero]=2*t[nonzero]*np.exp(-t[nonzero])/(-np.expm1(-2*t[nonzero]))
    return values


def dominated_function(t,family,omega):
    t=np.asarray(t)
    if family=='linear':return 1+t
    if family=='jump':return np.where(t<0.4,1.,-.75)
    if family=='complex':return np.exp(1j*omega*t)
    if family=='oscillatory':return np.sin(omega*t)
    raise ValueError('Famille inconnue.')


def dominated_kernel(t,n):
    t=np.asarray(t,dtype=float)
    with np.errstate(divide='ignore'):
        return np.exp(n*np.log1p(-t/n))


def dominated_integral(n,family,omega):
    points,weights=_gauss(96)
    intervals=[(0.,.4),(.4,1.)] if family=='jump' else [(0.,1.)]
    total=0j
    for a,b in intervals:
        t=a+(points+1)*(b-a)/2
        kernel=np.exp(-t) if n is None else dominated_kernel(t,n)
        total+=(b-a)/2*np.dot(weights,dominated_function(t,family,omega)*kernel)
    return total


def dominated_limit(family,omega):
    if family=='linear':return complex(2-3/math.e)
    if family=='jump':return complex(1-1.75*math.exp(-.4)+.75/math.e)
    z=-1+1j*omega
    value=np.expm1(z)/z
    return complex(value) if family=='complex' else complex(value.imag)


def _couche(p):
    n,delta=int(p['n']),float(p['delta']);x=_grid_peak(n)
    indices=np.unique(np.r_[np.geomspace(1,max(1000,n),140).astype(int),n])
    local=np.array([boundary_norm(int(k),delta) for k in indices])
    u=np.linspace(0,8,401)
    curves=[series(f'n={k}',x,k*x/(1+(k*x)**2)) for k in sorted(set([max(1,n//4),max(1,n//2),n]))]
    return result([metric('Norme sur [0,1]',.5),metric('Position exacte du maximum',1/n),metric('Norme sur [δ,1]',boundary_norm(n,delta)),metric('Majorant compact 1/(nδ)',1/(n*delta))],
        [chart('Convergence simple, pic persistant','x','fₙ(x)',*curves),chart('Deux normes, deux conclusions','n','norme',series('[0,1]',indices,np.full(len(indices),.5)),series('[δ,1]',indices,local),x_scale='log'),chart('Loupe x=u/n : un profil indépendant de n','u=nx','fₙ(u/n)',series('u/(1+u²)',u,u/(1+u*u)))],
        scene('convergence','La bosse garde sa hauteur','Le maximum analytique reste 1/2 en x=1/n, même si un maillage uniforme manque le pic.',n=n,delta=delta,peak_x=1/n,peak_y=.5,profile='boundary'),
        ['Pour x>0 fixé, fₙ(x)≤1/(nx)→0 ; fₙ(0)=0. La convergence est simple sur [0,1].','fₙ′(x)=n(1−n²x²)/(1+n²x²)² : le maximum sur [0,1] vaut exactement 1/2. La convergence uniforme y échoue.','Sur [δ,1], calculer le maximum à x=1/n si ce point appartient au compact, sinon à δ. La norme tend vers 0.','La variable dilatée u=nx garde le pic visible. Un graphique seul ne prouve aucune convergence uniforme.'],
        ['n entier ≥1 ; 0<δ≤1. Normes obtenues par étude de la dérivée, indépendamment des points du graphe.'])


def _concentration(p):
    n,x0=int(p['n']),float(p['x0']);x=_grid_peak(n);u=np.linspace(0,10,401)
    indices=np.unique(np.r_[np.geomspace(1,300,140).astype(int),n])
    areas=-np.expm1(-indices)-(indices*np.exp(-indices))
    area=-math.expm1(-n)-n*math.exp(-n)
    return result([metric('Aire exacte sur [0,1]',area),metric('Hauteur du pic',n/math.e),metric('Position du pic',1/n),metric('Valeur au point fixe x₀',n*n*x0*math.exp(-n*x0))],
        [chart('Une aire se concentre au bord','x','n²xe⁻ⁿˣ',series(f'n={n}',x,n*n*x*np.exp(-n*x))),chart('La limite ponctuelle ne préserve pas l’intégrale','n','aire',series('∫₀¹ fₙ',indices,areas),series('limite = 1',indices,np.ones(len(indices))),x_scale='log'),chart('Loupe : fₙ(u/n)/n = ue⁻ᵘ','u','densité dilatée',series('ue⁻ᵘ',u,u*np.exp(-u))),chart('Évaluer avant de passer à la limite','n','fₙ(x₀)',series(f'x₀={x0:g}',indices,indices**2*x0*np.exp(-indices*x0)),x_scale='log')],
        scene('convergence','Une masse invisible à la limite ponctuelle','Le pic a une largeur de l’ordre de 1/n et une hauteur de l’ordre de n.',n=n,peak_x=1/n,peak_y=n/math.e,profile='concentration'),
        ['En chaque x>0, l’exponentielle domine n² : fₙ(x)→0. En x=0, fₙ(0)=0.','Le changement u=nx donne ∫₀¹fₙ(x)dx=∫₀ⁿue⁻ᵘdu=1−(n+1)e⁻ⁿ→1.','Ainsi ∫lim fₙ=0 alors que lim∫fₙ=1. Les hypothèses d’un théorème d’interversion sont nécessaires.','Il n’existe pas de domination intégrable commune : elle rendrait les deux limites égales par convergence dominée.'],
        ['Fonctions positives sur [0,1]. La concentration se produit au bord 0 ; la « masse limite » illustre une mesure de Dirac, au-delà du cours de première année.'])


def _tp99(p):
    n,R,N=int(p['n']),float(p['R']),int(p['N']);x=np.linspace(-R,R,501)
    f=stable_tp99(x/n);partial=np.zeros_like(x)
    for k in range(1,N+1):partial+=stable_tp99(x/k)
    local=-math.pi**4*x**4/270
    indices=np.arange(1,max(80,n)+1)
    return result([metric('Majorant sup |fₙ|',(5/12)*(R/n)**4),metric('Borne uniforme du reste de Σ après N',5*R**4/(36*N**3)),metric('Ordre du premier terme non nul',4),metric('Nombre de termes sommés',N)],
        [chart('L’annulation de l’ordre deux','x','n⁴fₙ(x)',series('n⁴fₙ(x)',x,n**4*f),series('limite −x⁴/3',x,-x**4/3)),chart('Sommer puis comparer au développement local','x','somme',series('S_N(x)',x,partial),series('premier terme local −π⁴x⁴/270',x,local)),chart('Une majoration sommable sur le compact','n','majorant',series('(5/12)(R/n)⁴',indices,(5/12)*(R/indices)**4),x_scale='log',y_scale='log')],
        scene('series','Deux approximations distinctes','Le développement local du terme et celui de la somme ne sont pas une identité globale.',n=n,terms=N,radius=R,formula='cos(x/n)−(1+(x/n)²)⁻¹ᐟ²'),
        ['Poser u=x/n. Les développements de cos u et de (1+u²)⁻¹ᐟ² ont le même terme −u²/2 ; leur différence commence par −u⁴/3.','Taylor avec reste donne |cos u−1+u²/2|≤u⁴/24 et |(1+u²)⁻¹ᐟ²−1+u²/2|≤3u⁴/8. Donc |fₙ(x)|≤5R⁴/(12n⁴) sur [−R,R].','Le critère de Weierstrass fournit la convergence normale sur tout compact et autorise notamment continuité et intégration de la somme.','Sommer les coefficients d’ordre quatre donne −ζ(4)x⁴/3=−π⁴x⁴/270. Il s’agit du premier terme du développement en 0 ; la courbe compare ce terme à la somme partielle.'],
        ['n≥1. La série est prise à partir de n=1. La borne du reste utilise Σ_{n>N}n⁻⁴≤∫_N∞t⁻⁴dt=1/(3N³). Les très petites différences sont évaluées par un développement stable.'])


def _geometrie(p):
    N,r=int(p['N']),float(p['r']);x=np.linspace(-r,r,501)
    coeff=np.ones(N+1);partial=np.polynomial.polynomial.polyval(x,coeff)
    deriv=np.polynomial.polynomial.polyval(x,np.arange(1,N+1))
    remainder=r**(N+1)/(1-r)
    deriv_bound=r**N*((N+1)-N*r)/(1-r)**2
    return result([metric('Rayon de convergence',1),metric('Borne du reste uniforme',remainder),metric('Borne du reste de la dérivée',deriv_bound),metric('Distance du compact au bord',1-r)],
        [chart('Approcher la somme sur un compact','x','somme',series('Σ₀ᴺ xᵏ',x,partial),series('1/(1−x)',x,1/(1-x))),chart('La dérivée requiert davantage de termes','x','dérivée',series('Σ₁ᴺ kxᵏ⁻¹',x,deriv),series('1/(1−x)²',x,1/(1-x)**2)),chart('Reste exactement calculé','x','reste',series('xᴺ⁺¹/(1−x)',x,x**(N+1)/(1-x)))],
        scene('series','Un compact à l’intérieur du disque','Le bord du disque est en x=±1 ; les opérations sont justifiées pour tout r<1.',radius=r,terms=N+1,formula='Σxᵏ=1/(1−x)'),
        ['L’identité finie (1−x)Σ₀ᴺxᵏ=1−xᴺ⁺¹ conduit à la somme et au reste exact.','Sur |x|≤r<1, |xᵏ|≤rᵏ : la convergence est normale. Le majorant du reste est atteint en x=r.','La série dérivée est normalement convergente sur les compacts : Σk rᵏ⁻¹<∞. On peut donc dériver terme à terme.','Quand r→1, une même troncature N devient moins précise. Le rayon de convergence ne dit pas à lui seul combien de termes calculer.'],
        ['N est le degré du polynôme : N+1 termes. L’atelier travaille strictement à l’intérieur du disque de convergence.'])


def _arcsin(p):
    N,r=int(p['N']),float(p['r']);x=np.linspace(-r,r,501);cs=arcsin_coefficients(N)
    poly=x*np.polynomial.polynomial.polyval(x*x,cs);exact=np.arcsin(x)/np.sqrt(1-x*x)
    residual=-2*N*cs[-1]*x**(2*N)
    bound=r**(2*N+1)/(1-r*r)
    return result([metric('Rayon de convergence',1),metric('Dernier coefficient calculé',float(cs[-1])),metric('Borne uniforme du reste',bound),metric('Erreur maximale du polynôme',float(np.max(np.abs(exact-poly))))],
        [chart('Une EDO donne une approximation impaire','x','f(x)',series('arcsin(x)/√(1−x²)',x,exact),series(f'polynôme : {N} termes',x,poly)),chart('Reste et amplification près du bord','x','f−P',series('reste',x,exact-poly)),chart('Défaut dans l’équation différentielle','x','(1−x²)P′−xP−1',series('résidu exact du polynôme',x,residual)),chart('Une récurrence simple','k','cₖ',series('coefficient de x²ᵏ⁺¹',np.arange(N),cs))],
        scene('series','La récurrence remplace les dérivations répétées','c₀=1 et cₖ=(2k)/(2k+1)cₖ₋₁ ; seuls les degrés impairs subsistent.',terms=N,radius=r,coefficients=cs[:12].tolist(),formula='(1−x²)f′−xf=1'),
        ['L’identité (1−x²)f′−xf=1 avec f(0)=0 fournit a₀=0, a₁=1 et (n+2)aₙ₊₂=(n+1)aₙ.','Écrire f(x)=Σcₖx²ᵏ⁺¹ : c₀=1 et cₖ=2k cₖ₋₁/(2k+1). Le rapport des termes tend vers x², d’où le rayon 1.','Les coefficients vérifient 0<cₖ≤1. Le reste après N termes est donc majoré par r²ᴺ⁺¹/(1−r²) sur |x|≤r.','Le polynôme ne satisfait pas exactement l’EDO : son résidu vaut −2N cₙ₋₁x²ᴺ. Cette vérification relie calcul algébrique et précision.'],
        ['L’analyticité se prouve par la série obtenue, de rayon 1, puis l’EDO et son unicité. N désigne le nombre de termes impairs, et non le degré.'])


def _asymptotique(p):
    x,N=float(p['x']),int(p['N']);lam=math.exp(2)*x
    ratio=poisson_scaled_sum(x);partial=poisson_scaled_sum(x,N)
    xs=np.linspace(.2,max(x,30),151);ratios=[poisson_scaled_sum(float(v)) for v in xs]
    end=min(900,int(lam+10*math.sqrt(lam+1)+40))
    ns=np.unique(np.r_[np.linspace(2,end,min(630,end-1)).astype(int),max(2,int(lam))])
    weights=np.exp(ns*np.log(lam)-np.array([math.lgamma(int(k)+1) for k in ns])-lam)
    rns=np.exp(coefficient_log_ratio(ns))
    log_s=lam+math.log(ratio)
    return result([metric('λ=e²x',lam),metric('S(x)/exp(λ)',ratio),metric('S_N(x)/exp(λ)',partial),metric('log S(x)',log_s),metric('Rayon de convergence','∞')],
        [chart('Le bon équivalent apparaît comme un rapport','x','S(x)/exp(e²x)',series('rapport normalisé',xs,ratios),series('limite 1',xs,np.ones(len(xs)))),chart('Le poids de chaque indice dans la somme','n','contribution normalisée',series('e⁻λ λⁿ/n!',ns,weights),series('aₙxⁿe⁻λ',ns,weights*rns)),chart('Les coefficients deviennent équivalents','n','aₙ / (e²ⁿ/n!)',series('rapport des coefficients',ns,rns),series('limite 1',ns,np.ones(len(ns))))],
        scene('series','Une somme entière sous une loi de Poisson','Le cœur de la somme se trouve vers n≈λ. Une troncature antérieure au pic peut être très trompeuse.',terms=N,lambda_=lam,ratio=ratio,formula='S(x)e⁻λ=Σ_{n≥2}P(Poisson(λ)=n)rₙ'),
        ['n³ln(1+2/n²)=2n−2/n+O(n⁻³), donc aₙ∼e²ⁿ/n!. La formule de Cauchy–Hadamard ou le critère du rapport donne R=∞.','Poser λ=e²x et rₙ=aₙn!/e²ⁿ. Alors 0<rₙ<1 et rₙ→1 ; S(x)e⁻λ est une moyenne pondérée par une loi de Poisson, amputée des indices 0 et 1.','Pour ε>0, choisir m avec |rₙ−1|≤ε si n≥m. La contribution des n<m est un polynôme en λ multiplié par e⁻λ, donc tend vers 0.','Les indices n≥m ont une masse qui tend vers 1 : le rapport tend vers 1. On conclut S(x)∼exp(e²x) lorsque x→+∞.'],
        ['x>0. Les rapports sont calculés en logarithmes, avec une troncature automatique au-delà de λ+16√(λ+1)+70 ; l’erreur de cette troncature est inférieure à une queue de Poisson. N sert à montrer les risques d’une somme partielle insuffisante.'])


def _binomiale(p):
    alpha=int(p['p'])+.5;N,r=int(p['N']),float(p['r']);u=np.linspace(-r,r,501);cs=binomial_coefficients(alpha,N+1)
    approximation=np.polynomial.polynomial.polyval(u,cs[:-1]);exact=(1-u)**(-alpha)
    q=r*(1+max(alpha-1,0)/(N+1))
    if q<1:bound=abs(cs[N])*r**N/(1-q)
    else:
        outer=(1+r)/2;maximum=(1-outer)**(-alpha) if alpha>=0 else (1+outer)**(-alpha)
        bound=maximum*(r/outer)**N/(1-r/outer)
    return result([metric('Exposant α',alpha),metric('Rayon de convergence',1),metric('Borne uniforme du reste',bound),metric('Erreur maximale constatée',float(np.max(np.abs(exact-approximation))))],
        [chart('Du binôme à l’exposant demi-entier','u','(1−u)⁻ᵅ',series('fonction',u,exact),series(f'{N} termes',u,approximation)),chart('Reste sur le compact','u','fonction−polynôme',series('reste',u,exact-approximation)),chart('Les coefficients et leurs signes','n','cₙ',series('c₀=1 ; cₙ₊₁=(α+n)cₙ/(n+1)',np.arange(N),cs[:-1]))],
        scene('series','Une même récurrence, plusieurs profils','Pour α=1/2, cₙ=binom(2n,n)/4ⁿ ; les autres demi-entiers utilisent la même construction.',terms=N,alpha=alpha,radius=r,coefficients=cs[:12].tolist(),formula='(1−u)⁻ᵅ=Σ(α)ₙuⁿ/n!'),
        ['La fonction satisfait (1−u)f′=αf et f(0)=1. Identifier les coefficients donne cₙ₊₁=(α+n)cₙ/(n+1).','La série obtenue a pour rayon 1 ; l’EDO identifie sa somme à (1−u)⁻ᵅ sur ]−1,1[.','Pour α=1/2, la récurrence donne cₙ=binom(2n,n)/4ⁿ. Elle prépare le calcul de l’intégrale elliptique.','Le reste est majoré en contrôlant le rapport des termes à partir du premier terme omis ; si ce contrôle géométrique ne suffit pas, une borne de Cauchy sur un cercle plus grand est utilisée.'],
        ['p entier de −3 à 3, α=p+1/2. Le cas p=0 relie explicitement l’expérience à la racine inverse. Le compact |u|≤r reste strictement dans le disque de convergence.'])


def _pendulum(p):
    degrees,N,length=float(p['angle']),int(p['N']),float(p['length']);amplitude=math.radians(degrees);k=math.sin(amplitude/2)
    ratio=elliptic_ratio(k);approx=elliptic_ratio(k,N);T0=2*math.pi*math.sqrt(length/9.81);T=T0*ratio
    first_omitted=binomial_coefficients(.5,N+1)[N]**2*k**(2*N)
    tail_bound=first_omitted/(1-k*k)
    times=np.linspace(0,2*T,601);theta=np.empty(len(times));theta[0]=amplitude;velocity=0.;dt=times[1]
    def rhs(q,v):return np.array([v,-9.81/length*math.sin(q)])
    for j in range(1,len(times)):
        state=np.array([theta[j-1],velocity]);a=rhs(*state);b=rhs(*(state+dt*a/2));c=rhs(*(state+dt*b/2));d=rhs(*(state+dt*c));state+=dt*(a+2*b+2*c+d)/6;theta[j],velocity=state
    angles=np.linspace(0,160,161);ks=np.sin(np.radians(angles)/2);exact_curve=[elliptic_ratio(float(v)) for v in ks];series_curve=[elliptic_ratio(float(v),N) for v in ks]
    ns=np.arange(1,max(N,45)+1);partials=[elliptic_ratio(k,int(v)) for v in ns]
    return result([metric('Module k=sin(θ₀/2)',k),metric('T/T₀ exact (quadrature)',ratio),metric('Période T',T,'s'),metric('Erreur relative de la série',max(0.,(ratio-approx)/ratio)),metric('Période des petites oscillations',T0,'s'),metric('Borne du reste sur T/T₀',tail_bound)],
        [chart('L’amplitude allonge la période','θ₀ (°)','T/T₀',series('intégrale elliptique',angles,exact_curve),series(f'{N} termes',angles,series_curve),series('petites oscillations',angles,np.ones(len(angles)))),chart('Pendule non linéaire et modèle harmonique','t (s)','θ (°)',series('θ″+(g/ℓ)sin θ=0',times,np.degrees(theta)),series('θ₀cos(√(g/ℓ)t)',times,degrees*np.cos(math.sqrt(9.81/length)*times))),chart('Accumuler les coefficients positifs','nombre de termes','T_N/T₀',series('somme partielle',ns,partials),series('intégrale',ns,np.full(len(ns),ratio)))],
        scene('pendulum','Quand sin θ ne se confond plus avec θ','La période est issue de la conservation de l’énergie puis d’un changement de variable.',angle=degrees,length=length,period=T,small_period=T0,time=times.tolist(),theta=theta.tolist(),k=k),
        ['Conserver E=(ℓ²/2)θ̇²+gℓ(1−cos θ) puis poser sin(θ/2)=k sin φ, avec k=sin(θ₀/2). On obtient T=4√(ℓ/g)K(k).','Dans le recueil I(k)=∫₀π(1−k²sin²t)⁻¹ᐟ²dt=2K(k). Donc T/T₀=I(k)/π.','Développer la racine inverse puis intégrer sin²ⁿt : I(k)=πΣ[binom(2n,n)/4ⁿ]²k²ⁿ. La convergence normale pour |k|≤r<1 justifie l’interversion.','Tous les coefficients sont positifs : les sommes partielles sous-estiment la période. Quand θ₀→180°, k→1 et la période diverge.'],
        ['Pendule idéal sans frottement, g=9,81 m·s⁻². Quadrature de Gauss à 160 points ; trajectoire obtenue par Runge–Kutta d’ordre 4 sur deux périodes. L’énergie et le facteur 2 entre I et K déterminent la normalisation.'])


def _sinh(p):
    N,T=int(p['N']),float(p['T']);t=np.unique(np.r_[np.linspace(0,T,401),np.linspace(0,min(T,8/N),181)])
    partial=np.zeros_like(t);nz=t>0
    partial[nz]=sinh_integrand(t[nz])*(-np.expm1(-2*N*t[nz]))
    odd=2*np.arange(N)+1;areas=2/odd**2;total=float(areas.sum());reference=math.pi**2/4
    ns=np.arange(1,max(N,100)+1);cumulative=np.cumsum(2/(2*np.arange(len(ns))+1)**2)
    lo=1/(2*N+1);hi=lo+2/(2*N+1)**2
    return result([metric('Intégrale exacte',reference),metric('Somme des N premières aires',total),metric('Reste exact',reference-total),metric('Borne supérieure du reste',hi),metric('Borne de la queue au-delà de T',2*(T+1)*math.exp(-T)/(1-math.exp(-2*T)))],
        [chart('Une somme de modes positifs','t','intégrande',series('t/sinh t, prolongée en 0',t,sinh_integrand(t)),series('N modes',t,partial),*[series(f'mode n={j}',t,2*t*np.exp(-(2*j+1)*t)) for j in range(min(N,3))]),chart('Les aires convergent avec un reste contrôlé','N','aire',series('somme des aires',ns,cumulative),series('π²/4',ns,np.full(len(ns),reference))),chart('Le reste entre deux bornes intégrales','N','reste',series('reste',ns,reference-cumulative),series('borne inférieure 1/(2N+1)',ns,1/(2*ns+1)),series('borne supérieure',ns,1/(2*ns+1)+2/(2*ns+1)**2),x_scale='log',y_scale='log')],
        scene('series','De la série géométrique à une intégrale impropre','Chaque mode a une aire exacte 2/(2n+1)². La positivité autorise l’addition des aires.',terms=N,area=total,limit=reference,tail_lower=lo,tail_upper=hi,formula='t/sinh t=Σ₂te⁻⁽²ⁿ⁺¹⁾ᵗ (t>0)'),
        ['Pour t>0, 1/sinh t=2e⁻ᵗ/(1−e⁻²ᵗ), puis développer le dénominateur en série géométrique.','Chaque terme 2te⁻⁽²ⁿ⁺¹⁾ᵗ est positif et intégrable, avec aire 2/(2n+1)² ; la somme de ces aires est finie.','La convergence monotone (ou le théorème d’intégration des séries avec somme des intégrales absolues finie) autorise l’interversion sur ]0,+∞[.','La somme des inverses des carrés impairs vaut (1−1/4)ζ(2)=π²/8 ; l’intégrale vaut donc π²/4. Les bornes intégrales affichées encadrent le reste.'],
        ['En t=0, la fonction prolongée vaut 1 mais chaque somme partielle vaut 0 : l’égalité de série est sur t>0. Ce seul point ne modifie pas l’intégrale. La fenêtre [0,T] est uniquement une représentation ; les aires affichées sont sur [0,+∞[.'])


def _dominee(p):
    n,family,omega=int(p['n']),p['family'],float(p['omega']);t=np.unique(np.r_[np.linspace(0,1,501),.4]);f=dominated_function(t,family,omega)
    un=f*dominated_kernel(t,n);u=f*np.exp(-t);value=dominated_integral(n,family,omega);limit=dominated_limit(family,omega)
    ns=np.unique(np.r_[np.geomspace(1,max(n,200),110).astype(int),n]);values=np.array([dominated_integral(int(j),family,omega) for j in ns]);errors=np.abs(values-limit)
    integral_majorant={'linear':1.5,'jump':.85,'complex':1.,'oscillatory':1.}[family]
    bound=integral_majorant*(1 if n==1 else 1/(2*(n-1)))
    return result([metric('Partie réelle de Iₙ',value.real),metric('Partie imaginaire de Iₙ',value.imag),metric('|Iₙ−I|',abs(value-limit)),metric('Borne quantitative',bound),metric('Limite : Re I',limit.real),metric('Limite : Im I',limit.imag)],
        [chart('Le noyau tend vers l’exponentielle','t','noyau',series('(1−t/n)ⁿ',t,dominated_kernel(t,n)),series('e⁻ᵗ',t,np.exp(-t))),chart('Un signal pondéré : parties réelle et imaginaire','t','f(t) × noyau',series('Re uₙ',t,un.real),series('Re u',t,u.real),series('Im uₙ',t,un.imag),series('Im u',t,u.imag)),chart('L’intégrale converge dans le plan complexe','Re Iₙ','Im Iₙ',series('chemin des Iₙ',values.real,values.imag),series('limite I',[limit.real],[limit.imag])),chart('Une erreur contrôlée','n','|Iₙ−I|',series('erreur',ns,np.maximum(errors,1e-18)),series('majorant',ns,integral_majorant/np.maximum(1,2*(ns-1))),x_scale='log',y_scale='log')],
        scene('convergence','Dominer avant d’intégrer','|(1−t/n)ⁿ|≤1 sur [0,1], donc |uₙ(t)|≤|f(t)|, une fonction intégrable.',n=n,family=family,real=value.real,imag=value.imag,limit_real=limit.real,limit_imag=limit.imag,profile='dominated'),
        ['Pour t∈[0,1] fixé, n ln(1−t/n)→−t. Au cas n=1, t=1, le noyau est défini directement par 0.','La fonction f est continue par morceaux ; |f| est intégrable sur [0,1]. Le noyau appartient à [0,1], ce qui fournit une domination indépendante de n.','La convergence dominée s’applique séparément aux parties réelle et imaginaire. Ainsi Iₙ→I=∫₀¹f(t)e⁻ᵗdt, même pour une fonction complexe ou avec un saut.','Pour n≥2, 0≤e⁻ᵗ−(1−t/n)ⁿ≤1/[2(n−1)]. En multipliant par |f| puis en intégrant, on obtient la borne quantitative affichée.'],
        ['t et ω sont sans dimension. Le signal à saut vaut 1 avant 0,4 et −0,75 ensuite ; son intégrale est calculée en deux intervalles. Les valeurs Iₙ utilisent une quadrature de Gauss, tandis que I est calculée analytiquement.'])


MODELS={'couche_limite':_couche,'concentration':_concentration,'tp99_original':_tp99,'geometrie':_geometrie,'arcsin_ex4':_arcsin,'asymptotique_ex5':_asymptotique,'binomiale_ex10':_binomiale,'elliptique_pendule':_pendulum,'integrale_sh_ex11':_sinh,'dominee_ex12':_dominee}


def calculate(lab_id,p):
    return MODELS[lab_id](p)
