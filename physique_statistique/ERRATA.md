# Clarifications du volet de physique statistique

Ces précisions concernent les thèmes utilisés dans **MemoCPGEScientifAR2027-PS.pdf**, pages imprimées 434–442. Les leçons et exercices donnent les calculs complets. Le fichier personnel et ses illustrations ne sont pas inclus dans le dépôt.

| Page imprimée | Passage | Formule ou interprétation retenue |
| --- | --- | --- |
| 434 | Gaz parfait quantique | Une distance interparticulaire très supérieure à la longueur d’onde thermique correspond au régime classique dilué : `nλth³/g_s≪1`. Un gaz sans interaction peut néanmoins être quantique et dégénéré lorsque cette condition n’est plus satisfaite. |
| 435 | Dégénérescence et probabilité | `g_j` est le nombre de microétats du niveau j. Pour un microétat, `p_i=exp(−βE_i)/Z` ; pour le niveau, `P_j=g_jexp(−βE_j)/Z`. L’occupation d’un état BE/FD est une grandeur différente. |
| 435 | Partition continue | `Z=∫D(E)exp(−βE)dE` pour le spectre d’un système canonique décrit ainsi. `∫D(E)n_BE/FD(E)dE` calcule un nombre de particules, pas ce Z. |
| 435 | Entropie et additivité | L’entropie est calculée sur les microétats. Avec des niveaux dégénérés, `S=−kBΣ_jP_jln(P_j/g_j)`. L’additivité se démontre pour des distributions indépendantes ; les corrélations doivent être prises en compte séparément. |
| 436 | Pression cinétique | Seuls les incidents `v_z>0` frappent une face : `P=2mn∫_{v_z>0}v_z²f(v)d³v=mn⟨v_z²⟩=nkBT`. Le flux et la projection de l’impulsion interviennent chacun une fois. |
| 436 | Paroi poreuse | La conservation `Ṅ₁=−Ṅ₂` vaut pendant toute l’évolution. L’égalité des flux `N₁√T₁/V₁=N₂√T₂/V₂` vaut à l’état stationnaire, d’où `P₁/√T₁=P₂/√T₂`. Avec des thermostats de températures différentes, ce n’est pas un équilibre thermique global. |
| 437 | Apparition d’un condensat | Dans un gaz idéal uniforme 3D, un seul état interne, `nλth³=ζ(3/2)` à T_c et `T_c=(2πℏ²/(mkB))[n/ζ(3/2)]^{2/3}`. ζ porte la puissance 2/3. Au-dessous, `N₀/N=1−(T/T_c)^{3/2}` : la condensation ne place pas immédiatement tous les bosons dans le fondamental. |
| 438 | Dérivées microcanoniques | `dS=dE/T+PdV/T−μdN/T`, donc `(∂S/∂N)_{E,V}=−μ/T`. |
| 438 | Paramètres des ensembles | En canonique, les dérivées sont prises à nombre de particules fixé. Le grand potentiel `J(T,V,μ)` vérifie `⟨N⟩=−∂μJ` et `S=−∂TJ`. `μ=(∂F/∂N)_{T,V}` appartient au potentiel libre F ; N n’est pas une variable indépendante naturelle de J. |
| 438 | Sens des transferts | Si `T₁>T₂`, `dS_total=(1/T₁−1/T₂)dE₁>0` exige `dE₁<0` : le plus chaud perd de l’énergie. À température commune et `P₁>P₂`, une augmentation `dV₁>0` augmente l’entropie. |
| 439 | Spectres photonique et énergétique | Une densité par longueur d’onde se transforme avec le jacobien positif `c/λ²`. `u_λ=8πhc/[λ⁵(exp(hc/(λkBT))−1)]` et `B_λ=cu_λ/(4π)`. Les maxima par fréquence et par longueur d’onde sont différents. |
| 440, 441 | Capacité à deux niveaux | Pour Δ l’écart d’énergie, `C=NkB(βΔ)²/[4cosh²(βΔ/2)]`. Le facteur 1/4 manque dans l’expression imprimée. |
| 441 | Partition de N sites à deux niveaux | Pour des spins ou sites indépendants identifiés, `Z=zᴺ`, sans `1/N!`. Le facteur de Gibbs intervient dans le gaz classique de particules identiques, avec un autre comptage de microétats. |
| 440, 442 | Ising périodique 1D | Si 2q est le nombre de parois, `E_q=−JN+4Jq`, `g_q=2C(N,2q)`. L’approximation de Stirling donne `q≈N/[2(1+exp(2βJ))]` : le facteur2 de l’exponentielle est nécessaire. La partition finie par les niveaux ou par transfert est exacte. |
| 440, 441 | Rendement de la lampe | L’énoncé emploie 390–780 nm, le corrigé 390–760 nm. À 2500 K, la fraction énergétique d’un corps noir est respectivement ≈5,896 % et≈5,187 %. La valeur d’environ 7 % reste un ordre de grandeur ; une efficacité visuelle ou électrique exige d’autres facteurs. |
| 441 | Équipartition | Compter les variables quadratiques indépendantes du Hamiltonien complet. Un oscillateur strictement 1D possède deux termes et `U=kBT`; une particule 3D rappelée seulement selon x possède quatre termes et `U=2kBT`. Les contraintes et degrés libres doivent être annoncés. |
| 442 | Ortho–para et spin nucléaire | Le singulet de deux spins 1/2 est antisymétrique, le triplet symétrique. Les restrictions rotationnelles pair/impair supposent deux noyaux identiques, par exemple les protons de H₂ avec un état électronique symétrique. Elles ne valent pas pour une molécule A–B hétéroatomique arbitraire. Un rapport canonique ortho/para suppose une conversion permettant l’équilibre. |

Pour l’Ising carré, l’atelier utilise la température critique exacte d’Onsager et l’aimantation spontanée démontrée par Yang. Les conditions sont le réseau carré isotrope, le champ nul et la limite thermodynamique ; il ne s’agit pas d’une approximation de champ moyen. Les moyennes finies de simulation `⟨m⟩` et `⟨|m|⟩` ne sont pas la même grandeur que l’ordre spontané défini après la limite de taille infinie.

Les thèmes Fermi/BEC, fluctuations grand canoniques et Ising 2D sont des extensions guidées dont la profondeur varie selon la filière. Les sommes tronquées et les simulations indiquent leurs limites : un diagnostic entre deux coupures ne certifie pas toute la queue ; près d’une transition, l’autocorrélation et l’équilibrage doivent être examinés.
