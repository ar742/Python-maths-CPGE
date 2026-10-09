"""Équations fonctionnelles et intégrales à paramètre : domaines et majorations explicites."""
from __future__ import annotations
import math
from functools import lru_cache
import numpy as np
from commun import metric, series, chart, result, integrate


@lru_cache(maxsize=8)
def gauss_rule(n=256):
    return np.polynomial.legendre.leggauss(n)


def quadrature(fun, left, right, n=256):
    nodes, weights = gauss_rule(n)
    t = (right-left)*nodes/2+(right+left)/2
    return float((right-left)/2*np.dot(weights, fun(t)))


def curves_scene(title, x, curves, x_label='t', y_label='Intégrande', description='', **extra):
    return dict(kind='curves', title=title, description=description, x=x, curves=[dict(label=label, y=y) for label, y in curves], xLabel=x_label, yLabel=y_label, **extra)


def heat_scene(title, axis, residual, candidates, x_label='x', y_label='y', description=''):
    return dict(kind='heatmap', title=title, description=description, x=axis, y=axis, z=residual, xLabel=x_label, yLabel=y_label, candidates=candidates)


def cauchy_additive(p):
    a,b=p['a'],p['b']; x=np.linspace(-4,4,601); axis=np.linspace(-2,2,65)
    X,Y=np.meshgrid(axis,axis); fun=lambda u:a*u+b*np.sin(u)
    residual=fun(X+Y)-fun(X)-fun(Y); diagonal=fun(2*x)-2*fun(x)
    return result([metric('Défaut maximal sur les couples testés',np.max(abs(residual))),metric('f(0)',0),metric('Dérivée du candidat en 0',a+b),metric('Pente de la solution exacte',a)],
        [chart('Une courbe proche de la solution ne suffit pas','x','f(x)',series('Candidat ax+b sin x',x,fun(x)),series('Solution ax',x,a*x)),
         chart('Condition nécessaire : f(2x)=2f(x)','x','Défaut',series('f(2x)−2f(x)',x,diagonal),series('Valeur exigée',x,x*0))],
        heat_scene('Résidu f(x+y)−f(x)−f(y) : chaque case teste une égalité',axis,residual,[dict(label='Candidat',x=x,y=fun(x))],description='Les deux axes sont les arguments x et y. La couleur mesure un défaut signé ; l’égalité additive exige zéro dans toutes les cases, puis une preuve pour tous les couples.'),
        ['Poser x=y=0 : f(0)=0. Puis y=−x : f(−x)=−f(x). Les solutions sont donc impaires.',
         'Par récurrence, f(nx)=nf(x) pour n entier ; en divisant puis en prenant x=1, f(r)=r f(1) pour tout rationnel r.',
         'Fixer a=f(1). Pour un réel x, choisir des rationnels rₙ→x. La continuité donne f(x)=lim f(rₙ)=ax.',
         'Vérifier la réciproque dans l’équation initiale : a(x+y)=ax+ay. Une carte de résidus n’est qu’un test sur un nombre fini de points.'],
        ['La classification annoncée suppose f continue en au moins un point ; l’équation transporte cette continuité en 0 puis partout.',
         'Sans hypothèse de régularité, il existe des fonctions additives qui ne sont pas des droites. Le laboratoire ne construit pas ces solutions.',
         'Le défaut b sin x est une famille de candidats à rejeter pour b≠0 ; sa dérivée en 0 ne suffit pas à valider l’équation.'])


def cauchy_multiplicative(p):
    a,b=p['a'],p['b']; mode=p['equation']; u=np.linspace(-3,3,601); axis=np.linspace(-1.5,1.5,65)
    U,V=np.meshgrid(axis,axis)
    if mode=='log':
        h=lambda s:a*s+b*s*s; exact=a*u; residual=h(U+V)-h(U)-h(V); diag=h(2*u)-2*h(u)
        equation='f(xy)=f(x)+f(y)'; profile='a ln x+b(ln x)²'; derivative=a; fone=0
        reasoning=['Poser x=y=1 : f(1)=0. Poser y=1/x : f(1/x)=−f(x).',
         'Définir h(u)=f(eᵘ), pour u réel. Alors h(u+v)=h(u)+h(v). La continuité de f implique celle de h.',
         'Le résultat de Cauchy donne h(u)=au. Revenir à x=eᵘ : f(x)=a ln x pour x>0.',
         'Vérifier la réciproque avec ln(xy)=ln x+ln y. Le logarithme réel impose x>0 et y>0.']
    else:
        h=lambda s:np.exp(a*s+b*np.sin(s)); exact=np.exp(a*u); residual=h(U+V)-h(U)*h(V); diag=h(2*u)-h(u)**2
        equation='f(xy)=f(x)f(y)'; profile='exp[a ln x+b sin(ln x)]'; derivative=a+b; fone=1
        reasoning=['Si f n’est pas identiquement nulle, l’équation à y=1 donne f(1)=1. Avec y=1/x, f(x)f(1/x)=1, donc f ne s’annule pas.',
         'Pour x>0, écrire x=(√x)² : f(x)=f(√x)²>0. On peut donc poser h(u)=ln f(eᵘ).',
         'La fonction h est continue et additive ; h(u)=au. Il en résulte f(x)=exp(a ln x)=xᵃ.',
         'Vérifier la réciproque ; ajouter séparément f≡0, qui n’est pas représentée par cette famille strictement positive.']
    return result([metric('Défaut maximal sur les couples testés',np.max(abs(residual))),metric('f(1)',fone),metric('f′(1) du candidat',derivative),metric('Coefficient a',a)],
        [chart('Le changement de variable x=eᵘ','u=ln x','f(eᵘ)',series(profile,u,h(u)),series('Solution attendue',u,exact)),
         chart('Tester x=y=eᵘ','u=ln x','Défaut',series('Résidu de l’équation choisie',u,diag),series('Valeur exigée',u,u*0))],
        heat_scene('Résidu de '+equation+' en coordonnées logarithmiques',axis,residual,[dict(label=profile,x=u,y=h(u))],'u=ln x','v=ln y',description='Les arguments positifs sont x=eᵘ et y=eᵛ. Leurs produits deviennent des sommes sur la carte, mais la couleur évalue bien le résidu de l’équation choisie pour f.'),
        reasoning,['Domaine : x,y strictement positifs. L’équation est vérifiée pour tous les couples, pas seulement x=y.',
         'Les classifications reposent sur la continuité. Les perturbations servent à tester des conditions nécessaires, puis à rappeler la nécessité de la réciproque.',
         'La carte utilise des abscisses logarithmiques ; les résidus portent bien sur f et non sur une équation transformée différente.'])


def dalembert(p):
    k,b=p['k'],p['b']; family=p['family']; x=np.linspace(-3,3,601); axis=np.linspace(-2,2,65)
    if family=='cos': base=lambda u:np.cos(k*u); lam=-k*k; fzero=1
    elif family=='cosh': base=lambda u:np.cosh(k*u); lam=k*k; fzero=1
    else: base=lambda u:np.zeros_like(u); lam=0; fzero=0
    fun=lambda u:base(u)+b*u*u; X,Y=np.meshgrid(axis,axis)
    residual=fun(X+Y)+fun(X-Y)-2*fun(X)*fun(Y)
    differential=2*b-lam*b*x*x
    return result([metric('Défaut maximal de l’équation fonctionnelle',np.max(abs(residual))),metric('f(0)',fzero),metric('f′(0)',0),metric('Coefficient λ de f″=λf',lam)],
        [chart('Solution exacte et candidat perturbé','x','f(x)',series('Candidat',x,fun(x)),series('Solution exacte',x,base(x))),
         chart('Résidu de l’équation différentielle','x','f″−λf',series('Résidu du candidat',x,differential),series('Valeur exigée',x,x*0))],
        heat_scene('Résidu f(x+y)+f(x−y)−2f(x)f(y)',axis,residual,[dict(label='Candidat',x=x,y=fun(x))],description='Chaque case compare les deux membres de l’équation de d’Alembert. La parité et la valeur en 0 peuvent rester correctes tandis que cette égalité à deux variables échoue.'),
        ['Poser y=0 : f(x)[1−f(0)]=0. Ou bien f≡0, ou bien f(0)=1.',
         'Dans le second cas, poser x=0 : f(y)+f(−y)=2f(y), donc f est paire. Si elle est dérivable, f′(0)=0.',
         'Sous l’hypothèse f∈C², dériver deux fois par rapport à y puis poser y=0 : f″(x)=f″(0)f(x). Noter λ=f″(0).',
         'Résoudre ce problème initial : λ<0 donne cos(√(−λ)x), λ=0 donne 1 et λ>0 donne cosh(√λx). Vérifier chaque famille avec ses formules d’addition.'],
        ['La classification du laboratoire se fait sous l’hypothèse f∈C². Le recueil propose aussi une approche par les subdivisions dyadiques.',
         'La solution nulle doit être isolée avant de diviser par f(0). Pour une solution non nulle, les conditions f(0)=1 et f′(0)=0 sont indispensables.',
         'La carte est un contrôle numérique ; la formule d’addition fournit la vérification pour tous les réels.'])


def identified(x):
    return x*x*(x+1)/(1+x*x)


def identification_symetrie(p):
    b,R=p['b'],p['radius']; x=np.linspace(-R,R,801); x=x[abs(x)>1e-12]
    fun=lambda u:identified(u)+b*np.sin(u); residual=fun(x)+fun(-x)/x-x
    even=x*x/(1+x*x); odd=x**3/(1+x*x)
    return result([metric('Défaut maximal dans l’équation initiale',np.max(abs(residual))),metric('f(1)',float(fun(1))),metric('f(−1)',float(fun(-1))),metric('Valeur du prolongement continu en 0',0)],
        [chart('La solution est la somme d’une partie paire et d’une partie impaire','x≠0','Valeur',series('Solution exacte',x,identified(x)),series('Partie paire x²/(1+x²)',x,even),series('Partie impaire x³/(1+x²)',x,odd),series('Candidat perturbé',x,fun(x))),
         chart('Revenir à l’égalité demandée','x≠0','f(x)+f(−x)/x−x',series('Résidu',x,residual),series('Valeur exigée',x,x*0))],
        curves_scene('Deux substitutions déterminent chaque valeur',x,[('f(x) exact',identified(x)),('Partie paire',even),('Partie impaire',odd)],'x≠0','f(x)',description='La courbe totale est la somme des parties paire et impaire. Son prolongement vaut 0 en l’origine ; le quotient de l’équation initiale n’y est cependant pas défini.'),
        ['Noter A=f(x) et B=f(−x), avec x≠0. L’égalité initiale donne A+B/x=x.',
         'Remplacer x par −x : B−A/x=−x. Multiplier la première par x puis éliminer B : A(1+x²)=x²(x+1).',
         'Ainsi f(x)=x²(x+1)/(1+x²). Le dénominateur reste strictement positif ; chaque valeur de f est déterminée de manière unique.',
         'Substituer cette expression dans l’équation initiale pour vérifier la suffisance. Décomposer f en x²/(1+x²)+x³/(1+x²). Le prolongement en 0 vaut 0, mais l’équation initiale n’y est pas définie.'],
        ['Le domaine de l’équation est ℝ privé de 0. Aucune continuité n’est nécessaire pour l’identification sur ce domaine.',
         'La valeur en 0 n’est déterminée que si l’on demande un prolongement continu.',
         'Les valeurs aux points ±x sont liées par un système linéaire. Une simple comparaison de courbes ne prouve pas l’unicité.'])


def gauss_tail(L):
    return math.exp(-L*L)/L


def continuite_gauss(p):
    a,L=p['a'],p['L']; t=np.linspace(-L,L,2401); env=np.exp(-t*t); kernel=env*np.cos(a*t)
    integral=float(integrate(kernel,t)); exact=math.sqrt(math.pi)*math.exp(-a*a/4); tail=gauss_tail(L)
    dt=t[1]-t[0]; second_bound=2+4/math.e+a*a+4*abs(a)/math.sqrt(2*math.e)
    quad_bound=2*L*dt*dt*second_bound/12
    parameters=np.linspace(-6,6,101); numerical=integrate(env[None,:]*np.cos(parameters[:,None]*t),t)
    return result([metric('Intégrale calculée sur [−L,L]',integral),metric('Valeur sur ℝ',exact),metric('Erreur absolue constatée',abs(integral-exact)),metric('Borne des deux queues',tail),metric('Borne totale : queues + trapèzes',tail+quad_bound)],
        [chart('Le paramètre varie, le majorant reste le même','a','F(a)',series('Sur ℝ : √π exp(−a²/4)',parameters,np.sqrt(np.pi)*np.exp(-parameters**2/4)),series('Calcul tronqué',parameters,numerical)),
         chart('Contrôler |f(a,t)|≤exp(−t²)','t','Intégrande',series('f(a,t)',t,kernel),series('Majorant positif',t,env),series('Opposé du majorant',t,-env))],
        curves_scene('Une même enveloppe pour tous les paramètres',t,[('f(a,t)',kernel),('φ(t)=exp(−t²)',env),('−φ(t)',-env)],description='Le paramètre a change les oscillations, tandis que les deux courbes ±exp(−t²) les encadrent pour tous les a réels. La fenêtre affichée est [−L,L], avec des queues contrôlées séparément.'),
        ['Domaine du paramètre : a∈ℝ ; domaine d’intégration : J=ℝ. Pour tout t, a↦e⁻ᵗ²cos(at) est continue.',
         'La majoration |f(a,t)|≤φ(t)=e⁻ᵗ² est uniforme en a. De plus ∫ℝφ=√π<∞. Le premier théorème de la page 63 donne F continue sur ℝ.',
         'La valeur F(a)=√πe⁻ᵃ²/⁴ se retrouve aussi par dérivation sous le signe intégral et intégration par parties : F′(a)=−aF(a)/2, F(0)=√π.',
         'Les deux queues ont une somme absolue au plus e⁻ᴸ²/L. Le calcul par trapèzes possède en outre une borne basée sur sup|∂²f/∂t²| ; la dernière mesure les additionne.'],
        ['La continuité est démontrée par la domination, indépendamment de la formule explicite et des graphiques.',
         'La borne des queues est valable pour L>0. La borne de quadrature concerne la valeur de a sélectionnée.',
         'Cette intégrale est la partie réelle de la transformée de Fourier de la gaussienne, avec la convention utilisant e⁻ⁱᵃᵗ.'])


def concentration_envelope(t):
    """Supremum exact pour 0<a≤1 ; domaine t>0."""
    return np.where(t<=1,1/(math.e*t),np.exp(-t))


def continuite_defaut(p):
    a,eps,L=p['a'],p['epsilon'],p['L']; t=np.unique(np.concatenate([np.linspace(max(1e-5,a/100),min(8*a,L),501),np.linspace(max(1e-5,a/100),L,601)]))
    density=lambda width:np.exp(-t/width)/width
    cumulative=np.linspace(0,L,501); mass=-math.expm1(-eps/a); tail=math.exp(-L/a)
    local=2/a*np.exp(-t/(2*a)); all_envelope=concentration_envelope(t)
    return result([metric('F(a) pour a>0',1),metric('F(0)',0),metric('Masse dans [0,ε]',mass),metric('Masse après L',tail),metric('Différence ∫|fₐ−f₀|',1)],
        [chart('Le pic se déplace vers 0 et devient plus haut','t>0','Densité',series('Largeur a',t,density(a)),series('Largeur a/2',t,density(a/2)),series('Largeur 2a',t,density(2*a)),series('Majorant local pour a/2≤α≤2a',t,local)),
         chart('La masse cumulée est exactement 1−exp(−T/a)','T','∫₀ᵀ fₐ(t)dt',series('Largeur a',cumulative,-np.expm1(-cumulative/a)),series('Largeur a/2',cumulative,-np.expm1(-cumulative/(a/2))),series('Masse totale',cumulative,cumulative*0+1)),
         chart('L’enveloppe de toute la famille n’est pas intégrable près de 0','t>0','Enveloppe supérieure des densités',series('Borne supérieure pour 0<α≤1',t,all_envelope),y_scale='log')],
        curves_scene('Une masse constante dans une fenêtre qui rétrécit',t,[('fₐ',density(a)),('fₐ/₂',density(a/2)),('Majorant local autour de a>0',local)],description='Quand la largeur diminue, le pic devient plus haut et son aire reste égale à 1. Le majorant dessiné couvre un voisinage du a positif sélectionné ; il ne couvre pas uniformément la limite a=0.',note='La valeur au point t=0 est fixée à 0 ; une valeur en un seul point ne modifie pas l’intégrale.'),
        ['Définir fₐ(t)=e⁻ᵗ/ᵃ/a pour a>0,t>0 ; fixer fₐ(0)=0 et f₀(t)=0. Pour chaque t fixé, fₐ(t)→0 quand a→0⁺.',
         'Le changement de variable t=au donne ∫₀∞fₐ(t)dt=∫₀∞e⁻ᵘdu=1. Ainsi lim F(a)=1≠F(0)=0.',
         'Pour 0<t≤1, le maximum sur 0<a≤1 est atteint en a=t et vaut 1/(et). Tout majorant commun devrait dominer cette fonction, dont l’intégrale diverge près de 0.',
         'Autour d’un a strictement positif, a/2≤α≤2a donne fα(t)≤(2/a)e⁻ᵗ/⁽²ᵃ⁾, qui est intégrable. La continuité locale sur ]0,+∞[ ne résout pas le passage à a=0.'],
        ['Le point t=0 est défini séparément pour avoir une convergence ponctuelle partout ; cette modification ne change aucune intégrale.',
         'Le théorème de continuité ne s’applique pas au voisinage de 0, faute de majorant intégrable commun.',
         'Les intégrales et les masses affichées sont analytiques. Une grille uniforme en t peut manquer le pic ; le changement de variable t=au évite ce défaut.'])


def frullani_kernel(a,b,t):
    """La fonction sinc exponentielle est évaluée sans soustraction de deux proches nombres."""
    t=np.asarray(t,dtype=float); d=b-a; small=(t==0); safe=np.where(small,1,t)
    # La réécriture par la plus petite exponentielle évite aussi un débordement.
    if d>=0: value=np.exp(-a*t)*(-np.expm1(-d*t))/safe
    else: value=-np.exp(-b*t)*(-np.expm1(d*t))/safe
    return np.where(small,d,value)


def leibniz_frullani(p):
    a,b,L=p['a'],p['b'],p['L']; t=np.linspace(0,L,801); m=a/2
    kernel=frullani_kernel(a,b,t); derivative=-np.exp(-a*t); envelope=np.exp(-m*t)
    value=quadrature(lambda z:frullani_kernel(a,b,z),0,L); exact=math.log(b/a)
    tail=abs(b-a)*math.exp(-min(a,b)*L)/min(a,b); derivative_truncated=-(-math.expm1(-a*L))/a
    params=np.linspace(.25,4,71); values=[quadrature(lambda z:frullani_kernel(aa,b,z),0,L) for aa in params]
    return result([metric('F(a,b) calculé jusqu’à L',value),metric('ln(b/a)',exact),metric('Erreur absolue constatée',abs(value-exact)),metric('Borne absolue de la queue de F',tail),metric('∂F/∂a sur [0,L]',derivative_truncated),metric('∂F/∂a sur [0,∞[',-1/a)],
        [chart('Une constante fixée par F(b,b)=0','a>0','F(a,b)',series('ln(b/a)',params,np.log(b/params)),series('Intégrale jusqu’à L',params,values)),
         chart('La compensation rend le point t=0 régulier','t','f(a,b,t)',series('(e⁻ᵃᵗ−e⁻ᵇᵗ)/t',t,kernel)),
         chart('Leibniz : dominer la dérivée, et pas seulement f','t','Valeur absolue',series('|∂f/∂a|=e⁻ᵃᵗ',t,-derivative),series('φ(t)=e⁻⁽ᵃ/²⁾ᵗ',t,envelope))],
        curves_scene('Intégrande compensée et dérivée paramétrique',t,[('f(a,b,t)',kernel),('∂f/∂a',derivative),('Majorant de |∂f/∂a|',envelope)],description='La différence d’exponentielles enlève la singularité apparente en t=0. Dériver en a donne une exponentielle négative ; exp(−at/2) domine sa valeur absolue sur un voisinage du paramètre choisi.'),
        ['Domaine : (a,b)∈]0,+∞[² ; dérivation en a à b fixé. En 0, le quotient a pour limite b−a ; le prolonger par cette valeur.',
         'Pour a voisin du point sélectionné, choisir α≥a/2. Alors |∂f/∂α|=e⁻ᵅᵗ≤e⁻⁽ᵃ/²⁾ᵗ, dont l’intégrale vaut 2/a.',
         'Le théorème de Leibniz donne ∂F/∂a=−∫₀∞e⁻ᵃᵗdt=−1/a. Donc F(a,b)=−ln a+C(b).',
         'F(b,b)=0 impose C(b)=ln b. Par le théorème des accroissements finis, |f(a,b,t)|≤|b−a|e⁻ᵐⁱⁿ⁽ᵃ,ᵇ⁾ᵗ, d’où la borne de queue affichée.'],
        ['Le majorant est local en a ; il n’est pas uniforme lorsque a approche 0.',
         'La quadrature de Gauss se fait après régularisation du quotient en 0. La borne de queue ne comprend pas l’erreur de quadrature.',
         'Le domaine a,b>0 garantit la convergence à l’infini et le logarithme réel ln(b/a).'])


def arctan_kernel(a,t):
    return np.exp(-a*t)*np.sinc(t/np.pi)


def leibniz_arctan(p):
    a,L=p['a'],p['L']; t=np.linspace(0,L,1001); envelope=np.exp(-a*t/2)
    kernel=arctan_kernel(a,t); derivative=-np.exp(-a*t)*np.sin(t)
    value=quadrature(lambda z:arctan_kernel(a,z),0,L); dvalue=quadrature(lambda z:-np.exp(-a*z)*np.sin(z),0,L)
    exact=math.atan(1/a); params=np.linspace(.2,3,71)
    values=[quadrature(lambda z:arctan_kernel(aa,z),0,L) for aa in params]
    return result([metric('F(a) calculé jusqu’à L',value),metric('arctan(1/a)',exact),metric('Erreur absolue constatée',abs(value-exact)),metric('Borne absolue de la queue de F',math.exp(-a*L)/(a*L)),metric('F′(a) calculé jusqu’à L',dvalue),metric('F′(a) exact',-1/(1+a*a)),metric('Borne de la queue de F′',math.exp(-a*L)/a)],
        [chart('Calculer une intégrale par une équation différentielle','a>0','F(a)',series('arctan(1/a)',params,np.arctan(1/params)),series('Intégrale jusqu’à L',params,values)),
         chart('Une intégrande oscillante amortie','t','Valeur',series('e⁻ᵃᵗ sin(t)/t',t,kernel),series('Dérivée −e⁻ᵃᵗ sin t',t,derivative)),
         chart('Domination locale de la dérivée','t','Valeur absolue',series('|∂f/∂a|',t,abs(derivative)),series('φ(t)=e⁻⁽ᵃ/²⁾ᵗ',t,envelope))],
        curves_scene('L’amortissement contrôle les oscillations',t,[('Intégrande',kernel),('Dérivée paramétrique',derivative),('Majorant local de la dérivée',envelope)],description='Le facteur exponentiel amortit les lobes de sin t. Le majorant positif encadre la valeur absolue de la dérivée en a, ce qui autorise Leibniz localement pour a>0.'),
        ['Domaine : a>0 et t≥0. Le prolongement sin(t)/t=1 en t=0 rend f continue en t.',
         'Sur le voisinage α∈[a/2,3a/2], |∂f/∂α|=e⁻ᵅᵗ|sin t|≤e⁻⁽ᵃ/²⁾ᵗ, qui est intégrable. Leibniz est donc applicable localement.',
         'Intégrer l’exponentielle complexe, ou intégrer deux fois par parties : ∫₀∞e⁻ᵃᵗsin t dt=1/(1+a²). Ainsi F′(a)=−1/(1+a²).',
         'Comme |F(a)|≤∫₀∞e⁻ᵃᵗdt=1/a, F(a)→0 à l’infini. Il en résulte F(a)=π/2−arctan a=arctan(1/a).'],
        ['La démonstration vaut pour a>0. Le passage à a=0 demande un argument supplémentaire ; la domination locale utilisée ici ne le justifie pas.',
         'Pour t≥L, |sin t/t|≤1/L, d’où la borne e⁻ᵃᴸ/(aL) de la queue. Pour la dérivée, la borne est e⁻ᵃᴸ/a.',
         'Les bornes de queue concernent la troncature ; la quadrature numérique est une autre source d’erreur.'])


def exponential_moment_tail(a,n,L):
    """∫_L^∞ t^n exp(-at) dt, n entier positif ou nul, par intégrations par parties."""
    return math.exp(-a*L)*sum(math.factorial(n)/math.factorial(n-j)*L**(n-j)/a**(j+1) for j in range(n+1))


def gamma_log_moment(a,n,U,T,points=384):
    return quadrature(lambda u:np.exp(a*u-np.exp(u))*u**n,-U,math.log(T),points)


def gamma_moment_tail_bound(a,n,U,T):
    lower=exponential_moment_tail(a,n,U)
    rate=max(a-1,0)/T+n/(T*math.log(T))
    upper=T**(a-1)*math.log(T)**n*math.exp(-T)/(1-rate)
    return lower+upper


def digamma_trigamma(a):
    """Déplacement puis développement asymptotique, utilisé comme contrôle indépendant."""
    z=a; d=0.0; tr=0.0
    while z<12:
        d-=1/z; tr+=1/(z*z); z+=1
    bernoulli=[1/6,-1/30,1/42,-1/30,5/66,-691/2730]
    d+=math.log(z)-1/(2*z)-sum(B/(2*k*z**(2*k)) for k,B in enumerate(bernoulli,1))
    tr+=1/z+1/(2*z*z)+sum(B/z**(2*k+1) for k,B in enumerate(bernoulli,1))
    return d,tr


def derivees_gamma(p):
    a,n,q,T=p['a'],int(p['n']),int(p['q']),p['T']; U=q*math.log(10); u=np.linspace(-U,math.log(T),1201)
    m,M=a/2,a+1; transformed=np.exp(a*u-np.exp(u)); kernel=transformed*u**n
    envelope=np.exp(np.where(u<=0,m*u,M*u)-np.exp(u))*(1+abs(u)**n)
    value=gamma_log_moment(a,n,U,T); coarser=gamma_log_moment(a,n,U,T,192)
    moments=[gamma_log_moment(a,k,U,T) for k in range(3)]
    psi=moments[1]/moments[0]; variance=moments[2]/moments[0]-psi*psi; psi_ref,var_ref=digamma_trigamma(a)
    params=np.linspace(.6,5,61); values=[gamma_log_moment(aa,n,U,T) for aa in params]
    return result([metric('Γ(a) : valeur de référence',math.gamma(a)),metric('Γ⁽ⁿ⁾(a) tronquée',value),metric('Borne des queues de Γ⁽ⁿ⁾',gamma_moment_tail_bound(a,n,U,T)),metric('Écart entre deux quadratures (indicateur)',abs(value-coarser)),metric('Moyenne de ln t : Γ′/Γ',psi),metric('Variance de ln t calculée',variance),metric('Variance de référence : (ln Γ)″',var_ref)],
        [chart('Dériver plusieurs fois sous l’intégrale','a>0','Valeur',series('Γ(a)',params,[math.gamma(aa) for aa in params]),series('Γ⁽ⁿ⁾(a), ordre n choisi',params,values)),
         chart('Le changement t=eᵘ rend les deux queues visibles','u=ln t','Intégrande après changement de variable',series('uⁿ exp(au−eᵘ)',u,kernel),series('Majorant commun, ordres 0 à n',u,envelope),series('Opposé du majorant',u,-envelope)),
         chart('Convexité de ln Γ : une variance strictement positive','a','(ln Γ)″(a)',series('Variance de référence',params,[digamma_trigamma(aa)[1] for aa in params]))],
        curves_scene('Dérivée d’ordre n et domination locale en coordonnées u',u,[('Intégrande de Γ⁽ⁿ⁾',kernel),('Majorant commun',envelope)],'u=ln t','Intégrande transformée',description='Le changement t=eᵘ transforme aussi dt. La courbe de l’intégrande est uⁿexp(au−eᵘ) ; le majorant contrôle tous les ordres jusqu’à n sur le voisinage [a/2,a+1].'),
        ['Domaine : a>0. Sur le voisinage α∈[a/2,a+1], les dérivées partielles valent tᵅ⁻¹(ln t)ᵏe⁻ᵗ, pour 0≤k≤n.',
         'Pour 0<t≤1, les dominer par t⁽ᵃ/²⁾⁻¹(1+|ln t|ⁿ)e⁻ᵗ ; pour t≥1, par tᵃ(1+(ln t)ⁿ)e⁻ᵗ. Ces deux fonctions sont intégrables.',
         'Le troisième théorème de la page 63 donne Γ∈Cⁿ sur ]0,+∞[ et Γ⁽ᵏ⁾(a)=∫₀∞tᵃ⁻¹(ln t)ᵏe⁻ᵗdt. Comme n est arbitraire, Γ est C∞.',
         'Normaliser la densité par Γ(a). Alors Γ′/Γ=E(ln t) et (ln Γ)″=E((ln t)²)−E(ln t)²=Var(ln t)>0. La convexité résulte aussi de Cauchy–Schwarz.',
         'Les bornes des queues utilisent s=−ln t en bas, puis une majoration exponentielle à partir de T en haut. L’écart de deux quadratures est un indicateur numérique, pas une borne rigoureuse.'],
        ['L’ordre n est entier. Les bornes de queues portent sur la dérivée sélectionnée, indépendamment de l’erreur de quadrature.',
         'Les moyennes et variances numériques sont calculées avec la densité tronquée et renormalisée ; la variance de référence utilise une méthode indépendante.',
         'Le majorant dessiné est transformé avec dt=eᵘdu. Omettre ce facteur changerait l’intégrale et la domination.'])


def derivees_laplace(p):
    a,n,L=p['a'],int(p['n']),p['L']; t=np.linspace(0,L,1001); m=a/2
    density=t**n*np.exp(-a*t); envelope=(1+t**n)*np.exp(-m*t); sign=(-1)**n
    total=math.factorial(n)/a**(n+1); tail=exponential_moment_tail(a,n,L); val=quadrature(lambda z:z**n*np.exp(-a*z),0,L)
    params=np.linspace(.25,3,71); truncated=[sign*quadrature(lambda z:z**n*np.exp(-aa*z),0,L) for aa in params]
    cumulative=np.array([total-exponential_moment_tail(a,n,T) for T in t]); cumulative=np.maximum(cumulative,0)
    return result([metric('F⁽ⁿ⁾(a) exact',sign*total),metric('F⁽ⁿ⁾(a) calculé jusqu’à L',sign*val),metric('Masse absolue après L',tail),metric('Fraction de masse capturée',val/total),metric('Position du maximum t=n/a',n/a),metric('Intégrale du majorant commun',1/m+math.factorial(n)/m**(n+1))],
        [chart('Dérivées de 1/a et intégrales tronquées','a>0','F⁽ⁿ⁾(a)',series('(−1)ⁿ n!/aⁿ⁺¹',params,sign*math.factorial(n)/params**(n+1)),series('Intégrale jusqu’à L',params,truncated)),
         chart('Le maximum se trouve en n/a','t','Valeur positive',series('tⁿe⁻ᵃᵗ',t,density),series('Majorant (1+tⁿ)e⁻⁽ᵃ/²⁾ᵗ',t,envelope),xMarker=n/a,xMarkerLabel='Maximum n/a'),
         chart('La masse cumulée révèle une troncature trop courte','T','Fraction de masse',series('∫₀ᵀ tⁿe⁻ᵃᵗ / masse totale',t,cumulative/total),series('Masse totale',t,t*0+1))],
        curves_scene('Dominer tous les ordres jusqu’à n',t,[('tⁿe⁻ᵃᵗ',density),('Majorant local commun',envelope)],'t','Valeur positive',description='La densité est positive, mais la dérivée F⁽ⁿ⁾ porte le signe (−1)ⁿ. Son pic est à n/a ; le majorant local commun permet de dériver aux ordres 0 à n.'),
        ['Domaine : a>0. La k-ième dérivée de e⁻ᵃᵗ par rapport à a est (−t)ᵏe⁻ᵃᵗ.',
         'Pour α∈[a/2,3a/2] et 0≤k≤n, tᵏ≤1+tⁿ. Le majorant (1+tⁿ)e⁻⁽ᵃ/²⁾ᵗ est donc intégrable et commun à tous les ordres.',
         'Le théorème de dérivation d’ordre n donne F⁽ⁿ⁾(a)=∫₀∞(−t)ⁿe⁻ᵃᵗdt. Comme F(a)=1/a, on obtient (−1)ⁿn!/aⁿ⁺¹.',
         'Ainsi (−1)ⁿF⁽ⁿ⁾(a)>0 pour chaque n : F est complètement monotone. Le changement de variable u=at retrouve le facteur a⁻ⁿ⁻¹.',
         'L’intégration par parties répétée fournit une expression exacte de la queue après L. Le maximum de tⁿe⁻ᵃᵗ est en t=n/a, qui peut sortir de la fenêtre.'],
        ['Le signe affiché dépend de la parité de n. La densité utilisée pour les masses est toujours positive.',
         'Le majorant est local en a. Aucun majorant commun intégrable ne couvre tous les a>0 lorsque a approche 0.',
         'La masse après L est analytique. La valeur tronquée est calculée par quadrature ; la masse cumulée est obtenue par la formule de la queue.'])


COMPUTE={name:globals()[name] for name in ['cauchy_additive','cauchy_multiplicative','dalembert','identification_symetrie','continuite_gauss','continuite_defaut','leibniz_frullani','leibniz_arctan','derivees_gamma','derivees_laplace']}
