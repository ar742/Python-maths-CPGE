# Physique statistique : sept séances CPGE

Le parcours utilise les thèmes des pages imprimées 434–442 du recueil de A. R. Les démarches, preuves et corrigés sont rédigés pour l’atelier ; le fichier personnel n’est pas reproduit. Chaque séance comporte une prédiction sur papier, une exploration, puis une justification. Compter 1 h 30 à 2 h par séance ; les dernières peuvent être divisées selon la filière et les connaissances acquises.

Les expressions « Sup », « Spé » et « extension » décrivent une progression. Les programmes réglementaires diffèrent selon les filières. Les modèles quantiques de gaz et la simulation d’Ising sont accompagnés d’hypothèses explicites. Un graphique numérique vérifie ou interroge une prédiction ; il ne prouve pas à lui seul un résultat infini.

## 1. Passer des microétats aux grandeurs thermiques

**Préparer :** comparer microétat, niveau d’énergie et macroétat ; normaliser les probabilités. Démontrer le poids de Boltzmann avec le développement de l’entropie d’un grand réservoir. Vérifier les signes dans `dS=dE/T+PdV/T−μdN/T`.

**Explorer :** dans le canonique, changer la dégénérescence du niveau intermédiaire ; distinguer sa population de celle d’un de ses microétats. Observer les limites chaudes et froides. Dans les spins, examiner une capacité Schottky et comparer aux deux niveaux `0,Δ`.

**Démontrer :** `U=−∂βlnZ`, `Var(E)=∂β²lnZ`, `C=Var(E)/(kBT²)`, et `S=kB(lnZ+βU)`. Utiliser Stirling sur `C(N,r)` pour relier les deux descriptions d’un ensemble de sites indépendants.

**Contrôle :** exercices 1 à 4. Le bilan doit expliquer le facteur 1/4 de Schottky, les dégénérescences et le sens d’un transfert de chaleur. Un pic de capacité d’un spectre fini ne suffit pas à qualifier une transition.

## 2. Reconnaître une limite classique

**Préparer :** réviser les intégrales de Gauss et l’équipartition. Écrire le Hamiltonien avant de compter les termes quadratiques. Retrouver les modes libres d’une boîte à partir du volet PQ.

**Explorer :** dans l’oscillateur, comparer `kBT≪hν` et `kBT≫hν`, le point zéro et la capacité. Dans le gaz cubique, varier taille, masse, température et coupure ; comparer les deux sommes et la limite `U/N=3kBT/2`.

**Démontrer :** la partition géométrique de l’oscillateur, `Z₁≈V/λth³`, le comptage continu `D(E)∝√E`, puis les expressions classiques `Z_N=Z₁ᴺ/N!`, `PV=NkBT` et `C_V=3NkB/2`.

**Contrôle :** exercices 5 à 8. Deux hypothèses doivent être séparées : spectre dense et faible dégénérescence statistique. Un écart `N_max→2N_max` est un diagnostic observé, sans être une borne absolue sur la queue restante.

## 3. Maxwell et pression : des chocs aux pascals

**Préparer :** transformer une gaussienne de vitesse vectorielle en distribution du module, avec le jacobien `4πv²`. Prévoir les dépendances en masse et température des trois vitesses caractéristiques.

**Explorer :** dans Maxwell, comparer vitesse la plus probable, moyenne et quadratique ; varier température et masse. Examiner les composantes de vitesse et le calcul cinétique de la pression. Si une illustration tirée au hasard est proposée, expliquer la différence entre dispersion physique et erreur d’échantillonnage.

**Démontrer :** `⟨v_z²⟩=kBT/m`, puis `P=2mn∫_{v_z>0}v_z²f(v)d³v=nkBT`. Le demi-espace incident, le flux `v_z` et l’impulsion `2mv_z` doivent apparaître séparément.

**Contrôle :** exercices 9 et 10. Le candidat doit dire pourquoi `⟨v_z⟩=0` ne signifie pas pression nulle, et pourquoi la masse disparaît de l’équation d’état à température fixée.

## 4. Effusion et échanges à travers une paroi poreuse

**Préparer :** préciser la condition d’un petit trou devant le libre parcours moyen. Calculer le flux de nombre `n⟨v⟩/4`. Distinguer température maintenue par un thermostat et refroidissement lors d’une fuite sans thermostat.

**Explorer :** dans l’effusion, prévoir l’influence de surface, masse et volume sur le temps de fuite. Comparer la distribution de vitesse intérieure à celle des particules sortantes. Étudier ensuite deux compartiments à températures différentes et suivre la relaxation des populations.

**Démontrer :** la loi exponentielle isotherme, l’énergie moyenne sortante `2kBT`, la relaxation vers `N₁,st`, puis `P₁/√T₁=P₂/√T₂`. Expliquer pourquoi la conservation instantanée de matière n’impose pas les flux stationnaires.

**Contrôle :** exercices 11 à 14. À températures inégales, la relation de transpiration thermique décrit un régime stationnaire maintenu, avec échange d’énergie ; elle ne constitue pas un équilibre thermique global. En extension, retrouver `T∝N^{1/3}` lors d’une effusion refroidissante idéale.

## 5. Gaz quantiques : Pauli et condensation

**Préparer :** sommer la partition d’un mode de bosons, puis celle d’un mode de fermions. Identifier un état complet, spin compris. Revoir la densité d’états 3D et la distinction entre occupation, population et dégénérescence.

**Explorer :** comparer BE/FD/MB au même potentiel chimique dans les occupations. Dans Fermi, remplir les états à `T=0`, puis suivre la détermination de `μ(T)` à nombre fixé. Dans Bose, refroidir un gaz uniforme et comparer population excitée et condensée.

**Démontrer :** les trois occupations et les fluctuations par mode ; `E_F=ℏ²(3π²n)^{2/3}/(2m)` pour le spin 1/2 ; `U/N=3E_F/5` et la pression à `T=0`. Déduire `T_c` du critère `nλth³=ζ(3/2)` et la fraction `1−(T/T_c)^{3/2}`.

**Contrôle :** exercices 15 à 19. La fraction au fondamental n’est pas 1 dès l’apparition de la condensation. Le facteur ζ porte la puissance 2/3. Les formules homogènes 3D ne sont pas transposées sans changement à un piège harmonique ou à une taille finie.

## 6. Corps noir et paramagnétisme : des modèles à leurs observables

**Préparer :** compter les photons avec deux polarisations et `μ=0`. Transformer un spectre en fréquence en spectre en longueur d’onde. Revoir le spin indépendant à deux niveaux.

**Explorer :** dans Planck, comparer au modèle Rayleigh–Jeans, repérer Wien et varier T pour Stefan–Boltzmann. Calculer une bande visible à 2500 K en annonçant ses bornes. Dans les spins, comparer la loi de Curie à la saturation et les limites `B→0`, `T→0`.

**Démontrer :** le jacobien `c/λ²`, le facteur π entre luminance et flux, la loi `σT⁴`, et l’expression de la fraction énergétique visible. Pour les spins, établir `m̄=μtanh(μB/kBT)` et relier susceptibilité et variance.

**Contrôle :** exercices 20 à 22. Le maximum dépend de la variable spectrale. Une fraction énergétique du visible n’est pas une efficacité visuelle pondérée. Le paramagnétisme sans interaction ne possède pas la transition du modèle d’Ising.

## 7. Ising : exact fini, exact infini et simulation

**Préparer :** compter les parois d’une chaîne périodique. Énumérer à la main les niveaux pour quatre spins et leur dégénérescence. Expliquer pourquoi le nombre de parois est pair.

**Explorer :** en chaîne, comparer niveau choisi, partition exacte et approximation de Stirling. Varier N et T sans confondre un pic avec une transition. Sur le carré, comparer référence Onsager/Yang et simulation Metropolis ; changer taille, durée, graine et initialisation. Séparer mise en équilibre et mesures, et observer les fluctuations corrélées.

**Démontrer :** `g_q=2C(N,2q)`, `E_q=−JN+4Jq`, puis `Z_N=(2coshβJ)ᴺ+(2sinhβJ)ᴺ`. Pour la chaîne infinie à T>0, discuter la décroissance des corrélations. Sur le carré, annoncer `θ_c=2/ln(1+√2)` comme résultat exact de référence, et expliquer l’ordre des limites définissant l’aimantation spontanée.

**Contrôle :** exercices 23 et 24. Le compte rendu doit identifier ce qui est démontré par comptage, ce qui est une référence exacte dans la limite thermodynamique et ce qui est estimé par simulation. `⟨m⟩`, `⟨|m|⟩` et `m_sp` ne sont pas interchangeables ; un faible bruit visuel ne garantit pas des échantillons indépendants.

## Oral de synthèse

Préparer cinq minutes sur un laboratoire : hypothèses, unités, prédiction, contrôle numérique et limite de validité. Question complémentaire au choix : « Pourquoi une pression subsiste à T=0 ? », « Pourquoi le faisceau effusif est-il plus énergétique ? », « Quel signe impose le deuxième principe ? », « Que mesure une occupation ? », « Pourquoi un maximum change-t-il avec la variable ? », « Quand une simulation finie permet-elle d’approcher un résultat infini ? ».

Une bonne réponse relie la formule à une observable, sait en donner une justification et évite de conclure au-delà du modèle annoncé.
