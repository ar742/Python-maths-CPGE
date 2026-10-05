# Physique statistique — cours et exercices

Volet 06 de Python-maths-CPGE. Huit laboratoires pour relier les états microscopiques, les probabilités et les équilibres thermiques.

Les résultats théoriques et les observations numériques sont distingués. Les approfondissements sont signalés.

## 1 · Microétats, entropie et équilibre

*SUP → SPÉ · FONDATIONS*

Un microétat précise les variables microscopiques nécessaires pour décrire le système ; un macroétat fixe des grandeurs comme E, V et N. Nous notons N le nombre de particules, n=N/V la densité volumique et n_mol une quantité en moles. En microcanonique, le système isolé à l’équilibre est décrit par des microétats accessibles équiprobables ; le choix d’une fenêtre d’énergie doit être spécifié.

pᵢ=1/Ω ; S=kB lnΩ.
Plus généralement : S=−kBΣᵢpᵢln pᵢ.
dS=dE/T+P dV/T−μ dN/T.

Pour deux préparations indépendantes, les probabilités se multiplient. Remplacer ln(pᵢqⱼ) par ln pᵢ+ln qⱼ dans l’entropie donne S_total=S_A+S_B. La factorisation peut échouer en présence de corrélations ou d’interactions ; une simple séparation géométrique ne suffit pas à la démontrer. L’extensivité décrit la dépendance macroscopique en taille, sous les hypothèses de limite thermodynamique appropriées.

Deux compartiments isolés ensemble :
dS_total=(1/T₁−1/T₂)dE₁+(P₁/T₁−P₂/T₂)dV₁−(μ₁/T₁−μ₂/T₂)dN₁.

Chaque transfert conservé vérifie dE₂=−dE₁, et de même pour V et N. Si T₁>T₂, le coefficient de dE₁ est négatif : une augmentation d’entropie exige que le compartiment chaud perde de l’énergie, dE₁<0. À températures égales, le compartiment de pression supérieure tend à augmenter son volume. Le signe de la dérivée en N est −μ/T ; il ne faut pas inverser le sens physique des transferts.

## 2 · Thermostat, Boltzmann et dégénérescence

*SUP → SPÉ · MÉTHODE*

Un système fermé peut échanger de l’énergie avec un thermostat de température T. Pour un grand réservoir, développer son entropie autour de l’énergie totale donne S_R(E_total−Eᵢ)≈constante−Eᵢ/T. Le nombre de ses microétats est proportionnel à exp(S_R/kB), ce qui produit le poids de Boltzmann du système.

β=1/(kBT) ; pᵢ=exp(−βEᵢ)/Z ; Z=Σ_microétats exp(−βEᵢ).
Niveau j de dégénérescence gⱼ : Pⱼ=gⱼexp(−βEⱼ)/Z.
Z=Σ_niveaux gⱼexp(−βEⱼ) ; S=−kBΣⱼPⱼln(Pⱼ/gⱼ).

pᵢ est la probabilité d’un microétat ; Pⱼ est celle d’un niveau entier. Une dégénérescence n’est pas le nombre de particules occupant le niveau. À haute température, les microétats deviennent équiprobables, mais les niveaux n’ont pas les mêmes populations si leurs dégénérescences diffèrent.

Le mode « trois » du laboratoire choisit les niveaux 0, ε, 2ε et les dégénérescences 1,g,1. Alors Z=1+gexp(−βε)+exp(−2βε). À β→0, les populations des niveaux tendent vers (1,g,1)/(g+2), U→ε et S→kBln(g+2). Calculer seulement −ΣPⱼlnPⱼ oublierait l’entropie interne des niveaux dégénérés. Une énergie ajoutée à tous les niveaux ne change pas les probabilités : elle multiplie Z par le même facteur.

## 3 · Dériver une partition et comprendre Schottky

*SPÉ · EXERCICE 2 PRIORITAIRE*

U=−∂β lnZ ; Var(E)=∂β²lnZ ; C_V=Var(E)/(kBT²)≥0.
S=kB(lnZ+βU) ; F=−kBTlnZ ; P=−(∂V F)_{T,N}.

**Preuve.** Dériver la somme de Z donne Z′=−ΣEᵢexp(−βEᵢ), donc U=−Z′/Z. Une seconde dérivée de lnZ donne ⟨E²⟩−⟨E⟩². Enfin dβ/dT=−1/(kBT²) produit la capacité. Les niveaux sont ici indépendants de T ; les paramètres tenus fixes doivent être déclarés.

N systèmes indépendants, deux niveaux 0 et Δ :
p_exc=1/(1+exp(βΔ)) ; U=NΔp_exc.
C/(NkB)=(βΔ)²/[4cosh²(βΔ/2)].

Le facteur 1/4 est indispensable. À basse température, l’excitation est gelée ; à haute température, les populations saturent à 1/2 et leur énergie cesse de varier : C tend vers 0 aux deux extrêmes. Le pic intermédiaire est un effet Schottky, pas une transition de phase. Dans le laboratoire des spins, la séparation est Δ=2μ|B|.

**Microcanonique.** Pour N sites distinguables avec r sites excités, Ω=C(N,r). Stirling donne S≈NkB[−p ln p−(1−p)ln(1−p)], p=r/N, lorsque les populations sont grandes. Avec E=rΔ, ∂S/∂E=1/T donne p=1/(1+exp(βΔ)), en accord avec le canonique. Pour des sites ou spins fixés, Z=zᴺ ; le facteur 1/N! appartient au gaz classique de particules identiques, pas à ce modèle de sites.

## 4 · Équipartition et oscillateur quantique

*SUP → SPÉ · EXERCICE 3*

Dans une intégrale classique, un terme indépendant ay² du Hamiltonien produit ∫exp(−βay²)dy∝β⁻¹ᐟ². Sa contribution à −∂βlnZ est donc kBT/2. Il faut compter les variables quadratiques indépendantes réellement autorisées : des contraintes peuvent supprimer des degrés de liberté.

Gaz monoatomique : trois termes pⱼ²/(2m) ⇒ U/N=3kBT/2.
Oscillateur 1D : p²/(2m)+mω²x²/2 ⇒ U=kBT en classique.
Oscillateur 3D : six termes ⇒ U=3kBT.

Un potentiel rappelant seulement selon x mais laissant libres y,z contient trois termes cinétiques et un terme de potentiel : U=2kBT. Ce système n’est pas un oscillateur 1D. Le nom du modèle ne remplace pas le comptage des variables. L’équipartition classique suppose des intégrales bien définies et des espacements quantiques négligeables devant kBT.

Oscillateur quantique, Eₙ=hν(n+1/2), x=hν/(kBT) :
Z=exp(−x/2)/(1−exp(−x)) ; ⟨n⟩=1/(exp x−1).
U=hν(1/2+⟨n⟩) ; C/kB=x²exp(−x)/(1−exp(−x))².

La somme géométrique est exacte. À T→0, U→hν/2 mais C→0 : le point zéro ne stocke pas d’énergie thermique variable. À haute température, U≈kBT et C→kB. La fenêtre graphique de n=0 à 24 n’est pas renormalisée ; sa masse restante vaut exp(−25x). Pour 3N oscillateurs de même fréquence, multiplier les grandeurs par 3N donne le modèle d’Einstein, qui ne représente pas les modes acoustiques d’un solide réel.

**Extension de l’exercice 6 : rotation de H₂.** Un rotor rigide a E_ℓ=bℓ(ℓ+1), b=ℏ²/(2I), et une dégénérescence spatiale 2ℓ+1. Pour deux protons identiques de spin 1/2 dans l’état électronique fondamental symétrique, l’antisymétrie totale impose un singulet nucléaire antisymétrique avec ℓ pair (para), ou un triplet symétrique avec ℓ impair (ortho). À équilibre de conversion, N_ortho/N_para=3z_impair/z_pair ; ce rapport tend vers 3 à chaud et vers 9exp(−2βb) à froid. Ces restrictions ne s’appliquent pas telles quelles à une molécule hétéroatomique A–B. Sans conversion ortho–para assez rapide, le rapport peut rester hors de l’équilibre.

## 5 · Gaz dans une boîte et densité d’états

*SPÉ · LIEN AVEC LE VOLET PQ*

Le TP quantique fournit E=E_L(nₓ²+nᵧ²+n_z²), E_L=π²ℏ²/(2mL²), nⱼ≥1 pour des parois infinies. Le canonique d’une seule particule factorise : Z₁=[Σ_{n≥1}exp(−βE_Ln²)]³. La somme du laboratoire est tronquée dans chaque direction ; comparer N_max et 2N_max contrôle un écart mesuré, sans fournir à lui seul une borne sur la queue infinie.

Comptage continu 3D, dégénérescence interne g_s :
G(E)=g_s V(2m/ℏ²)³ᐟ²E³ᐟ²/(6π²).
D(E)=dG/dE=g_s V(2m/ℏ²)³ᐟ²√E/(4π²).
λ_th=h/√(2πmkBT) ; Z₁≈g_s V/λ_th³.

G compte les états jusqu’à E ; D est une densité d’états, d’unité énergie⁻¹. En conditions périodiques, un état occupe (2π/L)³ dans l’espace des vecteurs d’onde. Le volume d’une sphère de rayon √(2mE)/ℏ donne G. Les parois ont le même terme dominant à grand volume, avec des corrections de bord.

Gaz classique identique, dilué : Z_N≈(V/λ_th³)ᴺ/N! pour g_s=1.
U=3NkBT/2 ; C_V=3NkB/2 ; PV=NkBT.

Deux critères sont distincts : kBT≫E_L rend le spectre quasi continu ; nλ_th³/g_s≪1 rend les effets d’échange négligeables. Un gaz parfait peut être quantique : « sans interaction » ne veut pas dire « classique ». La distance moyenne très supérieure à λ_th correspond justement au régime classique, contrairement au libellé du recueil. La somme d’une particule du laboratoire ne constitue pas un calcul exact de N bosons ou fermions. Dans cette boîte, la dilatation isotrope donne P=2U/(3V) ; PV=kBT est sa limite classique par particule.

## 6 · Maxwell : vitesses et pression cinétique

*SUP → SPÉ · TP PRIORITAIRE*

Un gaz classique dilué à l’équilibre a des composantes de vitesse gaussiennes indépendantes. Le passage du vecteur vitesse à son module introduit le jacobien sphérique 4πv² ; la vitesse la plus probable du module n’est donc pas la moyenne d’une composante.

f(v⃗)=(m/(2πkBT))³ᐟ²exp(−mv²/(2kBT)).
f_v(v)=4πv²f(v⃗), v≥0 ; ∫f_v(v)dv=1.
v_mp=√(2kBT/m) ; ⟨v⟩=√(8kBT/(πm)) ; v_rms=√(3kBT/m).

Ces trois vitesses sont dans cet ordre croissant. ⟨vₓ⟩=0, mais ⟨v⟩>0. Isotropie donne ⟨vₓ²⟩=⟨v²⟩/3=kBT/m. Dériver le logarithme de v²exp(−mv²/(2kBT)) donne v_mp ; les autres résultats viennent des intégrales de Gauss.

Flux vers une paroi : n v_z f(v⃗)d³v, v_z>0.
Impulsion d’une réflexion élastique : 2mv_z.
P=2mn∫_{v_z>0}v_z²f(v⃗)d³v=mn⟨v_z²⟩=nkBT.

Le premier facteur v_z compte les particules atteignant la paroi ; le second intervient dans leur impulsion. Les particules incidentes sont limitées au demi-espace v_z>0 : intégrer les mêmes chocs sur toute la sphère ferait perdre le facteur correct. La pression est une densité de flux de quantité de mouvement. Les collisions élastiques peuvent établir l’équilibre ; les négliger dans l’énergie d’un gaz idéal ne signifie pas interdire toute collision.

## 7 · Effusion : sélectionner les particules rapides

*SUP → SPÉ · TP PRIORITAIRE*

Choisir le mode « effusion » du laboratoire Maxwell. L’effusion traverse un orifice petit devant le libre parcours moyen ; les particules passent sans collisions dans le trou. Pour une grande ouverture, un écoulement hydrodynamique exige un autre modèle. L’extérieur est ici assimilé au vide et le gaz intérieur reste suffisamment bien mélangé.

Flux de particules par unité de surface :
Φ_N=n∫_{v_z>0}v_zf(v⃗)d³v=n√(kBT/(2πm))=n⟨v⟩/4.
À T et V constants : Ṅ=−(S/V)√(kBT/(2πm))N ; N(t)=N₀exp(−t/τ).
τ=(V/S)√(2πm/(kBT)).

Le facteur 1/4 combine une distribution isotrope et la projection de la vitesse sur la normale. Doubler la surface divise τ par deux ; à mêmes T et géométrie, τ∝√m. C’est le principe d’une séparation par effusion, avec toutes les réserves d’un modèle idéal.

Distribution des vitesses sortantes : f_eff(v)=v f_v(v)/⟨v⟩.
Énergie cinétique moyenne sortante : ⟨mv²/2⟩_eff=2kBT.

Les particules rapides atteignent plus souvent le trou : la sélection porte une énergie moyenne 2kBT, supérieure aux 3kBT/2 de l’intérieur. L’exponentielle de N suppose un thermostat. Sans thermostat, la fuite peut refroidir le gaz : avec U=3NkBT/2 et une énergie perdue 2kBT par particule, dU=2kBTdN donne T/T₀=(N/N₀)¹ᐟ³. C’est une extension du modèle, pas la même hypothèse d’évolution isotherme.

## 8 · Paroi poreuse et transpiration thermique

*SPÉ · TP PRIORITAIRE*

Choisir le mode « paroi » du laboratoire Maxwell. Deux enceintes communiquent par de petits orifices en régime d’effusion. Chaque compartiment est maintenu à sa propre température Tᵢ et reste décrit par Maxwell. La conservation Ṅ₁=−Ṅ₂ vaut à tout instant ; elle n’impose pas l’égalité des flux dans les deux sens. Celle-ci apparaît seulement dans l’état stationnaire des populations.

kᵢ=(S/Vᵢ)√(kBTᵢ/(2πm)).
Ṅ₁=−k₁N₁+k₂N₂ ; N₁+N₂=N_total.
N₁,st=N_total k₂/(k₁+k₂).
N₁(t)=N₁,st+[N₁(0)−N₁,st]exp[−(k₁+k₂)t].

Cette équation linéaire donne un temps de relaxation 1/(k₁+k₂). À l’état stationnaire, N₁√T₁/V₁=N₂√T₂/V₂. Remplacer nᵢ par Pᵢ/(kBTᵢ) montre la relation de transpiration thermique.

P₁/√T₁=P₂/√T₂ ; donc P₁/P₂=√(T₁/T₂).

Si T₁≠T₂, les pressions stationnaires ne sont pas égales. Ce n’est pas un équilibre thermique global : les thermostats maintiennent une différence de température. Même lorsque les flux de particules s’équilibrent, les particules venues du compartiment chaud transportent en moyenne plus d’énergie. Pour un même flux de particules dans chaque sens, le transfert énergétique net est dirigé du chaud vers le froid, avec 2kB(T₁−T₂) par paire de transferts opposés.

## 9 · Occupations quantiques et réservoir de particules

*SPÉ · TP FD/BE*

Grand canonique : Ξ=Σ exp[−β(E−μN)] ; J=−kBTlnΞ.
⟨N⟩=−(∂μJ)_{T,V} ; S=−(∂TJ)_{μ,V}.
Occupation d’un état d’énergie ε :
n_F=1/(exp[β(ε−μ)]+1) ; n_B=1/(exp[β(ε−μ)]−1).
Limite diluée : n_MB≈exp[−β(ε−μ)].

Pour un fermion dans un état complet, spin compris, les occupations permises sont 0 et 1. Sa partition est 1+z, z=exp[−β(ε−μ)] : la moyenne est z/(1+z). Pour un boson, les occupations sont 0,1,2,… ; sommer 1+z+z²+… donne 1/(1−z), pour z<1, puis la moyenne z/(1−z). Il faut μ<ε_min pour une description grand canonique non condensée.

Un mode indépendant en grand canonique :
Var(n)_FD=n_F(1−n_F) ; Var(n)_BE=n_B(1+n_B).
Régime MB dilué : Var(n)≈n_MB.

FD suit une Bernoulli ; BE suit une géométrique ; l’approximation MB donne une loi de Poisson. Les fluctuations d’un mode fermionique sont réduites par Pauli, celles d’un mode bosonique augmentées. Ces courbes sont des occupations par état, pas des densités de probabilité normalisées sur l’énergie : le nombre total demande une somme avec les dégénérescences ou une intégrale avec D(E).

Le mode « comparaison » compare les trois lois au même μ : c’est une expérience de réservoir. Dans les modes « Fermi » et « Bose » à N fixé, il faut déterminer μ(T,N,V) pour satisfaire la contrainte de nombre ; le μ de FD peut être positif. En continu, ∫D(E)n(E)dE calcule N, pas une partition canonique Z. Les photons thermiques ont μ=0 car leur nombre n’est pas conservé par les parois.

## 10 · Fermi : remplir une sphère d’états

*SPÉ · TP PRIORITAIRE*

Considérons un gaz homogène idéal de fermions non relativistes, dans un grand volume, avec dégénérescence de spin 2. À T=0, tous les états sous E_F sont occupés et ceux au-dessus vides : une sphère de rayon k_F est remplie dans l’espace k. Le niveau de Fermi reste non nul même à température nulle.

n=2×[4πk_F³/3]/(2π)³=k_F³/(3π²).
k_F=(3π²n)¹ᐟ³ ; E_F=ℏ²k_F²/(2m) ; T_F=E_F/kB.
U/N=3E_F/5 ; P=2nE_F/5, à T=0.

**Énergie.** La densité d’états est proportionnelle à √E. Donc N=A∫₀^{E_F}√E dE et U=A∫₀^{E_F}E³ᐟ²dE ; leur rapport vaut 3E_F/5. La pression suit P=2U/(3V) pour cette dispersion quadratique. Cette pression de dégénérescence ne dépend pas d’un mouvement thermique classique et ne contredit pas l’idéalité du gaz.

À T>0 et N fixé : n=∫₀∞[D(E)/V]n_F(E,μ,T)dE.
Pour T≪T_F, μ≈E_F[1−(π²/12)(T/T_F)²].
C_V/(NkB)≈(π²/2)(T/T_F).

L’intégrale de nombre détermine μ ; poser μ=E_F à toute température serait une approximation incontrôlée. Le développement de Sommerfeld est une extension valable à faible T/T_F. À haute température, la solution tend vers μ≈kBTln(nλ_th³/2) et les occupations deviennent diluées. Le laboratoire distingue référence T=0, solution numérique à T>0 et approximations asymptotiques ; sa coupure et ses diagnostics doivent être surveillés.

## 11 · Bose–Einstein : une capacité d’excitation limitée

*SPÉ · TP PRIORITAIRE ET EXTENSION*

On étudie des bosons sans interaction, homogènes en dimension 3, avec un seul état interne et une énergie fondamentale prise égale à 0. Au refroidissement, μ augmente vers 0 par valeurs négatives. Les états excités ont une capacité d’occupation totale qui devient insuffisante : le nombre restant s’accumule macroscopiquement dans le fondamental.

N_exc/V=λ_th⁻³g₃ᐟ₂(z), z=exp(βμ)≤1.
g_s(z)=Σ_{q≥1}z^q/q^s ; g₃ᐟ₂(1)=ζ(3/2)≈2,612375.
T_c=(2πℏ²/(mkB))[n/ζ(3/2)]²ᐟ³.
Pour T≤T_c : N₀/N=1−(T/T_c)³ᐟ².

**Origine de ζ.** Développer 1/(exp x−1)=Σ_{q≥1}exp(−qx). L’intégrande étant positif, Tonelli permet l’échange somme–intégrale. Le changement u=qx donne ∫₀∞x¹ᐟ²exp(−qx)dx=q⁻³ᐟ²Γ(3/2). La capacité d’excitation à μ=0 est donc Vζ(3/2)/λ_th³. Le facteur ζ du T_c est élevé à 2/3, comme la densité : le mettre sans cette puissance change la constante.

À T_c, la fraction condensée débute à 0 ; tous les bosons ne sont pas immédiatement dans le fondamental. À T=T_c/2, la fraction vaut 1−2⁻³ᐟ²≈0,6464. L’expression est celle d’une limite thermodynamique uniforme 3D ; un piège harmonique a une autre densité d’états et un autre exposant. Une taille finie arrondit la transition.

Le condensat doit être compté séparément de l’intégrale continue des états excités : un point discret peut porter un nombre macroscopique même s’il a une mesure nulle dans l’intégrale. Au-dessus de T_c, résoudre g₃ᐟ₂(z)=nλ_th³ fixe μ<0. Une approximation numérique de ζ ou de g_s doit annoncer sa queue ; observer une grande occupation près de μ=0 n’est pas, à lui seul, un calcul complet de condensation.

## 12 · Planck, Wien et Stefan–Boltzmann

*SUP → SPÉ · CORPS NOIR*

Le corps noir est un modèle de rayonnement thermique dont la distribution est isotrope dans la cavité. Les photons ont deux polarisations et μ=0. Leur densité de modes par volume et fréquence est 8πν²/c³ ; multiplier par l’énergie hν et l’occupation de Bose donne la densité spectrale d’énergie.

u_ν=8πhν³/[c³(exp(hν/(kBT))−1)].
B_ν=c u_ν/(4π)=2hν³/[c²(exp(hν/(kBT))−1)].
B_λ=B_ν|dν/dλ|=2hc²/[λ⁵(exp(hc/(λkBT))−1)].

Le jacobien |dν/dλ|=c/λ² est positif. B_λ est une luminance par longueur d’onde et stéradian, d’unité W m⁻³ sr⁻¹. Pour une valeur par micromètre, multiplier la valeur par mètre par 10⁻⁶. Une densité spectrale ne s’évalue pas par simple remplacement ν=c/λ ; son élément d’intégration change aussi.

Maximum de B_λ : 5(1−exp(−x))=x, x=hc/(λ_maxkBT).
λ_maxT=b≈2,897772×10⁻³ m K.
Flux surfacique F=π∫₀∞B_λdλ=σT⁴.
σ=2π⁵kB⁴/(15h³c²) ; ∫₀∞x³/(exp x−1)dx=π⁴/15.

Le facteur π vient de l’intégration angulaire de la luminance avec projection cosθ sur l’hémisphère. Dans la cavité, F=cu_total/4. La somme exponentielle, intégrée terme à terme, donne 6ζ(4)=π⁴/15. Rayleigh–Jeans remplace exp x−1 par x lorsque x≪1 ; son prolongement aux petites longueurs d’onde donne la catastrophe ultraviolette, hors de son domaine de validité.

## 13 · Spectres et rendement visible d’une lampe

*SUP → SPÉ · EXERCICE 1*

Un maximum spectral dépend de la variable choisie. Maximiser B_ν conduit à 3(1−exp(−y))=y, avec y=hν/(kBT), différent de la racine 5 du spectre par longueur d’onde. Le maximum de B_ν ne se convertit donc pas en λ_max de B_λ par λ=c/ν. Les spectres en nombre de photons ont encore un autre facteur d’énergie.

Fraction énergétique visible :
r(T;λ₁,λ₂)=π∫_{λ₁}^{λ₂}B_λ(T)dλ/(σT⁴).
À 2500 K : r(390–780 nm)≈5,896 % ; r(390–760 nm)≈5,187 %.

Le TP prend une émission de corps noir et une bande rectangulaire de visible : ce r est une fraction de puissance rayonnée. Il n’est ni le rendement électrique complet d’une lampe ni une efficacité lumineuse pondérée par la sensibilité de l’œil. La puissance perdue par conduction et convection, ainsi que l’émissivité réelle, nécessitent d’autres données.

L’énoncé du recueil donne 390–780 nm, puis le corrigé emploie 390–760 nm. Il faut choisir la bande avant d’intégrer. La valeur annoncée d’environ 7 % est seulement un ordre de grandeur ; les deux valeurs ci-dessus distinguent exactement les bornes. Une quadrature convergée du spectre ou une intégration en fréquence avec son jacobien donnent le même résultat.

## 14 · Paramagnétisme et fluctuations d’un spin

*SPÉ · DEUX NIVEAUX ET APPLICATION*

On considère des moments indépendants ±μ dans un champ B, sans interactions responsables de ferromagnétisme. Leurs énergies sont −μB et +μB. Le laboratoire propose μ en multiples du magnéton de Bohr ; ce moment électronique n’est pas celui du proton employé dans l’exemple RMN du volet PQ.

x=μB/(kBT) ; z=2cosh x.
Moment moyen : m̄=μtanh x ; U/N=−μB tanh x.
χ_par_spin=(∂B m̄)_T=μ²sech²x/(kBT).
C_B/(NkB)=x²sech²x ; S/(NkB)=ln(2cosh x)−x tanh x.

À |x|≪1, m̄≈μ²B/(kBT) : c’est la loi de Curie. La linéarisation n’est pas valable à forte polarisation ; la formule exacte sature entre −μ et +μ. La séparation Δ=2μ|B| relie directement cette capacité à la formule de Schottky de la leçon 3.

Pour B non nul, T→0 donne la saturation et S→0. À B=0, les deux niveaux sont dégénérés et le modèle conserve S=NkBln2. L’ordre de ces limites importe ; il ne s’agit pas d’une transition ferromagnétique d’un système de spins couplés. Les fluctuations du moment donnent χ_par_spin=βVar(m), ce qui relie réponse et fluctuations.

## 15 · Ising 1D : compter les parois de domaines

*SPÉ · EXERCICE 5 PRIORITAIRE*

Une chaîne périodique de N spins sᵢ=±1 a H=−JΣᵢsᵢsᵢ₊₁, J>0 et s_{N+1}=s₁, sans champ externe. Une liaison entre spins opposés coûte 2J par rapport à une liaison alignée. En parcourant une boucle, le nombre de changements de signe doit être pair : notons-le 2q.

E_q=−JN+4Jq ; g_q=2C(N,2q), 0≤q≤⌊N/2⌋.
Z_N=(2cosh βJ)ᴺ+(2sinh βJ)ᴺ.
U_N=−NJ[(cosh K)ᴺ⁻¹sinh K+(sinh K)ᴺ⁻¹cosh K]/[(cosh K)ᴺ+(sinh K)ᴺ], K=βJ.

**Comptage.** Choisir les 2q liaisons où le signe change, puis le premier spin : cela construit exactement deux configurations. La somme des g_q vaut 2ᴺ. Le fondamental est doublement dégénéré et vaut −JN. Sommer les puissances binomiales paires de exp(−2βJ), après décalage par E₀, donne Z_N. Le laboratoire calcule cette partition finie exactement par les niveaux.

Limite N→∞, T>0 : U/N=−Jtanh K ; C/(NkB)=K²sech²K.
Approximation de Stirling : q/N≈1/[2(1+exp(2K))].
⟨sᵢsᵢ₊ᵣ⟩=(tanh K)^r ; ξ/a=−1/ln(tanh K).

Le facteur 2 dans exp(2βJ) est le coût d’une paroi ; la formule du recueil l’omet dans la relation de Stirling. Cette relation est une approximation pour populations macroscopiques, tandis que Z_N est exact à N fini. À champ nul, la symétrie globale s→−s impose ⟨m⟩=0 à taille finie. En chaîne infinie à température positive, les corrélations décroissent et il n’existe pas d’aimantation spontanée. La croissance de ξ à basse température et un pic de capacité ne sont pas une transition à T>0.

## 16 · Ising 2D : Onsager, Yang et taille finie

*SPÉ · EXTENSION GUIDÉE*

Sur le réseau carré, chaque spin interagit avec ses quatre voisins, chaque liaison étant comptée une fois. Pour des bords périodiques, H=−JΣ_{liaisons}sᵢsⱼ possède deux liaisons par site, donc E₀/N=−2J. On reste à champ externe nul. Le résultat critique est celui d’Onsager ; la formule de l’aimantation spontanée a été démontrée par Yang.

θ=kBT/J ; θ_c=2/ln(1+√2)≈2,269185.
m_sp(θ)=[1−sinh⁻⁴(2/θ)]¹ᐟ⁸ si θ<θ_c ; m_sp=0 sinon.
Définition : m_sp=lim_{h→0⁺}lim_{N→∞}⟨m⟩_{T,h}.

Inverser les limites ne donne pas la même grandeur. Pour un réseau fini à champ nul, la moyenne d’ensemble signée reste 0 par symétrie, même sous T_c. La moyenne ⟨|m|⟩ est un indicateur utile, mais n’est pas exactement m_sp. Sa valeur finie au-dessus de T_c et les déplacements des pics doivent être distingués des résultats infinis.

Metropolis : proposer sᵢ→−sᵢ ; ΔE=2JsᵢΣ_voisins sⱼ.
Accepter avec min(1,exp(−ΔE/(kBT))).
À T fixe : C/(NkB)=Var(H)/(NkB²T²), pour l’ensemble canonique.

Dans la simulation, chaque site visité propose un retournement avec probabilité 1/2, sinon reste inchangé ; cette attente évite certains cycles déterministes. Les deux couleurs du damier sont mises à jour successivement, en recalculant les voisins entre couleurs. Le taux d’acceptation affiché porte sur les retournements réellement proposés. La règle Metropolis conserve la distribution de Boltzmann ; sa réalisation numérique ne garantit pas une mise en équilibre rapide.

Le laboratoire confronte une simulation de taille finie à la référence exacte dans la limite thermodynamique. Il faut laisser une phase de mise en équilibre, puis mesurer. Près de T_c, les temps de corrélation augmentent : espacer les mesures aide, sans garantir leur indépendance. À basse température, une trajectoire peut conserver longtemps le signe de son domaine et donner une moyenne signée non nulle.

Comparer deux initialisations, plusieurs graines et plusieurs tailles apprend à juger une simulation. Le pic d’une courbe finie, sa stabilité apparente ou un faible bruit ne prouvent pas seuls une transition. La référence affichée est le modèle carré exact à champ nul, pas une approximation de champ moyen ; le comportement à champ non nul ou avec interactions différentes n’est pas couvert par cette formule.

## Exercices corrigés

### 1 · Un niveau n’est pas un microétat

Trois niveaux 0, ε, 2ε ont les dégénérescences 1,4,1. Donner leurs populations et l’entropie lorsque T devient très grand.

**Correction.** Les six microétats deviennent équiprobables. Les populations des niveaux sont donc 1/6,4/6,1/6. S=kBln6, et U=ε. Calculer −kBΣP_jlnP_j sans les dégénérescences sous-estime S. La formule par niveaux est −kBΣP_jln(P_j/g_j).

### 2 · Boltzmann avec une dégénérescence

Pour les mêmes niveaux, calculer P_ε/P_0 et P_{2ε}/P_0. La population maximale est-elle nécessairement celle du fondamental ?

**Correction.** Les rapports sont 4exp(−βε) et exp(−2βε). Lorsque βε<ln4, le niveau intermédiaire est plus peuplé que le fondamental, bien que chacun de ses microétats le soit moins. À basse température le fondamental domine. Comparer les niveaux et les microétats répond à deux questions différentes.

### 3 · Retrouver le facteur 1/4

Pour N sites indépendants à deux niveaux 0, Δ, dériver U=NΔ/(1+exp(βΔ)). Donner C à βΔ=2.

**Correction.** C=NkB(βΔ)²exp(βΔ)/(1+exp(βΔ))²=NkB(βΔ)²/[4cosh²(βΔ/2)]. À βΔ=2, C/(NkB)=sech²1≈0,4200. Omettre le facteur 1/4 multiplie la capacité par quatre. Dans le laboratoire des spins, poser Δ=2μ|B|.

### 4 · Quel compartiment reçoit la chaleur ?

Deux systèmes isolés ensemble ont T₁>T₂ et échangent seulement une énergie dE₁=−dE₂. Quel signe de dE₁ augmente l’entropie totale ?

**Correction.** dS_total=(1/T₁−1/T₂)dE₁. Le coefficient est négatif, donc dE₁<0 donne dS_total>0 : le plus chaud perd de l’énergie. Le signe inversé ferait transférer spontanément la chaleur du froid au chaud. De même, (∂S/∂N)_{E,V}=−μ/T découle de dE=TdS−PdV+μdN.

### 5 · Compter les variables quadratiques

Comparer l’énergie classique d’un oscillateur strictement 1D et d’une particule 3D rappelée seulement selon x. Pourquoi les réponses diffèrent-elles ?

**Correction.** Le premier a p_x²/(2m)+kx²/2, soit deux termes indépendants : U=kBT. Le second a trois termes cinétiques et un potentiel kx²/2, soit quatre termes : U=2kBT. Des coordonnées libres doivent être confinées dans un volume fini pour normaliser la partition. Un vrai oscillateur 3D possède six termes et U=3kBT.

### 6 · Une énergie de point zéro sans capacité

Établir Z de l’oscillateur quantique et expliquer les limites U→hν/2 et C→0 lorsque T→0.

**Correction.** Z=Σexp[−βhν(n+1/2)]=exp(−βhν/2)/(1−exp(−βhν)). Dériver donne U=hν/2+hν/(exp(βhν)−1). Le second terme disparaît à froid, tandis que le premier est constant en T ; sa dérivée est nulle. À chaud, C→kB. Une énergie stockée constante n’est pas une capacité thermique.

### 7 · Compter les états libres

À partir d’un volume (2π/L)³ par état en k, établir G(E) pour une particule libre 3D avec un seul état interne.

**Correction.** La sphère de rayon k contient V×(4πk³/3)/(2π)³ états. Avec k=√(2mE)/ℏ, G(E)=V(2m/ℏ²)^{3/2}E^{3/2}/(6π²), et D(E)=V(2m/ℏ²)^{3/2}√E/(4π²). Une dégénérescence de spin g_s multiplie ces deux expressions. G est un comptage ; D est une densité par énergie.

### 8 · Deux conditions pour la limite classique

Pourquoi kBT≫E_L et nλ_th³≪1 ne sont-elles pas la même condition ? Que signale une comparaison N_max→2N_max ?

**Correction.** La première rend quasi continu le spectre de la boîte. La seconde, pour un état interne, rend négligeables les effets d’échange quantique d’un gaz de nombreuses particules. On peut vérifier l’une sans l’autre. La comparaison de coupures mesure la masse ou l’énergie ajoutée entre les deux sommes ; elle ne borne pas à elle seule la queue au-delà de 2N_max.

### 9 · Trois vitesses à ne pas confondre

Donner les rapports ⟨v⟩/v_mp et v_rms/v_mp. Si T est quadruplée, comment changent ces vitesses ?

**Correction.** v_mp=√(2kBT/m), ⟨v⟩=√(8kBT/(πm)) et v_rms=√(3kBT/m). Les rapports valent 2/√π≈1,128 et √(3/2)≈1,225. Toutes les vitesses doublent si T est quadruplée ; elles sont inversement proportionnelles à √m. La moyenne d’une composante est néanmoins nulle à l’équilibre.

### 10 · Pourquoi la pression contient v_z²

Pour des collisions élastiques sur une paroi normale à z, établir P=mn⟨v_z²⟩ et l’équation d’état idéale.

**Correction.** Le nombre incident par surface et temps est pondéré par v_z, pour v_z>0. Chaque collision transfère 2mv_z. Ainsi P=2mn∫_{v_z>0}v_z²f(v)d³v. La symétrie ramène le demi-espace à la moitié de l’intégrale totale : P=mn⟨v_z²⟩. Maxwell donne ⟨v_z²⟩=kBT/m, donc P=nkBT et PV=NkBT.

### 11 · Temps d’effusion

À géométrie et température identiques, comparer les temps de fuite de molécules de masses m et 4m. Que change un trou de surface doublée ?

**Correction.** τ=(V/S)√(2πm/(kBT)). La masse 4m donne un temps double. Doubler S donne un temps moitié. N=N₀exp(−t/τ) suppose T maintenue, un petit orifice en régime moléculaire et une fuite vers le vide. À t=τ, il reste N₀/e.

### 12 · Le gaz qui sort est-il représentatif ?

Montrer que le faisceau effusif porte en moyenne 2kBT par particule, au lieu de 3kBT/2. Quelle conséquence sans thermostat ?

**Correction.** La vitesse sortante est sélectionnée avec f_eff(v)=v f_v(v)/⟨v⟩. Le rapport des intégrales ∫v⁵exp(−av²)dv/∫v³exp(−av²)dv vaut 2/a, a=m/(2kBT), donnant ⟨mv²/2⟩=2kBT. Pour un intérieur restant à l’équilibre mais isolé thermiquement, d(3NkBT/2)=2kBTdN entraîne dT/T=dN/(3N), donc T∝N^{1/3} : la fuite refroidit.

### 13 · Une paroi poreuse ne donne pas toujours P₁=P₂

Deux enceintes de même volume ont T₂=4T₁ et échangent un même gaz par effusion. Donner N₁/N₂ et P₁/P₂ stationnaires.

**Correction.** L’égalité des flux donne N₁√T₁/V₁=N₂√T₂/V₂. À volumes égaux, N₁/N₂=2. Avec P_i=N_ikBT_i/V_i, P₁/P₂=1/2=√(T₁/T₂). La conservation Ṅ₁=−Ṅ₂ n’impose cette relation qu’à l’état stationnaire, pas pendant toute la relaxation.

### 14 · Stationnaire n’est pas équilibre thermique

Les flux de particules à travers la paroi poreuse sont égaux, mais T₁>T₂. L’énergie échangée est-elle nulle ?

**Correction.** Non. Chaque particule allant de 1 vers 2 porte en moyenne 2kBT₁ ; dans l’autre sens, 2kBT₂. Pour des flux de nombre égaux, il existe un transfert énergétique net 2kB(T₁−T₂) par couple de transferts, du chaud au froid. Les thermostats maintiennent ce régime stationnaire hors de l’équilibre thermique global.

### 15 · Fluctuations BE, FD et MB

Pour ε−μ=kBT, calculer les trois occupations. Pourquoi ne faut-il pas les sommer directement sur l’axe des énergies ?

**Correction.** n_BE=1/(e−1)≈0,5820, n_FD=1/(e+1)≈0,2689 et n_MB=e^{-1}≈0,3679. Leurs variances par mode indépendant sont n(1+n), n(1−n) et environ n. Pour obtenir N, il faut compter les états : N=Σg_jn_j, ou ∫D(E)n(E)dE. Une occupation n’est pas une probabilité normalisée en énergie.

### 16 · Énergie de Fermi d’électrons libres

Pour des électrons de spin 1/2 à densité 10²⁸ m⁻³, estimer E_F et T_F. Que devient E_F si la densité est multipliée par huit ?

**Correction.** Avec g_s=2, E_F=ℏ²(3π²n)^{2/3}/(2m_e)≈1,69 eV et T_F≈1,96×10⁴ K. E_F∝n^{2/3}, donc multiplier n par huit multiplie E_F par quatre. Le nombre de spin doit être compté une seule fois, dans la densité d’états ou dans l’intégrale, pas dans les deux.

### 17 · Un gaz idéal exerce une pression à T=0

À T=0, établir U/N et P pour le gaz de fermions 3D. Pourquoi PV=NkBT ne s’applique-t-elle pas ?

**Correction.** Avec D(E)=A√E, N=(2A/3)E_F^{3/2} et U=(2A/5)E_F^{5/2}. Donc U/N=3E_F/5. Une dispersion quadratique donne P=2U/(3V)=2nE_F/5. Le gaz est sans interaction mais dégénéré ; l’équation PV=NkBT exige la limite classique diluée, absente ici. La pression provient du remplissage imposé par Pauli.

### 18 · Le facteur ζ du T_c

Pour un gaz de bosons uniforme 3D à un seul état interne, déduire T_c de nλ_th³=ζ(3/2). Que devient T_c si la densité double ?

**Correction.** λ_th²=2πℏ²/(mkBT). Élever n/ζ à la puissance 2/3 donne T_c=(2πℏ²/(mkB))[n/ζ(3/2)]^{2/3}. Le facteur ζ est donc au dénominateur avec la puissance 2/3, pas 1. Doubler la densité multiplie T_c par 2^{2/3}≈1,5874, à masse et modèle fixés.

### 19 · Tous les bosons au fondamental ?

Donner N₀/N à T=T_c et T=T_c/2. Pourquoi faut-il séparer N₀ de l’intégrale des états excités ?

**Correction.** Dans la limite uniforme 3D, N₀/N=1−(T/T_c)^{3/2} sous T_c : la fraction est 0 à T_c et environ 0,6464 à T_c/2. Le fondamental est un état discret qui peut porter une population macroscopique ; l’intégrale continue ne le comptabilise pas comme tel. Un gaz piégé ou fini demande un modèle de densité d’états adapté.

### 20 · Le maximum dépend de la variable

Écrire le changement de variable de B_ν à B_λ. Pourquoi le maximum de l’un ne correspond-il pas à celui de l’autre ?

**Correction.** B_λdλ=B_ν|dν|, donc B_λ=B_ν(c/λ²). Le jacobien dépend de λ : il déplace le maximum. B_λ donne la racine 5(1−e^{-x})=x, alors que B_ν donne 3(1−e^{-y})=y. La loi λ_maxT≈2,898×10⁻³ m K concerne le spectre énergétique par unité de longueur d’onde.

### 21 · La lampe à 2500 K

Estimer la fraction énergétique visible d’un corps noir à 2500 K dans la bande 390–780 nm. Comparer à 390–760 nm et préciser ce que mesure ce ratio.

**Correction.** Calculer r=π∫B_λdλ/(σT⁴) sur la bande choisie. Une quadrature convergée donne environ 5,896 % pour 390–780 nm et 5,187 % pour 390–760 nm. L’énoncé et le corrigé du recueil ne choisissent pas les mêmes bornes ; la valeur d’environ 7 % est un ordre de grandeur. Ce ratio porte sur la puissance rayonnée, sans pondération de la vision ni autres pertes électriques ou thermiques.

### 22 · Curie et saturation

Pour un spin indépendant, montrer que la loi de Curie est une limite de m̄=μtanh(μB/(kBT)). Une droite extrapolée au-delà de μ décrit-elle le modèle ?

**Correction.** À |x|≪1, tanh x=x+O(x³), donc m̄≈μ²B/(kBT) et χ≈μ²/(kBT). À fort champ ou basse température, tanh x sature ; la moyenne reste entre −μ et +μ. L’extrapolation linéaire au-delà n’est pas valide. Sans interaction entre spins, il n’y a pas de transition ferromagnétique dans ce modèle.

### 23 · Une chaîne de quatre spins

Pour Ising périodique N=4 à champ nul, compter les états par nombre de parois et écrire Z. Retrouver le facteur2 dans l’exponentielle de Stirling.

**Correction.** Le nombre de parois est 0, 2 ou 4 : les dégénérescences sont 2, 12, 2 et les énergies −4J, 0, +4J. Donc Z=2exp(4βJ)+12+2exp(−4βJ), cohérent avec (2coshβJ)^4+(2sinhβJ)^4. Pour N grand, si 2q est le nombre de parois, leur coût individuel 2J donne q/N≈1/[2(1+exp(2βJ))]. Cette approximation n’est pas l’expression finie exacte.

### 24 · Une moyenne signée peut-elle être un ordre spontané ?

À champ nul, comparer ⟨m⟩ d’un réseau Ising carré fini, ⟨|m|⟩ simulé et m_sp de Yang. Quel ordre de limites définit l’aimantation spontanée ?

**Correction.** La moyenne d’ensemble signée finie est 0 par symétrie s→−s. ⟨|m|⟩ est positif et dépend de la taille ; il n’est pas directement m_sp. L’ordre spontané est lim_{h→0+}lim_{N→∞}⟨m⟩. La référence exacte à champ nul a θ_c=2/ln(1+√2)≈2,269185. Une simulation courte peut rester dans un secteur de signe ; des fluctuations corrélées, un pic et une moyenne non nulle ne démontrent pas seuls la limite thermodynamique.

## Sources et conventions

Recueil de A. R., extrait MemoCPGEScientifAR2027-PS.pdf, pages imprimées 434–442 : ensembles, TP Maxwell/pression/effusion/paroi poreuse, Fermi/Bose, rayonnement et exercices. Le PDF personnel n’est pas inclus dans le dépôt.

Développements, preuves, corrigés et parcours rédigés pour l’atelier. Les prolongements Fermi/BEC et Ising 2D sont guidés ; les attendus réglementaires et la profondeur varient selon la filière CPGE.

Constantes physiques : NIST, valeurs CODATA 2022, tableau officiel : https://physics.nist.gov/cuu/Constants/Table/allascii.txt . h, kB et e ont leurs valeurs exactes SI ; les exemples fixent explicitement masse et dégénérescence interne.

Référence complémentaire : MIT OpenCourseWare, 8.333 Statistical Mechanics I, notes de cours : https://ocw.mit.edu/courses/8-333-statistical-mechanics-i-statistical-mechanics-of-particles-fall-2013/pages/lecture-notes/ ; ensemble microcanonique, cours 12 : https://ocw.mit.edu/courses/8-333-statistical-mechanics-i-statistical-mechanics-of-particles-fall-2013/resources/lecture-12/ .

Références complémentaires Fermi et Bose : MIT OpenCourseWare, 8.333, cours 24 : https://ocw.mit.edu/courses/8-333-statistical-mechanics-i-statistical-mechanics-of-particles-fall-2013/resources/lecture-24/ ; cours 25 : https://ocw.mit.edu/courses/8-333-statistical-mechanics-i-statistical-mechanics-of-particles-fall-2013/resources/lecture-25/ .

Référence primaire Ising 2D : L. Onsager, Crystal Statistics I, Physical Review 65, 117 (1944), https://journals.aps.org/pr/abstract/10.1103/PhysRev.65.117 . Référence de l’aimantation spontanée : C. N. Yang, Physical Review 85, 808 (1952), https://journals.aps.org/pr/abstract/10.1103/PhysRev.85.808 . Les formules sont appliquées au réseau carré infini, isotrope et sans champ.

Conventions : N est un nombre de particules, n=N/V une densité et n_mol une quantité en moles ; p_i désigne un microétat et P_j un niveau. β=1/(kBT). Une occupation BE/FD n’est ni une dégénérescence ni une probabilité normalisée sur l’énergie.

Conventions spectrales : Bλ par mètre ou par micromètre selon l’axe, luminance par stéradian ; flux hémisphérique π∫Bλdλ. Le maximum par longueur d’onde diffère du maximum par fréquence. La fraction visible annoncée porte sur 390–780 nm, sauf autre bande indiquée.

Corrections explicitées : gaz classique si nλth³≪1 ; facteur 1/4 de la capacité à deux niveaux ; exp(2βJ) pour les parois Ising 1D ; ζ(3/2) à la puissance 2/3 dans T_c ; signe−μ/T en microcanonique ; transfert spontané du chaud vers le froid ; état stationnaire poreux distingué de la simple conservation de matière. Voir ERRATA.md.

Limites numériques : somme quantique de boîte tronquée, comparaisons de coupures sans certification de toute la queue ; simulations Ising finies avec autocorrélations ; approximations classiques et basses températures identifiées séparément. Une courbe ou un pic ne remplace pas la preuve d’une transition.
