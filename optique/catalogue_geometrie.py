"""Douze bancs d'optique géométrique : grandeurs et préréglages publics."""


def slider(key, label, lo, hi, step, value, unit=""):
    return dict(key=key, label=label, min=lo, max=hi, step=step, value=value, unit=unit, type="range")


def select(key, label, options, value):
    return dict(key=key, label=label, options=[dict(value=v, label=l) for v, l in options], value=value, unit="", type="select")


def preset(label, **values):
    return dict(label=label, values=values)


def lab(id_, title, category, intro, controls, presets):
    return dict(id=id_, title=title, category=category, intro=intro, controls=controls, presets=presets)


LABS = [
    lab("snell", "Snell : réfraction et réflexion totale", "Rayons et images",
        "Suivre les directions des rayons à une interface, puis distinguer l'amplitude d'un champ du flux d'énergie qu'il transporte.", [
            slider("n1", "Indice incident n₁", 1, 2, .01, 1), slider("n2", "Indice transmis n₂", 1, 2, .01, 1.5),
            slider("angle", "Incidence, mesurée à la normale", 0, 80, .1, 40, "°")], [
            preset("Air → verre", n1=1, n2=1.5, angle=40), preset("Verre → air : angle critique", n1=1.5, n2=1, angle=41.8103148958),
            preset("Réflexion totale", n1=1.5, n2=1, angle=60)]),
    lab("lentille", "Conjugaison : image réelle, virtuelle ou à l'infini", "Rayons et images",
        "Construire une image à partir de plusieurs rayons et contrôler la conjugaison de Descartes avec des distances orientées.", [
            select("type", "Lentille", [("convergente", "Convergente"), ("divergente", "Divergente")], "convergente"),
            slider("focal", "Valeur absolue de la focale", 20, 150, 1, 80, "mm"),
            slider("distance", "Distance de l'objet réel à O", 20, 500, 1, 200, "mm"),
            slider("height", "Hauteur de l'objet", 1, 30, 1, 15, "mm"), slider("aperture", "Demi-ouverture de la lentille", 5, 50, 1, 25, "mm")], [
            preset("Image réelle inversée", type="convergente", focal=80, distance=200),
            preset("Loupe : image virtuelle", type="convergente", focal=80, distance=50),
            preset("Objet dans le plan focal", type="convergente", focal=80, distance=80),
            preset("Lentille divergente", type="divergente", focal=80, distance=200)]),
    lab("bessel", "Bessel : mesurer une focale et ses incertitudes", "Bancs et instruments",
        "Explorer les deux mises au point, le cas limite de Silbermann et les incertitudes d'une mesure indirecte de focale.", [
            slider("distance", "Distance objet–écran D", 100, 1500, 10, 800, "mm"), slider("focal", "Focale vraie f′", 20, 200, 1, 120, "mm"),
            slider("position", "Position de la lentille : s/D", .05, .95, .005, .185, ""),
            slider("sigma_D", "Incertitude type sur D", .1, 5, .1, 1, "mm"), slider("sigma_d", "Incertitude type sur l'écart d", .1, 5, .1, 1, "mm")], [
            preset("Première mise au point", distance=800, focal=120, position=.183772233983162),
            preset("Seconde mise au point", distance=800, focal=120, position=.816227766016838),
            preset("Silbermann", distance=480, focal=120, position=.5),
            preset("Aucune mise au point", distance=400, focal=120, position=.5)]),
    lab("telescope", "Lunette astronomique : grossir ou résoudre ?", "Bancs et instruments",
        "Une lunette de Kepler sépare grossissement angulaire, mise au point afocale et résolution fixée par l'ouverture.", [
            slider("objective", "Focale de l'objectif", 300, 2000, 10, 1000, "mm"), slider("eyepiece", "Focale de l'oculaire", 10, 80, 1, 25, "mm"),
            slider("diameter", "Diamètre de l'objectif", 30, 300, 5, 100, "mm"), slider("angle", "Direction de l'astre", -10, 10, .1, 3, "min d'arc"),
            slider("defocus", "Écart à la séparation afocale", -20, 20, .1, 0, "mm"), slider("wavelength", "Longueur d'onde", 400, 750, 5, 550, "nm")], [
            preset("Lunette afocale ×40", objective=1000, eyepiece=25, defocus=0),
            preset("Grossir sans ouvrir davantage", objective=1000, eyepiece=10, diameter=100, defocus=0),
            preset("Défaut de mise au point", objective=1000, eyepiece=25, defocus=5)]),
    lab("microscope", "Microscope : image intermédiaire et ouverture numérique", "Bancs et instruments",
        "Relier la conjugaison de l'objectif, le grossissement commercial et une limite de résolution qui ne disparaît pas en changeant l'oculaire.", [
            slider("objective", "Focale de l'objectif", 4, 20, .5, 8, "mm"), slider("eyepiece", "Focale de l'oculaire", 15, 50, 1, 25, "mm"),
            slider("interval", "Intervalle optique F′₁F₂", 100, 250, 5, 160, "mm"), slider("height", "Hauteur de l'objet", .01, .1, .005, .05, "mm"),
            slider("NA", "Ouverture numérique de l'objectif", .05, .35, .01, .25), slider("wavelength", "Longueur d'onde", 400, 750, 5, 550, "nm"),
            slider("defocus", "Déplacement axial de l'objet", -50, 50, 1, 0, "µm")], [
            preset("Réglage à l'infini", objective=8, eyepiece=25, interval=160, defocus=0),
            preset("Fort grossissement", objective=4, eyepiece=20, interval=160, defocus=0),
            preset("Objet décalé de 20 µm", objective=8, eyepiece=25, interval=160, defocus=20)]),
    lab("oeil", "Œil : accommodation, défauts et correction", "Bancs et instruments",
        "Un œil réduit permet de suivre la tache rétinienne, la vergence nécessaire et l'effet opposé du diaphragme sur le flou et la diffraction.", [
            slider("distance", "Distance de l'objet", .1, 10, .05, 5, "m"), slider("retina", "Distance lentille–rétine", 15, 20, .1, 17, "mm"),
            slider("error", "Excès de vergence au repos", -6, 6, .25, 0, "δ"), slider("correction", "Vergence de la correction", -8, 8, .25, 0, "δ"),
            slider("accommodation", "Accommodation ajoutée", 0, 12, .25, 0, "δ"), slider("pupil", "Diamètre pupillaire", 2, 8, .25, 4, "mm")], [
            preset("Objet proche : accommoder", distance=.25, error=0, correction=0, accommodation=4),
            preset("Myopie de 3 dioptries", distance=10, error=3, correction=0, accommodation=0),
            preset("Myopie corrigée", distance=10, error=3, correction=-3, accommodation=.1),
            preset("Hypermétropie", distance=5, error=-3, correction=3, accommodation=.2)]),
    lab("fibre", "Fibre : cône d'acceptance et dispersion modale", "Rayons et milieux",
        "La réflexion totale guide des rayons méridiens ; leurs longueurs de trajet expliquent un étalement temporel que le modèle géométrique ne confond pas avec les modes ondulatoires.", [
            slider("core", "Indice du cœur n₁", 1.44, 1.6, .001, 1.48), slider("cladding", "Indice de la gaine n₂", 1.4, 1.55, .001, 1.46),
            slider("angle", "Angle d'entrée dans l'air, à l'axe", 0, 35, .1, 8, "°"), slider("radius", "Rayon du cœur", 2, 100, 1, 25, "µm"),
            slider("length", "Longueur de la fibre", 100, 10000, 100, 1000, "m"), slider("wavelength", "Longueur d'onde dans le vide", 500, 1600, 10, 850, "nm")], [
            preset("Rayon guidé", core=1.48, cladding=1.46, angle=8, radius=25),
            preset("Sortir du cône d'acceptance", core=1.48, cladding=1.46, angle=25),
            preset("Repère monomode : théorie ondulatoire nécessaire", core=1.45, cladding=1.444, radius=2, wavelength=1550, angle=0)]),
    lab("mirage", "Mirage : un rayon courbe dans un gradient d'indice", "Rayons et milieux",
        "Conserver n(z) cos θ et comparer une intégration de la loi du rayon à la parabole analytique du profil n₀√(1 + z/a).", [
            slider("n0", "Indice à z = 0", 1.0001, 1.01, .0001, 1.0003), slider("scale", "Échelle a du profil d'indice", 1000, 1000000, 1000, 20000, "m"),
            slider("altitude", "Altitude initiale z₀", .1, 20, .1, 2, "m"), slider("angle", "Angle initial à l'horizontale", -2, 2, .02, -.5, "°"),
            slider("length", "Distance horizontale étudiée", 100, 3000, 50, 1000, "m")], [
            preset("Descendre puis remonter", scale=20000, altitude=2, angle=-.5, length=1000),
            preset("Rencontrer le sol", scale=100000, altitude=2, angle=-1, length=1000),
            preset("Gradient presque nul", scale=1000000, altitude=2, angle=0, length=1000)]),
    lab("arcenciel", "Arc-en-ciel : stationnarité et dispersion d'une goutte", "Rayons et milieux",
        "Tracer les réfractions et réflexions dans une goutte, puis retrouver l'angle de concentration des rayons et l'inversion des couleurs du second arc.", [
            select("reflections", "Arc étudié", [("1", "Primaire : une réflexion interne"), ("2", "Secondaire : deux réflexions internes")], "1"),
            slider("angle", "Angle d'incidence sur la goutte", 20, 89, .1, 59.4, "°"), slider("wavelength", "Longueur d'onde", 400, 750, 5, 550, "nm"),
            slider("cauchy_a", "Coefficient a de Cauchy", 1.3, 1.34, .001, 1.322), slider("cauchy_b", "Coefficient b de Cauchy", .001, .006, .0001, .003, "µm²")], [
            preset("Arc primaire, rouge", reflections="1", wavelength=700, angle=59.5),
            preset("Arc primaire, violet", reflections="1", wavelength=420, angle=59.1),
            preset("Arc secondaire", reflections="2", wavelength=550, angle=71.8)]),
    lab("prisme", "Prisme : goniomètre, minimum et Cauchy", "Rayons et milieux",
        "Repérer le retournement d'une raie à la déviation minimale, déduire n et comparer différentes longueurs d'onde sans extrapoler Cauchy hors du visible.", [
            slider("apex", "Angle au sommet A", 30, 75, .5, 60, "°"), slider("angle", "Incidence à la première face", 0, 85, .1, 49, "°"),
            slider("wavelength", "Longueur d'onde", 400, 750, 5, 589, "nm"), slider("cauchy_a", "Coefficient a", 1.3, 1.7, .005, 1.48),
            slider("cauchy_b", "Coefficient b", .001, .015, .0001, .004, "µm²")], [
            preset("Voisinage du minimum", apex=60, angle=48.43, wavelength=589),
            preset("Spectre visible", apex=60, angle=55, wavelength=450),
            preset("Pas d'émergence à la seconde face", apex=60, angle=10, wavelength=589)]),
    lab("aberrations", "Miroir : la sphère face au paraboloïde", "Limites et méthodes",
        "Calculer les réflexions exactes d'un faisceau axial ; réduire l'ouverture rend la sphère presque stigmatique, tandis que le paraboloïde focalise exactement ce faisceau.", [
            select("surface", "Surface réfléchissante", [("sphere", "Miroir sphérique"), ("parabole", "Miroir parabolique")], "sphere"),
            slider("radius", "Rayon R de courbure au sommet", 100, 1000, 10, 400, "mm"), slider("opening", "Demi-ouverture / R", .02, .65, .01, .45),
            slider("screen", "Position de l'écran : −x/R", .3, .7, .005, .5)], [
            preset("Aberration sphérique visible", surface="sphere", opening=.45, screen=.5),
            preset("Conditions de Gauss", surface="sphere", opening=.05, screen=.5),
            preset("Paraboloïde axial stigmatique", surface="parabole", opening=.45, screen=.5)]),
    lab("fermat", "Fermat : choisir le passage le plus rapide", "Limites et méthodes",
        "Minimiser un chemin optique à deux segments : le trajet le plus court en longueur n'est généralement pas le plus court en temps.", [
            slider("n1", "Indice au-dessus de l'interface", 1, 2, .01, 1), slider("n2", "Indice au-dessous de l'interface", 1, 2, .01, 1.5),
            slider("distance", "Séparation horizontale des points", 5, 30, .5, 20, "cm"), slider("h1", "Altitude du point A", 2, 20, .5, 8, "cm"),
            slider("h2", "Profondeur du point B", 2, 20, .5, 5, "cm"), slider("crossing", "Point de passage : x/D", 0, 1, .01, .5)], [
            preset("Air → verre", n1=1, n2=1.5, crossing=.5), preset("Même indice : une droite", n1=1.5, n2=1.5, crossing=8/13),
            preset("Milieu lent au départ", n1=1.8, n2=1, crossing=.5)]),
]

LAB_BY_ID = {item["id"]: item for item in LABS}
