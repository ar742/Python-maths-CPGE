"""Six expériences : rayonnement, mesures et couplages de la fiche P24."""
from commun import lab, slider, preset

CATEGORY='Effets couplés & mesures'

LABS=[
    lab('cube_leslie','Cube de Leslie : comparer des surfaces à même température',CATEGORY,
        'Quatre surfaces à même température ne rayonnent pas autant. Relier leur émission et leur absorption au bilan thermique du cube de Leslie.',
        [slider('T','Température T du cube',300,450,1,373,'K'),slider('Tamb','Température ambiante Tₐ',280,320,1,293,'K'),slider('side','Côté a du cube',.05,.20,.01,.10,'m'),slider('h','Coefficient de convection h',2,25,1,8,'W·m⁻²·K⁻¹'),slider('capacity','Capacité thermique totale Cₜₕ',200,2000,50,900,'J·K⁻¹')],
        [preset('TP : eau chaude dans une pièce',T=373,Tamb=293,h=8),preset('Près de l’ambiance : comparer les mécanismes',T=305,Tamb=293,h=8),preset('Convection plus forte',T=373,Tamb=293,h=20)]),
    lab('seebeck','Thermocouple : calibrer et compenser la jonction froide',CATEGORY,
        'Deux métaux et deux températures produisent une tension. Étalonner un thermocouple et corriger la température de sa jonction de référence.',
        [slider('Th','Température Tₕ à mesurer',250,650,.05,423.15,'K'),slider('Tc','Température Tf de la jonction froide',250,330,.05,293.15,'K'),slider('S0','Coefficient S₀ à 273,15 K',30,60,1,40,'µV·K⁻¹'),slider('slope','Pente s₁ du coefficient Seebeck',-.03,.03,.001,.015,'µV·K⁻²'),slider('cold_error','Erreur sur la température de la jonction froide',-10,10,.5,0,'K')],
        [preset('Coefficient constant : mesure linéaire',S0=40,slope=0,Th=423.15,Tc=293.15,cold_error=0),preset('Calibration légèrement courbe',S0=40,slope=.025,Th=600,Tc=293.15,cold_error=0),preset('Jonction froide mal mesurée',S0=40,slope=.015,Th=423.15,Tc=313.15,cold_error=5)]),
    lab('peltier','Module Peltier : refroidir demande un bilan complet',CATEGORY,
        'Un courant transporte de la chaleur entre deux faces. Comparer refroidissement, pertes Joule et consommation électrique d’un module Peltier.',
        [slider('Tc','Température froide Tc',260,310,1,280,'K'),slider('delta','Écart ΔT entre les faces',0,60,1,20,'K'),slider('I','Courant I orienté pour refroidir',0,10,.1,3,'A'),slider('alpha','Coefficient thermoélectrique α',.01,.08,.002,.05,'V·K⁻¹'),slider('R','Résistance électrique R',.5,4,.1,1.5,'Ω'),slider('K','Conductance thermique K',.1,2,.1,.7,'W·K⁻¹'),slider('load','Charge thermique à extraire',0,50,1,5,'W')],
        [preset('Refroidissement possible',Tc=280,delta=20,I=3,alpha=.05,R=1.5,K=.7),preset('Trop de courant : Joule prend le dessus',Tc=280,delta=20,I=10,alpha=.03,R=2,K=.7),preset('Courant coupé : la fuite réchauffe',Tc=280,delta=30,I=0,alpha=.05,R=1.5,K=.7)]),
    lab('thermoacoustique','Onde sonore : coupler compression et diffusion thermique',CATEGORY,
        'Dans un gaz, une onde de pression fait varier la température. Étudier comment la conduction modifie la propagation et atténue l’onde.',
        [slider('frequency','Fréquence f',20,20000,20,6000,'Hz'),slider('conductivity','Conductivité thermique λ',0,100,.001,.026,'W·m⁻¹·K⁻¹'),slider('P0','Pression au repos P₀',50000,200000,5000,100000,'Pa'),slider('T0','Température au repos T₀',250,350,1,293,'K'),slider('rho','Masse volumique au repos ρ₀',.5,3,.1,1.2,'kg·m⁻³'),slider('gamma','Rapport γ des capacités thermiques',1.1,1.8,.05,1.4),slider('length','Longueur observée L',.1,200,.1,100,'m')],
        [preset('Gaz peu conducteur : presque adiabatique',frequency=6000,conductivity=.026,length=100,gamma=1.4),preset('Conduction renforcée : observer le couplage',frequency=12000,conductivity=50,length=5,gamma=1.4),preset('Limite sans diffusion thermique',frequency=6000,conductivity=0,length=100,gamma=1.4)]),
    lab('piezo_resonateur','Quartz : réciprocité, résonance et antirésonance',CATEGORY,
        'Une tension déforme un quartz, qui produit à son tour une charge. Relier cette réciprocité à la résonance et au circuit électrique équivalent.',
        [slider('mass_mg','Masse m',50,1000,10,200,'mg'),slider('stiffness_MN','Raideur k',.2,3,.1,1,'MN·m⁻¹'),slider('capacity_nF','Capacité C',.2,5,.1,1,'nF'),slider('theta_mC','Couplage θ',2,20,1,10,'mC·m⁻¹ = mN·V⁻¹'),slider('damping','Amortissement relatif ζ',.002,.08,.002,.01),slider('ratio','Fréquence réduite f/fᵣ',.6,1.8,.01,1),slider('voltage','Amplitude V de la tension',.1,10,.1,1,'V')],
        [preset('Résonance peu amortie',damping=.004,ratio=1,theta_mC=10),preset('Antirésonance : couplage marqué',capacity_nF=1,stiffness_MN=1,theta_mC=20,ratio=1.18,damping=.004),preset('Amortissement : des pics plus larges',damping=.06,ratio=1,theta_mC=10)]),
    lab('brouillard','Détente d’une vapeur saturante : décider du début de condensation',CATEGORY,
        'Une vapeur saturante se détend et refroidit. Comparer les pentes de pression pour prévoir le début de condensation, sans prolonger le modèle après ce début.',
        [slider('Tstar','Température initiale T*',250,380,.05,293.15,'K'),slider('latent_MJ','Chaleur latente L* à T*',.2,2.8,.01,2.44,'MJ·kg⁻¹'),slider('B','Coefficient B de la loi de Regnault',500,3000,10,2370,'J·kg⁻¹·K⁻¹'),slider('gamma','Rapport γ des capacités thermiques',1.1,1.67,.01,1.33),slider('drop','Refroidissement exploré ΔT',.01,15,.01,5,'K')],
        [preset('Vapeur d’eau : début immédiat de condensation',Tstar=293.15,latent_MJ=2.44,B=2370,gamma=1.33,drop=5),preset('Comparer les pentes sans condensation initiale',Tstar=320,latent_MJ=.2,B=1500,gamma=1.33,drop=10),preset('Sensibilité au rapport des capacités',Tstar=300,latent_MJ=1,B=2370,gamma=1.1,drop=10)])
]
