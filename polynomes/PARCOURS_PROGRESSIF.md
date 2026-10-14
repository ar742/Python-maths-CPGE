# Parcours progressif sup / spé — Polynômes & Géométrie

Commencer par les techniques de calcul et de preuve, puis choisir les prolongements qui donnent envie d’aller plus loin. Les vingt laboratoires du plan complexe et des polynômes multivariés sont reliés ici à des séances concrètes.

**5 séances de sup · 3 séances de spé · 2 approfondissements · 4 pistes au-delà.**

Prévoir 60 à 90 minutes pour chacune des premières séances, corrigé compris. Les compléments et les branches au-delà du programme peuvent être répartis sur plusieurs séances et choisis indépendamment.

Les repères sont ceux des programmes MPSI et MP. « Socle » désigne les techniques à maîtriser, pas la totalité du laboratoire ni tous ses théorèmes. Les exemples sont accompagnés : une formule fournie peut servir à exercer une technique du programme sans devenir un résultat à mémoriser. Les identités générales de Newton, le réciproque conjugué, Gauss–Lucas et Rouché ne sont pas présentés comme des obligations supplémentaires en MPSI/MP.

[Ouvrir le parcours dans l’atelier local](http://127.0.0.1:8784/#parcours) · [Guide de lancement](LISEZ_MOI.md) · [18 séances pour les 36 TP](PARCOURS.md)

## Trois catégories

- **Techniques incontournables :** priorité aux outils du programme. Les limites indiquent les parties facultatives du TP.
- **Approfondissement accessible CPGE :** exercice guidé utilisant ces outils ; les définitions et formules nouvelles sont fournies.
- **Au-delà du programme :** théorèmes ou méthodes nouveaux, à choisir après le socle.

## Avant de commencer

- Sup : opérations sur les complexes, module et conjugaison, racines de l’unité, sommes géométriques et formule du binôme.
- Sup : degré, division, factorisation, racines et multiplicité d’un polynôme; relations de Viète pour la somme et le produit.
- Sup : suites récurrentes, dérivation et étude d’une fonction réelle; aucune connaissance préalable des bases de Gröbner ou de la géométrie projective.
- Spé : développements limités, théorème spectral pour les matrices symétriques, calcul différentiel et optimisation sous une contrainte régulière.

## Pour chaque séance

1. Lire le but, les objets et les hypothèses du laboratoire avant de déplacer un réglage.
2. Prévoir un signe, un degré, une racine ou une borne sur papier, puis lancer l’expérience.
3. Faire varier un seul paramètre et justifier le changement par une identité ou une inégalité.
4. Terminer par un exercice corrigé et une phrase distinguant ce qui est prouvé de ce qui est seulement observé.

## Sup : cinq séances pour construire le socle

Les complexes et les polynômes servent d’abord à calculer, factoriser et contrôler les hypothèses. Les dessins soutiennent des arguments élémentaires.

### 1. Une somme géométrique et ses racines

**Techniques incontournables** · Sup · complexes et polynômes

Utiliser une somme géométrique, les racines de l’unité et le coefficient dominant pour obtenir une factorisation complète.

**À faire :** Prendre le degré n=3, le centre complexe c=−1 et le rayon réel r=2. Pour l’indéterminée Z, factoriser P(Z)=1+(Z+1)/2+((Z+1)/2)²+((Z+1)/2)³, puis situer ses racines sur le cercle.

**Acquis attendu :** Exclure le candidat Z=1, conserver le coefficient dominant 1/8 et retrouver le produit des racines −15.

**Limites et compléments :** Le transport affine des racines est un exercice. Il n’ajoute aucun théorème de géométrie complexe à apprendre.

**TP et cours associés**

- **Une somme géométrique dessine un cercle** — [35. La somme géométrique fournit les racines](COURS.md#35-la-somme-géométrique-fournit-les-racines) · [36. Le cercle ne détermine pas le coefficient dominant](COURS.md#36-le-cercle-ne-détermine-pas-le-coefficient-dominant)

### 2. Du cercle unité aux tangentes

**Techniques incontournables** · Sup · binôme, factorisation et Viète

Combiner changement de variable, développement binomial et comparaison des coefficients sans perdre un candidat interdit.

**À faire :** Pour l’indéterminée Z, développer P₂(Z)=(Z+1)⁴−(Z−1)⁴. Retrouver ses racines avec le changement de variable fourni dans le TP, puis prévoir la somme et le produit des tangentes non nulles.

**Acquis attendu :** Obtenir P₂=8Z(Z−i)(Z+i), expliquer pourquoi le degré est 3 et pourquoi le candidat associé à une division par zéro est exclu.

**Limites et compléments :** La formule de changement de variable est fournie. Le nom « transformation de Cayley » et son interprétation projective ne sont pas des connaissances obligatoires.

**TP et cours associés**

- **Racines de l’unité et sommes de tangentes** — [33. Une substitution avec un point interdit](COURS.md#33-une-substitution-avec-un-point-interdit) · [34. Lire une somme et un produit dans les coefficients](COURS.md#34-lire-une-somme-et-un-produit-dans-les-coefficients)

### 3. Passer des racines aux coefficients

**Techniques incontournables** · Sup · somme, produit et développement

Maîtriser les relations de Viète pour la somme et le produit, puis retrouver les autres coefficients par développement.

**À faire :** Dans le TP symétrique, choisir les trois racines réelles u=−1, v=1, w=2 et reconstruire le polynôme. Permuter ces racines. Dans le TP complexe, garder les coefficients par défaut et prévoir la somme et le produit des six racines.

**Acquis attendu :** Retrouver les mêmes coefficients après permutation; justifier la somme nulle et le produit 0,5−0,8i des six racines complexes, sans les calculer.

**Limites et compléments :** À ce palier, travailler surtout somme et produit. Les autres relations se retrouvent par développement; les identités générales de Newton et le théorème fondamental des polynômes symétriques ne sont pas exigés.

**TP et cours associés**

- **Viète et Newton avec des coefficients complexes** — [45. Les premières identités de Newton](COURS.md#45-les-premières-identités-de-newton) · [46. Après le degré : une récurrence et un lien aux traces](COURS.md#46-après-le-degré--une-récurrence-et-un-lien-aux-traces)
- **Trois racines, trois coefficients symétriques** — [61. Newton retrouve les puissances à partir des coefficients](COURS.md#61-newton-retrouve-les-puissances-à-partir-des-coefficients) · [62. Le discriminant décrit les collisions de racines](COURS.md#62-le-discriminant-décrit-les-collisions-de-racines)

### 4. Deux variables : lire les degrés, puis substituer

**Techniques incontournables** · Sup · introduction guidée aux polynômes multivariés

Reconnaître les monômes de deux indéterminées et résoudre un système par substitution, sans supposer une théorie multivariée préalable.

**À faire :** Pour les indéterminées x,y, lire les degrés de P(x,y)=x⁴+x²y³+y⁴+1. Puis chercher les points réels communs au cercle x²+y²=1 et à la parabole y=x²−9/8 en remplaçant y dans la première équation.

**Acquis attendu :** Distinguer le degré total 5 des deux degrés partiels 4; obtenir un quartique en x, poser t=x² et vérifier quels candidats donnent quatre points réels.

**Limites et compléments :** La théorie de K[X] du programme porte sur une indéterminée. Les deux variables servent ici d’introduction par calcul et substitution. Le polygone de Newton, Bézout projectif et les multiplicités d’intersection sont des prolongements.

**TP et cours associés**

- **Lire les monômes dans un plan d’exposants** — [53. Trois notions de degré à séparer](COURS.md#53-trois-notions-de-degré-à-séparer) · [54. Support et spécialisation : ce que le dessin permet](COURS.md#54-support-et-spécialisation--ce-que-le-dessin-permet)
- **Un cercle et une parabole : où sont les quatre intersections ?** — [55. Éliminer une variable avant de dessiner](COURS.md#55-éliminer-une-variable-avant-de-dessiner) · [56. Bézout : compter au bon endroit et avec multiplicité](COURS.md#56-bézout--compter-au-bon-endroit-et-avec-multiplicité)

### 5. Une récurrence avec ses données initiales

**Techniques incontournables** · Sup · suites et calcul polynomial

Utiliser une récurrence et ses deux valeurs initiales; distinguer les racines d’un polynôme des racines caractéristiques au point où on l’évalue.

**À faire :** Reprendre la famille source : P₀(Z)=1, P₁(Z)=2Z et Pₖ₊₂(Z)=−ZPₖ₊₁(Z)−Pₖ(Z), où Z est l’indéterminée et k un rang entier. Calculer P₂ et P₃, puis vérifier P₈(2) par la récurrence.

**Acquis attendu :** Obtenir P₂=−2Z²−1, P₃=2Z³−Z et P₈(2)=−39; expliquer pourquoi changer les valeurs initiales change la famille.

**Limites et compléments :** Cette famille est une application guidée, pas une famille de polynômes à mémoriser. Le cas caractéristique double et la rotation des coefficients complexes peuvent être repris dans un second temps.

**TP et cours associés**

- **Une récurrence, deux racines caractéristiques** — [51. Résoudre à un point complexe fixé](COURS.md#51-résoudre-à-un-point-complexe-fixé) · [52. Le cas double et les coefficients complexes](COURS.md#52-le-cas-double-et-les-coefficients-complexes)

## Spé : trois séances pour organiser une preuve

Priorité aux inégalités, au théorème spectral et aux extrema sous contrainte. Chaque séance sépare les techniques du programme des résultats complémentaires fournis.

### 6. Encadrer sans résoudre

**Techniques incontournables** · Spé · inégalités et étude d’une fonction

Transformer une égalité complexe en une inégalité réelle, puis exploiter une fonction monotone pour localiser les racines.

**À faire :** Garder le polynôme complexe par défaut. Noter α une de ses racines et ρ le rayon calculé à partir des coefficients. À l’aide de l’inégalité triangulaire et de l’équation réelle définissant ρ, démontrer |α|≤ρ.

**Acquis attendu :** Justifier la monotonie et les limites de la fonction utilisée; distinguer une borne valable pour chaque racine d’une borne sur le plus grand module.

**Limites et compléments :** Le socle est la technique d’inégalité et d’étude de fonction. La formule de la borne de Cauchy est fournie et n’est pas présentée comme un résultat du programme à mémoriser; le second encadrement peut rester facultatif.

**TP et cours associés**

- **Six racines et une borne de Cauchy** — [37. Une équation réelle localise les racines complexes](COURS.md#37-une-équation-réelle-localise-les-racines-complexes) · [38. Une borne inférieure du plus grand module](COURS.md#38-une-borne-inférieure-du-plus-grand-module)

### 7. Une forme en trois variables et sa matrice

**Techniques incontournables** · Spé · théorème spectral et calcul différentiel

Relier une expression quadratique à sa matrice symétrique, à ses valeurs propres et à sa hessienne; ne pas conclure à partir d’une seule tranche.

**À faire :** Prendre Q(x,y,z)=x²+y²+2z²+xy+yz pour trois variables réelles x,y,z. Écrire sa matrice symétrique, prouver sa positivité par complétion des carrés et comparer aux trois valeurs propres affichées.

**Acquis attendu :** Retrouver les demi-coefficients des termes croisés dans la matrice, la hessienne égale au double de cette matrice et une justification globale de la positivité.

**Limites et compléments :** Le théorème spectral et la positivité des matrices symétriques appartiennent au socle de MP. Le critère de Sylvester est présenté comme un complément, sans obligation de le mémoriser.

**TP et cours associés**

- **Une forme quadratique en trois variables** — [67. La matrice symétrique et ses valeurs propres](COURS.md#67-la-matrice-symétrique-et-ses-valeurs-propres) · [68. Sylvester et complétion des carrés](COURS.md#68-sylvester-et-complétion-des-carrés)

### 8. Un quartique sur un cercle

**Techniques incontournables** · Spé · extrema sous une contrainte

Relier existence des extrema, condition nécessaire de Lagrange et comparaison globale par un paramétrage.

**À faire :** Optimiser f(x,y)=x⁴+y⁴+xy sur le cercle x²+y²=1. Paramétrer x=cosθ, y=sinθ, où θ est un angle réel, puis comparer les candidats avec ceux de la méthode de Lagrange.

**Acquis attendu :** Vérifier que la contrainte est régulière, trouver les huit points stationnaires et justifier le minimum 0 et le maximum 9/8; ne pas confondre stationnaire et extremum.

**Limites et compléments :** L’optimisation sous une contrainte régulière est au programme MP. La fusion de points stationnaires au seuil et le développement d’ordre 4 sont des approfondissements facultatifs.

**TP et cours associés**

- **Optimiser un quartique sur un cercle** — [71. Le cercle rend les deux méthodes équivalentes](COURS.md#71-le-cercle-rend-les-deux-méthodes-équivalentes) · [72. Une parabole donne les bornes globales](COURS.md#72-une-parabole-donne-les-bornes-globales)

## Compléments accessibles : définitions et formules fournies

Ces deux séances utilisent les outils de sup et de spé. Elles n’ajoutent pas de théorèmes obligatoires au programme.

### 9. Retourner les coefficients et calculer les puissances

**Approfondissement accessible CPGE** · Sup / Spé · algèbre guidée

Appliquer une définition de réciproque conjugué en surveillant le degré, puis utiliser les identités de Newton pour calculer sans résoudre.

**À faire :** Dans le premier TP, rendre la racine mobile nulle et expliquer la perte de degré. Dans le second, noter s₄ la somme des quatrièmes puissances des six racines et retrouver s₄=−4 pour les coefficients par défaut, avec l’identité fournie.

**Acquis attendu :** Traiter séparément zéro, conserver la convention de degré lors du double retournement et calculer une somme de puissances à partir des coefficients.

**Limites et compléments :** Le réciproque conjugué et les identités générales de Newton sont des compléments fournis. Ils ne doivent pas être présentés comme des résultats obligatoires en MPSI/MP.

**TP et cours associés**

- **Réciproque conjugué et cercle unité** — [43. Conjuguer puis retourner les coefficients](COURS.md#43-conjuguer-puis-retourner-les-coefficients) · [44. Une racine nulle change le degré effectif](COURS.md#44-une-racine-nulle-change-le-degré-effectif)
- **Viète et Newton avec des coefficients complexes** — [45. Les premières identités de Newton](COURS.md#45-les-premières-identités-de-newton) · [46. Après le degré : une récurrence et un lien aux traces](COURS.md#46-après-le-degré--une-récurrence-et-un-lien-aux-traces)

### 10. Racines proches et perturbation complexe

**Approfondissement accessible CPGE** · Spé · racines carrées et développements limités

Comparer une formule exacte, une approximation au premier ordre et un calcul numérique au voisinage d’une racine double.

**À faire :** Noter δ la demi-distance initiale des deux racines mobiles et ε le module de la perturbation. Fixer ε=10⁻⁸, comparer δ=0,4 puis δ=0 et expliquer le passage d’un déplacement presque linéaire à un déplacement de taille √ε.

**Acquis attendu :** Vérifier l’hypothèse ε≪δ² avant d’utiliser ε/(2δ); retrouver le déplacement 10⁻⁴ pour la racine double et distinguer résidu et erreur de position.

**Limites et compléments :** Les racines carrées et les développements limités sont des outils CPGE; le conditionnement numérique est expliqué comme une application complémentaire. La perturbation agit sur le facteur quadratique, pas sur une constante ajoutée au polynôme entier.

**TP et cours associés**

- **Deux racines proches amplifient une perturbation** — [49. L’échelle qui contrôle le premier ordre](COURS.md#49-léchelle-qui-contrôle-le-premier-ordre) · [50. Une racine double ne répond plus linéairement](COURS.md#50-une-racine-double-ne-répond-plus-linéairement)

## Au-delà : quatre branches au choix

Ces branches explorent des résultats hors du programme. Les définitions et preuves nécessaires sont apportées par les laboratoires; leur étude est facultative.

### A. Géométrie, comptage et dynamique complexe

**Au-delà du programme** · Au-delà · après les complexes et la dérivation

Passer d’une preuve algébrique de localisation à un certificat de comptage, puis à une expérience de convergence dans le plan complexe.

**À faire :** Dans Gauss–Lucas, expliquer les poids positifs d’une racine de la dérivée. Dans Rouché, certifier deux puis cinq racines avec les exemples proposés. Dans les bassins de Newton, réduire le nombre d’itérations et examiner la catégorie « Non classé ».

**Acquis attendu :** Distinguer les trois conclusions : appartenance à une enveloppe convexe, nombre de racines certifié sur un disque et classement numérique après un calcul fini.

**Limites et compléments :** Gauss–Lucas, Rouché et les bassins de Newton complexes sont hors du programme. Une carte ou une courbe échantillonnée ne remplace ni la preuve ni l’hypothèse stricte sur tout le cercle.

**TP et cours associés**

- **La dérivée reste dans l’enveloppe convexe** — [41. L’identité qui remplace Rolle dans le plan](COURS.md#41-lidentité-qui-remplace-rolle-dans-le-plan) · [42. L’enveloppe convexe contient les racines de la dérivée](COURS.md#42-lenveloppe-convexe-contient-les-racines-de-la-dérivée)
- **Compter les racines dans un disque** — [39. Rouché : une hypothèse stricte sur tout le bord](COURS.md#39-rouché--une-hypothèse-stricte-sur-tout-le-bord) · [40. Un critère suffisant peut ne pas conclure](COURS.md#40-un-critère-suffisant-peut-ne-pas-conclure)
- **Quatre racines, quatre bassins de Newton** — [47. Pourquoi une racine simple attire localement](COURS.md#47-pourquoi-une-racine-simple-attire-localement) · [48. Le dessin possède une catégorie non classée](COURS.md#48-le-dessin-possède-une-catégorie-non-classée)

### B. Élimination, ordre des monômes et autres cartes

**Au-delà du programme** · Au-delà · après substitutions et déterminants

Éliminer une variable sans accepter de solution fictive, contrôler des divisions exactes et comprendre comment un changement de carte représente un point à l’infini.

**À faire :** Pour les réglages par défaut du résultant, vérifier puis rejeter le candidat x=0. Dans Gröbner, changer l’ordre des monômes et contrôler les restes nuls. Dans l’homogénéisation de la parabole, montrer comment son point à l’infini devient l’origine dans une autre carte.

**Acquis attendu :** Revenir aux équations initiales après élimination, distinguer ordre de calcul et ensemble de solutions, puis vérifier les substitutions entre les deux cartes.

**Limites et compléments :** Résultants, bases de Gröbner, idéaux et géométrie projective sont des prolongements. Les calculs réutilisent déterminants et substitutions, mais les théories nouvelles ne sont pas exigibles au titre du socle MPSI/MP.

**TP et cours associés**

- **Éliminer y, puis vérifier chaque candidat** — [57. Un déterminant qui élimine y](COURS.md#57-un-déterminant-qui-élimine-y) · [58. Le candidat parasite vient d’une chute de degré](COURS.md#58-le-candidat-parasite-vient-dune-chute-de-degré)
- **Changer l’ordre des monômes, conserver les solutions** — [59. L’ordre lexicographique expose une substitution](COURS.md#59-lordre-lexicographique-expose-une-substitution) · [60. Trois divisions au lieu de deux : le critère qui certifie](COURS.md#60-trois-divisions-au-lieu-de-deux--le-critère-qui-certifie)
- **Voir un point à l’infini dans une autre carte** — [65. Tous les monômes doivent avoir le même degré](COURS.md#65-tous-les-monômes-doivent-avoir-le-même-degré) · [66. Une deuxième carte explique le point à l’infini](COURS.md#66-une-deuxième-carte-explique-le-point-à-linfini)

### C. Un gradient nul, trois géométries

**Au-delà du programme** · Au-delà · après calcul différentiel et étude locale

Comprendre qu’une singularité de courbe exige à la fois l’équation de la courbe et l’annulation de son gradient.

**À faire :** Pour F(x,y)=y²−x³−tx², où x,y sont réels et t un paramètre, comparer t=1, t=0 puis t=−1. Calculer le gradient et lire les tangentes à partir des termes de plus bas degré.

**Acquis attendu :** Écarter les points où seul le gradient s’annule; distinguer deux tangentes, une tangente double et un point réel isolé.

**Limites et compléments :** Le calcul du gradient est un outil de spé; la classification en nœud, pointe et point isolé relève d’un prolongement sur les courbes algébriques.

**TP et cours associés**

- **Nœud, pointe ou point isolé ?** — [63. Le gradient seul ne classe pas une singularité](COURS.md#63-le-gradient-seul-ne-classe-pas-une-singularité) · [64. Trois signes, trois dessins](COURS.md#64-trois-signes-trois-dessins)

### D. Non négatif ne signifie pas somme de carrés

**Au-delà du programme** · Au-delà · après inégalités et comparaison des coefficients

Prouver un signe sur tout le plan, puis découvrir pourquoi le résultat des formes quadratiques ne s’étend pas automatiquement aux degrés supérieurs.

**À faire :** Noter λ le coefficient du TP. Pour λ=3, prouver la non-négativité par l’inégalité arithmético-géométrique et trouver les quatre zéros. Pour λ=4, calculer le minimum global, puis suivre la preuve par coefficients qui interdit une somme de carrés polynomiaux.

**Acquis attendu :** Séparer trois propriétés : valeur minimale, non-négativité partout et représentation comme somme de carrés de polynômes; justifier chaque conclusion sans se fonder sur les pixels.

**Limites et compléments :** Le contre-exemple de Motzkin et la théorie des sommes de carrés sont hors du programme. La preuve fournie réinvestit des inégalités et des coefficients accessibles en CPGE; elle ne concerne pas les carrés de fractions rationnelles.

**TP et cours associés**

- **Positif ne signifie pas somme de carrés** — [69. Un minimum global démontré sur tout ℝ²](COURS.md#69-un-minimum-global-démontré-sur-tout-ℝ²) · [70. Le coefficient négatif interdit toute somme de carrés](COURS.md#70-le-coefficient-négatif-interdit-toute-somme-de-carrés)

## Repères de programme

- [Programme officiel de mathématiques MPSI](https://prepas.org/ups.php?document=69)
- [Programme officiel de mathématiques MP](https://prepas.org/ups.php?document=85)
