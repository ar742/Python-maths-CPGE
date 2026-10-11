"""Champs, conduction et conversion : paramètres et expériences reproductibles."""


def range_(key, label, low, high, step, value, unit="", **extra):
    return dict(key=key, label=label, min=low, max=high, step=step, value=value, unit=unit, type="range", **extra)


def select(key, label, choices, value):
    return dict(key=key, label=label, options=[dict(value=v, label=l) for v, l in choices], value=value, unit="", type="select")


def preset(label, **values):
    return dict(label=label, values=values)


def lab(id_, title, category, intro, controls, presets):
    return dict(id=id_, title=title, category=category, intro=intro, controls=controls, presets=presets)


LABS = [
    lab("dipoles", "Deux charges : quand le dipôle devient exact", "Champs", 'Comparer le champ exact de deux charges à l’approximation dipolaire. Les charges sont +q et −q, avec q en nC ; a est leur séparation en m et r la distance d’observation. Repérer à partir de quel rapport r/a l’approximation convient.', [
        range_("q", "Charge positive q", .1, 100, .1, 10, "nC"),
        range_("a", "Séparation des charges a", .02, 1, .01, .2, "m"),
        range_("angle", "Orientation du dipôle", -180, 180, 5, 0, "°"),
        range_("distance", "Distance d’observation r/a", 1, 30, .1, 5, "")], [
        preset("Dipôle horizontal", angle=0, distance=5), preset("Dipôle vertical", angle=90, distance=5), preset("Très loin des charges", distance=20)]),
    lab("gauss", "Gauss : sphère chargée et câble coaxial", "Champs", 'Choisir une surface de Gauss avec la symétrie du système, puis calculer champ et potentiel. Pour la sphère, Q est la charge en nC et R le rayon en m ; pour le coaxial, a et b sont les rayons des conducteurs. Vérifier la capacité et l’énergie par deux méthodes.', [
        select("mode", "Géométrie", [("sphere", "Sphère uniformément chargée en volume"), ("coax", "Condensateur coaxial idéal")], "sphere"),
        range_("Q", "Charge totale de la sphère", -100, 100, 1, 20, "nC"),
        range_("R", "Rayon de la sphère", .05, 1, .01, .2, "m"),
        range_("a", "Rayon du conducteur interne coaxial", .2, 5, .1, 1, "cm"),
        range_("ratio", "Rapport b/a des rayons coaxiaux", 1.2, 5, .1, 2, ""),
        range_("length", "Longueur du câble", .1, 5, .1, 1, "m"),
        range_("voltage", "Tension Vinterne−Vexterne", -500, 500, 10, 100, "V")], [
        preset("Sphère volumique", mode="sphere", Q=20), preset("Sphère négative", mode="sphere", Q=-20), preset("Coaxial et énergie", mode="coax", voltage=100)]),
    lab("biotsavart", "Oersted, spire et solénoïde finis", "Champs", 'Calculer le champ d’un courant orienté et reconnaître les limites d’un fil ou d’un solénoïde long. I est en A, R le rayon de bobine en m et N le nombre de spires. Comparer les géométries avant de choisir Biot–Savart ou Ampère.', [
        select("mode", "Source de courant", [("wire", "Fil rectiligne de longueur finie"), ("loop", "Spire circulaire"), ("solenoid", "Solénoïde de longueur finie")], "loop"),
        range_("I", "Intensité orientée I", -10, 10, .1, 2, "A"),
        range_("R", "Rayon de la spire / bobine", .02, .5, .01, .1, "m"),
        range_("length", "Longueur du fil / solénoïde", .1, 2, .1, 1, "m"),
        range_("turns", "Nombre de spires N", 1, 500, 1, 100, "", integer=True)], [
        preset("Spire et limite dipolaire", mode="loop"), preset("Fil : expérience d’Oersted", mode="wire"), preset("Solénoïde fini", mode="solenoid", length=1, turns=100)]),
    lab("helmholtz", "Helmholtz : fabriquer une zone uniforme", "Champs", 'Régler deux bobines pour rendre leur champ presque uniforme au centre. R est leur rayon en m, d leur écartement et I le courant en A dans chacune. Comparer les profils à plusieurs valeurs de d/R, puis expliquer le réglage par les dérivées du champ.', [
        range_("R", "Rayon commun R", .05, .5, .01, .15, "m"),
        range_("spacing", "Écartement normalisé d/R", .2, 2, .05, 1, ""),
        range_("I", "Intensité orientée I", -5, 5, .1, 1, "A"),
        range_("turns", "Nombre de spires par bobine", 1, 300, 1, 100, "", integer=True)], [
        preset("Réglage de Helmholtz", spacing=1), preset("Bobines trop proches", spacing=.5), preset("Bobines trop éloignées", spacing=1.5)]),
    lab("drude", "Drude : la conduction a une mémoire", "Milieux", 'Relier la vitesse moyenne des porteurs au courant et à la conductivité. n est leur nombre par m³, τ le temps de relaxation en fs et m* leur masse effective. Comparer la réponse à un échelon et à un champ sinusoïdal, de fréquence réglée en THz.', [
        range_("logn", "log₁₀(n / m⁻³), densité des porteurs", 20, 29, .1, 28.9, ""),
        range_("tau", "Temps de relaxation τ", 1, 100, 1, 25, "fs"),
        range_("mass", "Masse effective m*/me", .1, 5, .1, 1, ""),
        range_("frequency", "Fréquence harmonique f", .01, 1000, .01, 1, "THz"),
        range_("E", "Amplitude / échelon du champ E", 1, 1000, 1, 100, "V·m⁻¹"),
        select("carrier", "Signe des porteurs", [("electron", "Électrons : q=−e"), ("hole", "Porteurs positifs : q=+e")], "electron")], [
        preset("Métal : faible ωτ", frequency=.01, logn=28.9), preset("Réponse inertielle", frequency=100), preset("Porteurs positifs", carrier="hole", logn=23, mass=.5)]),
    lab("hall", "Hall : le signe des porteurs devient mesurable", "Milieux", 'Déduire le signe et la densité des porteurs d’une tension transverse. Le courant I va vers +x, le champ Bz vers +z ; la largeur w est suivant y et l’épaisseur t suivant z, en mm. Garder les mêmes bornes de tension lorsque le signe du champ change.', [
        range_("logn", "log₁₀(n / m⁻³)", 20, 29, .1, 23, ""),
        range_("I", "Courant I vers +x", -2, 2, .02, .2, "A"),
        range_("B", "Champ Bz vers +z", -2, 2, .05, .5, "T"),
        range_("width", "Largeur w suivant y", .5, 20, .5, 5, "mm"),
        range_("thickness", "Épaisseur t suivant z", .05, 2, .05, .2, "mm"),
        select("carrier", "Porteurs majoritaires", [("electron", "Électrons : q=−e"), ("hole", "Trous : q=+e")], "electron")], [
        preset("Plaquette à électrons", carrier="electron", I=.2, B=.5), preset("Même montage à trous", carrier="hole", I=.2, B=.5), preset("Champ inversé", B=-.5)]),
    lab("induction", "Lenz : le freinage se paie en chaleur", "Conversion", 'Relier mouvement, variation de flux, courant et énergie dissipée. Bz est le champ en T, R la résistance en Ω et L l’inductance réglée en mH. Comparer un barreau sur rails à un cadre qui entre dans une zone de champ.', [
        select("mode", "Montage", [("rail", "Barreau sur rails : freinage RL"), ("frame", "Cadre entrant dans une zone magnétique")], "rail"),
        range_("B", "Champ uniforme Bz", 0, 1, .05, .5, "T"),
        range_("length", "Longueur active du barreau / largeur du cadre", .05, 1, .05, .2, "m"),
        range_("height", "Hauteur du cadre", .05, 1, .05, .2, "m"),
        range_("R", "Résistance totale R", .1, 20, .1, 1, "Ω"),
        range_("L", "Inductance du rail L", 1, 100, 1, 10, "mH"),
        range_("mass", "Masse mobile", 10, 2000, 10, 100, "g"),
        range_("v0", "Vitesse initiale vers l’avant / vers le bas", 0, 5, .1, 1, "m·s⁻¹"),
        range_("duration", "Durée observée", .1, 10, .1, 2, "s")], [
        preset("Rail : échange puis dissipation", mode="rail", v0=1), preset("Rail inductif oscillant", mode="rail", B=1, length=.5, mass=10, L=100, R=.1), preset("Cadre : entrée puis chute libre", mode="frame", v0=0, B=.5, length=.2, height=.2, duration=2)]),
    lab("hautparleur", "Haut-parleur : deux équations, un même couplage", "Conversion", 'Comprendre la résonance d’un haut-parleur en reliant circuit et mouvement. x est le déplacement de la membrane ; m, k et b désignent sa masse, sa raideur et son amortissement. Le coefficient κ relie courant et force, puis vitesse et tension induite.', [
        range_("R", "Résistance électrique de la bobine", 1, 16, .1, 6, "Ω"),
        range_("L", "Inductance électrique", .1, 5, .1, .5, "mH"),
        range_("mass", "Masse mobile", 1, 100, 1, 15, "g"),
        range_("stiffness", "Raideur de suspension k", 100, 10000, 100, 1500, "N·m⁻¹"),
        range_("damping", "Amortissement mécanique b", .1, 10, .1, 1, "N·s·m⁻¹"),
        range_("coupling", "Coefficient κ=Bℓ actif", .5, 15, .5, 5, "N·A⁻¹ = V·s·m⁻¹"),
        range_("frequency", "Fréquence f", 10, 2000, 5, 50, "Hz"),
        range_("voltage", "Tension sinusoïdale, valeur crête", .5, 20, .5, 2, "V")], [
        preset("Près de la résonance mécanique", frequency=50), preset("La contre-fem limite le courant", frequency=50, coupling=10), preset("Régime au-dessus de la résonance", frequency=500)]),
    lab("hysteresis", "Mesurer B et H, reconstruire une hystérésis", "Milieux", 'Reconstruire le cycle magnétique d’un tore à partir du courant primaire et de la tension secondaire. H est en A·m⁻¹ et B en T ; Hc règle l’échelle coercitive et Bs la contribution saturée. Relier l’aire du cycle à une énergie dissipée par volume.', [
        range_("Hc", "Échelle coercitive des domaines Hc", 100, 10000, 100, 1000, "A·m⁻¹"),
        range_("amplitude", "Amplitude d’excitation Hmax/Hc", .1, 3, .1, 2, ""),
        range_("Bs", "Contribution magnétique saturée Bs", 0, 2, .05, 1, "T"),
        range_("mur", "Perméabilité relative réversible μr", 1, 100, 1, 5, ""),
        range_("frequency", "Fréquence du cycle", 10, 1000, 10, 50, "Hz"),
        range_("length", "Longueur moyenne du tore ℓ", .1, 1, .05, .3, "m"),
        range_("area", "Section du tore S", .5, 10, .5, 2, "cm²"),
        range_("N1", "Nombre de spires au primaire", 10, 500, 10, 100, "", integer=True),
        range_("N2", "Nombre de spires au secondaire ouvert", 10, 500, 10, 100, "", integer=True)], [
        preset("Cycle majeur préparé", amplitude=2, Bs=1), preset("Cycle mineur après saturation négative", amplitude=.8), preset("Milieu réversible sans hystérésis", Bs=0)]),
    lab("synchrone", "Synchrone : angle de charge et stabilité", "Conversion", 'Chercher l’orientation stable d’un rotor dans un champ tournant. ℳ est son moment magnétique en A·m², B le champ en T et δ le retard angulaire en degrés. Comparer le couple résistant au couple maximal avant d’interpréter le verrouillage.', [
        range_("moment", "Moment magnétique du rotor ℳ", .1, 20, .1, 2, "A·m²"),
        range_("B", "Amplitude du champ tournant B", .05, 2, .05, .5, "T"),
        range_("frequency", "Fréquence du champ tournant f", 5, 100, 5, 50, "Hz"),
        range_("phase", "Retard mécanique δ du dipôle rotor", -180, 180, 5, 30, "°"),
        range_("load", "Couple résistant normalisé Tcharge/Tmax", 0, 1.4, .05, .5, ""),
        range_("J", "Moment d’inertie mécanique J", .01, 1, .01, .1, "kg·m²")], [
        preset("Verrouillage stable", phase=30, load=.5), preset("Branche instable", phase=150, load=.5), preset("Décrochage statique", phase=90, load=1.2)]),
    lab("asynchrone", "Asynchrone : glissement et partage de puissance", "Conversion", 'Suivre l’énergie entre stator, rotor et arbre moteur avec un circuit équivalent. Le glissement s compare la vitesse du rotor à celle du champ tournant ; la tension est une valeur efficace par phase. Distinguer puissance reçue par le rotor, chaleur et conversion mécanique.', [
        range_("voltage", "Tension simple efficace par phase", 20, 300, 5, 230, "V"),
        range_("frequency", "Fréquence électrique", 5, 100, 5, 50, "Hz"),
        range_("poles", "Nombre de paires de pôles", 1, 4, 1, 2, "", integer=True),
        range_("slip", "Glissement s=(Ωs−Ωr)/Ωs", -.5, 1.5, .01, .05, ""),
        range_("R1", "Résistance statorique par phase", .1, 10, .1, 1, "Ω"),
        range_("R2", "Résistance rotorique ramenée au stator", .1, 10, .1, .5, "Ω"),
        range_("L1", "Inductance de fuite statorique", .1, 20, .1, 3, "mH"),
        range_("L2", "Inductance de fuite rotorique ramenée", .1, 20, .1, 3, "mH"),
        range_("Lm", "Inductance de magnétisation", 5, 500, 5, 100, "mH")], [
        preset("Moteur à faible glissement", slip=.05), preset("Rotor arrêté : démarrage", slip=1), preset("Génératrice hypersynchrone", slip=-.05), preset("Synchronisme : pas de courant rotor", slip=0)]),
    lab("peau", "Peau harmonique et diffusion magnétique", "Milieux", 'Comparer la pénétration d’un champ sinusoïdal et celle d’un échelon dans un métal. σ est la conductivité en MS·m⁻¹, μr la perméabilité relative et f la fréquence en Hz. Mesurer une profondeur de pénétration et la relier à la diffusion.', [
        select("mode", "Excitation de la surface", [("harmonic", "Champ harmonique établi"), ("step", "Échelon continu, diffusion transitoire")], "harmonic"),
        range_("logf", "log₁₀(f / Hz)", 1, 7, .1, 3, ""),
        range_("sigma", "Conductivité électrique σ", 1, 60, 1, 58, "MS·m⁻¹"),
        range_("mur", "Perméabilité relative μr supposée constante", 1, 1000, 1, 1, ""),
        range_("B", "Champ magnétique à la surface", .1, 100, .1, 10, "mT"),
        range_("time", "Temps depuis l’échelon", .01, 10, .01, 1, "ms")], [
        preset("Cuivre, 1 kHz", mode="harmonic", logf=3, sigma=58, mur=1), preset("Fréquence multipliée par 100", mode="harmonic", logf=5), preset("Échelon : pénétration croissante", mode="step", time=1)]),
]

LAB_BY_ID = {item["id"]: item for item in LABS}
