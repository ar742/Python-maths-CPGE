"""Calculs exacts des expériences arithmétiques et certificats indépendants."""
from __future__ import annotations
from functools import lru_cache
from itertools import product
import math
import warnings
import numpy as np
import sympy as sp
from commun import chart, series, metric, result, table, curve_scene, plane_scene, formula
X=sp.Symbol('X')

def poly(expr,field='Q'):
    return sp.Poly(expr,X,domain=sp.QQ) if field=='Q' else sp.Poly(expr,X,modulus=int(field))
def txt(value): return formula(value.as_expr() if isinstance(value,sp.Poly) else value)
def deg(P): return -1 if P.is_zero else int(P.degree())
def evaluation(P,x):
    values=np.polyval(np.array([float(c) for c in P.all_coeffs()]),x)
    return values.tolist()
def coefficients(P):
    n=max(0,deg(P)); return list(range(n+1)),[int(P.nth(k)) if P.nth(k).is_Integer else float(P.nth(k)) for k in range(n+1)]
def bernoulli_poly(n): return sp.Poly(sp.bernoulli(n,X),X,domain=sp.QQ)
def bernoulli_number(n): return sp.Rational(sp.bernoulli(n,0))
def euclide_bezout(params):
    cas=params['cas']; t=int(params['translation']); c=int(params['scale']); Y=X-t
    if cas=='tp': A=poly(c*Y**4); B=poly((Y-1)*(Y-2)*(Y-3))
    elif cas=='composition': A=poly(c*(Y**4+5*Y**3+5*Y**2-Y-2)); B=poly(Y**2+Y-1)
    else: A=poly(c*(Y**2+1)*(Y**3-2*Y+1)); B=poly((Y**2+1)*(Y**2+Y+2))
    U,V,D=sp.gcdex(A,B); ledger=[]; old,current=A,B; degrees=[deg(A),deg(B)]
    while not current.is_zero:
        Q,R=old.div(current); ledger.append([txt(old),txt(current),txt(Q),txt(R)])
        if not R.is_zero: degrees.append(deg(R))
        old,current=current,R
    cert=(A*U+B*V-D).is_zero
    nodes=list(range(len(degrees))); x=np.linspace(t-1.4,t+3.4,280)
    charts=[chart('Les degrés descendent strictement après le premier diviseur','Rang dans l’algorithme','Degré',series('Degré du reste',nodes,degrees)),chart('Polynômes de départ et PGCD unitaire','x','Valeur',series('A(x)',x.tolist(),evaluation(A,x)),series('B(x)',x.tolist(),evaluation(B,x)),series('D(x)',x.tolist(),evaluation(D,x)))]
    return result([metric('PGCD unitaire D',txt(D)),metric('Nombre de divisions',len(ledger)),metric('Certificat AU+BV=D','exact' if cert else 'non validé'),metric('Premier reste',ledger[0][3])],charts,
        curve_scene('Du dessin au certificat exact',nodes,[('Degrés successifs',degrees)],'Rang','Degré','Les degrés expliquent la fin de l’algorithme. Le tableau conserve les divisions exactes.'),
        [f'A={txt(A)} et B={txt(B)}.',f'U={txt(U)}; V={txt(V)}.',f'AU+BV={txt(D)}. La différence calculée est le polynôme nul.',f'Le dernier reste non nul est normalisé pour obtenir un PGCD unitaire.'],
        ['Calculs exacts dans ℚ[X]; les courbes sont seulement une visualisation réelle.','Le degré du polynôme nul est −∞; aucun point de degré n’est tracé pour lui.'],
        table('Division euclidienne : dividende = diviseur × quotient + reste',['Dividende','Diviseur','Quotient','Reste'],ledger))

def gauss_eisenstein(params):
    cas=params['cas']; n=int(params['n']); p=int(params['p']); t=int(params['translation']); c=int(params['content'])
    if cas=='eisenstein': prim=poly((X-t)**n+p*(X-t)+p); witness=poly(prim.as_expr().subs(X,X+t)); proof=f'Après X→X+{t}, Eisenstein en {p} : coefficients non dominants divisibles par {p}, terme constant {p} non divisible par {p*p}.'
    elif cas=='reduction': prim=poly(X**4+X+1); witness=poly(prim.as_expr(),'2'); proof='Sur F₂, pas de racine et pas de division par X²+X+1, seul quadratique unitaire irréductible : le degré 4 est irréductible.'
    else: prim=poly(X**4+4); witness=prim; proof='X⁴+4=(X²−2X+2)(X²+2X+2). Les deux quadratiques sont sans racine réelle : absence de racine rationnelle ne suffit pas.'
    A=prim.mul_ground(c); B=poly(3*(X+1)**2); contentA,_=A.primitive(); contentB,_=B.primitive(); contentAB,_=(A*B).primitive()
    ks,cs=coefficients(A); bk,bc=coefficients(B); ak,ac=coefficients(A*B)
    irr=bool(prim.is_irreducible); factor=sp.factor(A.as_expr())
    rows=[[k,txt(witness.nth(k)),int(witness.nth(k))%p if cas=='eisenstein' else '—'] for k in range(deg(witness)+1)]
    return result([metric('Contenu c(A)',str(contentA)),metric('Contenu c(AB)',str(contentAB)),metric('c(A)c(B)',str(contentA*contentB)),metric('Irréductible sur ℚ', 'oui' if irr else 'non')],
        [chart('Le contenu est un facteur commun des coefficients','Puissance de X','Coefficient',series('A',ks,cs),series('B',bk,bc),series('AB',ak,ac),style='bars')],
        curve_scene('Comparer le polynôme et sa partie primitive',ks,[('A',cs),('Partie primitive',coefficients(prim)[1])],'Puissance de X','Coefficient','Les coefficients sont exacts; la barre verticale représente leur valeur et non une racine.'),
        [f'A={txt(A)}; partie primitive {txt(prim)}.',f'B={txt(B)}; c(B)={contentB}.',f'c(AB)={contentAB}=c(A)c(B).',proof,f'Factorisation rationnelle : {txt(factor)}.'],
        ['Le contenu est le PGCD positif des coefficients entiers.','Le lemme de Gauss concerne le passage ℤ[X]↔ℚ[X]; le théorème de Gauss de divisibilité est un autre énoncé.'],
        table('Coefficients du polynôme témoin : translaté ou réduit selon le cas',['Rang k','Coefficient','Reste modulo p si Eisenstein'],rows))

def inverse_quotient(params):
    field=params['field']; a=int(params['a']); b=int(params['b']); A=poly(X**2+a*X+b,field)
    M=poly(X**4+X+1 if params['modulus']=='generic' else (X**2+1)*(X**2+X+1),field)
    U,V,D=sp.gcdex(A,M); invertible=deg(D)==0; inv=U.rem(M) if invertible else None
    columns=[]
    for j in range(deg(M)):
        C=(A*poly(X**j,field)).rem(M); columns.append([txt(C.nth(i)) for i in range(deg(M))])
    rows=[[f'X^{j}',*columns[j]] for j in range(deg(M))]
    sample=list(range(deg(M))); coeff=[float(A.nth(j)) for j in sample]
    if invertible:
        second=[float(inv.nth(j)) for j in sample]; status='inversible'; steps=[f'A={txt(A)}; M={txt(M)}.',f'Bézout : ({txt(U)})A+({txt(V)})M=1.',f'L’inverse est U mod M={txt(inv)}.',f'Le reste de A×inverse modulo M est {txt((A*inv).rem(M))}.']
    else:
        witness=M.exquo(D); second=[float(witness.nth(j)) for j in sample]; status='non inversible'; steps=[f'A={txt(A)}; M={txt(M)}.',f'PGCD(A,M)={txt(D)} n’est pas constant.',f'La classe non nulle de M/D={txt(witness)} est annulée par A.',f'A×(M/D) mod M={txt((A*witness).rem(M))}; c’est un diviseur de zéro.']
    fieldname='ℚ' if field=='Q' else f'F{field}'
    return result([metric('Corps des coefficients',fieldname),metric('Dimension du quotient',deg(M)),metric('Classe de A',status),metric('PGCD(A,M)',txt(D))],
        [chart('Coordonnées dans la base 1, X, X², X³','Rang de la puissance','Coefficient',series('A mod M',sample,coeff),series('Inverse' if invertible else 'Élément annulé',sample,second),style='bars')],
        curve_scene('Une classe est un vecteur de quatre coefficients',sample,[('A',coeff),('Inverse' if invertible else 'Élément annulé',second)],'Rang','Coefficient','Dans Fₚ, la hauteur représente un résidu entier, pas une mesure réelle dans le corps.'),steps,
        ['Dans K[X]/(M), les classes sont représentées par des polynômes de degré strictement inférieur à deg M.','Le quotient est une algèbre; il n’est un corps que si M est irréductible.'],
        table('Multiplication par A : coordonnées de A·Xʲ modulo M',['Vecteur','1','X','X²','X³'],rows))

def restes_chinois(params):
    cas=params['cas']; a=int(params['a']); b=int(params['b'])
    if cas=='coprime': M1=poly(X**2+1); M2=poly(X**3-X+1); R1=poly(a*X+b); R2=poly(X**2+b*X+a)
    else: M1=poly((X-1)*(X**2+1)); M2=poly((X-1)*(X**2+X+2)); R1=poly(a*X+b); R2=poly(a*X+b+(X-1)*X+(1 if cas=='incompatible' else 0))
    R1=R1.rem(M1);R2=R2.rem(M2);D=M1.gcd(M2); difference=R2-R1; compatible=difference.rem(D).is_zero; L=M1.lcm(M2)
    rows=[['M₁',txt(M1)],['M₂',txt(M2)],['R₁',txt(R1)],['R₂',txt(R2)],['D=PGCD',txt(D)],['L=PPCM',txt(L)]]
    x=np.linspace(-1.4,2.0,280); curves=[series('R₁(x)',x.tolist(),evaluation(R1,x)),series('R₂(x)',x.tolist(),evaluation(R2,x))]
    steps=[f'On cherche S≡{txt(R1)} (mod {txt(M1)}) et S≡{txt(R2)} (mod {txt(M2)}).',f'La condition est D | R₂−R₁. Le reste par D vaut {txt(difference.rem(D))}.']
    if compatible:
        A=M1.exquo(D); B=M2.exquo(D); inv=sp.invert(A,B); W=(difference.exquo(D)*inv).rem(B); S=(R1+M1*W).rem(L)
        rows.extend([['S',txt(S)],['S mod M₁',txt(S.rem(M1))],['S mod M₂',txt(S.rem(M2))]])
        curves.append(series('S(x)',x.tolist(),evaluation(S,x))); steps.extend([f'On écrit S=R₁+M₁W et résout (M₁/D)W≡(R₂−R₁)/D modulo M₂/D.',f'S={txt(S)}; tous les autres représentants valent S+LQ, Q∈ℚ[X].'])
        if deg(D)==0:
            E1=(M2*sp.invert(M2,M1)).rem(L); E2=poly(1)-E1
            rows.extend([['E₁',txt(E1)],['E₂',txt(E2)]])
            steps.append(f'E₁+E₂=1; Eᵢ²≡Eᵢ et E₁E₂≡0 modulo L. S≡R₁E₁+R₂E₂.')
    else: steps.append('Aucune solution : les deux restes imposent des valeurs différentes au facteur commun X−1.'); S=None
    return result([metric('Compatibilité','oui' if compatible else 'non'),metric('PGCD des modules',txt(D)),metric('Degré du module commun',deg(L)),metric('Solution réduite',txt(S) if S else 'aucune' if not compatible else '0')],
        [chart('Les congruences portent sur des restes, pas sur toutes les valeurs','x','Valeur',*curves)],
        curve_scene('Recoller sans confondre égalité et congruence',x.tolist(),[(c['label'],c['y']) for c in curves],'x','Valeur','Le tableau certifie chaque congruence par une division exacte.'),steps,
        ['Calculs dans ℚ[X]. Une congruence S≡R modulo M signifie M | S−R.','Sans coprimalité, la compatibilité se vérifie modulo le PGCD et l’unicité modulo le PPCM.'],table('Certificats du recollement',['Objet','Polynôme exact'],rows))

def gvalue(n,kind,k):
    if kind=='phi': return int(sp.totient(n))
    if kind=='power': return n**k
    return 1
def fvalue(n,kind,k): return sum(gvalue(d,kind,k) for d in sp.divisors(n))
def mobius_diviseurs(params):
    n=int(params['n']); k=int(params['k']);kind=params['fonction']; ds=[int(d) for d in sp.divisors(n)]
    terms=[int(sp.mobius(d))*fvalue(n//d,kind,k) for d in ds]; recovered=sum(terms);target=gvalue(n,kind,k)
    nodes=list(range(1,n+1)); mus=[int(sp.mobius(j)) for j in nodes]
    conv=[sum(int(sp.mobius(d)) for d in sp.divisors(j)) for j in nodes]
    rows=[[d,txt(sp.factorint(d)),int(sp.mobius(d)),fvalue(n//d,kind,k),term] for d,term in zip(ds,terms)]
    return result([metric('g(n) calculé directement',target),metric('g(n) retrouvé par Möbius',recovered),metric('Nombre de diviseurs',len(ds)),metric('(μ∗1)(n)',sum(int(sp.mobius(d)) for d in ds))],
        [chart('Chaque diviseur apporte un terme signé','Diviseur d de n','μ(d) f(n/d)',series('Contribution exacte',ds,terms),style='bars'),chart('L’unité de convolution vaut 1 en n=1 seulement','Entier','Valeur',series('μ',nodes,mus),series('μ∗1',nodes,conv),style='bars')],
        curve_scene('Des contributions positives, négatives ou nulles',ds,[('μ(d)f(n/d)',terms)],'Diviseur d','Contribution','Un facteur carré annule μ(d). La somme de ces contributions reconstruit g(n).'),
        [f'f(n)=Σ_{{d|n}} g(d); ici f({n})={fvalue(n,kind,k)}.',f'La factorisation de n est {txt(sp.factorint(n))}.',f'g({n})=Σ_{{d|{n}}} μ(d)f({n}/d)={recovered}.','L’unité χ de la convolution vérifie χ(1)=1 et χ(n)=0 pour n>1.'],
        ['μ(1)=1; μ(d)=0 si un carré premier divise d; sinon μ(d)=(−1)^r avec r facteurs premiers distincts.','La convolution ∗ somme sur les diviseurs; ce n’est pas le produit usuel point par point.'],table('Une inversion complète sur les diviseurs de n',['d','Factorisation de d','μ(d)','f(n/d)','Contribution'],rows))

def irreducible_count(p,n): return sum(int(sp.mobius(d))*p**(n//d) for d in sp.divisors(n))//n
@lru_cache(maxsize=64)
def enumerated_irreducibles(p,n):
    if p**n>125: return None
    values=[]
    for coeff in product(range(p),repeat=n):
        P=sp.Poly(X**n+sum(coeff[k]*X**k for k in range(n)),X,modulus=p)
        if P.is_irreducible: values.append(P)
    return tuple(values)
def irreductibles_fp(params):
    p=int(params['p']);n=int(params['n']);ds=[int(d) for d in sp.divisors(n)];terms=[int(sp.mobius(d))*p**(n//d) for d in ds]
    count=irreducible_count(p,n);enumeration=enumerated_irreducibles(p,n)
    rows=[[d,int(sp.mobius(d)),n//d,p**(n//d),v] for d,v in zip(ds,terms)]
    steps=[f'Iₚ(n) désigne le nombre de polynômes unitaires irréductibles de degré n sur Fₚ.',f'p^n=Σ_{{d|n}} d Iₚ(d). Ici {p**n}={" + ".join(str(d*irreducible_count(p,d)) for d in ds)}.',f'nIₚ(n)=Σ_{{d|n}} μ(d)p^(n/d)={sum(terms)}; donc Iₚ({n})={count}.']
    if enumeration is not None: steps.append(f'Énumération de {p**n} polynômes unitaires : {len(enumeration)} irréductibles. Liste : '+ '; '.join(txt(P) for P in enumeration)+'.')
    else: steps.append('L’énumération est réservée aux cas pⁿ≤125. Le comptage par Möbius reste exact dans tous les réglages.')
    ns=list(range(1,n+1)); counts=[irreducible_count(p,j) for j in ns]
    return result([metric('Nombre Iₚ(n)',count),metric('Nombre nIₚ(n)',n*count),metric('Polynômes unitaires de degré n',p**n),metric('Énumération indépendante',str(len(enumeration))+' confirmés' if enumeration is not None else 'non effectuée : pⁿ>125')],
        [chart('Une somme signée, avant division par n','Diviseur d','Contribution',series('μ(d)p^(n/d)',ds,terms),style='bars'),chart('Combien d’irréductibles à chaque degré ?','Degré','Nombre',series('Iₚ(j)',ns,counts),style='bars')],
        curve_scene('Le degré n ne se confond pas avec le nombre pⁿ',ns,[('Nombre d’irréductibles',counts)],'Degré','Nombre','La somme des degrés de tous les facteurs de X^(pⁿ)−X vaut pⁿ.'),steps,
        ['p est premier, donc Fₚ est un corps. On compte seulement les polynômes unitaires.','Les calculs sont entiers exacts; les graphiques n’approximent que leur affichage.'],table('Inversion de Möbius pour le degré choisi',['d','μ(d)','n/d','p^(n/d)','Terme signé'],rows))

@lru_cache(maxsize=16)
def frobenius_factors(p,n):
    P=sp.Poly(X**(p**n)-X,X,modulus=p)
    with warnings.catch_warnings():
        warnings.simplefilter('ignore',sp.utilities.exceptions.SymPyDeprecationWarning)
        _,factors=P.factor_list()
    return P,tuple(factors)
def frobenius_fp(params):
    p=int(params['p']);n=int(params['n']);P,factors=frobenius_factors(p,n);D=P.gcd(P.diff()); groups={d:[] for d in sp.divisors(n)}
    for Q,m in factors: groups[deg(Q)].append(Q)
    rows=[[txt(Q),deg(Q),m,'oui' if n%deg(Q)==0 else 'non'] for Q,m in factors]
    ds=[int(d) for d in groups]; totals=[d*len(groups[d]) for d in ds]
    # Frobenius sur F_p : a^p=a; on n’emploie pas les résidus modulo p pour représenter tout F_(p^n).
    residues=list(range(p));fixed=[pow(a,p,p) for a in residues]
    return result([metric('Degré de X^(pⁿ)−X',p**n),metric('Nombre de facteurs',len(factors)),metric('PGCD avec la dérivée',txt(D)),metric('Tous les facteurs simples','oui' if all(m==1 for Q,m in factors) else 'non')],
        [chart('Contribution de chaque degré à pⁿ','Degré d divisant n','Nombre total de racines',series('d × nombre de facteurs',ds,totals),style='bars'),chart('Le Frobenius fixe le corps de base Fₚ','Résidu a','Résidu',series('a',residues,residues),series('aᵖ modulo p',residues,fixed),style='bars')],
        curve_scene('Les degrés divisent n',ds,[('Degrés cumulés des facteurs',totals)],'Degré','Contribution','Les barres comptent des racines dans une clôture algébrique, pas des points dans le plan complexe.'),
        [f'P=X^{p**n}−X dans F{p}[X].',f'P′=−1={txt(P.diff())} dans F{p}, donc PGCD(P,P′)=1.',f'Factorisation exacte : {" × ".join("("+txt(Q)+")" for Q,m in factors)}.',f'Σ d Iₚ(d)={sum(totals)}=pⁿ. Les degrés observés sont {", ".join(str(d) for d in ds if groups[d])}.','Les racines forment le corps à pⁿ éléments; les opérations y sont des opérations de corps fini, pas celles de ℂ.'],
        ['Calcul en caractéristique p : la dérivée de X^(pⁿ) est nulle.','Un irréductible de degré d divise X^(pⁿ)−X exactement lorsque d divise n.'],table('Tous les facteurs calculés sur Fₚ',['Facteur unitaire','Degré','Multiplicité','Degré divisant n'],rows))

def cyclotomie(params):
    n=int(params['n']);Phi=poly(sp.cyclotomic_poly(n,X));ds=[int(d) for d in sp.divisors(n)]
    factors=[poly(sp.cyclotomic_poly(d,X)) for d in ds];productpoly=poly(1)
    for Q in factors: productpoly*=Q
    num=poly(1);den=poly(1); rows=[]
    for d in ds:
        mu=int(sp.mobius(n//d));Q=poly(X**d-1)
        if mu==1:num*=Q
        elif mu==-1:den*=Q
        rows.append([d,mu,txt(Q),txt(sp.cyclotomic_poly(d,X))])
    quotient,remainder=num.div(den);ks,cs=coefficients(Phi)
    roots=[dict(x=float(math.cos(2*math.pi*k/n)),y=float(math.sin(2*math.pi*k/n)),label=f'k={k}',group=1 if math.gcd(k,n)==1 else 0) for k in range(n)]
    return result([metric('Polynôme Φₙ',txt(Phi)),metric('Degré φ(n)',int(sp.totient(n))),metric('Racines primitives',sum(math.gcd(k,n)==1 for k in range(n))),metric('Produit ∏ Φ_d=Xⁿ−1','exact' if productpoly==poly(X**n-1) else 'non validé')],
        [chart('Coefficients parfois négatifs, racines toutes sur le cercle','Puissance de X','Coefficient',series('Φₙ',ks,cs),style='bars')],
        plane_scene('Racines de l’unité : distinguer l’ordre exact',points=roots,circles=[dict(x=0,y=0,r=1,label='Cercle unité')],bounds=[-1.25,1.25,-1.25,1.25],description='Le groupe 1 correspond à PGCD(k,n)=1 : ces racines ont exactement l’ordre n.'),
        [f'X^{n}−1=∏_{{d|{n}}} Φ_d(X).',f'Φ_{n}(X)=∏_{{d|{n}}}(X^d−1)^μ(n/d). Les exposants −1 indiquent une division exacte.',f'Numérateur : {txt(num)}; dénominateur : {txt(den)}.',f'Quotient : {txt(quotient)}; reste : {txt(remainder)}.',f'Les racines primitives sont exp(2πik/{n}) avec PGCD(k,{n})=1.'],
        ['Les polynômes cyclotomiques ont des coefficients entiers et sont irréductibles sur ℚ; ce dernier théorème est présenté comme un prolongement.','Le cercle représente les racines complexes; leur nombre est φ(n).'],table('Deux usages des diviseurs : factorisation et inversion',['d','μ(n/d)','X^d−1','Φ_d'],rows))

def bernoulli_faulhaber(params):
    p=int(params['power']);N=int(params['N']);a=sp.Rational(str(params['shift']));B=bernoulli_poly(p+1)
    S=poly((B.as_expr().subs(X,X+1)-B.eval(0))/(p+1))
    direct=sum(k**p for k in range(N+1));exact=S.eval(N);xs=list(range(N+1));sums=[sum(k**p for k in range(j+1)) for j in xs]
    u=np.linspace(0,1,240);bc=evaluation(B,u);translated=evaluation(poly(B.as_expr().subs(X,X+a)),u)
    numbers=[bernoulli_number(k) for k in range(p+2)]
    rows=[[k,txt(numbers[k]),txt(bernoulli_poly(k))] for k in range(p+2)]
    difference=sp.expand(B.as_expr().subs(X,X+1)-B.as_expr()-(p+1)*X**p)
    return result([metric('Somme directe Σ kᵖ',direct),metric('Formule polynomiale',str(exact)),metric('Identité de différence finie','exacte' if difference==0 else 'non validée'),metric('b₁=B₁(0)','−1/2')],
        [chart('Un polynôme retrouve chaque somme entière','Borne n','Somme',series('Somme directe',xs,sums),series('Polynôme Sₚ(n)',xs,[int(S.eval(j)) for j in xs])),chart('Les polynômes de Bernoulli sur une unité','x','Valeur',series(f'B{p+1}(x)',u.tolist(),bc),series(f'B{p+1}(x+a)',u.tolist(),translated))],
        curve_scene('Une différence finie remplace un long calcul',u.tolist(),[(f'B{p+1}(x)',bc),(f'B{p+1}(x+a)',translated)],'x','Valeur','a translate seulement le second dessin. La somme Σₖ₌₀ᴺkᵖ utilise Bₚ₊₁ sans cette translation.'),
        [f'B_{p+1}(X)={txt(B)}.',f'B_{p+1}(X+1)−B_{p+1}(X)=({p+1})X^{p}.',f'En sommant de k=0 à N, les termes intermédiaires s’annulent : Sₚ(N)=[Bₚ₊₁(N+1)−Bₚ₊₁(0)]/(p+1).',f'Sₚ(X)={txt(S)}; Sₚ({N})={exact}.'],
        ['p≥1, donc 0ᵖ=0. On évite ici la convention particulière 0⁰.','La convention employée partout est b₁=B₁(0)=−1/2; la somme est écrite avec N+1.'],table('Nombres et polynômes de Bernoulli dans une même convention',['k','bₖ=Bₖ(0)','Bₖ(X)'],rows))

def euler_maclaurin(params):
    kind=params['fonction'];N=int(params['N']);order=int(params['order']);degree=int(params['degree'])
    if kind=='inverse': f=1/X;sumexact=sum((sp.Rational(1,j) for j in range(1,N+1)),sp.Integer(0));integral=sp.log(N)
    elif kind=='exponential': f=sp.exp(-X/3);sumexact=sum((f.subs(X,j) for j in range(1,N+1)),sp.Integer(0));integral=3*(sp.exp(-sp.Rational(1,3))-sp.exp(-sp.Rational(N,3)))
    else:f=X**degree;sumexact=sp.Integer(sum(j**degree for j in range(1,N+1)));integral=sp.Rational(N**(degree+1)-1,degree+1)
    target=float(sumexact);endpoint=(f.subs(X,1)+f.subs(X,N))/2;partial=integral+endpoint
    approximations=[float(integral),float(partial)];labels=['Intégrale seule','Demi-extrémités']; rows=[['Intégrale',txt(integral),float(integral),abs(target-float(integral))],['Demi-extrémités',txt(endpoint),float(partial),abs(target-float(partial))]]
    for k in range(1,5):
        derivative=sp.diff(f,X,2*k-1);term=bernoulli_number(2*k)/sp.factorial(2*k)*(derivative.subs(X,N)-derivative.subs(X,1));partial+=term
        approximations.append(float(partial));labels.append(f'Correction k={k}');rows.append([f'k={k}',txt(term),float(partial),abs(target-float(partial))])
    chosen=approximations[order+1];errors=[abs(target-v) for v in approximations]
    if order==0:
        # |B_1 périodique|≤1/2 : borne du reste R_0.
        derivative=sp.diff(f,X);bound=float(abs(f.subs(X,N)-f.subs(X,1))/2)
    else:
        derivative=sp.diff(f,X,2*order)
        if derivative==0 or (kind=='polynomial' and degree<=2*order): bound=0.0
        else:
            # Pour ces trois familles, la dérivée paire ne change pas de signe sur [1,N].
            primitive=sp.diff(f,X,2*order-1);variation=abs(primitive.subs(X,N)-primitive.subs(X,1));bound=float(abs(bernoulli_number(2*order))/sp.factorial(2*order)*variation)
    xs=np.linspace(1,N,300);fy=np.array(sp.lambdify(X,f,'numpy')(xs));fy=np.full(xs.shape,float(fy)) if fy.ndim==0 else fy
    stages=list(range(-1,5))
    return result([metric('Somme de j=1 à N',target),metric('Approximation choisie',chosen),metric('Erreur absolue',abs(target-chosen)),metric('Borne garantie du reste',bound)],
        [chart('Lire les corrections avec la somme de référence','Rang : −1 intégrale, 0 extrémités, k corrections','Valeur',series('Approximation',stages,approximations),series('Somme exacte',stages,[target]*len(stages))),chart('Une borne ne promet pas une décroissance à chaque ordre','Rang','Erreur absolue',series('Erreur observée',stages,errors))],
        curve_scene('Somme discrète et aire sous une courbe',xs.tolist(),[('f(x)',fy.tolist())],'x','f(x)','La somme inclut les deux extrémités 1 et N; l’intégrale porte sur [1,N].'),
        [f'f(x)={txt(f)}; S=Σ_{{j=1}}^{N} f(j).',f'On part de ∫₁ᴺf + [f(1)+f(N)]/2.',f'À l’ordre k, on ajoute b₂ₖ[f^(2k−1)(N)−f^(2k−1)(1)]/(2k)!.',f'k={order} : approximation {chosen:.12g}, erreur {abs(target-chosen):.6g}, borne {bound:.6g}.','Pour un polynôme, assez de corrections donnent une formule exacte car les dérivées suivantes sont nulles.'],
        ['Les trois fonctions sont indéfiniment dérivables sur [1,N]; 1/x n’a pas de singularité sur cet intervalle.','Pour k≥1 : |Rₖ|≤|b₂ₖ|/(2k)! ∫₁ᴺ|f^(2k)(x)|dx. Pour k=0 : |R₀|≤½∫₁ᴺ|f′|.','Si deg f≤2k, le reste est exactement nul sur des bornes entières. La borne affichée est alors affinée à 0. Les flottants finaux peuvent laisser une erreur d’arrondi.'],table('Contributions exactes et erreurs numériques',['Étape','Terme ajouté','Approximation cumulée','Erreur absolue'],rows))

COMPUTE={name:globals()[name] for name in ['euclide_bezout','gauss_eisenstein','inverse_quotient','restes_chinois','mobius_diviseurs','irreductibles_fp','frobenius_fp','cyclotomie','bernoulli_faulhaber','euler_maclaurin']}
