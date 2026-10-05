# Clarifications mathématiques et physiques du volet PQ

Ces précisions accompagnent l’extrait personnel **MemoCPGEScientifAR2027-PQ.pdf**, pages imprimées 471–479. Elles portent sur les thèmes étudiés dans l’atelier. Les leçons et corrigés donnent les démonstrations ; le PDF n’est pas reproduit dans le dépôt.

| Page imprimée | Passage | Formule ou interprétation retenue |
| --- | --- | --- |
| 472 | Identité du commutateur d’un produit | `[A,BC]=[A,B]C+B[A,C]`, sans facteur `A` devant le membre de gauche. Pour les composantes position–impulsion, `[x_i,p_j]=iℏδ_ij I`. |
| 473 | Conditions de bord de la boîte | Aux parois infinies, `ψ=0` sur les faces. On n’impose pas `ψ′(0)=ψ′(L)` : cette égalité éliminerait les modes impairs. Les conditions périodiques définissent un autre problème, sans ces parois. |
| 473 | Superposition d’états | `ψ(r,t)=Σ_n c_n φ_n(r) exp(−iE_nt/ℏ)`, avec `c_n=⟨n\|ψ(0)⟩`. Une superposition d’énergies distinctes peut avoir une densité non stationnaire. |
| 473 | Énergie d’une onde libre | `E=+ℏ²k²/(2m)+V₀`, car `Δexp(ikx)=−k²exp(ikx)`. |
| 474 | Diffraction et Heisenberg | La largeur du lobe central est d’ordre `λ/a`. Pour une ouverture rectangulaire idéale, le profil sinc² a une variance d’impulsion infinie : cette largeur n’est pas un `Δp` fini. Une gaussienne permet le calcul exact d’écarts types. |
| 474 | Hydrogène | `a₀≈52,9 pm` est l’échelle de l’orbitale 1s et le maximum de sa densité de probabilité radiale ; `⟨r⟩=3a₀/2`. La minimisation avec `p∼ℏ/r` est heuristique. La famille normalisée `ψ_a∝exp(−r/a)` fournit une démarche variationnelle explicite. |
| 474 | Minimisation harmonique | Pour `f(u)=ℏ²/(8mu)+mω²u/2`, `f′(u)=−ℏ²/(8mu²)+mω²/2`. Son minimum vaut `ℏω/2`, atteint par le fondamental gaussien. |
| 474 | Intrication et polarisation | L’atelier choisit `Φ⁺=(\|00⟩+\|11⟩)/√2`, avec corrélation `cos[2(a−b)]` pour les analyseurs annoncés. Il est distinct du singulet de deux spins 1/2 `Ψ⁻=(\|01⟩−\|10⟩)/√2`. Les conventions d’axes et de polarisation doivent être précisées. |
| 475 | Relation énergie–temps | Le temps de Schrödinger est un paramètre. `ΔEΔt≥ℏ/2` ne se déduit pas « de même » de `[x,p]=iℏI` : une relation de durée d’évolution, telle Mandelstam–Tamm, requiert une définition propre de cette durée. |
| 475 | Densité et continuité | La densité spatiale est `ρ(r)=\|ψ(r)\|²`. L’opérateur densité est `ρ̂=\|ψ⟩⟨ψ\|`, ou un mélange de projecteurs. `∂tρ+div j=0`, avec `j=(ℏ/m)Im(ψ*∇ψ)` ; séparément, `iℏρ̂̇=[H,ρ̂]`. |
| 478 | Raccordement à potentiel fini | `ψ′(x₀+ε)−ψ′(x₀−ε)=(2m/ℏ²)∫(V−E)ψdx`, avec un signe positif. Pour un potentiel borné, l’intégrale tend vers zéro et `ψ′` est continue. |
| 479 | Josephson | Avec une paire de charge absolue `q=2e`, `I=I_c sinδ`, `δ̇=2eV/ℏ`, `f_J=2e\|V\|/h`. `I_c` est indépendant de `δ`. Dans un modèle diagonal symétrique, les énergies `±qV/2` ont une différence `qV` ; les écrire `±qV` double celle-ci. |
| 477, 479 | RMN et Rabi | Une identité `ℏω₀I` ne sépare pas deux niveaux. Choisir leur ordre puis écrire `H₀=(ℏω₀/2)Z`. Dans le modèle tournant annoncé, `H_rot=(ℏ/2)(ΔZ+ΩX)` et `P₁=Ω² sin²(√(Ω²+Δ²)t/2)/(Ω²+Δ²)`. Le Zeeman physique est `H_Z=−γS·B`. |

Dans le moteur, `sinc(v)=sin(πv)/(πv)` : le profil de la fente est donc `sinc²(a sinθ/λ)`, équivalent à `[sin u/u]²` avec `u=πa sinθ/λ`. Les angles des curseurs sont en degrés ; les formules trigonométriques utilisent des radians.

Le champ radiofréquence **circulaire** idéal permet le passage exact au référentiel tournant. Pour un champ **linéaire** réel, l’approximation de l’onde tournante retient une composante circulaire d’amplitude moitié : le facteur 2 doit apparaître dans la définition de la pulsation de Rabi.

La profondeur exigée varie selon les filières CPGE. La sphère de Bloch, le bruit de Werner, CHSH, le SQUID idéal, les états cohérents et les circuits Bell/Grover sont présentés comme des **extensions guidées** : l’atelier annonce leurs hypothèses et les connaissances ajoutées au lieu de les supposer acquises.
