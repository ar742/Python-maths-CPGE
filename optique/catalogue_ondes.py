"""Douze bancs d'optique ondulatoire : paramètres publics et situations d'étude."""


def slider(key, label, lo, hi, step, value, unit=""):
    return dict(key=key, label=label, min=lo, max=hi, step=step,
                value=value, unit=unit, type="range")


def select(key, label, options, value):
    return dict(key=key, label=label,
                options=[dict(value=v, label=l) for v, l in options],
                value=value, unit="", type="select")


def preset(label, **values):
    return dict(label=label, values=values)


def lab(id_, title, category, intro, controls, presets):
    return dict(id=id_, title=title, category=category, intro=intro,
                controls=controls, presets=presets)


LABS = [
    lab("young", "Young : franges, enveloppe et déséquilibre", "Interférences",
        'Une même source éclaire deux fentes et produit des franges sous une enveloppe de diffraction. Modifier leur largeur, leur séparation et leur cohérence permet de distinguer interfrange, contraste et largeur de l’enveloppe.', [
            slider("wavelength", "Longueur d'onde dans l'air", 400, 780, 5, 600, "nm"),
            slider("separation", "Distance entre les centres des fentes a", .1, 2, .01, .5, "mm"),
            slider("width", "Largeur de chaque fente b", .01, .09, .001, .04, "mm"),
            slider("distance", "Distance du plan d'observation D", .5, 5, .1, 2, "m"),
            slider("ratio", "Rapport d'intensité I₂/I₁", 0, 2, .02, 1),
            slider("phase", "Phase supplémentaire du second trajet", 0, 360, 1, 0, "°"),
            select("mode", "Éclairage", [("coherent", "Deux fentes, source commune"), ("independent", "Deux sources indépendantes"), ("single", "Une seule fente")], "coherent")], [
                preset("Deux échelles visibles", separation=.5, width=.04, ratio=1, mode="coherent"),
                preset("Contraste déséquilibré", ratio=.1, mode="coherent"),
                preset("La somme sans interférence", mode="independent"),
                preset("Une seule ouverture", mode="single")]),
    lab("reseau", "Réseau : résoudre un doublet spectral", "Interférences",
        'Additionner les ondes issues de plusieurs fentes pour séparer deux raies proches. Le nombre de fentes et l’ordre d’observation relient la largeur des maxima au pouvoir de résolution du réseau.', [
            slider("wavelength", "Longueur d'onde centrale", 400, 780, 1, 589.3, "nm"),
            slider("doublet", "Écart des deux raies", 0, 2, .01, .6, "nm"),
            slider("pitch", "Pas du réseau d", 1, 10, .1, 2, "µm"),
            slider("count", "Nombre de fentes éclairées N", 5, 1000, 1, 500),
            slider("fill", "Fraction ouverte b/d", .1, .9, .01, .4),
            slider("incidence", "Angle d'incidence θ₀", -30, 30, 1, 0, "°"),
            slider("order", "Ordre spectral étudié m", 1, 3, 1, 1)], [
                preset("Doublet du sodium peu résolu", count=100, doublet=.6, order=1),
                preset("Doublet au critère de Rayleigh", count=982, doublet=.6, order=1),
                preset("Ordre deux plus dispersif", count=500, doublet=.6, order=2),
                preset("Ordre absent", pitch=1, incidence=30, order=3)]),
    lab("diffraction", "Ouvertures : rectangle et apodisation", "Diffraction",
        'Observer dans un plan focal la lumière transmise par une ouverture. Comparer une transmission uniforme et une transmission adoucie explique le compromis entre largeur du maximum central et intensité des maxima secondaires.', [
            select("aperture", "Pupille", [("rectangle", "Rectangle uniforme"), ("slit", "Fente longue"), ("apodized", "Rectangle apodisé en x : cos(πx/a)")], "rectangle"),
            slider("width", "Largeur horizontale a", .02, 2, .01, .2, "mm"),
            slider("height", "Hauteur verticale b", .02, 2, .01, .8, "mm"),
            slider("wavelength", "Longueur d'onde", 400, 780, 5, 600, "nm"),
            slider("focal", "Focale de la lentille d'observation", 100, 1000, 10, 300, "mm")], [
                preset("Rectangle étroit", aperture="rectangle", width=.2, height=.8),
                preset("Fente et premier zéro", aperture="slit", width=.1),
                preset("Élargir pour atténuer les lobes", aperture="apodized", width=.2, height=.8)]),
    lab("polarisation", "Jones : lame à retard et analyseur", "Polarisation",
        'Faire traverser une lame à retard puis un analyseur à une onde polarisée. Les composantes du champ, l’ellipse et la transmission permettent de relier déphasage, état de polarisation et mesure d’intensité.', [
            select("input", "État incident", [("linear", "Rectiligne"), ("circular", "Circulaire : Ey = i Ex"), ("elliptical", "Elliptique : Ey = i Ex/2")], "linear"),
            slider("input_angle", "Orientation incidente / de l'ellipse", -90, 90, 1, 45, "°"),
            slider("axis", "Orientation de l'axe de la lame", -90, 90, 1, 0, "°"),
            slider("retardance", "Retard de phase de la seconde composante", 0, 360, 1, 90, "°"),
            slider("analyzer", "Orientation de l'analyseur", -90, 90, 1, 0, "°")], [
                preset("Quart d'onde à 45°", input="linear", input_angle=45, axis=0, retardance=90),
                preset("Demi-onde : tourner une droite", input="linear", input_angle=30, axis=0, retardance=180),
                preset("Analyser un état circulaire", input="circular", input_angle=0, retardance=0),
                preset("Extinction de Malus", input="linear", input_angle=0, retardance=0, analyzer=90)]),
    lab("michelson", "Michelson : anneaux et coin d'air", "Interférences",
        'Déplacer ou incliner un miroir d’un interféromètre de Michelson. Le calcul de la différence de marche explique le facteur deux de la translation, les anneaux et les franges d’un coin d’air.', [
            select("mode", "Configuration", [("rings", "Lame d'air : égale inclinaison"), ("wedge", "Coin d'air : égale épaisseur")], "rings"),
            slider("wavelength", "Longueur d'onde dans l'air", 400, 780, 1, 546, "nm"),
            slider("gap", "Écart longitudinal équivalent des miroirs e", 0, 1000, 1, 500, "µm"),
            slider("tilt", "Petit angle du coin d'air α", 0, 2, .01, .15, "mrad"),
            slider("focal", "Focale d'observation / échelle d'image", 100, 500, 10, 200, "mm"),
            slider("field", "Demi-angle du champ en lame d'air", 1, 6, .1, 5, "°"),
            slider("phase", "Phase réglable complémentaire", 0, 360, 1, 0, "°")], [
                preset("Anneaux d'une raie de mercure", mode="rings", wavelength=546, gap=500, field=5),
                preset("Contact optique", mode="rings", gap=0, phase=0),
                preset("Franges du coin", mode="wedge", gap=0, tilt=.15),
                preset("Coin deux fois plus incliné", mode="wedge", gap=0, tilt=.3)]),
    lab("coherence", "Cohérence : spectre, source étendue et battements", "Interférences",
        'Des franges perdent leur contraste lorsque la source possède plusieurs fréquences ou une grande étendue. Sommer les contributions permet de distinguer cohérence temporelle, cohérence spatiale et battements d’un doublet.', [
            select("spectrum", "Spectre / corrélation", [("gaussian", "Spectre gaussien, largeur Δν"), ("doublet", "Deux raies fines d'égales intensités"), ("independent", "Deux sources mutuellement indépendantes")], "gaussian"),
            slider("wavelength", "Longueur d'onde centrale", 400, 780, 1, 589.3, "nm"),
            slider("linewidth", "Largeur spectrale FWHM Δν", .01, 100, .01, 20, "GHz"),
            slider("doublet", "Écart des deux raies", .01, 2, .01, .6, "nm"),
            slider("opd", "Différence de marche centrale δ", 0, 20, .01, 2, "mm"),
            slider("source_width", "Largeur uniforme de la source s", 0, 2, .01, .2, "mm"),
            slider("source_distance", "Distance source–fentes Ds", .5, 5, .1, 1, "m"),
            slider("separation", "Distance entre les fentes a", .1, 2, .01, .5, "mm")], [
                preset("Spectre fin et source ponctuelle", spectrum="gaussian", linewidth=.1, source_width=0),
                preset("Perte de cohérence temporelle", spectrum="gaussian", linewidth=100, source_width=0, opd=10),
                preset("Battements du doublet", spectrum="doublet", doublet=.6, source_width=0, opd=.2894),
                preset("Source large : facteur spatial", spectrum="gaussian", linewidth=.1, source_width=1.1786, separation=.5)]),
    lab("fabryperot", "Fabry–Perot : coefficient d'Airy et finesse", "Résonateurs",
        'Une cavité transmet fortement certaines fréquences après de multiples réflexions. Sommer les amplitudes permet de calculer ses résonances et de distinguer leur espacement, leur largeur et la finesse.', [
            slider("length", "Épaisseur de cavité e", .1, 10, .1, 1, "mm"),
            slider("index", "Indice n de la cavité", 1, 2, .01, 1),
            slider("reflectivity", "Réflectivité en intensité R des miroirs", 0, .99, .01, .85),
            slider("wavelength", "Longueur d'onde de référence dans le vide", 400, 780, 1, 600, "nm"),
            slider("angle", "Angle interne θ", 0, 20, .1, 0, "°"),
            slider("detuning", "Désaccord à la résonance / ISL", -1, 1, .001, .12)], [
                preset("Sur la résonance", reflectivity=.85, detuning=0),
                preset("Haute finesse", reflectivity=.99, detuning=0),
                preset("Sans miroirs réfléchissants", reflectivity=0, detuning=.5),
                preset("Anti-résonance", reflectivity=.85, detuning=.5)]),
    lab("fourier", "Banc 4f : filtrer vraiment une image", "Imagerie",
        'Utiliser deux lentilles et un masque pour modifier les fréquences spatiales d’une image. Suivre le champ puis son intensité explique un filtrage optique et permet de contrôler le bilan de puissance.', [
            select("object", "Objet d'amplitude ou de phase", [("grid", "Grille : traits verticaux et horizontaux"), ("cells", "Deux disques et une mire"), ("phase", "Objet de phase pure")], "grid"),
            select("filter", "Masque du plan de Fourier", [("identity", "Aucun masque"), ("lowpass", "Disque passe-bas"), ("highpass", "Disque passe-haut"), ("vertical", "Fente verticale : |νx| < νc"), ("horizontal", "Fente horizontale : |νy| < νc")], "lowpass"),
            slider("cutoff", "Fréquence spatiale de coupure νc", 5, 80, 1, 20, "mm⁻¹"),
            slider("pixel", "Pas de l'échantillonnage objet", 5, 20, 1, 10, "µm"),
            slider("focal", "Focale des deux lentilles", 50, 400, 10, 200, "mm"),
            slider("wavelength", "Longueur d'onde", 400, 780, 5, 600, "nm")], [
                preset("Image inchangée, énergie conservée", filter="identity", object="grid"),
                preset("Supprimer les détails fins", filter="lowpass", cutoff=12),
                preset("Conserver les contours", filter="highpass", cutoff=12),
                preset("Sélection de l'orientation", filter="vertical", cutoff=8),
                preset("Rendre visible une phase", object="phase", filter="highpass", cutoff=8)]),
    lab("laser", "Laser : stabilité, seuil et saturation", "Résonateurs",
        'Tester si une cavité confine un faisceau, puis si son gain compense les pertes. Séparer ces deux conditions permet de comprendre la stabilité géométrique, le seuil laser et la saturation de la puissance.', [
            slider("length", "Distance entre les miroirs L", 50, 500, 10, 200, "mm"),
            slider("curvature1", "Courbure du miroir 1 : 1/R₁", 0, 10, .1, 2, "m⁻¹"),
            slider("curvature2", "Courbure du miroir 2 : 1/R₂", -10, 10, .1, 2, "m⁻¹"),
            slider("reflectivity1", "Réflectivité R₁ en intensité", .8, .999, .001, .99),
            slider("reflectivity2", "Réflectivité R₂ du coupleur", .5, .99, .01, .9),
            slider("loss", "Pertes réparties α en intensité", 0, 2, .01, .05, "m⁻¹"),
            slider("gain", "Gain non saturé g₀ en intensité", 0, 20, .05, 1, "m⁻¹"),
            slider("saturation", "Puissance intracavité de saturation Ps", .1, 20, .1, 2, "W"),
            slider("wavelength", "Longueur d'onde", 400, 1550, 5, 633, "nm")], [
                preset("Mode stable au-dessus du seuil", length=200, curvature1=2, curvature2=2, gain=1),
                preset("Cavité stable, gain insuffisant", length=200, curvature1=2, curvature2=2, gain=.05),
                preset("Miroir convexe : instabilité", length=200, curvature1=2, curvature2=-5),
                preset("Cavité confocale, limite marginale", length=200, curvature1=5, curvature2=5)]),
    lab("gaussien", "Faisceau gaussien : waist, diffraction et Gouy", "Lasers",
        'Un faisceau plus étroit à son col diverge davantage ensuite. Calculer son profil, sa puissance et sa phase permet de relier largeur transverse, diffraction et déphasage de Gouy dans un modèle paraxial.', [
            slider("waist", "Rayon w₀ à 1/e² d'intensité", 10, 1000, 5, 50, "µm"),
            slider("wavelength", "Longueur d'onde dans le vide", 400, 1550, 5, 633, "nm"),
            slider("index", "Indice du milieu homogène", 1, 2, .01, 1),
            slider("power", "Puissance totale P", .1, 20, .1, 2, "mW"),
            slider("position", "Plan observé z/zR", -5, 5, .05, 2)], [
                preset("Au waist", position=0),
                preset("À la longueur de Rayleigh", position=1),
                preset("Petit waist, forte divergence", waist=10, position=3),
                preset("Waist large", waist=500, position=2)]),
    lab("airy", "Airy : séparer deux étoiles", "Astronomie",
        'Chercher si un instrument sépare deux étoiles indépendantes. Comparer les taches d’une pupille pleine et d’une pupille annulaire relie diffraction, diamètre d’ouverture et contraste entre deux sources.', [
            slider("diameter", "Diamètre de la pupille D", 20, 3000, 10, 200, "mm"),
            slider("wavelength", "Longueur d'onde", 400, 1000, 5, 550, "nm"),
            slider("separation", "Séparation / repère 1,22λ/D", 0, 2.5, .01, 1),
            slider("ratio", "Flux relatif de la seconde étoile", .05, 1, .01, 1),
            slider("obstruction", "Rapport diamètre obstacle / pupille", 0, .5, .01, 0)], [
                preset("Critère de Rayleigh, deux étoiles égales", separation=1, ratio=1, obstruction=0),
                preset("Étoiles très proches", separation=.5, ratio=1),
                preset("Compagnon faible", separation=1, ratio=.1),
                preset("Pupille annulaire", obstruction=.4, separation=1)]),
    lab("nonlineaire", "χ² : doubler la fréquence et épuiser la pompe", "Au-delà",
        'Convertir une partie de la lumière incidente en lumière de fréquence double dans un cristal. Comparer pompe supposée constante et ondes couplées permet de suivre l’énergie et de comprendre l’accord de phase.', [
            select("model", "Modèle", [("coupled", "Ondes couplées : déplétion de la pompe"), ("small", "Pompe constante : faible conversion")], "coupled"),
            slider("wavelength", "Longueur d'onde fondamentale dans le vide", 400, 1600, 5, 1064, "nm"),
            slider("intensity", "Intensité fondamentale incidente", .01, 2, .01, .2, "GW·cm⁻²"),
            slider("coefficient", "Coefficient effectif d = χeff/2", 1, 30, .1, 5, "pm·V⁻¹"),
            slider("index1", "Indice du fondamental nω", 1.4, 2, .01, 1.65),
            slider("index2", "Indice effectif à 2ω", 1.4, 2, .01, 1.65),
            slider("length", "Longueur du cristal L", .1, 10, .1, 3, "mm"),
            slider("mismatch", "Désaccord Δk effectif réglé par orientation", -5, 5, .01, 0, "mm⁻¹")], [
                preset("Accord parfait, déplétion", model="coupled", mismatch=0, intensity=.2, coefficient=5, length=3),
                preset("Faible conversion en sinc²", model="small", intensity=.01, coefficient=1, length=1, mismatch=2),
                preset("Désaccord et reconversion", model="coupled", mismatch=2, intensity=.2, coefficient=5, length=5),
                preset("Conversion saturée", model="coupled", mismatch=0, intensity=2, coefficient=20, length=10)])
]

LAB_BY_ID = {item["id"]: item for item in LABS}
for item in LABS:
    for control in item["controls"]:
        if control["key"] in ("count", "order"):
            control["integer"] = True
