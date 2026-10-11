# Thermodynamique — corrections de formules

Ces corrections concernent uniquement des formules de l’extrait P22–P24 du recueil de A. R., contrôlées dans le contexte des pages imprimées. Les conventions de signe sont celles indiquées à chaque entrée.

## P22, page 454 — signes du travail et de la chaleur isothermes

La page 450 définit W et Q positifs lorsqu’ils sont reçus par le gaz. Soient n la quantité de gaz parfait, R la constante des gaz, T₀ la température constante et V₁,V₂ les volumes initial et final. Pour une transformation isotherme réversible :

**W=−nRT₀ ln(V₂/V₁)** et **Q=−W=+nRT₀ ln(V₂/V₁)**.

Le signe devant le logarithme dans la formule imprimée de W doit donc être négatif. Pour une isotherme irréversible contre une pression extérieure constante Pext, le travail reçu est −Pext(V₂−V₁). Puisque ΔU=0, **Q=+Pext(V₂−V₁)** ; l’entropie échangée avec le thermostat est ainsi **Q/T₀=+Pext(V₂−V₁)/T₀**. Le signe négatif imprimé sur cette dernière expression doit être positif.

## P22, page 458 — travaux de pression dans le compresseur

Pour une même quantité de gaz, soient U₁,U₂ les énergies internes, P₁,V₁ et P₂,V₂ les états d’entrée et de sortie. W′ est le travail du moteur reçu par le gaz et Q la chaleur reçue. En négligeant les variations d’énergie cinétique et potentielle :

**U₂−U₁=W′+Q+P₁V₁−P₂V₂**.

Les deux termes de pression sont inversés dans la première égalité imprimée. Avec H=U+PV, le bilan corrigé donne bien **H₂−H₁=W′+Q**, comme la ligne suivante du recueil.

## P23, page 461 — Langevin et relation d’Einstein

Soient x la position suivant un axe, v=dx/dt la vitesse, α le coefficient de frottement dans la force −αv, T la température absolue et kB la constante de Boltzmann. La barre désigne une moyenne statistique. Dans le régime diffusif :

**d⟨x²⟩/dt = 2⟨xv⟩**, donc **⟨x²⟩ ≃ 2(kBT/α)t** et **D=kBT/α**.

Le facteur 2 manque lors de l’intégration dans le TP ; D=kBT/(2α) doit donc être remplacé par D=kBT/α. Pour une sphère de rayon a, dans un fluide de viscosité η, α=6πηa donne **D=kBT/(6πηa)**. Pour les ions décrits plus bas, avec un coefficient de frottement f et une mobilité électrique positive μ=|q|/f : **D=kBT/f=kBTμ/|q|**.

Vérification : la définition ⟨x²⟩=2Dt suivant un seul axe est aussi celle de la marche au hasard, page 465. Pour une vitesse initiale à l’équilibre, le résultat avec inertie est 2D[t−τ(1−exp(−t/τ))], où τ=m/α et m est la masse.

## P24, page 468 — conduction dans l’équation thermoacoustique

Soient θ la variation de température, p la surpression, ρ₀ la masse volumique à l’équilibre, cP la capacité thermique massique à pression constante et λ la conductivité thermique. Le bilan de chaleur donne :

**λ ∂²θ/∂x² = ρ₀cP ∂θ/∂t − ∂p/∂t.**

Le coefficient à gauche doit être λ, plutôt que la diffusivité χ définie page 460. Pour un gaz parfait de pression P₀ et de température T₀, avec γ=cP/cV : ρ₀cP=[γ/(γ−1)]P₀/T₀. La relation de dispersion imprimée utilise d’ailleurs λ. Chaque terme du bilan est une puissance par unité de volume.

## P24, page 468 — condition sur le déterminant

Les amplitudes complexes p₀ et θ₀ vérifient un système linéaire homogène M(p₀,θ₀)ᵀ=0. Une solution non nulle existe si et seulement si **det M=0**, et non det M≠0. C’est cette condition qui produit la relation de dispersion affichée juste après.

## P24, page 468 — transformation de Legendre piézoélectrique

Le texte fixe dU=T dS−PA de+V dq : U est l’énergie interne, S l’entropie, P la pression, A l’aire constante, e l’épaisseur, V la tension et q la charge. Pour utiliser P et V comme variables indépendantes, la transformation cohérente est :

**Ω=U+PAe−Vq**, puis **dΩ=T dS+Ae dP−q dV**.

Par égalité des dérivées croisées : **(∂q/∂P)S,V = −A(∂e/∂V)S,P**. Ces signes découlent directement de la différentielle dU donnée dans le recueil.

Dans la formulation tensorielle de la même page, G=U−TS−σjkεjk−EiDi implique ∂G/∂σjk=−εjk et ∂G/∂Ei=−Di. Le coefficient piézoélectrique vérifie donc **dijk=−∂²G/(∂Ei∂σjk)** ; les deux expressions par dérivation des déformations εjk et des déplacements électriques Di gardent leur signe positif.
