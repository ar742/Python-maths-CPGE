"""Repères accessibles avant les huit expériences de physique statistique."""
from cours import LESSONS


def guide(intro,objects,assumptions,techniques,steps,sup,spe,beyond,expected):
    return dict(intro=intro,purpose=intro,objects=objects,assumptions=assumptions,
                techniques=techniques,first_steps=steps,levels=dict(sup=sup,spe=spe,beyond=beyond),
                expected=expected,lesson_numbers=[])


LAB_GUIDES={
 'maxwell':guide(
    'T est la température du gaz et M sa masse molaire. Partir des vitesses individuelles pour retrouver la pression, puis étudier une fuite par un petit trou. Dans deux compartiments à températures différentes, comparer la conservation du nombre de particules à l’égalité des flux stationnaires.',
    ['T₁,T₂ en K ; M en g/mol ; m=M/Nₐ est la masse d’une particule après conversion en kg/mol.','n : nombre de particules par m³, réglé par log₁₀ n ; V₁,V₂ en litres ; S : aire du trou en mm².','N₁,N₂ : nombres de particules ; τ : temps caractéristique ; t/τ : temps réduit.'],
    ['Gaz parfait classique, dilué, à vitesses isotropes ; chaque compartiment reste thermostaté.','Effusion : trou petit devant le libre parcours moyen ; extérieur vide pour la fuite, deux gaz pour la paroi.'],
    ['Calculer moyenne et moment quadratique d’une distribution.','Écrire un flux avec la composante de vitesse normale.','Résoudre une équation linéaire de conservation.'],
    ['Comparer vitesse la plus probable, vitesse moyenne et vitesse quadratique moyenne à 300 K.','Choisir la fuite et doubler S : prévoir le changement de τ.','Choisir la paroi avec T₂=2T₁ et comparer les pressions stationnaires.'],
    'Entrée Sup : gaz parfait, pression, unités et bilan de particules.',
    'MP §7 : lien microscopique–macroscopique ; distributions et effusion comme approfondissements guidés.',
    'Transpiration thermique et fuite sans thermostat : prolongements du modèle de gaz dilué.',
    'Une pression expliquée par un flux de quantité de mouvement et des hypothèses distinctes pour fuite et paroi.'),
 'canonique':guide(
    'ε est l’écart entre niveaux et T la température du thermostat. Calculer les populations, l’énergie moyenne et ses fluctuations. Comparer deux niveaux non dégénérés à trois niveaux, puis distinguer un système à énergie imposée d’un système en contact avec un thermostat.',
    ['ε en meV ; T en K ; kB : constante de Boltzmann ; ε/(kBT) compare les deux échelles d’énergie.','N : nombre de sites indépendants ; fraction excitée : proportion de sites au niveau ε.','g : nombre de microétats du niveau ε dans le modèle à trois niveaux 0,ε,2ε.'],
    ['Niveaux indépendants de T ; sites distinguables sans interaction.','Canonique : thermostat à T ; microcanonique : nombre d’excitations fixé et configurations équiprobables.'],
    ['Normaliser les poids de Boltzmann.','Compter des configurations avec un coefficient binomial.','Relier une variance à une capacité thermique.'],
    ['Choisir deux niveaux et comparer kBT à ε avant de lire les populations.','Augmenter T : observer le maximum intermédiaire de capacité.','Choisir trois niveaux et augmenter g : comparer probabilité d’un niveau et d’un microétat.'],
    'Entrée Sup : probabilités, dénombrement et température.',
    'MP §7.1–7.2 : Boltzmann, niveaux discrets, fluctuations et système à deux niveaux.',
    'Dégénérescence et comparaison des ensembles statistiques : approfondissements ; pas un socle commun à toutes les filières.',
    'Des probabilités normalisées et un pic de capacité expliqué sans l’appeler transition de phase.'),
 'gaz':guide(
    'L est le côté d’une boîte et m la masse de la particule. Sommer les probabilités thermiques de ses modes, puis comparer le résultat au gaz classique. Augmenter le nombre de modes conservés permet de vérifier la troncature avant d’interpréter l’énergie ou la pression.',
    ['T en K ; L en nm ; m en multiples de la masse électronique mₑ.','Nmax : nombre de modes unidimensionnels conservés ; n : densité de particules en m⁻³.','λth=h/√(2πmkBT) : longueur d’onde thermique ; nλth³ est sans dimension.'],
    ['Une particule dans un cube à parois infinies ; absence d’interactions.','La partition classique d’un gaz de nombreuses particules suppose le régime dilué ; la somme du cube n’est pas celle de N bosons ou fermions.'],
    ['Factoriser une somme sur trois indices.','Comparer une somme discrète à une intégrale.','Contrôler une troncature et un paramètre sans dimension.'],
    ['Choisir confinement quantique et comparer l’énergie à celle du fondamental.','Choisir limite classique et comparer U à 3kBT/2 par particule.','Prendre la troncature courte puis augmenter Nmax : observer l’écart au calcul avec 2Nmax.'],
    'Entrée Sup : gaz parfait, énergie cinétique et sommes finies.',
    'MP §7.2–7.3 : particule confinée à température donnée et limite classique ; le cube prolonge la boîte 1D.',
    'Densité d’états et longueur d’onde thermique ; statistiques de particules identiques traitées séparément.',
    'Une comparaison quantique/classique accompagnée d’un contrôle du nombre de modes.'),
 'oscillateur':guide(
    'ν est la fréquence de l’oscillateur et T sa température. Comparer le quantum hν à kBT pour comprendre quand une excitation est gelée ou classique. Le compteur r décrit séparément un modèle classique à trois termes cinétiques et r termes quadratiques supplémentaires.',
    ['ν en THz ; T en K ; h : constante de Planck ; n : nombre de quanta d’excitation.','U : énergie moyenne ; C : sa dérivée en T à fréquence fixée ; kB : constante de Boltzmann.','r est un entier ; le modèle classique 3+r n’est pas nécessairement l’oscillateur 1D.'],
    ['Oscillateur harmonique quantique indépendant ; fréquence constante.','Équipartition classique seulement pour des variables quadratiques indépendantes et thermiquement accessibles.'],
    ['Sommer une série géométrique.','Dériver une énergie moyenne.','Compter les termes quadratiques et comparer deux limites.'],
    ['Choisir presque fondamental : distinguer énergie de point zéro et capacité thermique.','Augmenter T jusqu’à kBT≫hν : retrouver l’équipartition de l’oscillateur 1D.','Modifier r et compter sur papier les variables du modèle classique séparé.'],
    'Entrée Sup : oscillateur, énergie et chaleur.',
    'MP §7.3 : équipartition et capacités thermiques ; la somme quantique approfondit ces techniques.',
    'Modèle d’Einstein et rotation ortho/para : prolongements guidés.',
    'Une capacité qui tend vers zéro à froid, malgré une énergie fondamentale non nulle.'),
 'spins':guide(
    'μ est le moment d’un spin indépendant et B le champ magnétique. Les deux énergies sont ±μB. Comparer agitation thermique et alignement, puis distinguer la loi linéaire de Curie de la saturation à forte polarisation.',
    ['T en K ; B en T ; μ donné en multiples du magnéton de Bohr μB, en J/T.','x=μB/(kBT) : rapport sans dimension ; le moment moyen est exprimé en multiples de μ.','C_B : capacité à champ fixé ; la susceptibilité par spin est la dérivée du moment moyen par rapport à B.'],
    ['Deux niveaux, spins indépendants, champ homogène ; aucune interaction ferromagnétique.','La loi de Curie est une approximation pour |x|≪1.'],
    ['Normaliser deux poids de Boltzmann.','Développer tanh près de zéro.','Relier une réponse à une fluctuation.'],
    ['Choisir Curie et comparer formule exacte et droite.','Choisir saturation : observer les bornes ±μ.','Mettre B=0, puis discuter séparément la limite T→0.'],
    'Entrée Sup : dipôle magnétique et concurrence entre deux énergies.',
    'MP §7.2 : application du système à deux niveaux ; aimantation comme prolongement.',
    'Interactions et transition ferromagnétique demandent un autre modèle, notamment Ising.',
    'Une approximation linéaire placée dans son domaine et un modèle indépendant distingué d’un aimant ferromagnétique.'),
 'planck':guide(
    'T est la température du corps noir et λ la longueur d’onde observée. Lire une puissance répartie sur le spectre, localiser son maximum et comparer la loi de Planck à Rayleigh–Jeans. La fraction visible porte sur une bande annoncée ; elle n’est pas le rendement électrique d’une lampe.',
    ['T en K ; λ en µm ; h,kB,c : constantes de Planck, de Boltzmann et célérité de la lumière.','Bλ : luminance spectrale en W·m⁻²·sr⁻¹·µm⁻¹ ; une intensité par longueur d’onde.','σT⁴ : flux total par unité de surface ; bande visible [390,780] nm dans le modèle.'],
    ['Émission idéale de corps noir ; distribution spectrale par longueur d’onde.','Rayleigh–Jeans seulement lorsque hc/(λkBT)≪1.'],
    ['Chercher un maximum par dérivation.','Changer de variable avec son jacobien.','Intégrer une densité spectrale pour obtenir une puissance.'],
    ['Choisir 300 K et situer le maximum par rapport au visible.','Choisir 5800 K, puis doubler T : prévoir λmax et le flux total.','Comparer Planck et Rayleigh–Jeans aux grandes et petites longueurs d’onde.'],
    'Entrée Sup : spectre, longueurs d’onde et énergie rayonnée.',
    'Outils Spé : intégrales et changement de variable ; modèle statistique complet comme prolongement.',
    'Comptage des modes photoniques et photométrie pondérée par l’œil.',
    'Un maximum associé à une variable spectrale précise et une fraction de puissance avec ses bornes.'),
 'occupations':guide(
    'Une occupation moyenne compte les particules dans un état quantique. Comparer fermions, bosons et gaz dilué, puis imposer une densité totale dans les modes Fermi ou Bose. La température T et le potentiel chimique μ n’ont pas le même rôle : à nombre fixé, μ doit être déterminé.',
    ['T en K ; n en m⁻³ ; ε : énergie d’un état ; μ : potentiel chimique en J.','Comparaison : ε/(kBT) et μ/(kBT) sont des paramètres sans dimension.','Mode Bose : masse en unités atomiques u ; mode Fermi : électrons ; EF et Tc sont des repères du modèle.'],
    ['Gaz idéaux homogènes 3D, sans interactions ; états internes précisés dans chaque mode.','Une occupation n’est pas une densité de probabilité normalisée sur toutes les énergies.'],
    ['Sommer une série géométrique ou deux occupations possibles.','Intégrer avec une densité d’états.','Résoudre une contrainte de nombre et comparer des échelles thermiques.'],
    ['En comparaison, prendre μ/(kBT)=−6 : retrouver la limite diluée commune.','Choisir Fermi et comparer T à TF.','Choisir Bose de part et d’autre de Tc et compter séparément le condensat.'],
    'Entrée Sup : probabilités, nombres d’occupation et unités.',
    'Outils Spé : intégrales et contraintes ; Fermi/Bose sont des prolongements du socle statistique MP cité.',
    'Grand canonique, condensation et développement de Sommerfeld : approfondissements guidés.',
    'Une occupation par état distinguée du nombre total, avec μ déterminé lorsque la densité est imposée.'),
 'ising':guide(
    'Chaque spin vaut +1 ou −1 ; J>0 favorise les voisins alignés. La température réduite θ=kBT/J compare agitation et interaction. Compter exactement les configurations d’une chaîne, puis observer une simulation sur un carré : distinguer résultat fini, limite théorique et estimation numérique.',
    ['N : nombre de spins de la chaîne ; q : nombre de paires de parois entre domaines.','Carré de côté L sites, N=L² ; θ sans dimension ; énergie en unités de J.','Un balayage visite les sites ; préparation avant mesure ; graine pour reproduire les tirages.'],
    ['Couplage ferromagnétique entre voisins, champ nul et bords périodiques.','Onsager/Yang : référence du carré infini ; simulation : réseau fini, mesures corrélées.'],
    ['Dénombrer avec des coefficients binomiaux.','Former une partition et ses dérivées.','Comparer des moyennes, des fluctuations et des tailles de système.'],
    ['Choisir la chaîne et retrouver pourquoi le nombre de parois est pair.','Passer au carré près de θc et comparer deux états initiaux.','Augmenter durée ou taille, puis distinguer ⟨m⟩, ⟨|m|⟩ et aimantation spontanée.'],
    'Entrée Sup : dénombrement, probabilités et moyenne de variables ±1.',
    'Outils Spé : combinatoire et Boltzmann ; Ising constitue un prolongement du programme MP.',
    'Transition d’Onsager, limite thermodynamique et simulation Monte-Carlo corrélée.',
    'Un résultat exact de chaîne séparé d’une mesure sur carré fini, sans confondre un pic fini avec une preuve de transition.')
}
for lab,g in LAB_GUIDES.items():
    g['lesson_numbers']=[i+1 for i,l in enumerate(LESSONS) if l['lab']==lab]

LAB_OBJECTS = {'maxwell': ['T₁,T₂ sont les températures en K ; M la masse molaire en g·mol⁻¹. N_A est la constante '
             'd’Avogadro ; m=M/N_A est la masse moléculaire après conversion de M en kg·mol⁻¹.',
             'n est la densité de particules en m⁻³, réglée par son logarithme décimal ; V₁,V₂ sont les '
             'volumes en L et S l’aire du trou en mm².',
             'N₁,N₂ comptent les particules ; τ est le temps caractéristique de fuite et t/τ le temps '
             'réduit. kB est la constante de Boltzmann.'],
 'canonique': ['ε est l’écart de niveaux en meV et T la température en K ; kB est la constante de '
               'Boltzmann. β=1/(kBT) est l’inverse de l’énergie thermique.',
               'N compte les sites indépendants ; U est l’énergie moyenne et C la capacité thermique, '
               'dérivée de U par rapport à T.',
               'g compte les microétats du niveau ε dans le modèle à trois niveaux 0,ε,2ε. La probabilité '
               'd’un niveau additionne celles de ses microétats.'],
 'gaz': ['T est la température en K, L le côté de la boîte en nm et m la masse en multiples de la masse '
         'électronique mₑ. h est la constante de Planck et kB celle de Boltzmann.',
         'Nmax est le nombre de modes unidimensionnels conservés ; n est la densité de particules en m⁻³. '
         'E_L est l’échelle d’énergie de confinement.',
         'λ_th=h/√(2πmkBT) est la longueur d’onde thermique ; nλ_th³ compare cette longueur à l’espacement '
         'des particules. U est l’énergie moyenne par particule.'],
 'oscillateur': ['ν est la fréquence en THz et T la température en K ; h est la constante de Planck et kB '
                 'celle de Boltzmann. n≥0 compte les quanta d’excitation.',
                 'U est l’énergie moyenne et C sa dérivée par rapport à T à fréquence fixée. hν est '
                 'l’écart entre deux niveaux voisins.',
                 'r est le nombre de termes quadratiques supplémentaires d’un modèle classique ayant déjà '
                 'trois termes cinétiques ; il ne compte pas les niveaux de l’oscillateur 1D.'],
 'spins': ['T est la température en K et B le champ en T ; μ est la norme du moment en multiples du '
           'magnéton de Bohr μB, en J·T⁻¹. kB est la constante de Boltzmann.',
           'x=μB/(kBT) compare énergie magnétique et énergie thermique ; le moment moyen est donné en '
           'multiples de μ.',
           'C_B est la capacité thermique à champ fixé ; la susceptibilité par spin est la dérivée du '
           'moment moyen par rapport à B.'],
 'planck': ['T est la température en K et λ la longueur d’onde en µm ; h,kB,c sont la constante de Planck, '
            'celle de Boltzmann et la célérité de la lumière.',
            'B_λ est la luminance spectrale en W·m⁻²·sr⁻¹·µm⁻¹ ; elle est rapportée à une unité de '
            'longueur d’onde, pas à une unité de fréquence.',
            'σ est la constante de Stefan–Boltzmann ; σT⁴ est le flux total par aire. La bande visible '
            'retenue est [390,780] nm.'],
 'occupations': ['T est la température en K et n la densité en m⁻³ ; ε est l’énergie d’un état et μ le '
                 'potentiel chimique en J par particule. kB est la constante de Boltzmann.',
                 'En mode comparaison, ε/(kBT) et μ/(kBT) sont sans dimension. Les occupations moyennes '
                 'sont des nombres de particules par état.',
                 'En mode Bose, la masse est en unités atomiques u ; en mode Fermi, ce sont des électrons. '
                 'E_F est l’énergie de Fermi, T_F=E_F/kB sa température et T_c la température critique de '
                 'Bose du modèle.'],
 'ising': ['sᵢ=±1 est le spin du site i ; J>0 l’énergie de couplage et kB la constante de Boltzmann. '
           'θ=kBT/J est la température réduite.',
           'N est le nombre de sites de la chaîne ; 2q compte ses parois de domaines. Le carré a L sites '
           'par côté et N=L² sites au total.',
           'm est l’aimantation par site ; un balayage Monte-Carlo tente en moyenne une mise à jour par '
           'site. La graine fixe les tirages ; la préparation sert à réduire l’influence de l’état '
           'initial.']}
for _lab, _objects in LAB_OBJECTS.items():
    LAB_GUIDES[_lab]["objects"] = _objects

LAB_PURPOSES = {'maxwell': 'Passer des vitesses moléculaires à la pression, puis comparer une fuite et un échange entre '
            'deux enceintes.',
 'canonique': 'Utiliser les poids de Boltzmann pour relier populations, énergie moyenne et capacité '
              'thermique.',
 'gaz': 'Distinguer effet du confinement, troncature numérique des modes et limite classique du gaz.',
 'oscillateur': 'Expliquer le gel des excitations et retrouver l’équipartition à température élevée.',
 'spins': 'Relier les deux niveaux magnétiques à la saturation, à la loi de Curie et au maximum de '
          'capacité thermique.',
 'planck': 'Lire un spectre par longueur d’onde et calculer la fraction de rayonnement dans une bande '
           'précisée.',
 'occupations': 'Reconnaître le domaine où les statistiques quantiques s’approchent de Maxwell–Boltzmann '
                'et comparer Fermi et Bose.',
 'ising': 'Comparer comptage exact, simulation et limite infinie pour préciser ce que signifie un ordre '
          'magnétique.'}
for _lab, _purpose in LAB_PURPOSES.items():
    LAB_GUIDES[_lab]["purpose"] = _purpose
    LAB_GUIDES[_lab]["levels"]["sup"] = LAB_GUIDES[_lab]["levels"]["sup"].removeprefix("Entrée Sup : ")
