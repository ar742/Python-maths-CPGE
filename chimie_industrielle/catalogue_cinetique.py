"""Huit expériences de cinétique et de génie des réactions."""
from commun import lab,slider,select,preset
CATEGORY='Cinétique & Réacteurs'
LABS=[
lab('horloge_iode','Une horloge chimique pour identifier une loi de vitesse',CATEGORY,'Exploiter les six mesures du TP p.546, puis tester ce qu’un ajustement permet réellement de conclure.',
[slider('vmax','Volume final supposé V∞',8,14,.25,10,'mL')],
[preset('Hypothèse du recueil : 10 mL',vmax=10),preset('Tester une autre asymptote',vmax=12),preset('Une asymptote plus basse',vmax=8)]),
lab('arrhenius_catalyse','Accélérer sans déplacer l’équilibre',CATEGORY,'Comparer une énergie d’activation et un profil catalysé; retrouver le facteur d’accélération à température fixée.',
[slider('temperature','Température T',350,850,10,500,'K'),slider('ea','Énergie d’activation Ea',30,120,5,80,'kJ/mol'),slider('gain','Abaissement de la barrière',0,30,2,20,'kJ/mol')],
[preset('Une voie catalysée',temperature=500,ea=80,gain=20),preset('Sans catalyseur',gain=0),preset('Effet de la température',temperature=750)]),
lab('reacteurs_residence','Choisir un temps de séjour et un réacteur',CATEGORY,'Comparer un réacteur piston, une cuve agitée et plusieurs cuves en série pour une réaction du premier ordre.',
[slider('k','Constante cinétique k',.001,.1,.001,.01,'s⁻¹'),slider('tau','Temps de séjour τ',.1,30,.1,5,'min'),slider('n','Nombre N de cuves',1,8,1,3,integer=True)],
[preset('Même temps de séjour, trois organisations',k=.01,tau=5,n=3),preset('Une seule cuve',n=1),preset('Approcher le piston',n=8)]),
lab('selectivite_successive','Arrêter au bon moment pour conserver l’intermédiaire',CATEGORY,'Étudier A→B→C et chercher quand le produit B est maximal; traiter aussi deux constantes égales.',
[slider('k1','Constante k₁ : A→B',.01,.5,.01,.1,'min⁻¹'),slider('k2','Constante k₂ : B→C',.01,.5,.01,.04,'min⁻¹'),slider('time','Temps de réaction t',1,300,1,15,'min')],
[preset('Former puis consommer B',k1=.1,k2=.04,time=15),preset('Deux constantes égales',k1=.1,k2=.1,time=10),preset('B disparaît vite',k1=.04,k2=.3,time=8)]),
lab('catalyse_surface','Une surface saturée peut ralentir la production',CATEGORY,'Décrire une adsorption compétitive et relier occupation des sites, pression et vitesse.',
[slider('pa','Pression partielle pA',.05,5,.05,1,'bar'),slider('pb','Pression du compétiteur pB',0,10,.25,2,'bar'),slider('ka','Constante d’adsorption KA',.1,10,.1,2,'bar⁻¹'),slider('kb','Constante d’adsorption KB',.1,10,.1,1,'bar⁻¹')],
[preset('Deux espèces en compétition',pa=1,pb=2,ka=2,kb=1),preset('Sans compétiteur',pb=0),preset('Surface occupée par B',pb=10,kb=8)]),
lab('ethanal_aeqs','Une chaîne radicalaire produit un ordre non entier',CATEGORY,'Reprendre le mécanisme de l’éthanal p.549–550 et distinguer ordre apparent, bilan atomique et AEQS.',
[slider('logk1','Exposant a : k₁=10ᵃ s⁻¹',-9,-3,1,-6,integer=True),slider('logk5','Exposant b : k₅=10ᵇ L·mol⁻¹·s⁻¹',0,3,1,2,integer=True),slider('logk6','Exposant c : k₆=10ᶜ L·mol⁻¹·s⁻¹',3,8,1,6,integer=True),slider('concentration','Concentration d’éthanal [E]',.001,1,.001,.1,'mol/L')],
[preset('Propagation dominante',logk1=-6,logk5=2,logk6=6,concentration=.1),preset('Amorçage plus visible',logk1=-3,logk5=0,logk6=8,concentration=.001),preset('Régime intermédiaire',logk1=-4,logk5=1,logk6=5,concentration=.01)]),
lab('emballement_thermique','Chaleur produite et chaleur évacuée : quel équilibre ?',CATEGORY,'Coupler Arrhénius à un bilan de chaleur et distinguer équilibre stable, instable et trajectoire calculée.',
[slider('ambient','Température du fluide extérieur Ta',290,340,5,300,'K'),slider('qref','Chaleur produite à 300 K',.02,2,.02,.5,'W/L'),slider('ea','Énergie d’activation Ea',30,100,5,60,'kJ/mol'),slider('h','Coefficient d’évacuation h',.05,1,.05,.2,'W/(L·K)'),slider('initial','Température initiale T₀',300,380,5,300,'K')],
[preset('Retour à un équilibre stable',ambient=300,qref=.5,ea=60,h=.2,initial=300),preset('Dissipation plus faible',h=.05),preset('Même appareil, démarrage plus chaud',h=.2,initial=350)]),
lab('diffusion_grain','Un catalyseur poreux ne travaille pas toujours partout',CATEGORY,'Comparer réaction et diffusion dans un grain sphérique; calculer le facteur d’efficacité interne.',
[slider('radius','Rayon R du grain',50,1500,50,500,'µm'),slider('logd','Exposant d : Deff=10ᵈ m²/s',-10,-6,1,-8,integer=True),slider('k','Constante k du premier ordre',.001,1,.001,.1,'s⁻¹')],
[preset('Gradient dans le grain',radius=500,logd=-8,k=.1),preset('Petit grain bien alimenté',radius=50,logd=-6,k=.01),preset('Diffusion limitante',radius=1500,logd=-10,k=1)])]
