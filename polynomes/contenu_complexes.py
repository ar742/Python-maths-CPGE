"""Buts, méthodes et exercices pour la famille Racines & Plan complexe."""
GUIDES = {}
LESSONS = []
EXERCISES = []

def guide(id_,purpose,objects,hypotheses,techniques,sup,spe,beyond,first_steps,expected):
    GUIDES[id_]=dict(purpose=purpose,objects=objects,hypotheses=hypotheses,techniques=techniques,levels=dict(sup=sup,spe=spe,beyond=beyond),first_steps=first_steps,expected=expected)

def lesson(id_,title,level,html):
    LESSONS.append(dict(lab=id_,title=title,level=level,html=html))

def exercise(id_,title,level,question,answer):
    EXERCISES.append(dict(lab=id_,title=title,level=level,question=question,answer=answer))

guide('cayley_tangentes','Résoudre l’exercice 5 de la page 31 puis relier ses tangentes aux coefficients d’un polynôme.',
    ['n est un entier positif; le réglage commence à n=2. Pₙ(Z)=(Z+1)²ⁿ−(Z−1)²ⁿ est un polynôme en l’indéterminée Z.',
     'z est une solution complexe; w=(1+z)/(1−z) est le nouveau complexe lorsque z≠1.',
     'k numérote les racines de l’unité wₖ=e^(ikπ/n). Leur image αₖ=i tan(kπ/(2n)) est une racine de Pₙ.',
     'Re et Im désignent les parties réelle et imaginaire. Toutes les quantités sont sans unité.'],
    ['k=n est exclu : wₙ=−1 n’a pas d’image finie.', 'Le produit de tangentes omet aussi k=0, dont le terme est nul.'],
    ['Racines de l’unité','Développement binomial','Factorisation dans ℂ[Z]','Relations entre coefficients et racines'],
    'Sup : complexes, racines de l’unité et formule du binôme.', 'Spé : exploiter une factorisation et comparer les coefficients.',
    'Transformation de Cayley et point à l’infini; les calculs utilisés restent élémentaires.',
    ['Choisir n=2 et écrire P₂ à la main.', 'Retrouver les trois racines 0, i et −i.', 'Passer à n=5 et prévoir la somme puis le produit des tangentes non nulles.'],
    'Le degré est 2n−1, le coefficient dominant 4n; le changement de variable ne fournit que 2n−1 racines finies.')
lesson('cayley_tangentes','Une substitution avec un point interdit','Sup',
    '<p>On cherche les complexes z tels que ((1+z)/(1−z))²ⁿ=1, avec n entier positif et z≠1. Posons w=(1+z)/(1−z). Les candidats sont wₖ=e^(ikπ/n), pour 0≤k&lt;2n.</p><p>La résolution de (1+z)=w(1−z) donne z=(w−1)/(w+1). Le candidat w=−1 est impossible : il correspond à k=n. Pour les autres, factoriser e^(ikπ/(2n)) au numérateur et au dénominateur donne <strong>z=i tan(kπ/(2n))</strong>. Les racines sont donc sur l’axe imaginaire.</p>')
lesson('cayley_tangentes','Lire une somme et un produit dans les coefficients','Sup / Spé',
    '<p>Le polynôme Pₙ(Z)=(Z+1)²ⁿ−(Z−1)²ⁿ est impair. Le binôme donne Pₙ=2Σⱼ impair binom(2n,j)Z^(2n−j). Son degré est 2n−1 et son coefficient dominant 4n.</p><p>Sa factorisation est Pₙ=4n∏ₖ≠n(Z−i tan(kπ/(2n))), pour 0≤k&lt;2n. Le coefficient de Z^(2n−2) est nul : la somme des tangentes vaut 0. Le coefficient de Z vaut 4n : le produit des racines non nulles vaut 1. Comme i^(2n−2)=(−1)^(n−1), <strong>∏ₖ₌₁,ₖ≠ₙ²ⁿ⁻¹ tan(kπ/(2n))=(−1)^(n−1)</strong>.</p>')
exercise('cayley_tangentes','Le premier cas non trivial','Sup',
    'Développer P₂(Z)=(Z+1)⁴−(Z−1)⁴ puis le factoriser dans ℂ[Z].',
    'P₂=8Z³+8Z=8Z(Z−i)(Z+i). Les trois racines sont 0, i et −i. Le quatrième candidat de la transformation, w=−1, n’a pas d’image finie.')
exercise('cayley_tangentes','Une somme sans calcul trigonométrique','Sup',
    'Pour n=5, calculer Σₖ₌₀,ₖ≠₅⁹ tan(kπ/10), puis le produit des huit termes non nuls.',
    'La somme vaut 0, par Viète ou par appariement des indices k et 10−k. Le produit vaut (−1)⁴=1. On doit omettre k=5 dans les deux expressions et k=0 dans le produit.')
exercise('cayley_tangentes','Le degré explique le candidat perdu','Spé',
    'Pourquoi une équation faisant intervenir une puissance 2n ne donne-t-elle que 2n−1 solutions finies ici ?',
    'Après suppression du dénominateur, (Z+1)²ⁿ−(Z−1)²ⁿ=0 : les termes Z²ⁿ s’annulent. Le coefficient suivant est 4n≠0, donc le degré est 2n−1. Le candidat w=−1 est précisément celui perdu lors de l’inversion z=(w−1)/(w+1).')

guide('geometrique_affine','Résoudre en une seule fois une famille de polynômes, puis transporter ses racines dans le plan.',
    ['n est le degré; c est un centre complexe, r un rayon réel strictement positif.', 'Pₙ(Z)=Σⱼ₌₀ⁿ((Z−c)/r)ʲ. On pose t=(Z−c)/r pour utiliser une somme géométrique.', 'αₖ=c+r e^(2ikπ/(n+1)), pour 1≤k≤n, sont les racines. Le point c+r n’est pas une racine.', 'Les coefficients et les racines sont sans unité.'],
    ['n≥2 dans le laboratoire; r>0.', 'Avec c=−1 et r=2, on retrouve exactement l’exercice 5 de M17.'],
    ['Somme géométrique','Affinité du plan complexe','Coefficient dominant','Viète'],
    'Sup : sommes géométriques, racines de l’unité et polynômes complexes.', 'Spé : factorisation d’une famille et contrôle des constantes.', 'Transport des racines; coefficients non réels lorsque Im(c)≠0.',
    ['Garder c=−1, r=2 et n=3; prévoir les quatre candidats.', 'Identifier le candidat exclu grâce à Pₙ(c+r)=n+1.', 'Donner une partie imaginaire à c : suivre le cercle et les racines.'],
    'Les n racines sont simples et situées sur un cercle; la factorisation comporte le facteur dominant r^(−n).')
lesson('geometrique_affine','La somme géométrique fournit les racines','Sup',
    '<p>Soient c∈ℂ, r&gt;0 et n entier positif. Posons t=(Z−c)/r et Pₙ(Z)=1+t+⋯+tⁿ. L’identité (1−t)Pₙ=1−t^(n+1) montre que les racines correspondent aux racines (n+1)-ièmes de l’unité autres que 1.</p><p>Au point t=1, Pₙ=n+1, donc ce point est bien exclu. Ainsi <strong>αₖ=c+r e^(2ikπ/(n+1)), 1≤k≤n</strong>. Chacune est simple : les racines de T^(n+1)−1 sont simples et l’une seulement a été retirée.</p>')
lesson('geometrique_affine','Le cercle ne détermine pas le coefficient dominant','Sup / Spé',
    '<p>Le terme de plus haut degré de Pₙ=Σⱼ₌₀ⁿ((Z−c)/r)ʲ est r^(−n)Zⁿ. On a donc Pₙ(Z)=r^(−n)∏ₖ₌₁ⁿ(Z−αₖ). Oublier r^(−n) conserve les racines, mais change le polynôme.</p><p>Dans le cas c=−1, r=2, Pₙ(0)=2−2^(−n), Pₙ(1)=n+1 et Pₙ(3)=2^(n+1)−1. Viète donne <strong>∏αₖ=(−1)ⁿ(2^(n+1)−1)</strong>. L’évaluation au point 0 contrôle donc le produit des racines.</p>')
exercise('geometrique_affine','Un facteur indispensable','Sup',
    'Pour P₃(Z)=Σⱼ₌₀³((Z+1)/2)ʲ, donner P₃(1), son coefficient dominant et le produit de ses racines.',
    'P₃(1)=4. Le coefficient dominant est 1/8. Le produit vaut (−1)³×8×P₃(0)=−8×15/8=−15. La factorisation sans 1/8 ne serait pas celle de P₃.')
exercise('geometrique_affine','Des coefficients vraiment complexes','Sup',
    'Pour n=2, c=i et r=1, développer P₂(Z)=1+(Z−i)+(Z−i)² et situer ses racines.',
    'P₂(Z)=Z²+(1−2i)Z−i. Ses coefficients ne sont pas réels. Les racines sont i+e^(2iπ/3) et i+e^(4iπ/3), sur le cercle de centre i et de rayon 1.')
exercise('geometrique_affine','Simplicité des racines','Spé',
    'Justifier que Pₙ(Z)=Σⱼ₌₀ⁿ((Z−c)/r)ʲ possède exactement n racines simples lorsque r>0.',
    'Dans la variable T=(Z−c)/r, (1−T)Pₙ=1−T^(n+1). Les n+1 racines de T^(n+1)−1 sont distinctes car sa dérivée (n+1)Tⁿ ne s’annule sur aucune d’elles. T=1 est supprimé; l’affinité Z=c+rT, de pente non nulle, conserve les n autres racines et leurs multiplicités.')

guide('racines_coefficients','Encadrer les racines d’un polynôme complexe de degré 6 par des inégalités prouvées.',
    ['P(Z)=Z⁶+aZ⁴+(1+i)Z²+bZ+(0,5−0,8i). Les réglages donnent les parties réelles et imaginaires de a et b.', 'Dans P=Σₖ₌₀⁶aₖZᵏ, a₆=1. α₁,…,α₆ sont les racines comptées avec multiplicité.', 'ρ est l’unique racine positive de Q(r)=r⁶−Σₖ₌₀⁵|aₖ|rᵏ. M=max|αₖ| est le plus grand module.', 'Le résidu d’une racine approchée α est |P(α)|; ce n’est pas automatiquement son erreur de position.'],
    ['Les termes complexes fixes empêchent d’imposer un polynôme réel.', 'Le terme constant est non nul : Q(r)/r⁶ part de −∞ lorsque r tend vers 0.'],
    ['Inégalité triangulaire','Étude d’une fonction réelle','Relations de Viète','Calcul approché et résidu'],
    'Sup : modules, factorisation sur ℂ et étude de fonctions.', 'Spé : bornes sur une famille de racines; exercice 9 de M17.', 'Localisation plus fine et conditionnement des racines.',
    ['Lire les six racines et le disque de rayon ρ.', 'Faire varier Im(a) : observer l’absence de symétrie obligatoire.', 'Comparer M au petit rayon (2^(1/6)−1)ρ : seule la plus éloignée est concernée.'],
    'La borne supérieure vaut pour chaque racine; la borne inférieure vaut pour le maximum de leurs modules.')
lesson('racines_coefficients','Une équation réelle localise les racines complexes','Sup / Spé',
    '<p>Soit P(Z)=aₙZⁿ+⋯+a₀, avec aₙ≠0 et a₀≠0. Posons Q(r)=rⁿ−Σₖ₌₀ⁿ⁻¹|aₖ/aₙ|rᵏ pour r&gt;0. La fonction h(r)=Q(r)/rⁿ=1−Σ|aₖ/aₙ|/r^(n−k) est strictement croissante, tend vers −∞ en 0 et vers 1 à l’infini.</p><p>Elle possède un unique zéro ρ&gt;0. Si P(α)=0, l’inégalité triangulaire donne |α|ⁿ≤Σ|aₖ/aₙ||α|ᵏ, donc h(|α|)≤0 lorsque α≠0. Ainsi <strong>|α|≤ρ</strong>. Une racine nulle vérifie aussi cette borne.</p>')
lesson('racines_coefficients','Une borne inférieure du plus grand module','Spé',
    '<p>On note α₁,…,αₙ les racines comptées avec multiplicité et M=max|αₖ|. Les relations de Viète donnent |aₖ/aₙ|≤binom(n,k)M^(n−k).</p><p>Comme Q(ρ)=0, on obtient ρⁿ≤Σₖ₌₀ⁿ⁻¹binom(n,k)M^(n−k)ρᵏ=(ρ+M)ⁿ−ρⁿ. D’où <strong>(2^(1/n)−1)ρ≤M≤ρ</strong>. Le membre de gauche concerne M, et non chacun des |αₖ|. Les racines numériques illustrent ces inégalités; la preuve n’en dépend pas.</p>')
exercise('racines_coefficients','Une borne facilement calculable','Sup',
    'Pour P(Z)=Z⁵+(2+i)Z²−3i, prouver que toutes les racines vérifient |α|≤1+max(√5,3)=4.',
    'Poser A=max des modules des coefficients non dominants=3. Pour r>1+A=4, Σₖ₌₀⁴|aₖ|rᵏ≤A(r⁵−1)/(r−1)<r⁵. Une racine de module r serait incompatible avec l’inégalité triangulaire. Donc |α|≤4. Cette borne simple peut être moins fine que ρ.')
exercise('racines_coefficients','Vérifier une monotonie','Spé',
    'Pour P(Z)=Z⁶+aZ⁴+(1+i)Z²+bZ+(0,5−0,8i), écrire h(r)=Q(r)/r⁶ et justifier son unique zéro positif.',
    'h(r)=1−|a|/r²−√2/r⁴−|b|/r⁵−√0,89/r⁶. Sa dérivée est strictement positive, même si a=b=0. Ses limites sont −∞ en 0 et 1 à l’infini. Le théorème des valeurs intermédiaires et la stricte monotonie donnent un unique zéro.')
exercise('racines_coefficients','Une confusion de quantificateurs','Spé',
    'La borne (2^(1/n)−1)ρ≤max|αₖ| implique-t-elle que toutes les racines sont hors du petit disque ?',
    'Non : elle affirme qu’au moins une racine a un module supérieur ou égal à ce rayon. Les autres peuvent être dans le petit disque, voire à l’origine pour un autre polynôme. La borne supérieure |αₖ|≤ρ, elle, concerne chaque racine.')

guide('rouche_disque','Distinguer un comptage numérique d’un certificat valable sur un cercle entier.',
    ['P(Z)=Z⁵+aZ²+b, avec a et b complexes; R>0 est le rayon du disque ouvert |z|<R.', 'On écrit P=f+g. Le terme f=cZᵏ est choisi parmi Z⁵, aZ² et b; g regroupe les deux autres.', 'Sur |z|=R, |f|=|c|Rᵏ. La somme des modules des autres termes fournit un majorant de |g|.', 'La marge est |f| moins ce majorant. Le nombre de racines est compté avec multiplicité.'],
    ['Une marge strictement positive suffit au théorème de Rouché.', 'Une marge négative ou nulle signifie seulement que ce critère ne conclut pas.'],
    ['Modules et inégalité triangulaire','Majorant uniforme','Hypothèse stricte d’un théorème','Comptage avec multiplicité'],
    'Sup : modules, polynômes et contrôle des hypothèses.', 'Spé : réinvestir les inégalités; le théorème est fourni comme prolongement.', 'Rouché et analyse complexe; hors du socle CPGE courant.',
    ['Choisir le premier exemple : vérifier |a|>1+|b| pour R=1.', 'Passer à R=2 et prévoir un autre terme dominant.', 'Prendre R=1,6 : lire pourquoi ce critère ne donne plus de certificat.'],
    'Une inégalité analytique sur tout le bord certifie le comptage; une courbe échantillonnée ne suffit pas.')
lesson('rouche_disque','Rouché : une hypothèse stricte sur tout le bord','Au-delà accompagné',
    '<p>Soient f et g deux polynômes et R&gt;0. Le théorème de Rouché affirme que si |g(z)|&lt;|f(z)| pour tout z tel que |z|=R, alors f et f+g possèdent le même nombre de racines dans |z|&lt;R, comptées avec multiplicité.</p><p>Avec P=Z⁵+aZ²+b et f=aZ², on a |g|=|Z⁵+b|≤R⁵+|b|. La condition <strong>|a|R²&gt;R⁵+|b|</strong> est suffisante pour certifier deux racines dans le disque. L’inégalité doit être stricte et valable pour chaque point du cercle.</p>')
lesson('rouche_disque','Un critère suffisant peut ne pas conclure','Au-delà accompagné',
    '<p>Pour P=Z⁵+aZ²+b, trois comparaisons sont possibles. Si R⁵&gt;|a|R²+|b|, on certifie cinq racines. Si |a|R²&gt;R⁵+|b|, on en certifie deux. Si |b|&gt;R⁵+|a|R², on en certifie zéro.</p><p>Lorsque les trois comparaisons échouent, le théorème pourrait encore s’appliquer avec une comparaison plus fine. Le laboratoire affiche alors <strong>« le critère ne conclut pas »</strong>. Il ne transforme jamais l’échec du majorant en une preuve d’absence de racines.</p>')
exercise('rouche_disque','Deux racines sans les calculer','Au-delà accompagné',
    'Pour P(Z)=Z⁵+(−4+i)Z²+0,5+0,3i, certifier le nombre de racines dans |z|<1. Le théorème de Rouché est fourni.',
    'Choisir f=(−4+i)Z². Sur |z|=1, |f|=√17 et |P−f|≤1+√0,34. Comme √17>1+√0,34, P possède autant de racines que f : exactement deux, comptées avec multiplicité.')
exercise('rouche_disque','Agrandir le disque','Au-delà accompagné',
    'Pour le même polynôme, certifier le nombre de racines dans |z|<2.',
    'Choisir f=Z⁵ : |f|=32. Les autres termes sont majorés par 4√17+√0,34<32. Rouché donne cinq racines. Le grand disque contient donc toutes les racines du polynôme de degré 5.')
exercise('rouche_disque','Une égalité qui ne suffit pas','Au-delà accompagné',
    'La condition de comparaison avec f=Z⁵ échoue. Peut-on en déduire que P possède moins de cinq racines dans le disque ?',
    'Non. Le majorant utilisé est une condition suffisante, pas nécessaire. Son échec ne fournit aucun comptage. Il faut une autre décomposition, une inégalité plus fine ou une méthode différente; le calcul approché constitue une observation, pas ce certificat.')

guide('gauss_lucas','Prolonger l’interlacement réel des racines par une propriété géométrique du plan complexe.',
    ['α₁,…,α₅ sont cinq racines complexes données. P(Z)=∏ₖ₌₁⁵(Z−αₖ); le réglage déplace α₅.', 'β₁,…,β₄ sont les racines de P′, triées par parties réelle puis imaginaire pour les numéroter.', 'L’enveloppe convexe est le plus petit ensemble convexe contenant les αₖ; le dessin montre son polygone.', 'Lorsque P(β)≠0, les poids λₖ sont proportionnels à 1/|β−αₖ|² et leur somme vaut 1.'],
    ['Le polynôme est unitaire de degré 5; des racines peuvent se confondre.', 'Une racine commune à P et P′ est déjà dans l’enveloppe convexe.'],
    ['Dérivée d’un produit','Dérivée logarithmique P′/P','Conjugaison','Barycentre à poids positifs'],
    'Sup : dérivation des polynômes et racines multiples; convexité du plan.', 'Spé : combiner identité algébrique et preuve géométrique.', 'Théorème de Gauss–Lucas, prolongement fourni et démontré.',
    ['Observer les racines de P′ à l’intérieur du polygone.', 'Déplacer α₅ très loin puis vers l’intérieur.', 'Choisir une racine β de P′ et vérifier les cinq poids positifs de son barycentre.'],
    'Les racines de P′ restent dans l’enveloppe convexe des racines de P, même sans coefficients réels.')
lesson('gauss_lucas','L’identité qui remplace Rolle dans le plan','Au-delà accompagné',
    '<p>Écrivons P(Z)=∏ₖ₌₁ⁿ(Z−αₖ), avec les racines comptées autant de fois que leur multiplicité. Pour P(z)≠0, la dérivation du produit donne P′(z)/P(z)=Σₖ1/(z−αₖ).</p><p>Si P′(β)=0 et P(β)≠0, cette somme est nulle. Après conjugaison, Σₖ(β−αₖ)/|β−αₖ|²=0. Ainsi <strong>β=Σₖλₖαₖ</strong>, où λₖ=(1/|β−αₖ|²)/(Σⱼ1/|β−αⱼ|²). Tous les poids sont positifs et leur somme vaut 1.</p>')
lesson('gauss_lucas','L’enveloppe convexe contient les racines de la dérivée','Au-delà accompagné',
    '<p>Un barycentre à poids positifs appartient à l’enveloppe convexe des points utilisés. L’identité précédente prouve donc le théorème de Gauss–Lucas pour les racines β de P′ qui ne sont pas racines de P. Si P(β)=0, β est lui-même l’un des points αₖ : le résultat est immédiat.</p><p>Pour un polynôme réel dont toutes les racines sont réelles, l’enveloppe convexe devient l’intervalle entre les racines extrêmes. Rolle fournit alors une information plus précise d’interlacement. <strong>Gauss–Lucas localise dans le plan; il ne fournit pas un ordre entre points complexes.</strong></p>')
exercise('gauss_lucas','Un barycentre forcé','Au-delà accompagné',
    'On fournit P′/P=Σ1/(Z−αₖ). Pour une racine β de P′ telle que P(β)≠0, établir sa représentation comme barycentre à poids positifs.',
    'Conjuguer l’égalité nulle : Σ(β−αₖ)/|β−αₖ|²=0. Mettre β en facteur puis diviser par Σ1/|β−αₖ|²>0. Les coefficients obtenus sont strictement positifs et de somme 1; β appartient à l’enveloppe convexe.')
exercise('gauss_lucas','Un centre de gravité partagé','Spé',
    'P est unitaire de degré n≥2, de coefficient c₁ devant Z^(n−1). Comparer la moyenne des racines de P et celle des racines de P′.',
    'Viète donne Σαₖ=−c₁. P′ a coefficient dominant n et coefficient suivant (n−1)c₁, donc Σβⱼ=−(n−1)c₁/n. Après division par les nombres respectifs de racines n et n−1, les deux moyennes valent −c₁/n.')
exercise('gauss_lucas','La racine commune','Sup',
    'Si α est racine de multiplicité m≥2 de P, quelle est sa multiplicité dans P′ ? Pourquoi ne pose-t-elle pas de difficulté pour Gauss–Lucas ?',
    'Écrire P=(Z−α)^mQ avec Q(α)≠0. P′=(Z−α)^(m−1)[mQ+(Z−α)Q′], dont le crochet vaut mQ(α)≠0. La multiplicité est m−1. La racine α est déjà dans l’ensemble des racines de P, donc dans son enveloppe convexe.')

guide('reciproque_conjugue','Distinguer le réciproque réel du réciproque conjugué complexe et traiter correctement une racine nulle.',
    ['P(Z)=Σₖ₌₀⁵aₖZᵏ a cinq racines données et un coefficient dominant 1+0,4i.', 'Le réciproque conjugué de degré ambiant 5 est P*(Z)=Σₖ₌₀⁵conj(a₅₋ₖ)Zᵏ.', 'La racine mobile α₁=ρe^(iθ) est réglée par son module ρ et son argument θ, en degrés.', 'Une racine non nulle α est envoyée vers 1/conj(α); le cercle unité est |z|=1.'],
    ['La conjugaison est nécessaire pour des coefficients complexes.', 'Si α=0, son image réciproque n’est pas finie et P* perd un degré.'],
    ['Renversement des coefficients','Conjugaison et module','Multiplicité de zéro','Degré et involution'],
    'Sup : calcul complexe, racines et coefficients.', 'Spé : identités de polynômes et cas limites.', 'Polynômes autoinversifs et localisation sur le cercle unité.',
    ['Choisir ρ=0,7 : vérifier que le module de l’image vaut 1/ρ.', 'Choisir ρ=1 : observer une racine fixe.', 'Choisir ρ=0 : lire la perte de degré et la convention nécessaire au second retournement.'],
    'Le module s’inverse, l’argument se conserve; zéro exige un traitement séparé du degré.')
lesson('reciproque_conjugue','Conjuguer puis retourner les coefficients','Sup / Spé',
    '<p>Soit P(Z)=Σₖ₌₀ⁿaₖZᵏ de degré n. Son réciproque conjugué est P*(Z)=Σₖ₌₀ⁿconj(aₙ₋ₖ)Zᵏ. Pour z≠0, <strong>P*(z)=zⁿconj(P(1/conj(z)))</strong>.</p><p>Si α≠0 est racine, 1/conj(α) est racine de P*, avec la même multiplicité. Pour α=ρe^(iθ), l’image est ρ^(−1)e^(iθ) : le module s’inverse et l’argument reste le même. Les points du cercle unité sont fixes.</p>')
lesson('reciproque_conjugue','Une racine nulle change le degré effectif','Spé',
    '<p>Si le terme constant de P est non nul, P* garde le degré n et un second réciproque conjugué retrouve P. Si P=ZᵐQ avec Q(0)≠0, le degré effectif de P* vaut n−m : les m racines nulles n’ont pas d’image finie.</p><p>Le double retournement avec le même degré ambiant n retrouve toujours le vecteur de coefficients initial. Mais, si l’on utilise le degré effectif n−m au second retournement, on obtient Q=P/Zᵐ. <strong>Préciser le degré est indispensable pour parler d’involution en présence d’une racine nulle.</strong></p>')
exercise('reciproque_conjugue','Un calcul avec des coefficients non réels','Sup',
    'Calculer le réciproque conjugué de P(Z)=(1+i)Z³+2Z²+(1−2i)Z+3i.',
    'P*(Z)=−3iZ³+(1+2i)Z²+2Z+(1−i). Il faut inverser l’ordre des coefficients et conjuguer chacun d’eux; un simple renversement donnerait un autre polynôme.')
exercise('reciproque_conjugue','Même direction, autre module','Sup',
    'Une racine vaut α=1+i. Calculer son image réciproque conjuguée, puis comparer modules et arguments.',
    '1/conj(α)=1/(1−i)=(1+i)/2. Le module passe de √2 à 1/√2 et l’argument reste π/4. Le réciproque sans conjugaison, (1−i)/2, aurait l’argument opposé.')
exercise('reciproque_conjugue','Le zéro et le second retournement','Spé',
    'P(Z)=Z(Z−(1+i))(Z−2) est de degré 3. Quel est le degré effectif de P* ? Que donne son réciproque conjugué pris en degré effectif ?',
    'P a une racine nulle simple et ses deux autres racines sont non nulles. P* a donc degré 2. En retournant ensuite ses trois coefficients de degré 2, on obtient P/Z=(Z−(1+i))(Z−2), et non P. En gardant dès le départ quatre coefficients de degré ambiant 3, le double retournement retrouve P.')

guide('viete_newton','Calculer des sommes de puissances sans résoudre un polynôme complexe de degré 6.',
    ['P(Z)=Z⁶+aZ⁴+(1+i)Z²+bZ+(0,5−0,8i). Les réglages donnent a et b complexes.', 'On écrit aussi P=Z⁶+c₁Z⁵+⋯+c₆; c₁=0, c₂=a, c₃=0, c₄=1+i, c₅=b et c₆=0,5−0,8i.', 'α₁,…,α₆ sont les racines avec multiplicité. sₖ=Σⱼ₌₁⁶αⱼᵏ est la somme de puissances d’ordre k.', 'm choisit la somme sₘ affichée; toutes les quantités sont sans unité.'],
    ['Le polynôme est unitaire de degré 6.', 'Les identités portent sur les racines comptées avec multiplicité, pas seulement sur les racines distinctes.'],
    ['Relations de Viète','Identités de Newton','Récurrence sur les sommes','Contrôle indépendant'],
    'Sup : somme, produit et coefficients d’un polynôme scindé.', 'Spé : relations déterminant–traces et calcul de sommes de puissances.', 'Fonctions symétriques et lien avec le spectre d’un endomorphisme.',
    ['Choisir m=1 et justifier s₁=0.', 'Choisir m=4 : calculer s₄=2a²−4(1+i) avant de lire le résultat.', 'Passer à m=8 : utiliser la récurrence sans terme 8c₈.'],
    'Les coefficients déterminent les sommes; résoudre les racines n’est utile que comme vérification numérique.')
lesson('viete_newton','Les premières identités de Newton','Sup / Spé',
    '<p>Soit P(Z)=Zⁿ+c₁Z^(n−1)+⋯+cₙ, de racines α₁,…,αₙ avec multiplicité. On définit sₖ=Σαⱼᵏ. Pour 1≤k≤n, <strong>sₖ+c₁sₖ₋₁+⋯+cₖ₋₁s₁+kcₖ=0</strong>.</p><p>Les premières sont s₁=−c₁, s₂=−c₁s₁−2c₂ et s₃=−c₁s₂−c₂s₁−3c₃. Dans le laboratoire, c₁=c₃=0 : s₁=s₃=0 et s₂=−2a. Les coefficients complexes ne changent aucune de ces identités.</p>')
lesson('viete_newton','Après le degré : une récurrence et un lien aux traces','Spé',
    '<p>Pour k&gt;n, chaque racine satisfait αⱼⁿ+c₁αⱼ^(n−1)+⋯+cₙ=0. Multiplier par αⱼ^(k−n) puis sommer donne <strong>sₖ+c₁sₖ₋₁+⋯+cₙsₖ₋ₙ=0</strong>. Le terme kcₖ des premières identités disparaît : il n’existe pas de coefficient cₖ au-delà du degré.</p><p>Si A est un endomorphisme complexe dont le polynôme caractéristique est P, alors tr(Aᵏ)=sₖ et det(A)=∏αⱼ. Ces relations permettent de relier traces et coefficients caractéristiques; elles restent vraies sans supposer A diagonalisable.</p>')
exercise('viete_newton','Quatrième somme exacte','Spé',
    'Pour P(Z)=Z⁶+(1+i)Z⁴+(1+i)Z²+(−1+0,5i)Z+0,5−0,8i, calculer s₄=Σαⱼ⁴ sans déterminer les racines.',
    's₁=s₃=0 et s₂=−2(1+i). Newton au rang 4 donne s₄+(1+i)s₂+4(1+i)=0. Ainsi s₄=2(1+i)²−4(1+i)=4i−4−4i=−4.')
exercise('viete_newton','Une somme et un produit','Sup',
    'Pour le polynôme général du laboratoire, déterminer la somme et le produit des six racines, comptées avec multiplicité.',
    'Le coefficient de Z⁵ est nul, donc la somme vaut 0. Le degré 6 est pair et le polynôme unitaire : le produit vaut son terme constant, 0,5−0,8i. Aucune symétrie de conjugaison n’est nécessaire.')
exercise('viete_newton','Cinquième et septième sommes','Spé',
    'Dans la famille P=Z⁶+aZ⁴+(1+i)Z²+bZ+0,5−0,8i, calculer s₅ puis s₇.',
    'Comme s₁=s₃=0, l’identité au rang 5 donne s₅=−5b. Au rang 7, la récurrence donne s₇=−a s₅−(1+i)s₃−b s₂−c₆s₁=5ab+2ab=7ab. Les rangs 5 et 7 n’utilisent pas exactement la même forme de l’identité.')

guide('newton_bassins','Comprendre la portée locale de Newton et la dépendance au point initial dans le plan complexe.',
    ['P est un polynôme complexe de degré 4, donné par quatre racines simples α₁,…,α₄. P′ est sa dérivée.', 'z₀ est un point de départ complexe; zₖ₊₁=zₖ−P(zₖ)/P′(zₖ) lorsque le dénominateur n’est pas nul.', 'N est le nombre maximal d’itérations; le maillage comporte M points par côté dans une fenêtre carrée.', 'Une couleur signifie qu’une racine est atteinte à distance inférieure à 10⁻⁶. « Non classé » est une cinquième catégorie.', 'L’orbite choisie utilise les réglages Re(z₀), Im(z₀); le résidu est |P(zₖ)|.'],
    ['Les quatre racines du polynôme choisi sont distinctes.', 'Une dérivée trop petite ou une excursion très grande arrête le calcul; la catégorie non classée est conservée.'],
    ['Tangente et méthode de Newton','Résidu et erreur','Convergence locale','Lecture d’un calcul fini'],
    'Sup : dérivation des polynômes et suites récurrentes.', 'Spé : Newton pour un problème réel; cette carte complexe est un prolongement.', 'Bassins d’attraction et frontières en dynamique complexe.',
    ['Repérer les quatre racines et leurs couleurs.', 'Déplacer z₀ de part et d’autre d’une frontière et suivre les orbites.', 'Réduire N puis l’augmenter : comparer la catégorie non classée.'],
    'Newton converge vite près d’une racine simple, mais une fenêtre et un nombre d’itérations finis ne donnent pas un théorème global.')
lesson('newton_bassins','Pourquoi une racine simple attire localement','Spé / prolongement complexe',
    '<p>Soit α une racine simple de P : P(α)=0 et P′(α)≠0. Pour z proche de α, poser e=z−α. Le développement polynomial donne P(z)=P′(α)e+P″(α)e²/2+O(e³).</p><p>Dans la récurrence zₖ₊₁=zₖ−P(zₖ)/P′(zₖ), l’erreur satisfait <strong>eₖ₊₁=[P″(α)/(2P′(α))]eₖ²+O(eₖ³)</strong>. La convergence est donc au moins quadratique pour un point de départ suffisamment proche. Cette conclusion locale ne promet pas la convergence depuis chaque point du plan.</p>')
lesson('newton_bassins','Le dessin possède une catégorie non classée','Au-delà accompagné',
    '<p>La carte choisit un point initial par pixel et effectue au plus N itérations. Un point reçoit la couleur de αⱼ seulement si sa distance à cette racine devient inférieure à 10⁻⁶. Les autres points restent « non classés ».</p><p>Un point non classé peut converger plus lentement, partir très loin ou rencontrer P′=0. Augmenter N peut changer son classement. Le maillage donne une expérience numérique : <strong>il ne démontre ni la frontière exacte des bassins ni la convergence pour tous les points</strong>.</p>')
exercise('newton_bassins','Un point qui ne démarre pas','Sup / prolongement',
    'Pour P(Z)=(Z−c)⁴−1, avec c=0,3+0,4i, expliquer pourquoi Newton ne peut pas démarrer en z₀=c.',
    'P(c)=−1 alors que P′(c)=4(c−c)³=0. Le quotient P(c)/P′(c) n’est pas défini. Le centre ne doit donc recevoir la couleur d’aucune racine; il est classé séparément.')
exercise('newton_bassins','Un résidu et une erreur','Spé',
    'Près d’une racine simple α, pourquoi |P(z)| petit ne donne-t-il une estimation de |z−α| qu’en tenant compte de P′(α) ?',
    'P(z)=P′(α)(z−α)+O((z−α)²). Au premier ordre, |z−α|≈|P(z)|/|P′(α)|. Une petite dérivée amplifie l’erreur de position correspondant à un même résidu; l’estimation exige d’être déjà dans un voisinage convenable de la racine.')
exercise('newton_bassins','La racine multiple ralentit Newton','Spé',
    'Pour P(Z)=(Z−α)^m et m≥2, écrire exactement la récurrence de Newton et le facteur de réduction de l’erreur.',
    'Pour z≠α, P/P′=(z−α)/m. Ainsi zₖ₊₁−α=(1−1/m)(zₖ−α). Le facteur est (m−1)/m : la convergence est linéaire, contrairement au cas d’une racine simple générique.')

guide('conditionnement_racines','Voir pourquoi deux racines proches rendent leur calcul sensible, puis traiter la racine double avec une formule exacte.',
    ['c=0,2+0,3i est le centre fixe; δ≥0 est la demi-distance initiale entre c−δ et c+δ.', 'Q(Z) est le produit des trois facteurs correspondant aux racines fixes −2+0,4i, 1,7+1,3i et 1−1,9i.', 'Pδ(Z)=[(Z−c)²−δ²]Q(Z). Sa perturbation est Pδ,η=[(Z−c)²−δ²−η]Q(Z).', 'η=εe^(iφ), où ε=10ᵉ>0 et φ est l’argument réglé en degrés. La formule exacte des racines mobiles est c±√(δ²+η).'],
    ['La perturbation vaut −ηQ(Z), et non une constante ajoutée au polynôme de degré 5.', 'L’approximation linéaire exige δ>0 et ε≪δ².'],
    ['Racines et multiplicité','Développement limité','Perturbation complexe','Comparaison formule exacte / calcul approché'],
    'Sup : racines d’une équation quadratique complexe et multiplicité.', 'Spé : développements limités et comparaison d’échelles.', 'Conditionnement numérique des racines et coalescence.',
    ['Commencer avec δ=0,4 et ε=10⁻⁶; comparer au premier ordre ε/(2δ).', 'Diminuer δ jusqu’à √ε : repérer la perte de validité du premier ordre.', 'Fixer δ=0 : vérifier un déplacement √ε, quel que soit l’argument φ.'],
    'Deux racines simples bien séparées réagissent linéairement; une racine double peut se séparer à l’échelle √ε.')
lesson('conditionnement_racines','L’échelle qui contrôle le premier ordre','Spé',
    '<p>Soient c∈ℂ, δ&gt;0 et η une petite perturbation complexe. Les racines de (Z−c)²−δ²−η sont c±√(δ²+η). Lorsque |η|≪δ², choisir la branche proche de δ donne √(δ²+η)=δ+η/(2δ)+O(|η|²/δ³).</p><p>Le déplacement de chaque racine a donc pour module environ |η|/(2δ). Le coefficient 1/(2δ) augmente lorsque les racines se rapprochent. <strong>La petite quantité pertinente est |η|/δ²</strong>, et non seulement |η|.</p>')
lesson('conditionnement_racines','Une racine double ne répond plus linéairement','Spé / prolongement numérique',
    '<p>Si δ=0, le facteur devient (Z−c)²−η. Ses racines sont c±√η, à distance exactement √|η| de c. Une perturbation de taille 10⁻⁸ provoque donc un déplacement de taille 10⁻⁴.</p><p>Le laboratoire multiplie ce facteur par un polynôme Q de degré 3 à racines fixes : l’ensemble reste un exemple de degré 5 à coefficients complexes. La formule quadratique donne une référence exacte pour mesurer l’erreur du calcul flottant. <strong>Un résidu petit ne suffit pas à certifier une position très précise près d’une racine multiple.</strong></p>')
exercise('conditionnement_racines','Vérifier l’hypothèse avant d’approximer','Spé',
    'δ=0,2 et ε=10⁻⁶. Estimer le déplacement des racines mobiles et vérifier la condition du premier ordre.',
    'ε/δ²=10⁻⁶/0,04=2,5×10⁻⁵≪1. Le déplacement a pour module ε/(2δ)=2,5×10⁻⁶. La correction suivante est d’ordre ε²/δ³; le développement est adapté à cette échelle.')
exercise('conditionnement_racines','Double racine et perturbation imaginaire','Sup / Spé',
    'Pour δ=0 et η=i×10⁻⁸, écrire les deux racines mobiles autour de c=0,2+0,3i.',
    '√η=10⁻⁴e^(iπ/4)=10⁻⁴(1+i)/√2. Les racines sont c±10⁻⁴(1+i)/√2, chacune à distance 10⁻⁴ du centre. Le choix de l’autre racine carrée échange simplement les deux racines.')
exercise('conditionnement_racines','Ce que le polynôme perturbé change','Spé',
    'Comparer Pδ,η=[(Z−c)²−δ²−η]Q à Pδ. Les trois racines de Q sont-elles déplacées ?',
    'Pδ,η−Pδ=−ηQ. Les trois racines de Q restent exactement racines du polynôme perturbé. Seule la paire du facteur quadratique se déplace. Cela permet une étude contrôlée, mais ce n’est pas la même expérience qu’ajouter une constante au polynôme de degré 5.')

guide('recurrence_complexe','Résoudre une récurrence de polynômes avec ses véritables données initiales, y compris lorsque les racines caractéristiques se confondent.',
    ['n est un rang entier et λ=e^(iθ) un complexe de module 1; θ se règle en degrés.', 'P₀(Z)=1, P₁(Z)=2λZ, Pₖ₊₂(Z)+λZPₖ₊₁(Z)+Pₖ(Z)=0. λ=1 retrouve l’exercice 6 de M17.', 'z est le point complexe d’évaluation; t=λz. Les racines caractéristiques r₊, r₋ vérifient r²+tr+1=0.', 'Pour les racines distinctes, A et B sont les constantes donnant Pₙ(z)=Ar₊ⁿ+Br₋ⁿ. Elles sont fixées par P₀ et P₁.'],
    ['Les racines caractéristiques peuvent être complexes ou doubles, aux valeurs t=±2.', 'La récurrence est utilisée directement dans le calcul, même lorsqu’une formule fermée est affichée.'],
    ['Récurrence linéaire d’ordre 2','Équation caractéristique','Données initiales','Racine double et changement de variable'],
    'Sup : suites récurrentes et polynômes; le cas complexe prolonge le calcul réel.', 'Spé : représentation d’une famille et identité polynomiale.', 'Stabilité du calcul près de racines caractéristiques confondues.',
    ['Choisir λ=1 et calculer P₂=−2Z²−1 à la main.', 'Fixer z=2 : vérifier la formule avec une racine caractéristique double.', 'Changer θ : observer la rotation des racines et les coefficients non réels.'],
    'L’équation caractéristique ne suffit pas : les deux valeurs initiales déterminent la famille et la forme du cas double.')
lesson('recurrence_complexe','Résoudre à un point complexe fixé','Sup / Spé',
    '<p>La famille est P₀=1, P₁=2λZ, Pₖ₊₂+λZPₖ₊₁+Pₖ=0. Au point z, posons t=λz et uₖ=Pₖ(z). La suite satisfait uₖ₊₂+tuₖ₊₁+uₖ=0, avec u₀=1 et u₁=2t.</p><p>Si r₊ et r₋ sont distincts, racines de r²+tr+1=0, on obtient <strong>uₙ=Ar₊ⁿ+Br₋ⁿ</strong>, avec A=(2t−r₋)/(r₊−r₋), B=1−A. Les racines caractéristiques ne sont pas les racines du polynôme Pₙ : elles dépendent du point d’évaluation z.</p>')
lesson('recurrence_complexe','Le cas double et les coefficients complexes','Sup / Spé',
    '<p>Lorsque t=±2, l’équation caractéristique a une racine double r=−t/2. La forme générale est uₙ=(A+Bn)rⁿ. Les conditions u₀=1 et u₁=2t donnent A=1 et B=−5 : <strong>uₙ=(1−5n)rⁿ</strong>.</p><p>Si Pₙ,₁ désigne la famille source avec λ=1, la récurrence montre Pₙ,λ(Z)=Pₙ,₁(λZ). Les racines tournent donc de l’angle −arg(λ). Dès que λ n’est pas réel, les coefficients peuvent devenir non réels. Cette famille n’est pas celle des Tchebychev usuels : ses données initiales et son signe de récurrence sont différents.</p>')
exercise('recurrence_complexe','L’initialisation compte','Sup',
    'Avec λ=1, calculer P₂ et P₃, à partir de P₀=1, P₁=2Z et Pₖ₊₂=−ZPₖ₊₁−Pₖ.',
    'P₂=−Z(2Z)−1=−2Z²−1. P₃=−Z(−2Z²−1)−2Z=2Z³−Z. Leurs degrés sont 2 et 3; ils ne sont pas les Tchebychev de première ou de deuxième espèce avec leur initialisation habituelle.')
exercise('recurrence_complexe','Une racine caractéristique double','Sup / Spé',
    'Avec λ=1 et z=2, calculer P₈(2) sans développer P₈.',
    't=2, donc r²+2r+1=(r+1)². La forme est (A+Bn)(−1)ⁿ. P₀=1 impose A=1 et P₁(2)=4 impose −(1+B)=4, soit B=−5. P₈(2)=(1−40)(−1)⁸=−39.')
exercise('recurrence_complexe','Transporter les racines','Spé',
    'Montrer Pₙ,λ(Z)=Pₙ,₁(λZ), puis en déduire les racines de P₂,λ pour λ=e^(iπ/4).',
    'Les deux familles ont les mêmes valeurs initiales après substitution Z↦λZ et satisfont la même récurrence : l’égalité suit par récurrence. P₂,λ=−2λ²Z²−1=−2iZ²−1. Les racines de P₂,₁ sont ±i/√2; celles de P₂,λ sont donc ±e^(iπ/4)/√2.')
