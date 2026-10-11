# Dix-huit séances d’électricité et technologies

Pour chaque TP : prévoir le résultat, effectuer les trois manipulations du guide puis justifier par les lois du circuit ou la fonction de transfert.

## Séance 01 — Commande & Numérique

### Séparer l’entrée et l’état initial

Expliquer pourquoi deux systèmes recevant la même entrée peuvent avoir des réponses différentes au départ.

**Objets et paramètres**

- t : temps en secondes ; y(t) : tension de sortie en volts ; y₀=y(0) : état initial.
- E : tension constante de l’échelon en volts ; K : gain statique sans unité ; τ : constante de temps en secondes.
- p : variable complexe de Laplace, en s⁻¹ ; Y(p) : transformée unilatérale de y ; H(p) : fonction de transfert à état initial nul.

**Repères** — Sup : Physique sup : transitoire du premier ordre et condition initiale. Spé : SI PT/PSI : fonction de transfert et réponse temporelle ; les formules de réponse sont fournies. Au-delà : Calcul de transformées et inversion de Laplace : accompagnement mathématique, non exigé en SI.

1. Choisir y₀=0 et lire la valeur finale KE.
2. Mettre y₀=3 et comparer les trois courbes.
3. Choisir y₀<0 et vérifier que la sortie initiale vaut y₀.

**À justifier :** La réponse totale commence en y₀ ; la contribution libre disparaît et la sortie tend vers KE.

### Relier résonance et réponse d’un second ordre

Relier le pic de gain, le dépassement et l’amortissement d’un même système.

**Objets et paramètres**

- ω₀ : pulsation propre en rad/s ; ζ : coefficient d’amortissement sans unité ; K : gain statique.
- p : variable de Laplace ; j : unité imaginaire ; ω : pulsation d’une excitation sinusoïdale en rad/s.
- H(p) : transfert du second ordre ; G=20 log₁₀|H(jω)| : gain en dB ; φ=arg H(jω) : phase, affichée en degrés.
- t : temps en secondes ; y : sortie normalisée après un échelon d’amplitude 1 ; les pôles sont les racines du dénominateur.

**Repères** — Sup : Physique et SI sup : réponses du premier et du second ordre, filtres et régimes sinusoïdaux. Spé : SI PT/PSI : comportement temporel et fréquentiel ; physique spé : comparaison des filtrages. Au-delà : Démonstration par inversion de Laplace et analyse générale des pôles.

1. Prendre ζ=0,2 et repérer le pic du gain.
2. Passer à ζ=0,8 : le pic a disparu, le dépassement subsiste.
3. Choisir ζ=1 et lire la réponse critique.

**À justifier :** La résonance disparaît dès ζ≥1/√2, tandis que le dépassement disparaît seulement pour ζ≥1.

## Séance 02 — Commande & Numérique

### Mesurer l’effet d’une contre-réaction

Quantifier la réduction de sensibilité obtenue par un retour négatif.

**Objets et paramètres**

- e : entrée unité ; s : sortie ; ε=e−βs : erreur à l’entrée de la chaîne directe.
- μ : gain statique direct ; β : gain du retour ; G=s/e : gain statique fermé. Les amplitudes sont normalisées.
- δ : variation relative de μ ; μ₂=μ(1+δ) : gain modifié ; τ : constante de temps directe en secondes.
- t : temps en secondes ; p : variable de Laplace ; Sμ=(μ/G)dG/dμ : sensibilité relative.

**Repères** — Sup : SI sup : schéma-blocs et rôle de l’asservissement. Spé : SI PT/PSI : précision, rapidité et comportement d’une boucle fermée. Au-delà : Sensibilités logarithmiques et robustesse quantitative.

1. Choisir β=0 et comparer les variations de μ et G.
2. Fermer le retour avec β=0,1.
3. Augmenter |δ| et lire l’écart à l’approximation locale.

**À justifier :** Un grand produit μβ réduit la variation relative de G, mais change aussi sa valeur statique.

### Reprendre le moteur X de la fiche P17

Retrouver les gains et les constantes de temps des deux schémas du TP P17.

**Objets et paramètres**

- E : amplitude de l’échelon de tension, en volts ; μ : gain sans unité de l’amplificateur.
- K₀ : gain statique du moteur seul, en rad·s⁻¹/V ; τ : constante de temps du moteur, en secondes.
- Ω : vitesse ouverte et Ω′ : vitesse fermée, en rad/s ; β : gain du capteur, en V/(rad/s).
- ε=E−βΩ′ : erreur en volts ; T₀=μK₀ et T₀′ : gains statiques ouvert et fermé ; τ′ : constante de temps fermée.
- t : temps en secondes ; p : variable de Laplace ; T(p) et T′(p) : transferts tension-vitesse.

**Repères** — Sup : SI sup : moteur modélisé, premier ordre et retour négatif. Spé : SI PT/PSI : précision et rapidité d’un asservissement. Au-delà : Inversion de Laplace : formule accompagnée, non exigée en SI.

1. Lire Ω∞ et Ω′∞ avec les réglages initiaux.
2. Vérifier τ′=τ/(1+μβK₀).
3. Mettre β=0 : les deux courbes se confondent.

**À justifier :** Le retour réduit la constante de temps et le gain tension-vitesse ; ces deux réductions ont le même facteur.

## Séance 03 — Commande & Numérique

### Relier courant et vitesse d’un moteur continu

Expliquer le démarrage d’un moteur par ses bilans électrique et mécanique.

**Objets et paramètres**

- U : tension d’alimentation en volts ; R : résistance en ohms ; L : inductance, réglée en mH puis convertie en H.
- i : courant en ampères ; Ω : vitesse angulaire en rad/s ; k : constante du moteur en V·s/rad et N·m/A.
- J : inertie, réglée en 10⁻³ kg·m² ; b : frottement visqueux, réglé en 10⁻³ N·m·s ; Cᵣ : couple résistant en N·m.
- ki : couple moteur ; kΩ : force contre-électromotrice ; t : temps en secondes ; i∞ et Ω∞ : valeurs permanentes.

**Repères** — Sup : SI sup : conversion électromécanique et bilans ; physique sup : inductance et régime transitoire. Spé : SI PT/PSI : modèle de moteur à courant continu et chaîne d’énergie. Au-delà : Résolution complète du système couplé à deux états, fournie par la simulation.

1. Démarrer à vide ; lire le courant sur la vue courte de durée 8L/R.
2. Ajouter Cᵣ et comparer les vitesses finales.
3. Augmenter J pour ralentir le démarrage mécanique.

**À justifier :** La vitesse réduit le courant par la tension kΩ ; une charge plus forte augmente le courant permanent et réduit la vitesse.

### Suivre une consigne avec un correcteur PI

Observer comment l’action intégrale réduit l’erreur constante et réagit à une limite de commande.

**Objets et paramètres**

- r : consigne ; y : sortie ; e=r−y : erreur. Ces grandeurs sont normalisées.
- K : gain du procédé ; τ : constante de temps en secondes ; Kₚ : gain proportionnel ; Tᵢ : temps d’intégration en secondes.
- v : action intégrale ; uₘₐₓ : limite de commande ; u : commande limitée ; Kₚe+v : commande demandée.
- t : temps en secondes ; p : variable de Laplace ; C(p)=Kₚ(1+1/(Tᵢp)) : correcteur PI.

**Repères** — Sup : SI sup : écart consigne-sortie et action proportionnelle. Spé : SI PT/PSI : correcteurs proportionnel et proportionnel intégral. Au-delà : Saturation et correction de l’accumulation intégrale par retour de saturation.

1. Observer le suivi avec une consigne accessible.
2. Choisir r=3 et uₘₐₓ=0,5.
3. Activer la correction et comparer le retour après la baisse de consigne.

**À justifier :** Une intégrale active élimine l’erreur constante seulement si la commande nécessaire est disponible ; la saturation peut accumuler v.

## Séance 04 — Commande & Numérique

### Lire les marges d’une boucle ouverte

Relier les marges lues sur la boucle ouverte à la stabilité de la boucle fermée.

**Objets et paramètres**

- K : gain ouvert ; τ₁, τ₂ et τ₃ : constantes de temps en secondes ; L(p) : transfert de boucle ouverte.
- p : variable de Laplace ; j : unité imaginaire ; ω : pulsation en rad/s ; ωc : pulsation où |L(jωc)|=1.
- ωπ : pulsation où la phase atteint −180° ; Mφ : marge de phase en degrés ; Mg : marge de gain en dB.
- t : temps en secondes ; y : sortie normalisée après un échelon unité ; les pôles fermés sont les racines de 1+L(p)=0 après réduction.

**Repères** — Sup : SI sup : fonctions de transfert et diagrammes fréquentiels. Spé : SI PT/PSI : marges de stabilité et correction des systèmes asservis. Au-delà : Calcul algébrique général des pôles ; critères de Routh et de Nyquist hors programme SI.

1. Partir de K=2 et lire les marges.
2. Augmenter K et observer la diminution de marge.
3. Prendre trois constantes égales et franchir K=8.

**À justifier :** Pour ce modèle, une marge de gain négative accompagne des pôles fermés à partie réelle positive.

### Atténuer le mouvement du sol par un retour

Reconstituer le retour de l’exercice sismique P17 et évaluer son effet selon la fréquence.

**Objets et paramètres**

- x₀ : déplacement du sol ; x : déplacement de la masse, calculés en mètres et affichés en mm ; F : force de l’actionneur en newtons.
- ωᵣ : pulsation propre en rad/s ; α : coefficient force-déplacement en m/N ; η : gain du dérivateur en N·s/m.
- I(p)=ωᵣ²/(p²+ωᵣ²) : transfert sans actionneur ; G(p)=x(p)/x₀(p) : transfert contrôlé ; p : variable de Laplace.
- c=αηωᵣ² : coefficient de vitesse en s⁻¹ ; ζ=c/(2ωᵣ) : amortissement ; f : fréquence du sol en Hz ; A₀ : son amplitude, réglée en mm.
- M : masse en kg ; l : longueur en m ; C : raideur de rotation en N·m/rad ; g : pesanteur en m/s². α=l²/(C−Mgl) et ωᵣ²=(C−Mgl)/(Ml²).
- t : temps en secondes ; j : unité imaginaire ; ω : pulsation du balayage fréquentiel en rad/s.

**Repères** — Sup : Physique sup : oscillateur harmonique et résonance ; SI sup : schéma-blocs. Spé : SI PT/PSI : boucle de contrôle ; application à un exercice de P17, calcul fourni. Au-delà : Isolation vibratoire active et limites d’un dérivateur idéal.

1. Choisir η=0 et comparer masse et sol.
2. Augmenter η pour amortir le voisinage de la résonance.
3. Augmenter f et comparer les transmissions avec et sans contrôle.

**À justifier :** Le contrôle amortit la résonance mais modifie aussi le numérateur du transfert ; son effet n’est pas une atténuation uniforme.

## Séance 05 — Commande & Numérique

### Distinguer repliement et quantification

Identifier séparément l’ambiguïté temporelle des échantillons et l’erreur d’un convertisseur.

**Objets et paramètres**

- f : fréquence du signal en Hz ; fₑ : fréquence d’échantillonnage en Hz ; Tₑ=1/fₑ : période en secondes ; k : indice entier des échantillons.
- A : amplitude en volts ; φ : phase initiale en degrés ; u(t)=A sin(2πft+φ) : signal.
- N : nombre de bits ; Vₘₐₓ : demi-plage bipolaire en volts ; q=2Vₘₐₓ/2ᴺ : pas de conversion ; code : entier de 0 à 2ᴺ−1.
- t : temps en secondes ; fₐ : fréquence repliée dans [0,fₑ/2] ; erreur RMS : racine de la moyenne des erreurs au carré.

**Repères** — Sup : Physique PTSI : acquisitions et analyse des signaux, première approche du spectre. Spé : Physique PT/PSI : échantillonnage, repliement, conversion analogique-numérique. Au-delà : Modèle statistique q/√12 et reconstruction du signal limité en bande.

1. Échantillonner 150 Hz à 1000 Hz.
2. Passer à f=800 Hz et observer l’alias de 200 Hz.
3. Réduire N puis dépasser la plage du convertisseur.

**À justifier :** Changer N modifie les niveaux mais ne résout pas le repliement ; augmenter fₑ ne supprime pas la saturation.

### Construire un filtre à mémoire finie

Construire un filtrage passe-bas avec une somme finie de valeurs retardées.

**Objets et paramètres**

- xₖ : entrée ; yₖ : sortie ; k : indice entier ; N : nombre de coefficients de la moyenne glissante.
- fₑ : fréquence d’échantillonnage en Hz ; Tₑ=1/fₑ : période ; ν=f/fₑ et νᵦ=fᵦ/fₑ : fréquences relatives du signal et du bruit.
- hₖ : réponse à x₀=1 puis xₖ=0 ; z : variable complexe de la transformée en z ; z⁻¹ représente un retard d’un échantillon.
- j : unité imaginaire ; H(z) : transfert ; f : fréquence en Hz ; le retard de groupe exprime le décalage de l’enveloppe.

**Repères** — Sup : Informatique et physique sup : sommes, suites et acquisition de signaux. Spé : Physique PT/PSI : réalisation numérique d’un filtre passe-bas. Au-delà : Fonction en z et retard de groupe général.

1. Observer les N termes de hₖ.
2. Choisir N=10 et νᵦ=0,3 pour annuler le bruit.
3. Augmenter N et repérer la perte de signal utile.

**À justifier :** Une fenêtre plus longue réduit certaines fréquences et accroît le retard ; son effet dépend de la fréquence du signal.

## Séance 06 — Commande & Numérique

### Suivre la mémoire d’un filtre récursif

Relier une récurrence simple à sa mémoire, sa réponse impulsionnelle et sa stabilité.

**Objets et paramètres**

- xₖ : entrée ; yₖ : sortie ; k : indice entier ; a : coefficient réel de retour et pôle dans le plan z.
- N : nombre de termes affichés ; hₖ : réponse à l’impulsion discrète x₀=1 puis 0.
- z : variable complexe de la transformée en z ; z⁻¹ : retard d’un échantillon ; j : unité imaginaire.
- H(z) : transfert ; f/fₑ : fréquence relative ; e⁻¹ : seuil servant à mesurer une durée de décroissance.

**Repères** — Sup : Mathématiques sup : suites et séries géométriques ; informatique : récurrences. Spé : Physique PT/PSI : filtrage numérique et comparaison à un passe-bas analogique. Au-delà : Stabilité entrée bornée-sortie bornée et plan z.

1. Prendre a=0,8 et comparer impulsion et échelon.
2. Approcher a=0,98 pour prolonger la mémoire.
3. Choisir a=−0,8 : la mémoire alterne de signe.

**À justifier :** Le signe de a change la forme du filtrage ; |a| proche de 1 prolonge la mémoire.

### Comparer trois discrétisations d’un passe-bas

Retrouver le calcul de P17 et distinguer condition initiale, impulsion discrète et entrée maintenue.

**Objets et paramètres**

- τ : constante de temps du filtre, réglée en ms ; Tₑ : période d’échantillonnage, réglée en µs ; tₖ=kTₑ.
- xₖ : entrée au pas k ; yₖ : sortie ; y₀ : état initial ; x₀=0 dans les trois comparaisons.
- p : variable de Laplace ; z : variable de la transformée en z ; z⁻¹ représente un retard ; H(p)=1/(1+τp).
- a=τ/(τ+Tₑ) et b=Tₑ/(τ+Tₑ) : coefficients d’Euler implicite ; aB=(2τ−Tₑ)/(2τ+Tₑ) : pôle bilinéaire ; aZ=exp(−Tₑ/τ) : pôle sous maintien exact.
- ZOH : maintien d’ordre zéro, donc une entrée constante sur chaque intervalle ; les amplitudes sont normalisées.

**Repères** — Sup : Physique sup : premier ordre ; informatique : récurrence et approximation. Spé : Physique PT/PSI : filtre numérique passe-bas ; SI PSI : passage à un correcteur discret. Au-delà : Transformée en z, transformation bilinéaire et comparaison des conventions temporelles.

1. Choisir τ=1 ms, Tₑ=50 µs et le cas y₀=1.
2. Lire y₁=1 puis y₂=20/21 pour Euler.
3. Choisir l’impulsion à état initial nul et comparer y₁=1/21.

**À justifier :** Le même x₁ ne donne pas la même sortie si y₀ change ; les trois méthodes convergent quand Tₑ/τ diminue.

## Séance 07 — Commande & Numérique

### Placer les pôles et les zéros dans le plan z

Relier les pôles à la durée d’une oscillation et les zéros à un creux du spectre.

**Objets et paramètres**

- z : variable complexe du temps discret ; j : unité imaginaire ; r : module des deux pôles ; θ : leur angle, réglé en degrés.
- ψ : angle des deux zéros, réglé en degrés ; les calculs trigonométriques utilisent les radians.
- H(z) : transfert ; c : facteur choisi pour H(1)=1 ; hₖ : réponse impulsionnelle ; k : indice entier ; N : nombre de termes.
- f/fₑ : fréquence relative, égale à l’angle en radians divisé par 2π ; le cercle unité est l’ensemble |z|=1.

**Repères** — Sup : Mathématiques sup : nombres complexes et suites récurrentes. Spé : Physique PT/PSI : filtrage numérique ; lien avec les observations expérimentales. Au-delà : Placement de pôles et zéros, stabilité dans le plan z.

1. Lire r et observer la décroissance de hₖ.
2. Approcher r=0,98 pour prolonger les oscillations.
3. Déplacer ψ et suivre le creux du gain.

**À justifier :** Un zéro placé sur le cercle unité annule une fréquence ; des pôles proches du cercle prolongent la réponse.

### Transmettre un message par modulation d’amplitude

Retrouver les trois raies de P19 et expliquer les limites d’un détecteur d’enveloppe.

**Objets et paramètres**

- f : fréquence du message en Hz ; F : fréquence de la porteuse en Hz ; F/f : rapport réglable.
- U : amplitude de la porteuse en volts ; m : taux de modulation ; uAM : tension modulée en volts.
- Pour multiplier deux tensions : Kₘ est le gain du multiplicateur en V⁻¹, UBF et UHF leurs amplitudes en volts ; ici U=Kₘ UBF UHF.
- t : temps en secondes ; RC : constante de temps du détecteur en secondes ; le réglage donne RC sous forme d’une fraction de 1/f.
- R : résistance et C : capacité du détecteur ; la diode charge le condensateur aux crêtes positives. La puissance indiquée utilise une autre résistance de référence de 1 Ω.
- U[1+m cos(2πft)] : enveloppe algébrique ; sa valeur absolue est l’enveloppe géométrique quand elle change de signe.

**Repères** — Sup : Physique sup : signaux sinusoïdaux, spectre et filtre passe-bas. Spé : Physique PSI : modulation-démodulation et démodulation synchrone ; P19 : exemple de détection d’enveloppe. Au-delà : Détection d’enveloppe diode-RC, rendement de puissance et surmodulation.

1. Choisir m=0,6 et lire les amplitudes des trois raies.
2. Changer RC pour observer ondulation et retard.
3. Passer à m=1,3 et comparer enveloppes algébrique et détectée.

**À justifier :** Les raies latérales ont chacune l’amplitude mU/2 ; pour m>1, un détecteur d’enveloppe perd le signe du message.

## Séance 08 — Circuits & conversion

### Équilibrer un pont de Wheatstone

Déterminer une résistance inconnue en annulant la tension d’un détecteur.

**Objets et paramètres**

- A et C sont les bornes d’alimentation; B et D sont les points milieux. Le potentiel de C est pris égal à zéro.
- E=UAC est la tension d’alimentation (V). R₁ relie A à B, R₂ relie B à C, R₃ relie A à D, R₄ relie D à C (Ω).
- Rm est la résistance d’entrée du voltmètre branché entre B et D (kΩ dans le réglage, Ω dans les formules). UBD=VB−VD est sa tension (V).
- Rth est la résistance de Thévenin vue de B et D (Ω). La sensibilité dUBD/dR₄ se mesure en V/Ω.

**Repères** — Sup : PTSI, physique : circuits résistifs, conventions de tension et mesure indirecte. Spé : PSI/PT : réinvestir les circuits et analyser l’influence d’un instrument; applications aux capteurs en SI. Au-delà : Ponts d’impédances, jauges de contrainte et mesure différentielle.

1. Choisir quatre résistances de 1 kΩ et vérifier UBD=0.
2. Augmenter R₄ de 10 % et prévoir le signe de UBD.
3. Réduire la résistance du voltmètre et comparer la tension au zéro du pont.

**À justifier :** L’équilibre dépend d’un rapport de résistances; la charge du voltmètre modifie la sensibilité, pas le zéro.

### Une ligne : propagation et réflexion

Relier le profil de tension dans un câble à la charge et aux pertes.

**Objets et paramètres**

- x est la position dans le câble, de 0 à d; d est sa longueur (m).
- f est la fréquence (MHz au réglage, Hz dans les formules); ω=2πf est la pulsation (rad/s). E est l’amplitude crête à l’entrée (V).
- R, L, G et C sont les paramètres par mètre : résistance (Ω/m), inductance (H/m), conductance (S/m), capacité (F/m). Les réglages emploient mΩ/m, µH/m, µS/m et pF/m.
- Zcharge est la résistance terminale (Ω). Z₀ est l’impédance caractéristique (Ω), γ=α+jβ la constante de propagation (m⁻¹). α est l’atténuation et β le nombre d’onde.
- V(x) et I(x) sont des amplitudes complexes crêtes (V, A). Γ est le coefficient de réflexion sans unité; P(x) est la puissance active (W).

**Repères** — Sup : PTSI, physique : célérité, retard, phase; les équations distribuées sont un prolongement. Spé : PSI, physique des ondes : câble coaxial et propagation; PT : réinvestissement de réflexion et d’ondes stationnaires. Au-delà : Équations des télégraphistes, impédance d’entrée et adaptation des câbles réels.

1. Choisir L=0,25 µH/m et C=100 pF/m; estimer √(L/C).
2. Comparer les charges de 50 Ω et 200 Ω.
3. Augmenter R et G, puis lire la diminution de puissance entre les extrémités.

**À justifier :** Une ligne adaptée réfléchit peu; une désadaptation module le profil. Les pertes abaissent la puissance transmise.

## Séance 09 — Circuits & conversion

### RLC : charge, oscillation et amortissement

Identifier le régime d’un RLC et vérifier son bilan d’énergie.

**Objets et paramètres**

- E est l’échelon de tension (V). R est la résistance série totale (Ω), L l’inductance (mH au réglage, H dans les calculs), C la capacité (µF au réglage, F dans les calculs).
- t est le temps depuis la fermeture (s, affiché en ms); uC est la tension du condensateur (V) et i le courant de la maille (A).
- ω₀=1/√(LC) est la pulsation propre (rad/s), ζ=R√(C/L)/2 le rapport d’amortissement sans unité.
- EC=CuC²/2 et EL=Li²/2 sont les énergies stockées (J); W est le travail de la source et QJ l’énergie dissipée (J).

**Repères** — Sup : PTSI, physique : oscillateurs amortis et circuits à deux éléments de stockage; mathématiques : EDO linéaire. Spé : PSI/PT : réinvestissement des pôles, de l’amortissement et des bilans. Au-delà : Identification des pertes réelles et amortissements dépendant de la fréquence.

1. Comparer R=20 Ω et R=300 Ω à L et C fixés.
2. Calculer 2√(L/C), puis choisir ce voisinage.
3. Comparer le travail fourni, les deux stockages et la dissipation cumulée.

**À justifier :** Une résistance faible autorise les échanges oscillants; une résistance forte les amortit. Le bilan inclut toujours la source.

### RLC sinusoïdal : trouver la résonance

Trouver une résonance en intensité et relier sa phase à sa puissance.

**Objets et paramètres**

- U est la tension efficace imposée (V). R, L et C sont la résistance (Ω), l’inductance (mH) et la capacité (µF) du circuit série.
- f₀ est la fréquence propre (Hz); le réglage f/f₀ est sans unité. ω=2πf est en rad/s.
- Z est l’impédance complexe (Ω), I le courant efficace complexe (A), φ=arg I−arg U le déphasage du courant (° dans l’affichage).
- Q=ω₀L/R est le facteur de qualité sans unité; Δf est la largeur à mi-puissance (Hz); p(t) et sa moyenne P sont en W.

**Repères** — Sup : PTSI, physique : régime sinusoïdal et résonance; mathématiques : nombres complexes. Spé : PSI/PT : exploitation expérimentale d’une résonance; PSI : puissance sinusoïdale. Au-delà : Distinguer résonance en courant et maximum de tension aux bornes du condensateur.

1. Choisir f/f₀=1 et vérifier la phase nulle.
2. Passer à 0,5 puis à 2; comparer avance et retard du courant.
3. Multiplier R par dix et observer la largeur de la résonance.

**À justifier :** À la résonance en intensité, le circuit série est résistif. Augmenter R réduit le maximum et élargit la bande.

## Séance 10 — Circuits & conversion

### Mesurer une impédance avec un GBF

Estimer une impédance sans confondre charge de la voie et incertitude de lecture.

**Objets et paramètres**

- R, L et C définissent le dipôle série choisi (Ω, mH, µF). f est la fréquence (Hz), E l’amplitude à vide du GBF (V), Rs sa résistance de sortie (Ω).
- R₀ est le résistor de référence en série (Ω). V₁ et V₂ sont les amplitudes complexes crêtes lues avant R₀ et aux bornes du dipôle (V).
- Rentrée et Centrée décrivent chaque voie d’oscilloscope (kΩ et pF au réglage). fb est sa bande passante (kHz au réglage).
- Z est l’impédance du dipôle (Ω), Yvoie l’admittance d’une voie (S). urel est l’incertitude-type relative de chaque amplitude (%); u(|Zmes|) est l’incertitude-type propagée (Ω).
- Δt est le retard de la voie 2 sur la voie 1 (µs); une valeur négative signifie une avance.

**Repères** — Sup : PTSI, formation expérimentale : GBF, oscilloscope, résistance d’entrée, bande passante et incertitudes. Spé : PSI/PT : mesure d’impédance, déphasage et interprétation de données. Au-delà : Voies désappariées et propagation complète incluant les incertitudes de phase.

1. Observer les deux voies pour un dipôle RC à 1 kHz.
2. Réduire la résistance d’entrée et comparer Zmes à Z corrigée.
3. Monter la fréquence jusqu’à la bande passante et lire la baisse d’amplitude.

**À justifier :** Le rapport des voies annule une réponse commune, mais la voie 2 reste une charge parallèle du dipôle.

### Redresser les deux alternances

Identifier les diodes conductrices et distinguer moyenne, valeur efficace et pertes.

**Objets et paramètres**

- E est la crête de tension alternative par enroulement (V), f sa fréquence (Hz), t le temps (s). uAB=E sin(2πft) est la tension entre A et B (V).
- R est la résistance de charge (Ω). Vd est le seuil de chaque diode (V). D₁, D₂, D₃, D₄ sont les diodes du pont.
- uR et iR sont la tension et le courant de charge (V, A); isource est le courant alternatif (A). La moyenne et la valeur efficace de uR sont en V.
- Le comparatif à point milieu utilise deux demi-enroulements opposés de même crête E; une seule diode conduit par alternance. Pcharge et Pdiodes sont des puissances moyennes (W).

**Repères** — Sup : PTSI : application documentaire des mailles, valeurs efficaces et non-linéarités; le redresseur n’est pas un cours autonome exigible. Spé : PSI, physique §5.4 : réinvestissement des interrupteurs idéaux dans un autre convertisseur. PT : lien possible avec des systèmes étudiés en SI. Au-delà : Commutation réelle, résistance source et redressement filtré.

1. Prendre Vd=0 et vérifier que les deux sorties se superposent.
2. Prendre Vd=0,7 V et compter les chutes dans chaque montage.
3. Réduire E à 2 V et observer les intervalles bloqués.

**À justifier :** La polarité de charge est conservée; le pont traverse deux diodes, le point milieu une seule.

## Séance 11 — Circuits & conversion

### Doubleur : charger deux condensateurs

Comprendre la charge alternée de deux condensateurs et l’effet de la charge résistive.

**Objets et paramètres**

- E et f sont la crête de tension alternative (V) et sa fréquence (Hz). Le point milieu des condensateurs est relié à un pôle de cette source.
- C₁ est la capacité supérieure et C₂ la capacité inférieure (µF au réglage). uC₁=Vhaut−Vmilieu et uC₂=Vmilieu−Vbas sont positives en fonctionnement normal (V).
- R est la résistance entre les deux extrémités (Ω); Rs est la résistance série source (Ω); Vd est le seuil des diodes (V).
- iD₁ et iD₂ sont les courants de recharge (A); iR=(uC₁+uC₂)/R est le courant de charge (A). L’ondulation est la différence entre maximum et minimum de sortie (V).

**Repères** — Sup : PTSI : prolongement des circuits RC et des stockages d’énergie. Spé : PSI : application des fonctions de commutation; PT/SI : mise en contexte de l’alimentation d’un système. Au-delà : Démarrage, asymétrie des capacités et conduction non linéaire.

1. Choisir une charge de 100 kΩ et lire les deux tensions de condensateur.
2. Réduire R à 1 kΩ et suivre la baisse de sortie.
3. Choisir C₁≠C₂ et comparer leurs ondulations.

**À justifier :** La tension doublée est une limite à vide. Sous charge, chaque condensateur perd de la charge pendant les intervalles sans recharge.

### Diode et RC : suivre les états de conduction

Déterminer quand une diode recharge réellement un condensateur.

**Objets et paramètres**

- usource(t)=E sin(2πft) est une tension imposée (V), de crête E (V) et fréquence f (Hz). Rs est la résistance série de la source (Ω).
- La diode conduit de la source vers la sortie; Vd est son seuil (V), iD son courant orienté positif (A).
- R et C sont en parallèle à la sortie : résistance en Ω, capacité en µF au réglage. uC=uR est leur tension (V).
- τ=RC est le temps de décharge (s). L’ondulation est une tension crête à crête (V); la fraction de conduction est un pourcentage de période.

**Repères** — Sup : PTSI, physique : RC et approche expérimentale des fonctions électroniques; diode comme modèle fourni. Spé : PSI : commutation spontanée et lissage de tension. PT/SI : analyse d’une alimentation ou d’un détecteur. Au-delà : Détection d’enveloppe, temps de conduction et impulsions de recharge.

1. Avec R=1 kΩ et C=100 µF, suivre une recharge et une décharge.
2. Passer à R=100 Ω et C=1 µF, puis comparer RC à T.
3. Afficher le courant de diode et repérer les changements d’état sur la dernière période.

**À justifier :** L’arrêt de conduction est déterminé par la continuité de tension et la compatibilité du courant.

## Séance 12 — Circuits & conversion

### Triphasé : tensions et transformateur

Appliquer le rapport de spires à un enroulement avant de calculer les grandeurs de ligne.

**Objets et paramètres**

- U₁ est la tension composée primaire efficace (V). Les tensions simples sont mesurées entre phase et neutre; les tensions composées entre phases.
- N₁ et N₂ sont les nombres de spires; m=N₂/N₁ est sans unité. D signifie triangle, Y étoile. En triangle, un enroulement reçoit Uligne; en étoile, Uligne/√3.
- Sref est la puissance apparente de référence (kVA au réglage). λ est la fraction du courant nominal; cosφ est le facteur de puissance de la charge.
- U₂₀ et U₂ sont les tensions composées secondaires à vide et sous charge (V); I₂ est le courant de ligne (A).
- Rs est la résistance série ramenée à une phase étoile secondaire (Ω); P₀ représente des pertes constantes (W). Pu, Pcuivre et η sont la puissance utile (W), les pertes cuivre (W), le rendement sans unité.

**Repères** — Sup : PTSI, physique : induction mutuelle et loi des tensions du transformateur; triphasé comme prolongement. Spé : PSI, physique : transformateur et conversion de puissance. Triphasé en PSI/PT : contexte technique, à relier au programme de SI effectivement étudié. Au-delà : Groupes horaires, essais à vide et en court-circuit, réactance de fuite.

1. Comparer D→Y à Y→Y avec le même rapport de spires.
2. Comparer vaN à vab et reconnaître le facteur √3.
3. Augmenter le courant de charge et lire les pertes cuivre ainsi que le rendement.

**À justifier :** Le rapport de tensions de ligne inclut les couplages; le rendement nécessite les pertes, pas seulement le rapport de spires.

### Onduleur : commande pleine onde ou décalée

Comparer une valeur efficace et un spectre sans confondre THD total et THD tronqué.

**Objets et paramètres**

- E est la tension continue du bus (V), f la fréquence fondamentale (Hz), T=1/f la période (s).
- δ est le retard d’allumage divisé par T, sans unité; la commande pleine onde correspond à δ=0. v vaut +E de δT à T/2, −E de (1/2+δ)T à T, zéro ailleurs.
- n est le rang harmonique, N le dernier rang affiché. An est l’amplitude crête d’une raie (V); Vn,eff=An/√2 est sa valeur efficace (V).
- Veff est la valeur efficace totale (V). THD est le rapport efficace des harmoniques hors fondamental au fondamental, sans unité, affiché en %.

**Repères** — Sup : PTSI : valeurs efficaces, décomposition fournie et filtrage d’un signal périodique. Spé : PSI, physique §5.4 : structure d’onduleur; analyse spectrale réinvestie. PT : réinvestissement de l’analyse harmonique, contexte possible en SI. Au-delà : Modulation de largeur d’impulsion, filtrage de charge et temps morts.

1. Comparer les plateaux pleine onde et δ=1/4 pour E=175 V.
2. Comparer amplitudes crêtes et valeurs efficaces du fondamental.
3. Augmenter N et lire la convergence du THD tronqué vers le THD total.

**À justifier :** La commande à T/4 réduit tension efficace et fondamental dans le même rapport. Pour ce signal idéal précis, son THD total égale celui de la pleine onde.

## Séance 13 — Circuits & conversion

### Hacheur série : alimenter une machine à courant continu

Calculer un courant d’induit avec les vrais états d’un hacheur série et de sa diode de roue libre.

**Objets et paramètres**

- E est la tension continue d’alimentation (V). Eₘ est la force contre-électromotrice de la machine (V), supposée constante sur les périodes affichées.
- R est la résistance d’induit (Ω), L son inductance (mH). i est le courant d’induit positif en fonctionnement moteur (A).
- f est la fréquence de hachage (kHz au réglage), T=1/f la période (s), α la fraction de période pendant laquelle l’interrupteur est fermé.
- u est la tension aux bornes de l’ensemble R–L–Eₘ (V). iS et iD sont les courants de source et de roue libre (A).
- imin, imax et ⟨i⟩ sont les courants minimal, maximal et moyen (A). Psource, R⟨i²⟩ et Eₘ⟨i⟩ sont les puissances moyennes (W).

**Repères** — Sup : PTSI : prolongement du RL et de la conversion électromécanique; le hacheur est abordé à partir d’un modèle fourni. Spé : PSI, physique §5.4 : hacheur série et moteur à courant continu, contenu central. PT : contexte de motorisation en SI, à distinguer du programme de physique. Au-delà : Conduction discontinue, ondulation exacte et couplage à la dynamique mécanique.

1. Lire le courant pendant fermeture et roue libre avec α=0,6.
2. Réduire L et f, puis observer l’extinction avant la fermeture suivante.
3. Augmenter Eₘ au-dessus de E et vérifier l’absence de courant moteur.

**À justifier :** La relation ⟨u⟩=αE suppose une roue libre active pendant toute l’ouverture. L’extinction impose un troisième état.

### Puissance : réduire le courant par compensation

Réduire le courant de ligne sans modifier la puissance active d’une charge.

**Objets et paramètres**

- U est la tension efficace de source (V), f sa fréquence (Hz), ω=2πf sa pulsation (rad/s).
- R et L sont la résistance (Ω) et l’inductance (mH) en série dans la charge. C est la capacité ajoutée en parallèle (µF).
- Icharge, IC et Iligne sont les courants efficaces complexes (A). Le courant positif entre dans chaque branche.
- P est la puissance active (W), Q la puissance réactive (var), S la puissance apparente (VA), P/S le facteur de puissance sans unité.
- Copt est la capacité qui annule Q (µF). La compensation peut réduire ou augmenter le module du courant de ligne.

**Repères** — Sup : PTSI : nombres complexes et puissance instantanée; la compensation est un prolongement. Spé : PSI, physique §5.1 : puissance active, facteur de puissance et adaptation énergétique. PT : contexte technique de la conversion et des systèmes électriques en SI. Au-delà : Puissance en régime déformé, harmoniques et facteur de puissance global.

1. Choisir C=0 et lire P, Q et le courant de ligne.
2. Régler C près de Copt; repérer le courant minimal.
3. Dépasser Copt et observer le retour d’un courant réactif, de signe opposé.

**À justifier :** Le minimum de courant correspond à Q=0; ajouter trop de capacité détériore le facteur de puissance.

## Séance 14 — Électronique analogique

### ALI : gain, bande et limites

Séparer trois causes de déformation d’une sortie amplifiée : bande finie, limites de tension ou de courant, et vitesse de balayage.

**Objets et paramètres**

- ALI : composant qui compare v₊ et v₋ et produit vₛ ; ces tensions et l’entrée vₑ sont en volts. La rétroaction est négative.
- G est le gain idéal demandé ; A₀ le gain différentiel statique ; β = 1/G la fraction réinjectée. Ces trois nombres sont sans unité.
- f est la fréquence d’entrée, fₜ la fréquence de transition et f_c la bande bouclée, en hertz ; le contrôle f et fₜ est affiché en kHz. ω = 2πf est en rad/s.
- E est l’amplitude crête d’entrée et Vₛₐₜ le rail positif, en volts ; Rₗ est la résistance de charge en ohms ; Iₘₐₓ le courant limite, affiché en mA.
- SR est la pente maximale de sortie, affichée en V/µs ; Vₒₛ est le décalage d’entrée affiché en mV. Le temps t est affiché en ms.
- G₀ est le gain statique bouclé sans unité. Le symbole s représente la dérivation du modèle ; j² = −1 et s = jω en régime sinusoïdal.

**Repères** — Sup : PTSI : gain complexe, ordre 1, régime sinusoïdal et loi d’Ohm. Spé : Physique PSI/PT : modèle d’ALI, produit gain–bande, saturation et limites de courant et de balayage. Au-delà : Décalage d’entrée ; il est exclu des contenus de physique PSI/PT et reste ici accompagné.

1. Choisir le régime linéaire et multiplier le gain demandé par quatre : suivre la bande.
2. Choisir « Pente limitée » puis augmenter SR : observer le retour vers une sinusoïde.
3. Choisir « Courant limité » puis augmenter Rₗ : prévoir le nouveau plafond IₘₐₓRₗ.

**À justifier :** Justifier quelle limite agit en premier et distinguer le gain linéaire d’une sortie déformée.

### Suiveur et association de filtres

Vérifier quand les fonctions de transfert de deux étages peuvent se multiplier et mesurer l’intérêt d’un suiveur.

**Objets et paramètres**

- Une cellule RC possède une résistance en série et un condensateur vers la masse ; R₁ et R₂ sont affichées en kΩ, C₁ et C₂ en nF.
- vₑ et vₛ sont les tensions d’entrée et de sortie, en volts ; E est la crête d’entrée ; f la fréquence en hertz ; t le temps affiché en ms.
- Le suiveur reçoit la première tension à sa borne positive ; sa sortie rejoint sa borne négative. Il transmet la tension et fournit le courant au second étage.
- H est le rapport complexe sortie/entrée, sans unité ; s = j2πf et j² = −1. Les fréquences propres 1/(2πRC) sont en hertz.
- Une seconde expérience statique possède un capteur de résistance interne Rₛ et une lecture de résistance Rₗ, affichées en kΩ. Leur rapport fixe la perte à la lecture.

**Repères** — Sup : Physique PTSI : intérêt des impédances lors d’une cascade, filtre du premier ordre et fonctions de transfert fournies. Spé : Physique PSI/PT : relation entrée–sortie du suiveur et association des filtres. Au-delà : Dimensionnement de la charge, des courants et de la bande d’un suiveur réel.

1. Choisir deux cellules identiques à leur fréquence propre : comparer les amplitudes.
2. Augmenter R₁ devant R₂ : observer la perturbation due au second étage.
3. Choisir la lecture d’un capteur : prévoir la perte puis la comparer au suiveur idéal.

**À justifier :** Expliquer avec les impédances et les courants pourquoi une cascade peut changer le transfert de ses étages.

## Séance 15 — Électronique analogique

### Sommateur inverseur

Construire une somme de deux signaux dont les poids et les signes sont prévisibles par la loi des nœuds.

**Objets et paramètres**

- Les tensions d’entrée vₑ₁ et vₑ₂ et la sortie vₛ sont en volts ; E₁ et E₂ sont les amplitudes crêtes des deux entrées.
- R₁ et R₂ relient les deux sources à la borne inverseuse ; Rf assure la contre-réaction. Leurs valeurs sont affichées en kΩ.
- La borne positive est à la masse. En régime linéaire idéal, la borne inverseuse est au potentiel nul sans liaison directe à la masse.
- La première entrée est à la fréquence f, en hertz ; la seconde à 2f avec une phase φ affichée en degrés. Le temps t est affiché en ms.
- Vₛₐₜ est la limite de tension de sortie, en volts ; les poids −Rf/R₁ et −Rf/R₂ sont sans unité.

**Repères** — Sup : PTSI : lois des nœuds, superposition et somme de sinusoïdes. Spé : PSI/PT : montage inverseur idéal, non-linéarité par saturation. Au-delà : Sommation à plusieurs entrées ; réalisation pratique avec bruit et impédances de source.

1. Choisir les poids 2 et 1, puis annuler chaque entrée à tour de rôle.
2. Doubler R₂ : prévoir le changement du second terme.
3. Choisir la saturation : comparer la prédiction idéale et la sortie limitée.

**À justifier :** Déterminer les coefficients d’une somme et expliquer la perte de superposition après saturation.

### Intégrer et dériver une tension

Relier une dérivée ou une intégrale à des composants et distinguer condition initiale et régime sinusoïdal.

**Objets et paramètres**

- vₑ est l’entrée, vₛ la sortie et E la crête d’entrée, en volts ; f est en hertz, ω = 2πf en rad/s et t est affiché en ms.
- L’intégrateur possède une résistance d’entrée R et une capacité de rétroaction C. Le dérivateur idéal permute ces éléments.
- Le dérivateur amélioré possède R et C en série à l’entrée, R′ et C′ en parallèle en rétroaction ; les résistances sont affichées en kΩ et les capacités en nF.
- RC et R′C′ sont des temps, en secondes. H est le transfert sans unité ; j² = −1 et s = jω en régime sinusoïdal.
- La borne positive de l’ALI est à la masse ; la contre-réaction utilise sa borne inverseuse. L’intégrateur part ici de vₛ(0) = 0.

**Repères** — Sup : Physique PTSI : conditions de fonctionnement d’un filtre comme intégrateur ou dérivateur. Spé : Physique PSI/PT : établir la relation du montage intégrateur et utiliser l’ALI idéal. Au-delà : Dérivateur amélioré étudié pas à pas ; stabilité et bruit d’une réalisation réelle.

1. Choisir l’intégrateur : vérifier le départ à zéro et la composante constante.
2. Choisir le dérivateur idéal : multiplier la fréquence par dix et observer l’amplitude.
3. Choisir le dérivateur amélioré : parcourir les deux fréquences de pôle.

**À justifier :** Établir une opération temporelle avec sa condition initiale et identifier une bande où l’approximation de dérivée convient.

## Séance 16 — Électronique analogique

### Comparateur à hystérésis

Mettre en évidence une mémoire de circuit à partir de deux seuils de basculement.

**Objets et paramètres**

- L’ALI reçoit la tension d’entrée vₑ à sa borne négative ; sa sortie vₛ prend les niveaux ±Vₛₐₜ, en volts.
- R₁ relie la sortie à l’entrée positive et R₂ cette entrée à la masse ; leurs valeurs sont affichées en kΩ. β = R₂/(R₁ + R₂) est sans unité.
- Les seuils haut et bas sont ±βVₛₐₜ, en volts. E est la crête de la rampe triangulaire et N celle de la perturbation ajoutée, en volts.
- f est la fréquence de la rampe en hertz ; la perturbation est une sinusoïde à 23f ; le temps t est affiché en ms.
- L’état initial indique le signe de la sortie avant le premier échantillon. Il reste nécessaire lorsque l’entrée demeure entre les seuils.

**Repères** — Sup : PTSI : diviseur de tension, signaux périodiques et reconnaissance d’une non-linéarité. Spé : Physique PSI/PT : cycle du comparateur à hystérésis et notion de mémoire. Au-delà : Temporisations réelles et choix d’un comparateur spécialisé.

1. Observer les basculements d’une rampe qui dépasse les deux seuils.
2. Réduire l’amplitude sous les seuils et changer l’état initial.
3. Ajouter la perturbation puis élargir l’hystérésis : expliquer les basculements obtenus.

**À justifier :** Prédire un état et un basculement avec le seuil correspondant, en tenant compte de l’histoire de l’entrée.

### Oscillateur de relaxation

Calculer une période d’oscillation à partir d’une charge exponentielle et de seuils de comparateur.

**Objets et paramètres**

- R₁ charge le condensateur C depuis la sortie de l’ALI ; R₂ relie sa borne positive à la commande continue Vₑ et R₃ à la sortie.
- Les résistances sont affichées en kΩ et C en nF. La tension du condensateur v_C, la sortie vₛ, la commande Vₑ et le niveau Vₛₐₜ sont en volts.
- τ = R₁C est le temps de charge, en secondes ; β = R₂/(R₂ + R₃) est sans unité ; h = (1 − β)Vₑ est en volts.
- Les seuils L = h − βVₛₐₜ et U = h + βVₛₐₜ sont en volts ; t₊ et t₋ sont les durées des deux états, en secondes.
- La période T = t₊ + t₋ est affichée en ms ; la fréquence 1/T est en hertz ; le rapport t₊/T est affiché en pourcentage.

**Repères** — Sup : PTSI : régime transitoire RC, exponentielles et continuité de la tension d’un condensateur. Spé : Physique PSI/PT : séquences, conditions de basculement et période d’un oscillateur de relaxation. Au-delà : Commande du rapport cyclique par tension continue et délais de comparateur.

1. Mettre la commande à zéro et vérifier les durées égales.
2. Augmenter la commande positive : prévoir quel état s’allonge.
3. Atteindre la limite |Vₑ| = Vₛₐₜ : expliquer l’arrêt sans utiliser une période finie.

**À justifier :** Déduire la période et le rapport cyclique des seuils et reconnaître une commande qui bloque les oscillations.

## Séance 17 — Électronique analogique

### Oscillateur à pont de Wien

Trouver une condition de démarrage d’oscillation et comprendre pourquoi le modèle linéaire ne fixe pas son amplitude.

**Objets et paramètres**

- Le pont comporte une branche série R₁–C₁ et une branche parallèle R₂–C₂ vers la masse ; les résistances sont affichées en kΩ, les capacités en nF.
- B est le rapport de tension du pont sans unité ; G est le gain non inverseur de l’amplificateur ; Gcrit est son gain critique. Le contrôle règle G/Gcrit.
- f₀ est la fréquence sélectionnée en hertz et ω₀ = 2πf₀ en rad/s ; s = jω et j² = −1 dans le modèle harmonique.
- a = R₁C₁ + R₂C₂ + R₂C₁ et b = R₂C₁ sont en secondes ; d = R₁R₂C₁C₂ est en secondes carrées ; γ est le taux initial de croissance en s⁻¹.
- A est l’amplitude de l’enveloppe en volts ; la petite perturbation initiale et l’échelle Vlim sont en volts ; le temps t est affiché en ms.

**Repères** — Sup : PTSI : fonction de transfert fournie et régime sinusoïdal. Spé : Physique PSI/PT : oscillateur quasi sinusoïdal, condition de démarrage et rôle des non-linéarités. Au-delà : Modèle d’enveloppe accompagné ; mécanismes réels de régulation d’amplitude.

1. Choisir un pont identique et retrouver un gain critique de 3.
2. Passer du gain inférieur au seuil au gain légèrement supérieur.
3. Dissymétriser les branches : recalculer la fréquence et le gain critique avant d’observer.

**À justifier :** Justifier la fréquence et le gain de démarrage, et préciser quelle hypothèse fournit le plateau d’amplitude.

### Redresseur de précision : valeur absolue

Montrer comment la contre-réaction compense un seuil de diode et vérifier sa marge d’alimentation.

**Objets et paramètres**

- L’entrée e, la sortie interne de l’ALI et les tensions de branche vₛ₁ et vₛ₂ sont en volts ; la sortie utile est vₛ₂ − vₛ₁.
- Les trois résistances d’entrée et de rétroaction sont égales ; les deux diodes des branches conduisent alternativement. La borne positive est à la masse.
- E est la crête de l’entrée sinusoïdale en volts ; f sa fréquence en hertz ; le temps t est affiché en ms.
- Vᴅ est le seuil d’une diode et Vₛₐₜ la limite positive de sortie de l’ALI, en volts. Le pont passif comparé traverse deux diodes.
- L’amplitude compensable Vₛₐₜ − Vᴅ tient compte de la tension supplémentaire que l’ALI fournit en interne.

**Repères** — Sup : PTSI : modèle de diode fourni, alternances et loi des nœuds. Spé : PSI/PT : application d’ALI et reconnaissance des limites de tension ; redresseur accompagné. Au-delà : Erreur de passage par zéro, récupération après saturation et diodes réelles.

1. Choisir une petite tension et comparer le pont passif à la sortie de précision.
2. Mettre le seuil des diodes à zéro : retrouver la valeur absolue dans les deux modèles.
3. Réduire Vₛₐₜ devant E + Vᴅ : prévoir la crête compensable.

**À justifier :** Expliquer l’absence de seuil dans la sortie utile et la présence d’une tension supplémentaire à l’intérieur du montage.

## Séance 18 — Électronique analogique

### Filtre actif à trois ALI

Relier les trois ALI à un passe-bande puis filtrer les harmoniques d’un créneau avec leurs gains et phases.

**Objets et paramètres**

- R₁ est à l’entrée ; R₂ est la rétroaction du premier ALI ; R₃ ramène la sortie de l’intégrateur ; R₄ et R₅ fixent l’inversion ; R₆ entre dans l’intégrateur. Les résistances sont affichées en kΩ.
- Les deux condensateurs ont une capacité commune C affichée en nF. Les tensions vₑ, vₛ, vₛ₁ et vₛ₂ sont en volts ; les deux dernières sont les états internes.
- H₀ est le gain central et Q le facteur de qualité, sans unité ; ω₀ est la pulsation centrale en rad/s et f₀ = ω₀/(2π) la fréquence centrale en hertz.
- ω₁ et ω₂ sont les bornes à −3 dB, en rad/s ; Δω = ω₂ − ω₁ est la largeur en rad/s ; Δf = Δω/(2π) est en hertz.
- E est la crête d’entrée en volts ; f est sa fondamentale en hertz, ωₑ = 2πf en rad/s ; k est un entier positif. Aₖ et Bₖ sont les coefficients sinusoïdaux en volts.
- Le nombre choisi compte les harmoniques impaires retenues ; j² = −1 définit le transfert complexe H(jω). Le temps t est affiché en ms.

**Repères** — Sup : Physique PTSI : utiliser un spectre fourni pour simuler le filtrage d’un signal périodique. Spé : Physique PSI/PT : filtres actifs, analyse spectrale et stabilité ; calcul du montage accompagné. Au-delà : Synthèse de filtre à variables d’état et surveillance des saturations internes.

1. Choisir une sinusoïde au centre et retrouver le gain H₀.
2. Choisir une fondamentale égale au tiers du centre : comparer somme complète et troisième harmonique.
3. Augmenter R₂ : prévoir la largeur et le gain central avant de regarder les courbes.

**À justifier :** Construire la sortie d’un filtre à partir d’un spectre et expliquer les effets distincts du centre, du gain et de la largeur.

### Transistor : polarisation et petits signaux

Dans un prolongement guidé, valider le repos d’un NPN avant de calculer son amplification de petites variations.

**Objets et paramètres**

- Un transistor NPN possède une base, un collecteur et un émetteur. Vcc est l’alimentation en volts ; Rc relie le collecteur à Vcc et Re l’émetteur à la masse.
- Rb₁ relie la base à la masse et Rb₂ la base à Vcc ; les résistances sont affichées en kΩ. Vth et Rth sont leur source et résistance de Thévenin.
- Ib et Ic sont les courants de base et de collecteur, en ampères ; Ve et Vc les tensions de repos en volts ; β est le gain en courant sans unité.
- Le modèle fixe Vbe = 0,7 V et Vce,sat = 0,2 V. Uₜ = 25,85 mV fixe gm = Ic/Uₜ, en siemens, et rπ = β/gm, en ohms, uniquement en régime actif.
- Le générateur possède une résistance Rg ; Rₗ est une charge en alternatif. C₁ relie l’entrée à la base ; Ce découple Re. Les capacités sont affichées en µF.
- e est une petite variation de tension de crête E, en volts, à la fréquence f en hertz ; s = j2πf avec j² = −1. Ze est l’impédance d’émetteur en ohms ; t est affiché en ms.

**Repères** — Sup : PTSI : lois des circuits, équivalent résistif et impédances capacitives réinvestis. Spé : Appui méthodologique : valider un modèle avant de l’utiliser. Le transistor amplificateur n’est pas une exigence de physique PSI/PT. Au-delà : Polarisation et petits signaux d’un transistor ; modèle accompagné distinct de l’interrupteur de puissance en SI.

1. Choisir le régime actif et vérifier la marge collecteur–émetteur.
2. Déconnecter Ce : comparer le gain et le rôle de Re.
3. Choisir saturation ou blocage au repos : expliquer pourquoi la réponse petit signal est désactivée.

**À justifier :** Identifier le régime de repos et justifier les conditions où une petite variation peut être amplifiée.
