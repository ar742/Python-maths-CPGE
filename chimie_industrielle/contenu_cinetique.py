"""Cinétique : huit TP, seize leçons et vingt-quatre TD corrigés."""
GUIDES = {}
LESSONS = []
EXERCISES = []


def guide(ident, purpose, objects, hypotheses, techniques, sup, spe, beyond, steps, expected):
    GUIDES[ident] = dict(purpose=purpose, objects=objects, hypotheses=hypotheses,
        techniques=techniques, levels=dict(sup=sup, spe=spe, beyond=beyond),
        first_steps=steps, expected=expected)


def lesson(ident, title, level, content):
    LESSONS.append(dict(lab=ident, title=title, level=level, html=content))


def exercise(ident, title, level, question, answer):
    EXERCISES.append(dict(lab=ident, title=title, level=level, question=question, answer=answer))


guide('horloge_iode',
    'Exploiter les six mesures du TP p.546 pour comparer des lois de vitesse. Comprendre ce qui est mesuré et ce qui dépend du modèle choisi.',
    ['t est le temps en secondes ; V est le volume cumulé de thiosulfate associé aux seuils colorés, en mL.',
     'V∞ est le volume final supposé. La fraction de peroxyde restante est modélisée par y=1−V/V∞.',
     'κ est un coefficient normalisé, en s⁻¹. L’erreur comparée est la moyenne des carrés des écarts de volume, en mL².'],
    ['Les six couples (t,V) du recueil sont conservés ; V(0)=0 est imposé.',
     'La relation entre volume et concentration est admise ; la dilution à chaque ajout n’est pas calculée.',
     'La concentration d’iodure et l’acidité sont considérées presque constantes.'],
    ['Identifier une grandeur indirectement mesurée', 'Intégrer les lois d’ordres 0, 1 et 2', 'Comparer les résidus dans la même unité'],
    'Sup : avancement, vitesse, ordre apparent et temps de demi-réaction.',
    'Spé : discuter un ajustement et les conditions de dégénérescence de l’ordre.',
    'Identification de paramètres et incertitude expérimentale : les six points ne fournissent pas tous les ordres partiels.',
    ['Garder V∞=10 mL et repérer V=5 mL à t=315 s.',
     'Comparer les trois courbes et les trois erreurs calculées sur V.',
     'Choisir V∞=12 mL : expliquer pourquoi l’ajustement change alors que les mesures restent identiques.'],
    'Une droite obtenue après transformation suggère une loi ; la conclusion dépend aussi du modèle de mesure.')

lesson('horloge_iode', 'Une coloration mesure un avancement', 'Sup · TP du recueil p.546',
    '<p>On note t le temps, V le volume cumulé associé aux seuils de coloration et V∞ son asymptote supposée. L’atelier reprend six couples : t=50,100,170,230,315,410 s et V=1,2,3,4,5,6 mL.</p>'
    '<p>Le diiode formé est consommé rapidement par le thiosulfate. Les ions iodure sont ainsi régénérés ; lorsque le thiosulfate ajouté est épuisé, le diiode colore l’amidon. Le seuil traduit donc une quantité formée, pas une mesure instantanée de vitesse.</p>'
    '<div class="formula">H₂O₂+2I⁻+2H⁺ → I₂+2H₂O ; I₂+2S₂O₃²⁻ → 2I⁻+S₄O₆²⁻.</div>'
    '<p>Dans le modèle, la fraction restante y=c(t)/c₀ vaut 1−V/V∞, où c₀ est la concentration initiale du réactif suivi. Avec V∞=10 mL, V=5 mL donne y=1/2 : le temps de demi-réaction observé est 315 s.</p>')

lesson('horloge_iode', 'Comparer des lois, pas des axes différents', 'Sup / Spé · identification d’un ordre apparent',
    '<p>On note y=c/c₀ la concentration réduite et κ le coefficient normalisé. Les modèles d’ordres 0, 1 et 2 donnent respectivement y=max(1−κt,0), y=exp(−κt) et y=1/(1+κt). Leurs transformations linéaires sont 1−y, −ln y et 1/y−1.</p>'
    '<p>Pour des mesures tᵢ et une transformation zᵢ, l’ajustement passant par l’origine donne κ=Σtᵢzᵢ/Σtᵢ². Chaque courbe est ensuite reconvertie en volume : on compare Σ(Vprévu−Vmesuré)²/6. Comparer les erreurs des trois axes transformés n’aurait pas la même signification.</p>'
    '<p>Avec V∞=10 mL, l’ordre 1 est le meilleur des trois modèles testés : κ≈2,2115×10⁻³ s⁻¹ et t½ ajusté≈313,43 s. Pour les ordres 0 et 2, κ vaut k/c₀ et kc₀ respectivement : son unité normalisée ne donne pas celle de k.</p>'
    '<p>Une seule série où iodure et acidité sont presque constants ne permet pas d’identifier séparément leurs ordres partiels. Il faudrait des séries supplémentaires où ces concentrations varient.</p>')

exercise('horloge_iode', 'Un seuil et une vitesse moyenne', 'Sup',
    '<p>On suppose V∞=10 mL et y=1−V/V∞. Le volume passe de 4 à 5 mL entre 230 et 315 s. Calculer la vitesse moyenne de consommation de la fraction y et le temps de demi-réaction observé.</p>',
    '<p>y passe de 0,6 à 0,5. La vitesse moyenne −Δy/Δt vaut 0,1/85≈1,1765×10⁻³ s⁻¹. Le seuil y=0,5 est atteint à 315 s : c’est t½ observé. Cette moyenne sur 85 s n’est pas une dérivée instantanée.</p>')
exercise('horloge_iode', 'Le coefficient dépend de la normalisation', 'Sup / Spé',
    '<p>Une réaction suit −dc/dt=kc², avec c en mol·L⁻¹. Poser y=c/c₀ et déterminer la relation entre k et le coefficient κ du modèle y=1/(1+κt). Préciser les unités.</p>',
    '<p>dy/dt=−kc₀y². Après intégration, 1/y−1=kc₀t ; κ=kc₀. Ainsi κ est en s⁻¹, tandis que k est en L·mol⁻¹·s⁻¹. Deux expériences ayant des concentrations initiales différentes peuvent avoir le même k mais des κ différents.</p>')
exercise('horloge_iode', 'Ce que l’horloge ne détermine pas', 'Spé · analyse de données',
    '<p>La loi proposée est v=k[H₂O₂]ᵃ[I⁻]ᵇ[H⁺]ᶜ. Iodure et acidité restent presque constants dans une série. Si l’ajustement indique a≈1, peut-on en déduire b et c ? Comment les étudier ?</p>',
    '<p>Non. La série mesure kappa=k[I⁻]ᵇ[H⁺]ᶜ lorsque a=1 ; elle ne sépare pas les trois facteurs. Pour b, comparer plusieurs séries à acidité fixée en faisant varier [I⁻] : ln(kappa₂/kappa₁)=b ln([I⁻]₂/[I⁻]₁), si le mécanisme reste le même. Faire de même pour c à iodure fixé. Le résultat porte sur les conditions explorées.</p>')


guide('arrhenius_catalyse',
    'Relier une variation de température à une constante cinétique, puis distinguer accélération et déplacement d’équilibre.',
    ['T est la température absolue en K ; Ea l’énergie d’activation, affichée en kJ·mol⁻¹ et convertie en J·mol⁻¹ dans l’exponentielle.',
     'R=8,314462618 J·mol⁻¹·K⁻¹ est la constante des gaz parfaits. La référence sans catalyse est kref=0,01 s⁻¹ à Tref=500 K.',
     'ΔEa est l’abaissement de la barrière ; les deux voies partagent le même préfacteur. Leur enthalpie de réaction illustrative vaut −40 kJ·mol⁻¹.'],
    ['Loi d’Arrhénius avec préfacteur indépendant de T sur l’intervalle étudié.',
     'Le profil énergétique est un schéma, sans calcul d’état de transition ni mécanisme industriel identifié.'],
    ['Rapport de constantes par Arrhénius', 'Lecture d’une pente logarithmique', 'Distinguer énergie d’activation et enthalpie de réaction'],
    'Sup : influence de T, catalyse et constante de vitesse.',
    'Spé : exploiter une énergie apparente et distinguer cinétique et thermodynamique.',
    'Le modèle représente une comparaison de voies ; l’activité d’un matériau réel peut aussi dépendre de l’adsorption et du transport.',
    ['À 500 K, vérifier k=0,01 s⁻¹ sans catalyse.',
     'Abaisser la barrière de 20 kJ·mol⁻¹ et prévoir le facteur exp(ΔEa/RT).',
     'Passer à 750 K : comparer les vitesses et le facteur relatif d’accélération.'],
    'Une barrière plus faible accélère la transformation ; les états initial et final restent les mêmes.')

lesson('arrhenius_catalyse', 'Arrhénius : calculer avant de chauffer le modèle', 'Sup · fiche C6 p.548',
    '<p>On note T la température en K, Ea l’énergie d’activation en J·mol⁻¹ et R la constante des gaz parfaits. Pour une constante cinétique k(T)=A exp(−Ea/RT), le préfacteur A a la même unité que k.</p>'
    '<div class="formula">ln[k(T₂)/k(T₁)]=(Ea/R)(1/T₁−1/T₂).</div>'
    '<p>Le TP utilise k(500 K)=0,01 s⁻¹, puis choisit Ea. Changer Ea conserve cette référence et ajuste donc A. Avec Ea=80 kJ·mol⁻¹, passer de 500 à 600 K multiplie k par environ 24,711 : k(600 K)≈0,24711 s⁻¹.</p>'
    '<p>Pour déterminer Ea à partir de mesures, représenter ln k en fonction de 1/T : la pente vaut −Ea/R. Les températures en degrés Celsius doivent être converties avant ce calcul.</p>')

lesson('arrhenius_catalyse', 'Le catalyseur change le chemin', 'Sup / Spé · vitesse et équilibre',
    '<p>On note ΔEa la diminution de la barrière, en J·mol⁻¹. À température fixée, si le préfacteur est le même pour les deux voies, kcat/k=exp(ΔEa/RT). À 500 K, un abaissement de 20 kJ·mol⁻¹ donne un facteur environ 122,84.</p>'
    '<p>Le profil dessiné relie les mêmes réactifs et produits : leur différence d’énergie, ici choisie égale à −40 kJ·mol⁻¹, ne change pas. L’énergie d’activation mesure une barrière ; l’enthalpie de réaction mesure une différence entre états.</p>'
    '<p>Un catalyseur ouvre une voie pour l’aller et le retour. À T fixée, il ne modifie pas la constante d’équilibre. Il peut aider un procédé à atteindre plus vite sa conversion thermodynamiquement accessible ; il ne garantit pas un rendement particulier.</p>'
    '<p>Adsorption, sélectivité, désactivation et diffusion dans le grain sont des questions distinctes, étudiées dans les autres laboratoires.</p>')

exercise('arrhenius_catalyse', 'Une référence et une deuxième température', 'Sup',
    '<p>Une constante du premier ordre vaut 0,01 s⁻¹ à 500 K. Avec Ea=80 kJ·mol⁻¹, calculer k à 600 K et le temps de demi-réaction.</p>',
    '<p>k₂=0,01 exp[(80000/R)(1/500−1/600)]≈0,24711 s⁻¹. Pour le premier ordre, t½=ln2/k₂≈2,805 s. À 500 K il vaut 69,315 s. L’énergie est convertie en joules pour être cohérente avec R.</p>')
exercise('arrhenius_catalyse', 'Un gain de barrière, pas un gain d’équilibre', 'Sup / Spé',
    '<p>À 500 K, la barrière passe de 80 à 60 kJ·mol⁻¹ avec le même préfacteur. Calculer le facteur d’accélération puis dire ce qu’il permet de conclure sur la constante d’équilibre.</p>',
    '<p>Le facteur est exp[20000/(R×500)]≈122,84. La constante catalysée du modèle vaut donc 1,2284 s⁻¹. Ce nombre concerne une vitesse ; il n’implique aucune multiplication de la constante d’équilibre, inchangée à T fixée pour les mêmes réactifs et produits.</p>')
exercise('arrhenius_catalyse', 'Retrouver une énergie à partir de deux mesures', 'Spé',
    '<p>On mesure k₂/k₁=10 entre T₁=450 K et T₂=500 K. Dans le modèle d’Arrhénius à préfacteur constant, calculer Ea.</p>',
    '<p>Ea=R ln10/(1/450−1/500)≈86,151 kJ·mol⁻¹. C’est une énergie apparente sur cet intervalle. Une courbure du graphe ln k en fonction de 1/T indiquerait que cette représentation avec une seule énergie est insuffisante.</p>')


guide('reacteurs_residence',
    'Passer d’une loi du premier ordre à un bilan de matière, puis comparer des organisations de réacteur à temps total égal.',
    ['A est le réactif, C₀ sa concentration d’entrée et C sa concentration de sortie, en mol·L⁻¹. X=1−C/C₀ est la conversion.',
     'k est la constante du premier ordre, en s⁻¹. τ est le séjour total affiché en minutes ; le calcul utilise 60τ secondes.',
     'N est le nombre entier de cuves identiques en série ; chacune a un séjour τ/N. Da=kτsecondes est le nombre de Damköhler, sans unité.'],
    ['Réaction A→B irréversible et isotherme ; débit volumique et densité constants.',
     'Cuve parfaitement mélangée ou réacteur piston idéal ; pas de diffusion ni de bilan thermique.'],
    ['Bilan entrée−sortie−consommation', 'Équation différentielle du premier ordre', 'Limite d’une suite de cuves'],
    'Sup : loi du premier ordre, bilan de matière et unités.',
    'Spé : bilans de la cuve agitée et du piston isotherme du premier ordre, au programme de chimie PC.',
    'La série de N cuves et sa limite sont des compléments guidés ; les autres filières peuvent aborder les bilans à partir des équations fournies.',
    ['Prendre k=0,01 s⁻¹ et τ=5 min ; calculer Da=3.',
     'Comparer une cuve, trois cuves et un piston à ce séjour total.',
     'Augmenter N sans changer τ : expliquer la convergence vers le piston.'],
    'Une loi cinétique identique peut donner des conversions différentes selon l’organisation des écoulements.')

lesson('reacteurs_residence', 'Une cuve agitée se calcule par un bilan', 'Sup / Spé · application industrielle guidée',
    '<p>On note Q le débit volumique, Vréac le volume de la cuve et τ=Vréac/Q le temps de séjour. Pour A→B, C₀ et C sont les concentrations d’entrée et de sortie ; k est la constante du premier ordre.</p>'
    '<p>À l’état stationnaire, la concentration uniforme de la cuve vaut celle de la sortie. Le bilan Q(C₀−C)=Vréac kC donne C=C₀/(1+kτ). La conversion X=1−C/C₀ vaut donc Da/(1+Da), avec Da=kτ.</p>'
    '<p>Le débit doit être exprimé avec le même temps que k. Ici k est en s⁻¹ et le curseur τ en minutes : Da=60kτ. Pour k=0,01 s⁻¹ et τ=5 min, Da=3 et X=75 %.</p>'
    '<p>La cuve mélangée expose tout le réacteur à la concentration de sortie. Cette propriété explique sa comparaison avec le piston pour cette seule cinétique du premier ordre.</p>')

lesson('reacteurs_residence', 'Piston et cuves en série', 'Spé · socle PC et complément guidé',
    '<p>On note τ le séjour total en secondes. Dans le réacteur piston idéal, chaque élément de fluide suit dC/dt=−kC : la conversion de sortie vaut Xpiston=1−exp(−kτ).</p>'
    '<p>Pour N cuves identiques à même séjour total, chaque cuve a un séjour τ/N. Les concentrations se multiplient par 1/(1+Da/N), d’où XN=1−(1+Da/N)⁻ᴺ. N=1 retrouve la cuve unique ; la limite N→∞ retrouve le piston.</p>'
    '<p>Avec Da=3 et N=3, XN=1−2⁻³=87,5 %, contre 95,021 % pour le piston. Les bilans de la cuve agitée et du piston du premier ordre relèvent du programme PC ; la série de cuves est un complément. Ajouter des appareils augmente aussi contraintes de mélange, coût et transferts, non calculés ici.</p>')

exercise('reacteurs_residence', 'Ne pas perdre un facteur 60', 'Sup',
    '<p>Pour k=0,01 s⁻¹, τ=5 min et N=3 cuves identiques, calculer Da et les conversions cuve, piston et série.</p>',
    '<p>τ=300 s et Da=3. La cuve donne 3/4=75 %. Le piston donne 1−e⁻³≈95,021 %. Trois cuves donnent 1−(1+3/3)⁻³=87,5 %. Les trois organisations ont le même séjour total, pas le même séjour par cuve.</p>')
exercise('reacteurs_residence', 'Quel séjour pour atteindre 90 % ?', 'Sup / Spé',
    '<p>Une réaction du premier ordre a k=0,01 s⁻¹. Déterminer le séjour nécessaire à X=0,90 dans une cuve unique et dans un piston idéal.</p>',
    '<p>Pour la cuve, Da=X/(1−X)=9, donc τ=900 s=15 min. Pour le piston, Da=−ln(1−X)=ln10, donc τ≈230,259 s=3,8376 min. La comparaison concerne ce modèle isotherme ; elle ne constitue pas à elle seule un choix d’équipement.</p>')
exercise('reacteurs_residence', 'Dimensionner un procédé continu', 'Spé · bilan industriel',
    '<p>Un débit volumique Q=2 L·min⁻¹ traverse un réacteur isotherme de constante k=0,01 s⁻¹. On vise X=90 %. Calculer le volume total pour une cuve, un piston et N=3 cuves identiques. Le séjour total est τ=Vtotal/Q.</p>',
    '<p>Pour la cuve, τ=15 min, donc Vtotal=30 L. Pour le piston, τ=ln10/(60k)≈3,83764 min, donc Vtotal≈7,67528 L. Pour trois cuves, 1−X=(1+Da/3)⁻³ donne Da=3(10¹ᐟ³−1)≈3,46330 ; τ≈5,77217 min et Vtotal≈11,54435 L, soit 3,84812 L par cuve. Ces volumes comparent les modèles à même débit et même objectif, sans calcul économique.</p>')


guide('selectivite_successive',
    'Chercher l’instant où un intermédiaire utile est le plus concentré, sans confondre disparition du réactif et rendement de cet intermédiaire.',
    ['A→B→C décrit deux étapes irréversibles du premier ordre. Les concentrations sont en mol·L⁻¹ ; A₀=1 mol·L⁻¹, B₀=C₀=0.',
     'k₁ et k₂ sont les constantes, en min⁻¹. t est le temps affiché en minutes.',
     'topt est l’instant qui maximise B ; la formation k₁A et la consommation k₂B sont en mol·L⁻¹·min⁻¹.'],
    ['Volume, température et constantes cinétiques fixes ; bilan A+B+C=A₀.',
     'Le modèle représente une stratégie de sélectivité, sans données de procédé commercial.'],
    ['Résoudre une équation différentielle linéaire', 'Contrôler un bilan de matière', 'Annuler une dérivée et traiter un cas limite'],
    'Sup : deux réactions du premier ordre et bilan de conservation.',
    'Spé : système linéaire, optimum et limite k₂→k₁.',
    'L’optimum de concentration n’intègre ni séparation, ni recyclage, ni coût de traitement.',
    ['Garder k₁=0,1 et k₂=0,04 min⁻¹ : repérer le pic de B.',
     'Lire les deux vitesses à ce pic : elles sont égales.',
     'Choisir k₁=k₂=0,1 min⁻¹ : vérifier la formule limite sans division par zéro.'],
    'Il faut arrêter selon la grandeur visée : attendre plus longtemps peut consommer le produit intermédiaire.')

lesson('selectivite_successive', 'Former puis consommer un produit utile', 'Sup / Spé · fiche C6 p.548',
    '<p>On note A,B,C les concentrations dans le schéma A→B→C. Les constantes k₁,k₂ sont positives et dans la même unité de temps. Avec A(0)=A₀, B(0)=C(0)=0, les bilans sont A′=−k₁A, B′=k₁A−k₂B et C′=k₂B.</p>'
    '<div class="formula">A=A₀e⁻ᵏ¹ᵗ ; B=A₀k₁(e⁻ᵏ¹ᵗ−e⁻ᵏ²ᵗ)/(k₂−k₁) si k₁≠k₂ ; C=A₀−A−B.</div>'
    '<p>B est d’abord formé, puis consommé. Un maximum intérieur vérifie k₁A=k₂B : sa formation compense sa consommation. La conversion de A continue pourtant à augmenter. Ce modèle donne une première lecture des stratégies de sélectivité lors de transformations successives.</p>')

lesson('selectivite_successive', 'Un optimum avec un cas limite régulier', 'Spé · dérivation et passage à la limite',
    '<p>On note topt l’instant du maximum de B. Pour k₁≠k₂, annuler B′ donne topt=ln(k₂/k₁)/(k₂−k₁), positif quel que soit l’ordre des deux constantes.</p>'
    '<p>Si k₁=k₂=k, la formule précédente doit être remplacée par sa limite : B=A₀kt exp(−kt). Son maximum est obtenu à t=1/k et vaut A₀/e. Une différence de deux exponentielles divisée par une petite différence de constantes demande aussi un calcul numérique adapté.</p>'
    '<p>Pour A₀=1 mol·L⁻¹, k₁=0,1 et k₂=0,04 min⁻¹, topt≈15,2715 min et Bmax≈0,542884 mol·L⁻¹. À t=15 min, A≈0,223130, B≈0,542802 et C≈0,234067 mol·L⁻¹ : leur somme reste 1.</p>')

exercise('selectivite_successive', 'Les deux constantes égales', 'Sup / Spé',
    '<p>Dans A→B→C, prendre k₁=k₂=0,1 min⁻¹ et A₀=1 mol·L⁻¹. Calculer l’instant et la concentration du maximum de B.</p>',
    '<p>B(t)=0,1t exp(−0,1t). Sa dérivée s’annule à t=10 min et change de signe de + à −. Bmax=1/e≈0,367879 mol·L⁻¹ ; au même instant A=1/e et C=1−2/e≈0,264241 mol·L⁻¹.</p>')
exercise('selectivite_successive', 'Contrôler le bilan à 15 minutes', 'Sup',
    '<p>Prendre A₀=1 mol·L⁻¹, k₁=0,1 et k₂=0,04 min⁻¹. Calculer A,B,C à t=15 min puis comparer t à topt.</p>',
    '<p>A=e⁻¹·⁵≈0,223130. B=(0,1/−0,06)(e⁻¹·⁵−e⁻⁰·⁶)≈0,542802. C=1−A−B≈0,234067 mol·L⁻¹. topt=ln(0,4)/(−0,06)≈15,2715 min : à 15 min B augmente encore légèrement.</p>')
exercise('selectivite_successive', 'Le temps très court montre les étapes', 'Spé',
    '<p>Pour A→B→C avec A₀&gt;0, B₀=C₀=0 et k₁,k₂&gt;0, obtenir les premiers termes de B(t) et C(t) lorsque t→0⁺.</p>',
    '<p>A=A₀(1−k₁t+k₁²t²/2)+O(t³). L’équation de B donne B=A₀k₁t−A₀k₁(k₁+k₂)t²/2+O(t³). Par conservation, C=A₀k₁k₂t²/2+O(t³). B apparaît au premier ordre en temps ; C nécessite les deux étapes et apparaît au second ordre.</p>')


guide('catalyse_surface',
    'Relier les sites disponibles d’un catalyseur à la vitesse, puis comprendre saturation et compétition entre espèces.',
    ['pA et pB sont les pressions partielles en bar. KA et KB sont des constantes d’adsorption en bar⁻¹ ; leurs produits avec les pressions sont sans unité.',
     'θA, θB et θlibre sont les fractions de sites occupés par A, par B ou libres ; leur somme vaut 1.',
     'Seul A adsorbé se transforme. kcat=1 s⁻¹ est fixé ; vsite=kcatθA est une vitesse par site, en s⁻¹.'],
    ['Sites identiques et adsorption réversible à l’équilibre ; un site n’accueille qu’une espèce.',
     'Pas de transport limitant ni de désactivation. B est un compétiteur sans réaction dans ce modèle.'],
    ['Bilan de sites', 'Équilibres d’adsorption', 'Limites faible et forte pression'],
    'Sup : équilibre, fractions et comparaison de vitesses.',
    'Spé : mécanisme apparent et ordre local dépendant des conditions.',
    'Langmuir compétitif est un modèle fourni ; les surfaces réelles peuvent présenter plusieurs types de sites.',
    ['Avec pA=1 bar, pB=2 bar, KA=2 et KB=1 bar⁻¹, calculer les trois fractions.',
     'Supprimer B : comparer la disponibilité des sites et la vitesse.',
     'Augmenter pA : observer la saturation sans dépasser kcat.'],
    'La pression accélère à faible occupation ; elle n’augmente pas indéfiniment une vitesse limitée par les sites.')

lesson('catalyse_surface', 'Un bilan de sites remplace une loi puissance', 'Spé · catalyse hétérogène guidée',
    '<p>On note θlibre la fraction de sites vacants et θA,θB celles occupées. Les pressions pA,pB sont en bar ; KA,KB sont en bar⁻¹. À l’équilibre d’adsorption, θA=KApAθlibre et θB=KBpBθlibre.</p>'
    '<div class="formula">θlibre=1/(1+KApA+KBpB) ; θA=KApA/(1+KApA+KBpB) ; θB=KBpB/(1+KApA+KBpB).</div>'
    '<p>Ces relations viennent de θlibre+θA+θB=1. Avec pA=1 bar, pB=2 bar, KA=2 et KB=1 bar⁻¹, le dénominateur vaut 5 : 20 % des sites sont libres, 40 % portent A et 40 % portent B.</p>'
    '<p>Ce modèle aide à lire l’effet d’une espèce concurrente sur un matériau catalytique. Il ne prétend pas représenter un catalyseur commercial précis.</p>')

lesson('catalyse_surface', 'Saturation, inhibition et ordre apparent', 'Spé · prolongement vers les procédés',
    '<p>On note kcat la constante de transformation de A adsorbé et vsite=kcatθA la vitesse par site. Dans l’atelier kcat=1 s⁻¹. À pB fixé, une faible pA donne vsite≈kcatKApA/(1+KBpB), presque proportionnelle à pA ; à forte pA, vsite tend vers kcat.</p>'
    '<p>L’ordre local en A est nA=∂ln(vsite)/∂ln(pA)=(1+KBpB)/(1+KApA+KBpB). Il passe de presque 1 à presque 0. L’ordre local en B est nB=−KBpB/(1+KApA+KBpB), négatif lorsque B occupe des sites.</p>'
    '<p>Un ordre apparent variable ne contredit pas un mécanisme : il peut résulter d’un équilibre d’adsorption suivi d’une transformation. La carte représente une fraction de sites, pas une température ni une concentration dans le grain.</p>')

exercise('catalyse_surface', 'Supprimer un compétiteur', 'Sup / Spé',
    '<p>Prendre pA=1 bar, KA=2 et KB=1 bar⁻¹. Comparer θA et vsite pour pB=2 bar puis pB=0 ; kcat=1 s⁻¹.</p>',
    '<p>Avec B, θA=2/(1+2+2)=0,4 et vsite=0,4 s⁻¹. Sans B, θA=2/(1+2)=2/3 et vsite=2/3 s⁻¹. Le facteur est (2/3)/0,4=5/3 ; on change la répartition des sites, pas kcat.</p>')
exercise('catalyse_surface', 'La pression de demi-saturation', 'Spé',
    '<p>Dans le modèle compétitif, déterminer la pression pA telle que θA=1/2 à pB fixé. Appliquer à KA=2 bar⁻¹, KB=1 bar⁻¹ et pB=2 bar.</p>',
    '<p>2KApA=1+KApA+KBpB donne pA=(1+KBpB)/KA. Ici pA=3/2=1,5 bar. La présence du compétiteur augmente la pression nécessaire pour occuper la moitié des sites avec A.</p>')
exercise('catalyse_surface', 'Deux ordres locaux au même point', 'Spé',
    '<p>Pour pA=1 bar, pB=2 bar, KA=2 et KB=1 bar⁻¹, calculer nA=∂ln vsite/∂ln pA et nB=∂ln vsite/∂ln pB. Interpréter leurs signes.</p>',
    '<p>Le dénominateur vaut 5. nA=1−KApA/5=3/5 ; nB=−KBpB/5=−2/5. Augmenter A accroît la vitesse avec un effet déjà atténué par saturation. Augmenter B la réduit. Ce sont des dérivées locales, pas des ordres constants valables partout.</p>')


guide('ethanal_aeqs',
    'Reprendre le mécanisme radicalaire p.549–550, garder les termes d’amorçage et de propagation, puis discuter l’ordre non entier.',
    ['E désigne l’éthanal CH₃CHO ; c=[E] est sa concentration, en mol·L⁻¹. Le point · indique un radical.',
     'k₁ est la constante d’amorçage, en s⁻¹ ; k₅ et k₆ celles de propagation et terminaison, en L·mol⁻¹·s⁻¹.',
     'vE est la vitesse de disparition d’E, en mol·L⁻¹·s⁻¹. L=vE/(k₁c) est la longueur de chaîne selon la définition du recueil.',
     'nlocal=d ln(vE)/d ln c est l’ordre local ; Eapp est l’énergie apparente locale, en kJ·mol⁻¹.'],
    ['Approximation des états quasi stationnaires, AEQS, admise pour les quatre intermédiaires du mécanisme source.',
     'Constantes réglables illustratives ; elles ne sont pas obtenues à partir des préfacteurs expérimentaux du mécanisme.',
     'Les courbes sont des vitesses en fonction de c, pas une évolution temporelle.'],
    ['Écrire et éliminer les bilans d’intermédiaires', 'Distinguer ordre élémentaire et ordre apparent', 'Contrôler les bilans atomiques'],
    'Sup : vitesse, mécanisme et bilan de matière.',
    'Spé : mécanismes en chaîne, AEQS et régime de propagation dominante.',
    'La validation dynamique de l’AEQS demande des échelles de temps ; un petit taux de radicaux ne suffit pas à la démontrer.',
    ['Avec les réglages par défaut, vérifier que l’ordre local est proche de 1,47 et non exactement 3/2.',
     'Choisir le préréglage où l’amorçage devient plus visible : observer l’ordre qui se rapproche de 1.',
     'Lire le tableau : vérifier les conservations du carbone, de l’hydrogène et de l’oxygène.'],
    'L’ordre 3/2 et l’énergie 201 kJ·mol⁻¹ décrivent un régime dominant, pas tous les réglages possibles.')

lesson('ethanal_aeqs', 'L’AEQS élimine les intermédiaires, pas les bilans', 'Spé · mécanisme source p.549–550',
    '<p>On note c=[CH₃CHO] la concentration d’éthanal et z=[CH₃·] celle du radical méthyle, en mol·L⁻¹. L’amorçage a pour vitesse k₁c ; la propagation CH₃·+CH₃CHO a pour vitesse k₅zc ; la terminaison de deux méthyles a pour vitesse k₆z².</p>'
    '<p>Les autres intermédiaires du recueil sont CHO·, H· et CH₃CO·. Leurs bilans quasi stationnaires donnent k₂[CHO·]=k₁c, k₃[H·]c=k₁c et k₄[CH₃CO·]=k₁c+k₅zc. Le bilan du méthyle devient 2k₁c−2k₆z²=0.</p>'
    '<div class="formula">z=√(k₁c/k₆) ; vE=2k₁c+k₅√(k₁/k₆)c³ᐟ².</div>'
    '<p>Le facteur 2 est conservé. Le mécanisme donne vCO=vE, vH₂=vC₂H₆=k₁c et vCH₄=k₅zc. Le tableau contrôle les atomes, même lorsque le régime d’amorçage n’est pas négligeable.</p>')

lesson('ethanal_aeqs', 'Un ordre non entier et une énergie composée', 'Spé · AEQS et Arrhénius',
    '<p>On pose u=2k₁c et w=k₅√(k₁/k₆)c³ᐟ², les deux contributions à vE=u+w. L’ordre local vaut nlocal=(u+1,5w)/(u+w). Il est compris entre 1 et 3/2 ; le régime 3/2 exige w≫u.</p>'
    '<p>Si kᵢ suit Arrhénius d’énergie Eᵢ, le coefficient de propagation k₅√(k₁/k₆) a l’énergie Eprop=E₅+(E₁−E₆)/2. Le recueil donne E₁=318, E₅=42 et E₆=0 kJ·mol⁻¹ : Eprop=201 kJ·mol⁻¹.</p>'
    '<p>Pour la vitesse totale à c fixé, Eapp=(318u+201w)/(u+w). L’énergie 201 n’est donc pas celle de tous les régimes. La définition de longueur retenue donne L=vE/(k₁c)=2+w/(k₁c) ; les valeurs réglables ne présupposent pas L≥100.</p>'
    '<p>Le rôle de l’AEQS est de simplifier un système cinétique. Sa validité physique se discute à partir des échelles de temps, séparément du contrôle algébrique des bilans.</p>')

exercise('ethanal_aeqs', 'Le facteur deux de terminaison', 'Spé',
    '<p>Une terminaison CH₃·+CH₃·→C₂H₆ a pour vitesse de réaction k₆z². Écrire son terme dans le bilan de z. Avec l’AEQS du mécanisme source, justifier z=√(k₁c/k₆).</p>',
    '<p>Chaque événement consomme deux radicaux : le terme est −2k₆z², tandis que la formation d’éthane vaut +k₆z². Après élimination des autres intermédiaires, le méthyle reçoit 2k₁c et les termes de propagation se compensent : 0=2k₁c−2k₆z². On obtient z²=k₁c/k₆, sans facteur √2 supplémentaire.</p>')
exercise('ethanal_aeqs', 'Un régime proche de 3/2', 'Spé',
    '<p>Prendre c=0,1 mol·L⁻¹, k₁=10⁻⁶ s⁻¹, k₅=10² et k₆=10⁶ L·mol⁻¹·s⁻¹. Calculer z, u=2k₁c, w=k₅zc, l’ordre local et L.</p>',
    '<p>z=√10⁻¹³≈3,1623×10⁻⁷ mol·L⁻¹. u=2×10⁻⁷ et w≈3,1623×10⁻⁶ mol·L⁻¹·s⁻¹. Ainsi nlocal=(u+1,5w)/(u+w)≈1,47026. L=(u+w)/(k₁c)≈33,6228. La propagation domine mais n’est pas seule ; l’ordre n’est pas exactement 3/2.</p>')
exercise('ethanal_aeqs', 'Énergie apparente et conservation du carbone', 'Spé · synthèse',
    '<p>Avec u,w définis dans le cours et les énergies source E₁=318, E₅=42, E₆=0 kJ·mol⁻¹, déterminer Eprop et Eapp. Vérifier le bilan du carbone à partir de vCO=u+w, vCH₄=w et vC₂H₆=u/2.</p>',
    '<p>Eprop=42+(318−0)/2=201 kJ·mol⁻¹. Eapp=(318u+201w)/(u+w), qui tend vers 201 seulement si w/u→∞. Le carbone entrant disparaît à 2vE=2(u+w) ; il ressort à vCO+vCH₄+2vC₂H₆=(u+w)+w+u=2(u+w). Le bilan est conservé pour tout rapport u/w.</p>')


guide('emballement_thermique',
    'Coupler une vitesse d’Arrhénius à un bilan thermique. Comprendre pourquoi une température d’équilibre peut être stable ou instable.',
    ['T est la température du milieu et Ta celle du fluide extérieur, en K. qref est la puissance produite à 300 K, en W·L⁻¹.',
     'Ea est l’énergie d’activation en kJ·mol⁻¹ ; R est la constante des gaz parfaits. h est le coefficient d’évacuation, en W·L⁻¹·K⁻¹.',
     'Cth=100 J·L⁻¹·K⁻¹ est la capacité thermique volumique fixée. T₀ est la température initiale.',
     'Le bilan F(T)=q(T)−h(T−Ta) est une puissance volumique ; sa dérivée classe les équilibres simples.'],
    ['Production de chaleur à concentration de réactif maintenue constante ; modèle de type Semenov.',
     'Les intersections sont recherchées sur [Ta,Ta+90 K] ; les racines tangentes ne sont pas détectées par un simple changement de signe.',
     'La trajectoire RK4 emploie un pas de 0,25 s et s’arrête avant qu’un pas ne sorte du domaine étudié.'],
    ['Bilan de chaleur', 'Équilibre d’une équation différentielle', 'Signe de la dérivée et stabilité locale'],
    'Sup : premier principe et évolution d’une température.',
    'Spé : rétroaction cinétique, linéarisation et stabilité.',
    'La prévention d’un emballement réel exige un modèle et des données adaptés ; l’atelier étudie seulement le bilan didactique annoncé.',
    ['Avec les réglages par défaut, repérer les deux intersections et lire leurs stabilités.',
     'Passer de T₀=300 à 350 K sans changer l’appareil : comparer les trajectoires.',
     'Réduire h puis lire l’état du calcul ; distinguer sortie du domaine et température finale atteinte.'],
    'La température accélère la production ; l’évacuation doit être comparée à cette accélération, pas seulement à une puissance initiale.')

lesson('emballement_thermique', 'Deux courbes pour un bilan de chaleur', 'Sup / Spé · cinétique et thermochimie',
    '<p>On note q(T) la puissance volumique de production, Ta la température du fluide extérieur et h le coefficient d’évacuation. La capacité thermique volumique Cth est constante. Les unités sont W·L⁻¹ pour q, W·L⁻¹·K⁻¹ pour h et J·L⁻¹·K⁻¹ pour Cth.</p>'
    '<div class="formula">Cth dT/dt=F(T)=q(T)−h(T−Ta) ; q(T)=qref exp[(Ea/R)(1/300−1/T)].</div>'
    '<p>Un équilibre T* est une intersection des deux courbes : F(T*)=0. La chaleur produite croît selon Arrhénius ; la chaleur évacuée croît linéairement dans ce modèle. À Ta=300 K, qref=0,5 W·L⁻¹, Ea=60 kJ·mol⁻¹ et h=0,2 W·L⁻¹·K⁻¹, deux équilibres sont trouvés dans [300,390 K], vers 303,230 et 338,459 K.</p>'
    '<p>La concentration est maintenue dans le modèle : aucun épuisement du réactif ne limite la chaleur. La représentation n’est donc pas celle d’un lot fermé complet.</p>')

lesson('emballement_thermique', 'Une intersection peut repousser la trajectoire', 'Spé · stabilité et limite du calcul',
    '<p>On note δT=T−T* le petit écart à un équilibre simple. La linéarisation donne Cth δT′≈F′(T*)δT. Si F′&lt;0, un petit écart décroît : l’équilibre est localement stable. Si F′&gt;0, il augmente : l’équilibre est instable.</p>'
    '<p>La dérivée vaut F′(T)=q(T)Ea/(RT²)−h, avec Ea en joules. Pour les réglages par défaut, elle vaut environ −0,14930 au premier équilibre et +0,28454 W·L⁻¹·K⁻¹ au second.</p>'
    '<p>Une intégration sur 1800 s n’est pas une preuve d’équilibre : depuis 300 K, elle atteint environ 303,018 K, encore distinct de 303,230 K. Depuis un départ plus chaud que l’équilibre instable, elle peut sortir du domaine étudié.</p>'
    '<p>Le logiciel interrompt l’évolution à Ta+90 K. Une courbe arrêtée représente une limite du calcul ; elle ne donne ni la température maximale réelle, ni l’effet des changements de phase ou de la consommation des réactifs.</p>')

exercise('emballement_thermique', 'Une pente décide de la stabilité', 'Spé',
    '<p>Au premier équilibre T*=303,230 K des réglages par défaut, q(T*)=h(T*−Ta) avec Ta=300 K et h=0,2 W·L⁻¹·K⁻¹. Prendre Ea=60000 J·mol⁻¹. Calculer F′(T*) et conclure.</p>',
    '<p>q(T*)≈0,64603 W·L⁻¹. F′=qEa/(RT*²)−h≈−0,14930 W·L⁻¹·K⁻¹. Le signe est négatif : les petits écarts décroissent. Le temps caractéristique linéaire vaut Cth/|F′|≈669,80 s pour Cth=100 J·L⁻¹·K⁻¹.</p>')
exercise('emballement_thermique', 'L’évacuation ne produit pas toujours de la chaleur', 'Sup',
    '<p>À Ta=300 K, h=0,2 W·L⁻¹·K⁻¹, qref=0,5 W·L⁻¹ et Cth=100 J·L⁻¹·K⁻¹, calculer dT/dt à T=300 K. Expliquer le signe du terme −h(T−Ta) si T&lt;Ta.</p>',
    '<p>À 300 K, q=qref=0,5 et l’échange vaut zéro : dT/dt=0,5/100=0,005 K·s⁻¹. Si T&lt;Ta, −h(T−Ta)&gt;0 : le fluide extérieur réchauffe le milieu. L’expression d’échange représente un transfert selon l’écart de température, pas une perte positive dans tous les cas.</p>')
exercise('emballement_thermique', 'Une courbe arrêtée n’est pas un état final', 'Spé · interprétation',
    '<p>Le calcul s’interrompt lorsque T atteint la limite Ta+90 K avant 1800 s. Peut-on donner cette température comme maximum du procédé ? Quelles conclusions restent justifiées ?</p>',
    '<p>Non. On sait que la trajectoire calculée a quitté le domaine où le modèle est exploré ; on ne connaît pas son maximum après cet arrêt. On peut commenter le signe du bilan avant la sortie et les équilibres simples localisés dans l’intervalle. Un procédé réel peut épuiser ses réactifs, changer de phase ou modifier ses transferts : ces effets sont absents du modèle.</p>')


guide('diffusion_grain',
    'Comprendre pourquoi les sites au centre d’un grain poreux peuvent manquer de réactif, même si la chimie intrinsèque est rapide.',
    ['R est le rayon du grain, affiché en µm et converti en m ; r est la distance au centre et ρ=r/R la coordonnée réduite.',
     'Deff est la diffusivité effective, en m²·s⁻¹ ; k est la constante du premier ordre, en s⁻¹.',
     'C est la concentration dans le grain et Cs celle imposée à sa surface. La carte représente C/Cs, sans unité.',
     'φ=R√(k/Deff) est le module de Thiele ; η est le rapport de la consommation réelle à celle d’un grain partout à Cs.'],
    ['Grain sphérique, isotherme et stationnaire ; diffusivité constante et réaction du premier ordre.',
     'Concentration de surface imposée ; résistance au transfert externe et perte de charge non calculées.'],
    ['Comparer temps diffusif et temps chimique', 'Résoudre une diffusion radiale stationnaire', 'Développement limité et moyenne volumique'],
    'Sup : diffusion, temps caractéristique et premier ordre.',
    'Spé : couplage réaction−diffusion et étude asymptotique.',
    'Le module de Thiele et le facteur d’efficacité sont des compléments de génie chimique, explicités dans le TP.',
    ['Avec R=500 µm, Deff=10⁻⁸ m²·s⁻¹ et k=0,1 s⁻¹, calculer φ.',
     'Réduire le rayon sans changer k : observer la remontée de C au centre.',
     'Choisir la diffusion limitante et comparer η au profil du grain.'],
    'Une grande surface interne n’assure pas que tous les sites travaillent ; la diffusion doit alimenter la réaction.')

lesson('diffusion_grain', 'Deux temps pour un grain poreux', 'Spé · prolongement réaction−diffusion',
    '<p>On note R le rayon du grain en mètres, Deff la diffusivité effective en m²·s⁻¹ et k la constante du premier ordre en s⁻¹. Le temps diffusif est td=R²/Deff ; le temps chimique est tc=1/k.</p>'
    '<div class="formula">φ²=td/tc=kR²/Deff.</div>'
    '<p>Si φ est petit, la diffusion est rapide devant la consommation : la concentration reste presque uniforme. Si φ est grand, le réactif est davantage consommé près de la surface avant d’atteindre le centre.</p>'
    '<p>Avec R=500 µm=5×10⁻⁴ m, Deff=10⁻⁸ m²·s⁻¹ et k=0,1 s⁻¹, td=25 s, tc=10 s et φ=√2,5≈1,58114. Diminuer R réduit td au carré, sans changer ici la cinétique intrinsèque.</p>')

lesson('diffusion_grain', 'Un profil radial et une efficacité moyenne', 'Spé · génie des catalyseurs, résultat fourni',
    '<p>On note ρ=r/R la distance réduite, C la concentration et Cs sa valeur de surface. Le bilan stationnaire sphérique est Deff ΔC−kC=0, avec C(R)=Cs et une solution régulière au centre.</p>'
    '<div class="formula">C/Cs=sinh(φρ)/(ρ sinhφ) ; au centre, C(0)/Cs=φ/sinhφ.</div>'
    '<p>Le facteur d’efficacité est la moyenne volumique de C/Cs pour une cinétique du premier ordre : η=3∫₀¹(C/Cs)ρ²dρ=3(φ cothφ−1)/φ². Le facteur ρ² vient des coquilles sphériques ; une moyenne sur le rayon seul serait incorrecte.</p>'
    '<p>Pour φ→0, η=1−φ²/15+2φ⁴/315+… ; pour φ grand, η≈3/φ. Les réglages par défaut donnent η≈0,86509 et C(0)/Cs≈0,67937. Ce facteur décrit l’utilisation interne du grain, sans calculer son coût ou la perte de charge du réacteur.</p>')

exercise('diffusion_grain', 'Un rayon en micromètres', 'Sup / Spé',
    '<p>Un grain a R=500 µm, Deff=10⁻⁸ m²·s⁻¹ et k=0,1 s⁻¹. Calculer td, tc et φ. Que devient φ si le rayon est divisé par deux ?</p>',
    '<p>R=5×10⁻⁴ m, donc td=R²/Deff=25 s et tc=10 s. φ=√(25/10)≈1,58114. Si R est divisé par deux, td est divisé par quatre et φ par deux. La constante k est conservée : on modifie l’alimentation interne, pas la réaction intrinsèque.</p>')
exercise('diffusion_grain', 'Le centre n’est pas singulier', 'Spé · limite',
    '<p>On fournit C/Cs=sinh(φρ)/(ρ sinhφ), avec φ&gt;0 et ρ=r/R. Déterminer sa limite au centre. Pour φ=2, calculer C(0)/Cs et η.</p>',
    '<p>sinh(φρ)=φρ+O(ρ³), donc C(0)/Cs=φ/sinhφ. À φ=2, ce rapport vaut environ 0,551441. Le facteur η=3(2coth2−1)/4≈0,805972. La moyenne volumique reste supérieure à la concentration centrale réduite.</p>')
exercise('diffusion_grain', 'Presque tout le grain est alimenté', 'Spé · développement limité',
    '<p>À partir de cothφ=1/φ+φ/3−φ³/45+2φ⁵/945+O(φ⁷), retrouver le développement de η=3(φcothφ−1)/φ². Estimer η pour φ=0,1.</p>',
    '<p>φcothφ−1=φ²/3−φ⁴/45+2φ⁶/945+O(φ⁸). Ainsi η=1−φ²/15+2φ⁴/315+O(φ⁶). À φ=0,1, η≈0,999333968 : la consommation est presque celle d’un grain uniformément à Cs. Le développement évite aussi la soustraction numérique de deux nombres presque égaux.</p>')
