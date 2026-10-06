# Huit missions pour apprendre à construire un modèle

Une expérience commence par une prévision écrite. Elle se termine par une explication reliée à une équation, accompagnée d’un contrôle d’unité et d’un domaine de validité. Les dix-huit laboratoires sont regroupés ci-dessous pour faire travailler conservation, conditions aux limites, ordre de grandeur et interprétation d’un graphique.

## Comment lire les trois niveaux

**Sup** désigne une porte d’entrée : mécanique du point, sinus et exponentielles, dérivées, intégrales simples, dimensions et thermodynamique. **Spé** indique la mobilisation des bilans, opérateurs, équations différentielles et techniques numériques déjà étudiés **selon la filière**. **Au-delà** signale un prolongement guidé : la formule spécialisée est donnée, puis contrôlée et exploitée ; sa connaissance préalable n’est pas exigée.

Ces niveaux sont des repères pédagogiques, pas une correspondance officielle commune à toutes les CPGE. Le [programme MPSI](https://www.education.gouv.fr/bo/21/Special1/ESRS2035779A.htm) permet notamment l’entrée par les signaux sinusoïdaux et la dispersion. Le [programme PSI](https://www.education.gouv.fr/bo/21/Hebdo31/ESRS2111748A.htm), annexe de physique-chimie §2.4, traite les bilans et la viscosité mais exclut explicitement les équations d’Euler et de Navier–Stokes. Le [programme PC](https://www.education.gouv.fr/bo/21/Hebdo31/ESRS2111703A.htm), annexe de physique §4.3, comprend une initiation aux fluides tout en excluant notamment l’approche lagrangienne, la fonction de courant, l’étude locale du gradient de vitesse et Bernoulli instationnaire. Ces sujets apparaissent donc ici comme extensions lorsqu’ils dépassent le programme suivi. Textes et liens vérifiés le 6 octobre 2026.

Pour chaque mission, garder une petite fiche : **hypothèses ; variables et unités ; prévision ; observations ; preuve ou calcul ; limite du modèle**. Une courbe superposée à une autre n’est pas une preuve générale ; un contrôle indépendant de conservation peut en revanche réfuter un calcul faux.

## Mission 1 — Tourner, déformer ou seulement transporter ?

**Laboratoires :** `cinematique`, `newtonien`. **But :** comprendre ce qu’un champ de vitesse fait localement à un petit élément fluide, puis relier cette déformation à une contrainte et à une puissance dissipée.

Les variables sont `a` et `γ̇`, taux en s⁻¹ ; `Ω`, rotation en rad·s⁻¹ ; `U`, vitesse en m·s⁻¹ ; `η`, viscosité en Pa·s ; `ρ`, masse volumique en kg·m⁻³. Les contrôles affichent parfois η en mPa·s : convertir avant un calcul.

1. Prévoir la forme d’une trajectoire en rotation pure et la dissipation d’une rotation rigide. Choisir le préréglage correspondant, puis comparer au cas d’étirement.
2. Pour le champ stationnaire du TP, expliquer pourquoi la trajectoire reste sur une ligne de courant. La figure `cinematique.svg` fournit ensuite un contre-exemple instationnaire : même champ figé, histoire différente.
3. Construire `D=(grad v+grad vᵀ)/2` et `W=(grad v−grad vᵀ)/2`. Faire varier la rotation ajoutée à déformation fixée : `τ=2ηD` et la dissipation doivent rester inchangés.

**Trace attendue :** un croquis, le calcul de la divergence et une explication de `D:W=0` qui justifie `2ηD:D≥0`.

**Sup :** suivre une position et vérifier des unités. **Spé :** calculer une dérivée particulaire ou un gradient lorsque ces objets sont étudiés. **Au-delà :** lire la décomposition tensorielle, la fonction de courant et l’exponentielle du champ linéaire avec les formules fournies.

## Mission 2 — Une parabole n’est pas encore un débit

**Laboratoires :** `couette`, `poiseuille`. **But :** passer de l’équation locale aux conditions aux limites, puis du profil à un débit et à un bilan de puissance.

`h` est l’écartement des plaques, `R` le rayon du tube et `L` sa longueur, en m ; `U0,U1` sont les vitesses des plaques en m·s⁻¹ ; `G=−dp/dx` est en Pa·m⁻¹ ; la chute de pression positive du tube est `Δp=pentrée−psortie`, en Pa. Distinguer `q`, débit par largeur en m²·s⁻¹, et `Q`, débit-volume en m³·s⁻¹.

1. Avant les tracés, annoncer les deux valeurs de vitesse aux parois et le signe de la courbure imposée par `ηu″=−G`.
2. Dans Couette, rechercher un débit nul alors que des particules bougent. Le préréglage « Débit nul mais mouvement » permet de lire des zones de sens opposés.
3. Dans le tube, prévoir l’effet d’un rayon doublé à Δp fixé : le débit est multiplié par 16. Retrouver `Q=2π∫u(r)r dr` et `ū=u_max/2`.
4. Vérifier que les puissances de pression et des parois compensent la dissipation. Une paroi peut recevoir de l’énergie : conserver les signes de son travail.

**Trace attendue :** intégrales de débit et bilan signé, puis une discussion de Reynolds et de la longueur d’entrée.

**Sup :** polynômes, intégrales et puissances. **Spé :** bilans et force visqueuse ; résolution de l’équation donnée selon filière. **Au-delà :** discuter la stabilité d’une solution formelle et les conditions d’un écoulement pleinement développé.

## Mission 3 — La viscosité transmet-elle le mouvement à une vitesse constante ?

**Laboratoires :** `diffusion`, `blasius`. **But :** reconnaître deux lois en racine carrée et comprendre leur origine sans confondre temps de diffusion et distance de développement.

`ν=η/ρ` est en m²·s⁻¹, `t` en s, `y,x,h` en m et `U∞` en m·s⁻¹. La profondeur de diffusion varie comme `√(νt)`. La couche limite plane varie comme `√(νx/U∞)`. Ici `h` est la hauteur totale du canal ; dans Hartmann, il sera une demi-hauteur.

1. Prévoir l’effet d’un temps multiplié par quatre. Sélectionner le demi-espace et vérifier que la longueur caractéristique double.
2. Passer au canal fini. À temps long, prévoir le profil qui satisfait les deux parois et constater la convergence vers Couette. Expliquer pourquoi l’erfc du demi-espace ne peut pas être la solution exacte de ce second problème.
3. Sur la plaque plane, superposer les profils avec la variable de similitude `ζ=y√(U∞/(νx))`. Relier le tir numérique à la condition `f′(∞)=1`, plutôt qu’à l’ajustement arbitraire d’une courbe.

**Trace attendue :** un contrôle dimensionnel et un graphique réduit ; préciser la définition opérationnelle de δ99 et la pente `f″(0)` qui commande le frottement.

**Sup :** analyse dimensionnelle et changements d’échelle. **Spé :** analogie avec les équations de diffusion, séparation des variables et résolution numérique fournies. **Au-delà :** premier problème de Stokes, série d’images et similitude de Blasius, avec discussion de transition laminaire.

## Mission 4 — Pression élevée : profondeur, vitesse ou pompe ?

**Laboratoires :** `hydrostatique`, `bernoulli`. **But :** distinguer un équilibre hydrostatique d’un bilan d’énergie dans un écoulement.

`z` est une altitude orientée vers le haut ; `p` est en Pa ; `ρ` en kg·m⁻³ ; `g` en m·s⁻² ; `Q` en m³·s⁻¹. La charge `H=p/(ρg)+z+αū²/(2g)` est une longueur en m. Dans le TP de gaz, `T` est une température absolue en K.

1. Prévoir comment la pression varie en profondeur dans un liquide et en altitude dans un gaz parfait isotherme. Retrouver respectivement une droite et une exponentielle ; identifier pourquoi ρ change dans le gaz.
2. Dans le Venturi idéal horizontal, augmenter la vitesse et prévoir le signe de `p2−p1`. Puis ajouter séparément altitude, pertes et pompe.
3. Calculer la puissance hydraulique à partir de la puissance électrique et du rendement. Vérifier `H2−H1=Hpompe−hpertes` avec les valeurs affichées.

**Trace attendue :** un schéma orienté, deux pressions calculées et une liste des hypothèses nécessaires à Bernoulli. La figure `hydrostatique.svg` propose aussi une surface libre en rotation dont la constante est fixée par le volume.

**Sup :** force de pression et équation d’état, selon parcours. **Spé :** conservation du débit et bilan entre sections. **Au-delà :** correction α, Colebrook, pertes singulières et Bernoulli instationnaire ; ces extensions restent distinctes du bilan idéal élémentaire.

## Mission 5 — Pourquoi un objet tombe, tourne ou reçoit une portance

**Laboratoires :** `sphere`, `vortex`, `magnus`. **But :** relier une résultante intégrale à une loi locale, puis identifier ce que le modèle ne peut pas prédire.

`R` est un rayon en m ; `η` en Pa·s ; `Γ` une circulation en m²·s⁻¹ ; `Ω` en rad·s⁻¹. Une force sur une sphère est en N. Le cylindre infini fournit une force **par longueur**, en N·m⁻¹.

1. Avec une sphère lente, prévoir la vitesse limite et la relaxation. Ajouter la poussée d’Archimède : l’accélération initiale n’est pas automatiquement `g`. Comparer Stokes à la corrélation à Reynolds fini sans extrapoler celle-ci au-delà de son domaine.
2. Dans Rankine, calculer la circulation d’un cercle intérieur puis extérieur au cœur. Vérifier la continuité de la vitesse et de la pression, alors que la vorticité change.
3. Pour le cylindre, choisir `U∞` vers `+x` et une circulation antihoraire. Prévoir le sens de la portance, puis comparer la résultante des pressions à `Fy′=−ρU∞Γ`. Inverser Γ : la force change de signe.

**Trace attendue :** une intégrale de circulation et une intégrale de force ; expliquer pourquoi la rotation d’un cylindre réel ne fixe pas Γ dans le seul problème parfait potentiel.

**Sup :** bilan des forces et équation du premier ordre. **Spé :** intégration de pression, Reynolds et coordonnées cylindriques selon filière. **Au-delà :** solution de Stokes, vortex de Rankine, topologie du potentiel et Kutta–Joukowski, tous accompagnés de leurs hypothèses.

## Mission 6 — La crête, le paquet et la particule voyagent-ils ensemble ?

**Laboratoire :** `houle`. **But :** distinguer phase, groupe et mouvement matériel d’une onde de surface.

`h` est la profondeur en m ; `k=2π/λ` le nombre d’onde en rad·m⁻¹ ; `ω` en rad·s⁻¹ ; `γ` la tension superficielle en N·m⁻¹ ; `a` l’amplitude de surface en m. Le modèle linéaire demande une amplitude petite devant les longueurs pertinentes.

1. En grandes longueurs d’onde et faible profondeur relative, prévoir `vφ≈vg≈√(gh)`.
2. En eau profonde et gravité dominante, montrer que `vg≈vφ/2`. Dans le régime capillaire profond, le rapport devient `3/2`. Utiliser `ω²=(gk+γk³/ρ)tanh(kh)` pour justifier ces limites.
3. Examiner les orbites selon la profondeur : elles deviennent elliptiques, avec déplacement vertical nul au fond. Une oscillation au premier ordre ne donne pas une dérive matérielle permanente.

**Trace attendue :** un tableau de trois limites, dérivé de la dispersion ; distinguer observation d’une crête et suivi d’un flotteur.

**Sup :** double périodicité et dérivation des puissances. **Spé :** vitesse de groupe et lecture de dispersion selon filière. **Au-delà :** dispersion gravito-capillaire, profondeur finie et dérive de Stokes d’ordre supérieur, absente de l’animation linéaire.

## Mission 7 — Un son transmis plus fort crée-t-il de l’énergie ?

**Laboratoires :** `acoustique`, `conduit`, `diffraction`, `thermo`. **But :** relier amplitudes, énergie et géométrie, en identifiant la bonne vitesse et la bonne échelle thermique.

`Z=ρc` est une impédance en Pa·s·m⁻¹ ; `f` est en Hz ; `λ=c/f` en m ; les indices `(m,n)` sont entiers. `Dth` est une diffusivité en m²·s⁻¹. Le rapport `γ=Cp/Cv` ne doit pas être confondu avec la tension superficielle de la mission précédente.

1. À une interface `Z2=4Z1`, prévoir le signe de la réflexion. Vérifier la continuité de pression et de vitesse normale ; calculer `rp=3/5`, `tp=8/5`, mais `R=9/25` et `T=16/25`. L’amplitude et le flux utilisent des normalisations différentes.
2. Dans le guide, partir du mode `(0,0)`, puis choisir un mode transverse. Calculer sa coupure et comparer phase/groupe au-dessus de celle-ci. Sous coupure, expliquer une décroissance sans l’interpréter comme une perte thermique.
3. Reprendre les ultrasons du recueil : λ=13,6 mm et fente de 10 mm. Prévoir un lobe large sans premier zéro ; lire la formule avec `sinθ`.
4. Comparer `cT=√(RT/M)` et `cS=√(γRT/M)`. Utiliser `δth=√(2Dth/ω)` pour comparer diffusion, longueur `1/k` et dimension du conduit ; ne pas inventer une interpolation entre les deux limites.

**Trace attendue :** bilan `R+T=1`, produit `vφvg=c²`, diagnostic de domaine angulaire et justification de l’hypothèse thermodynamique.

**Sup :** déphasage, sinus et équation d’état. **Spé :** linéarisation acoustique, impédance et thermodynamique selon filière. **Au-delà :** modes transverses, champ lointain et couches thermo-visqueuses ; l’échantillonnage stroboscopique fournit un prolongement de métrologie.

## Mission 8 — Faire confiance à un calcul grâce à un bilan indépendant

**Laboratoires :** `mhd`, `navier`. **But :** contrôler une solution exacte par l’équation et par une conservation, puis distinguer ce contrôle d’un résultat général de recherche.

Dans Hartmann, `h` est une **demi-hauteur**, `B` est en T, `σ` en S·m⁻¹, `Ha=Bh√(σ/η)` est sans dimension. Le circuit transverse fermé impose ici `Ez=0`. Dans Taylor–Green, `ν` est en m²·s⁻¹, `k=2π/L`, et l’énergie moyenne est en J·m⁻³.

1. À gradient de pression fixé, prévoir le freinage par B et la limite de Poiseuille à B=0. Vérifier `GQ=∫η(u′)²dy+∫j²/σ dy` et l’adhérence aux deux parois. Dire ce qui change si le circuit est ouvert.
2. Passer au modèle d’Alfvén : comparer les énergies cinétique et magnétique moyennes et la loi `vA=B0/√(μ0ρ)`. Les hypothèses de cette onde idéale diffèrent de celles du canal résistif.
3. Dans Taylor–Green, vérifier la divergence nulle et calculer le terme convectif. Le gradient de pression l’équilibre ; il ne disparaît pas. À ν=0, l’énergie reste constante ; à ν>0, `E=ρU0² exp(−4νk²t)/4` et sa dérivée oppose la dissipation.

**Trace attendue :** un bilan de puissance et une substitution dans une équation ; distinguer résidu numérique, exactitude dans un modèle et validité de ce modèle.

**Sup :** exponentielle, dérivée et bilan d’énergie. **Spé :** produit vectoriel, induction, analyse de champs et bilans selon filière. **Au-delà :** Hartmann, Alfvén et équations locales de Navier–Stokes. La solution particulière périodique 2D ne tranche pas la régularité générale 3D. Le [repère daté de Clay](https://www.claymath.org/news/navier-stokes-announcement/) et sa portée exacte figurent dans [ERRATA.md](ERRATA.md).

## Pour préparer un oral

Choisir une mission et présenter en cinq minutes une question, un schéma, trois variables, une prévision, un calcul et une limite. Un second candidat peut ensuite changer une hypothèse — deuxième paroi, circulation inversée, tube plus large, mode transverse, circuit ouvert — et demander quel résultat doit être recalculé. Les [seize illustrations autonomes](illustrations/README.md) peuvent accompagner cette présentation ; leurs légendes conservent les conventions nécessaires au raisonnement.
