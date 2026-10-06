"""Paramètres publics des 18 expériences ; toutes les unités affichées sont explicites."""


def slider(key, label, lo, hi, step, value, unit=""):
    return {"key": key, "label": label, "min": lo, "max": hi, "step": step,
            "value": value, "unit": unit, "type": "range"}


def select(key, label, options, value):
    return {"key": key, "label": label, "options": [
        {"value": v, "label": text} for v, text in options], "value": value,
        "unit": "", "type": "select"}


def preset(label, **values):
    return {"label": label, "values": values}


def lab(id_, title, category, intro, controls, presets):
    return dict(id=id_, title=title, category=category, intro=intro,
                controls=controls, presets=presets)


LABS = [
    lab("cinematique", "Suivre une particule, lire un champ", "Fondations",
        "Séparer transport, déformation et rotation dans un champ plan incompressible. Une ligne de courant n’est une trajectoire que si le champ est stationnaire.", [
            slider("a", "Taux d’étirement a", -1, 1, .05, .35, "s⁻¹"),
            slider("omega", "Rotation Ω", -1, 1, .05, .55, "rad·s⁻¹"),
            slider("U", "Translation uniforme U", -1, 1, .05, .3, "m·s⁻¹"),
            slider("L", "Demi-largeur de la fenêtre L", .5, 3, .1, 1, "m"),
            slider("time", "Durée suivie", 0, 5, .1, 2, "s")], [
                preset("Rotation solide", a=0, omega=.8, U=0),
                preset("Étirement incompressible", a=.6, omega=0, U=0),
                preset("Transport et tourbillon", a=.35, omega=.55, U=.3)]),
    lab("newtonien", "La viscosité mesure une déformation", "Fondations",
        "Construire D=(∇v+∇vᵀ)/2 et τ=2ηD : une rotation rigide ne produit aucune dissipation visqueuse.", [
            slider("eta", "Viscosité dynamique η", .1, 2000, .1, 100, "mPa·s"),
            slider("rho", "Masse volumique ρ", 1, 2000, .1, 1000, "kg·m⁻³"),
            slider("shear", "Taux de cisaillement γ̇", -20, 20, .2, 5, "s⁻¹"),
            slider("a", "Taux d’extension a", -5, 5, .1, 1, "s⁻¹"),
            slider("omega", "Rotation rigide Ω", -10, 10, .2, 2, "rad·s⁻¹")], [
                preset("Rotation sans dissipation", shear=0, a=0, omega=5),
                preset("Cisaillement simple", shear=10, a=0, omega=0),
                preset("Extension plane", shear=0, a=2, omega=0)]),
    lab("couette", "Couette–Poiseuille entre deux parois", "Écoulements",
        "Superposer entraînement par les parois et gradient de pression ; prévoir débit nul, reflux et bilan de puissance.", [
            slider("h", "Écartement h", .2, 20, .1, 4, "mm"),
            slider("U0", "Vitesse de la paroi basse", -1, 1, .02, .3, "m·s⁻¹"),
            slider("U1", "Vitesse de la paroi haute", -1, 1, .02, 0, "m·s⁻¹"),
            slider("G", "Force de pression G=−∂p/∂x", -2000, 2000, 10, 0, "Pa·m⁻¹"),
            slider("eta", "Viscosité dynamique η", 1, 1000, 1, 100, "mPa·s")], [
                preset("Couette pur", U0=.3, U1=0, G=0),
                preset("Pression motrice", U0=0, U1=0, G=1000),
                preset("Débit nul mais mouvement", h=10, eta=100, U0=.1, U1=0, G=-600),
                preset("Reflux près de la paroi", h=10, eta=100, U0=.1, U1=0, G=-1000)]),
    lab("poiseuille", "Poiseuille : le rayon à la puissance quatre", "Écoulements",
        "Intégrer un profil parabolique en coordonnées cylindriques, comparer débit, dissipation et résistance hydraulique.", [
            slider("R", "Rayon intérieur R", .2, 10, .1, 1, "mm"),
            slider("L", "Longueur L", .05, 5, .05, 1, "m"),
            slider("dp", "Chute de pression Δp=pentrée−psortie", 1, 20000, 1, 1000, "Pa"),
            slider("eta", "Viscosité dynamique η", .5, 1000, .5, 10, "mPa·s"),
            slider("rho", "Masse volumique ρ", 1, 2000, .1, 1000, "kg·m⁻³")], [
                preset("Capillaire laminaire", R=1, eta=10, dp=1000, L=1),
                preset("Rayon doublé", R=2, eta=10, dp=1000, L=1),
                preset("Microcanal visqueux", R=.2, eta=100, dp=20000, L=.2)]),
    lab("diffusion", "Démarrage d’une paroi et diffusion visqueuse", "Écoulements",
        "Distinguer le premier problème de Stokes en demi-espace de l’approche du profil de Couette entre deux parois.", [
            select("geometry", "Domaine", [("halfspace", "Demi-espace : Stokes"), ("finite", "Deux parois : Couette transitoire")], "halfspace"),
            slider("U", "Vitesse imposée à la paroi", .05, 1, .05, .5, "m·s⁻¹"),
            slider("nu", "Viscosité cinématique ν", .5, 200, .5, 10, "mm²·s⁻¹"),
            slider("h", "Distance de la seconde paroi / fenêtre", 1, 50, 1, 10, "mm"),
            slider("time", "Temps depuis la mise en mouvement", .001, 20, .001, .5, "s")], [
                preset("Début du démarrage", geometry="halfspace", nu=10, h=10, time=.05),
                preset("Couette en formation", geometry="finite", nu=10, h=10, time=.5),
                preset("Couette presque établi", geometry="finite", nu=10, h=10, time=10)]),
    lab("blasius", "Blasius : une couche limite qui s’épaissit", "Écoulements",
        "Passer d’une EDP à un profil universel par similitude puis intégrer l’équation de Blasius par Runge–Kutta.", [
            slider("U", "Vitesse extérieure U∞", .2, 30, .2, 5, "m·s⁻¹"),
            slider("nu", "Viscosité cinématique ν", 1, 100, 1, 15, "mm²·s⁻¹"),
            slider("x", "Distance au bord d’attaque x", .01, 2, .01, .3, "m"),
            slider("rho", "Masse volumique ρ", 1, 1500, .1, 1.2, "kg·m⁻³")], [
                preset("Air sur une plaque", U=5, nu=15, x=.3, rho=1.2),
                preset("Même fluide, plus loin", U=5, nu=15, x=1, rho=1.2),
                preset("Transition à discuter", U=30, nu=15, x=2, rho=1.2)]),
    lab("bernoulli", "Bernoulli généralisé : pertes et pompe", "Écoulements",
        "Établir un bilan de charge avec vitesse moyenne, correction cinétique, frottement, singularités et rendement de pompe.", [
            slider("Q", "Débit-volume Q", .01, 10, .01, .5, "L·s⁻¹"),
            slider("D1", "Diamètre à l’entrée D₁", 1, 15, .1, 5, "cm"),
            slider("D2", "Diamètre de la conduite D₂", 1, 15, .1, 3, "cm"),
            slider("L", "Longueur de la conduite", 0, 100, 1, 20, "m"),
            slider("dz", "Élévation z₂−z₁", -20, 20, .5, 5, "m"),
            slider("rho", "Masse volumique ρ", 1, 2000, .1, 1000, "kg·m⁻³"),
            slider("eta", "Viscosité dynamique η", .01, 1000, .01, 1, "mPa·s"),
            slider("roughness", "Rugosité absolue ε", 0, 1, .01, .05, "mm"),
            slider("K", "Pertes singulières ΣK", 0, 20, .1, 2, ""),
            slider("pump", "Puissance électrique de la pompe", 0, 3000, 10, 100, "W"),
            slider("efficiency", "Rendement de la pompe", .1, 1, .05, .7, ""),
            select("alpha", "Correction d’énergie cinétique α", [("1", "1 : profil quasi uniforme"), ("2", "2 : profil parabolique laminaire")], "1")], [
                preset("Pomper vers un étage", Q=.5, D1=5, D2=3, dz=5, pump=100),
                preset("Venturi sans pertes", Q=2, D1=5, D2=2, L=0, dz=0, K=0, pump=0),
                preset("Huile laminaire", Q=.1, D1=3, D2=3, eta=100, roughness=0, dz=0, alpha="2")]),
    lab("sphere", "Une sphère entre Stokes et inertie", "Écoulements",
        "Comparer traînée et sédimentation ; tester la validité de Stokes avant d’utiliser le temps de relaxation.", [
            slider("R", "Rayon de la sphère", .005, 5, .005, .05, "mm"),
            slider("U", "Vitesse relative imposée", .001, 1, .001, .01, "m·s⁻¹"),
            slider("eta", "Viscosité dynamique η", .01, 2000, .01, 100, "mPa·s"),
            slider("rho", "Masse volumique du fluide", 1, 2000, .1, 1000, "kg·m⁻³"),
            slider("rho_s", "Masse volumique de la sphère", 500, 10000, 100, 2500, "kg·m⁻³")], [
                preset("Microbille dans une huile", R=.05, U=.01, eta=100, rho=1000, rho_s=2500),
                preset("Bille dans l’eau", R=.5, U=.1, eta=1, rho=1000, rho_s=2500),
                preset("Limite de la corrélation", R=5, U=1, eta=1, rho=1000, rho_s=2500)]),
    lab("vortex", "Rankine : circulation et dépression", "Écoulements",
        "Raccorder un cœur en rotation solide à un tourbillon potentiel et intégrer le gradient de pression radial.", [
            slider("R", "Rayon du cœur R", .1, 10, .1, 2, "m"),
            slider("omega", "Vitesse angulaire du cœur Ω", -10, 10, .1, 3, "rad·s⁻¹"),
            slider("rho", "Masse volumique ρ", 1, 1500, .1, 1.2, "kg·m⁻³")], [
                preset("Vortex d’air", R=2, omega=3, rho=1.2),
                preset("Sens inversé", R=2, omega=-3, rho=1.2),
                preset("Vortex dans l’eau", R=.5, omega=2, rho=1000)]),
    lab("magnus", "Magnus : la portance vient de la circulation", "Écoulements",
        "Ajouter une circulation prescrite au potentiel d’un cylindre puis intégrer la pression pour retrouver Kutta–Joukowski.", [
            slider("R", "Rayon du cylindre", .05, 1, .01, .2, "m"),
            slider("U", "Vitesse uniforme U∞ vers +x", .2, 30, .2, 5, "m·s⁻¹"),
            slider("Gamma", "Circulation Γ, positive antihoraire", -30, 30, .2, 4, "m²·s⁻¹"),
            slider("rho", "Masse volumique ρ", 1, 1500, .1, 1.2, "kg·m⁻³")], [
                preset("Cylindre sans circulation", Gamma=0),
                preset("Portance vers le bas", Gamma=4),
                preset("Portance vers le haut", Gamma=-4)]),
    lab("houle", "Houle, rides et orbites des particules", "Ondes",
        "Relier Laplace, conditions aux limites et dispersion ; distinguer déplacement des particules et transport du paquet.", [
            slider("wavelength", "Longueur d’onde λ", .005, 20, .005, 1, "m"),
            slider("h", "Profondeur h", .01, 10, .01, 1, "m"),
            slider("amplitude", "Amplitude de surface a", .0001, .2, .0001, .02, "m"),
            slider("sigma", "Tension superficielle γ", 0, .1, .001, .072, "N·m⁻¹"),
            slider("rho", "Masse volumique ρ", 500, 1500, 10, 1000, "kg·m⁻³")], [
                preset("Houle du TP : λ=h=1 m", wavelength=1, h=1, amplitude=.02),
                preset("Eau peu profonde", wavelength=5, h=.05, amplitude=.002, sigma=0),
                preset("Ride capillaire", wavelength=.01, h=.1, amplitude=.0001)]),
    lab("acoustique", "Pression, vitesse et interface acoustique", "Ondes",
        "Construire l’impédance et distinguer les coefficients d’amplitude de pression, de vitesse et d’énergie.", [
            slider("rho1", "Masse volumique du milieu 1", 1, 1500, .1, 1.2, "kg·m⁻³"),
            slider("c1", "Célérité du milieu 1", 200, 1800, 10, 340, "m·s⁻¹"),
            slider("rho2", "Masse volumique du milieu 2", 1, 1500, .1, 1000, "kg·m⁻³"),
            slider("c2", "Célérité du milieu 2", 200, 1800, 10, 1500, "m·s⁻¹"),
            slider("frequency", "Fréquence f", 20, 25000, 10, 500, "Hz"),
            slider("pressure", "Amplitude incidente de pression", .001, 10, .001, 1, "Pa")], [
                preset("Air → eau", rho1=1.2, c1=340, rho2=1000, c2=1500),
                preset("Milieux identiques", rho1=1.2, c1=340, rho2=1.2, c2=340),
                preset("Eau → air", rho1=1000, c1=1500, rho2=1.2, c2=340)]),
    lab("conduit", "Un conduit sélectionne les modes", "Ondes",
        "La séparation des variables produit une fréquence de coupure ; sous la coupure, l’amplitude décroît sans propagation axiale.", [
            slider("width", "Largeur du conduit a", .05, 2, .01, .3, "m"),
            slider("height", "Hauteur du conduit b", .05, 2, .01, .2, "m"),
            slider("m", "Indice transverse m", 0, 4, 1, 1, ""),
            slider("n", "Indice transverse n", 0, 4, 1, 0, ""),
            slider("frequency", "Fréquence f", 20, 10000, 10, 800, "Hz"),
            slider("c", "Célérité c", 200, 1600, 10, 340, "m·s⁻¹")], [
                preset("Mode plan sans coupure", m=0, n=0, frequency=800),
                preset("Mode (1,0) propagatif", m=1, n=0, frequency=800),
                preset("Mode (1,0) évanescent", m=1, n=0, frequency=300)]),
    lab("diffraction", "Diffraction : une fente devient une antenne", "Ondes",
        "Comparer a et λ puis lire la loi sinc² sans transformer abusivement λ/a en un angle lorsque le premier zéro n’existe pas.", [
            slider("frequency", "Fréquence f", 500, 60000, 100, 25000, "Hz"),
            slider("a", "Largeur de fente a", .1, 10, .1, 1, "cm"),
            slider("c", "Célérité c", 200, 1600, 10, 340, "m·s⁻¹")], [
                preset("Ultrasons du TP : λ>a", frequency=25000, a=1, c=340),
                preset("Premier zéro visible", frequency=25000, a=4, c=340),
                preset("Fente très large", frequency=50000, a=10, c=340)]),
    lab("thermo", "Pourquoi le son est-il adiabatique ?", "Passerelles",
        "Relier compressibilité, équation d’état, capacité thermique et diffusion de chaleur : isotherme et isentropique donnent des célérités différentes.", [
            slider("T", "Température absolue T", 200, 600, 1, 290, "K"),
            slider("M", "Masse molaire M", 2, 100, .1, 29, "g·mol⁻¹"),
            slider("gamma", "Rapport γ=Cp/Cv", 1.05, 1.67, .01, 1.4, ""),
            slider("p", "Pression d’équilibre p₀", 20, 500, .001, 101.325, "kPa"),
            slider("frequency", "Fréquence f", 1, 100000, 1, 1000, "Hz"),
            slider("diffusivity", "Diffusivité thermique Dth", 1, 200, 1, 22, "mm²·s⁻¹")], [
                preset("Air à 17 °C", T=290, M=29, gamma=1.4),
                preset("Hélium", T=290, M=4, gamma=1.67),
                preset("Air chauffé", T=500, M=29, gamma=1.4)]),
    lab("mhd", "Hartmann et Alfvén : le fluide rencontre B", "Passerelles",
        "Comparer freinage de Lorentz, dissipation Joule et tension magnétique ; les modèles quasi statique et MHD idéale ont des hypothèses différentes.", [
            select("mode", "Expérience MHD", [("hartmann", "Hartmann : canal et freinage"), ("alfven", "Alfvén : onde transverse idéale")], "hartmann"),
            slider("B", "Champ magnétique B₀", 0, 2, .01, .2, "T"),
            slider("sigma", "Conductivité électrique σ", 1000, 5000000, 1000, 1000000, "S·m⁻¹"),
            slider("eta", "Viscosité dynamique η", 1, 100, 1, 10, "mPa·s"),
            slider("rho", "Masse volumique ρ", .001, 10000, .001, 1000, "kg·m⁻³"),
            slider("h", "Demi-hauteur du canal h", .1, 20, .1, 2, "mm"),
            slider("G", "Force de pression G=−∂p/∂x", 1, 20000, 1, 1000, "Pa·m⁻¹"),
            slider("wavelength", "Longueur d’onde Alfvén λ", .1, 100, .1, 10, "m"),
            slider("amplitude", "Amplitude de déplacement Alfvén", .001, .1, .001, .01, "m")], [
                preset("Hartmann sans champ", mode="hartmann", B=0),
                preset("Canal magnétique", mode="hartmann", B=.2),
                preset("Onde Alfvén idéale", mode="alfven", B=.2, rho=1000, wavelength=10)]),
    lab("navier", "Taylor–Green : un bilan exact de Navier–Stokes", "Passerelles",
        "Explorer une solution périodique plane : le terme non linéaire est équilibré par la pression et la viscosité amortit l’énergie.", [
            slider("U", "Amplitude initiale U₀", .1, 5, .1, 1, "m·s⁻¹"),
            slider("L", "Période spatiale L", .2, 10, .1, 2, "m"),
            slider("nu", "Viscosité cinématique ν", 0, .1, .001, .01, "m²·s⁻¹"),
            slider("time", "Temps t", 0, 20, .1, 2, "s"),
            slider("rho", "Masse volumique ρ", 1, 2000, 1, 1000, "kg·m⁻³")], [
                preset("Euler : énergie conservée", nu=0),
                preset("Navier–Stokes : amortissement", nu=.01),
                preset("Dissipation rapide", nu=.1, time=5)]),
    lab("hydrostatique", "Pression, profondeur et atmosphère", "Fondations",
        "Intégrer dp/dz=−ρg, avec ρ constante dans un liquide puis ρ(p,T) dans une atmosphère idéale isotherme.", [
            select("mode", "Milieu au repos", [("liquid", "Liquide incompressible"), ("gas", "Atmosphère idéale isotherme")], "liquid"),
            slider("height", "Profondeur liquide / altitude gaz", 0, 10000, 10, 100, "m"),
            slider("rho", "Masse volumique du liquide", 500, 1500, 10, 1000, "kg·m⁻³"),
            slider("p0", "Pression de référence p₀", 20, 200, .001, 101.325, "kPa"),
            slider("T", "Température atmosphérique", 200, 350, 1, 288, "K")], [
                preset("Plongée à 100 m", mode="liquid", height=100),
                preset("Altitude de 5 km", mode="gas", height=5000),
                preset("Atmosphère froide", mode="gas", height=5000, T=220)]),
]

LAB_BY_ID = {item["id"]: item for item in LABS}
