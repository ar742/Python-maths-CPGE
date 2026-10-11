"""Dix expériences d'électronique analogique, avec unités affichées."""
from commun import slider as s, select, preset as p, lab

CATEGORY = 'Électronique analogique'
LABS = [
    lab('ali_gain_bande', 'ALI : gain, bande et limites', CATEGORY,
        'Amplifier une sinusoïde, puis distinguer le retard du circuit, la saturation et la limite de pente.', [
        s('gain','Gain demandé',1,50,1,10), s('a0','Gain différentiel statique A₀',1000,1000000,1000,100000),
        s('ft','Fréquence de transition fₜ',10,10000,10,1000,'kHz'), s('f','Fréquence de l’entrée',0.01,1000,0.01,10,'kHz'),
        s('e','Amplitude de l’entrée',0.01,5,0.01,0.5,'V'), s('vsat','Limite de tension',2,15,0.1,12,'V'),
        s('imax','Limite de courant',1,100,1,20,'mA'), s('rl','Résistance de charge',50,10000,50,1000,'Ω'),
        s('sr','Vitesse de balayage maximale',0.01,20,0.01,0.5,'V/µs'), s('vos','Décalage d’entrée — prolongement',-5,5,0.1,0,'mV')],
        [p('Régime linéaire',gain=10,f=1,e=0.5,sr=1,rl=1000),p('Bande limitée',gain=40,f=100,e=0.1,sr=20),
         p('Pente limitée',gain=10,f=10,e=0.8,sr=0.05),p('Courant limité',gain=10,f=1,e=0.8,rl=100,imax=10),p('Tension saturée',gain=10,e=2,f=1)]),
    lab('suiveur_cascade','Suiveur et association de filtres',CATEGORY,
        'Comparer deux cellules RC directement reliées avec les mêmes cellules séparées par un suiveur.',[
        s('r1','Résistance de la première cellule',1,100,1,10,'kΩ'),s('r2','Résistance de la seconde cellule',1,100,1,10,'kΩ'),
        s('c1','Capacité de la première cellule',1,100,1,10,'nF'),s('c2','Capacité de la seconde cellule',1,100,1,10,'nF'),
        s('f','Fréquence de l’entrée',10,100000,10,1000,'Hz'),s('e','Amplitude de l’entrée',0.1,5,0.1,1,'V'),
        s('rs','Résistance interne d’un capteur',1,100,1,10,'kΩ'),s('rl','Résistance de lecture du capteur',1,1000,1,10,'kΩ')],
        [p('Deux cellules identiques',r1=10,r2=10,c1=10,c2=10,f=1590),p('Charge marquée',r1=100,r2=1,c1=10,c2=10,f=1000),p('Lecture d’un capteur',rs=100,rl=10)]),
    lab('sommateur_inverseur','Sommateur inverseur',CATEGORY,
        'Construire une somme pondérée de deux tensions, puis prévoir les signes et la saturation.',[
        s('r1','Résistance de la première entrée',1,100,1,10,'kΩ'),s('r2','Résistance de la seconde entrée',1,100,1,20,'kΩ'),
        s('rf','Résistance de rétroaction',1,100,1,20,'kΩ'),s('e1','Amplitude de la première entrée',0,5,0.1,1,'V'),
        s('e2','Amplitude de la seconde entrée',0,5,0.1,1,'V'),s('f','Fréquence de la première entrée',10,10000,10,1000,'Hz'),
        s('phase','Phase de la seconde entrée',-180,180,5,0,'°'),s('vsat','Limite de tension de sortie',2,15,0.1,12,'V')],
        [p('Poids 2 et 1',r1=10,r2=20,rf=20),p('Somme de même poids',r1=10,r2=10,rf=10),p('Saturation',rf=100,e1=3,e2=2)]),
    lab('integrateur_derivateur','Intégrer et dériver une tension',CATEGORY,
        'Relier une opération sur le temps à une fonction de transfert et observer l’effet des résistances de protection.',[
        select('mode','Montage',[('integrateur','Intégrateur idéal'),('derivee','Dérivateur idéal'),('ameliore','Dérivateur amélioré')],'ameliore'),
        s('r','Résistance d’entrée R',1,100,1,10,'kΩ'),s('c','Capacité d’entrée ou d’intégration C',1,1000,1,10,'nF'),
        s('rf','Résistance de rétroaction R′',1,100,1,100,'kΩ'),s('cf','Capacité de rétroaction C′',0.1,100,0.1,1,'nF'),
        s('e','Amplitude de l’entrée',0.1,3,0.1,1,'V'),s('f','Fréquence de l’entrée',10,100000,10,1000,'Hz')],
        [p('Dériver dans la bonne bande',mode='ameliore',r=10,c=10,rf=100,cf=1,f=100),p('Dérivateur limité en haute fréquence',mode='ameliore',f=20000),p('Intégrer depuis une sortie nulle',mode='integrateur',f=1000)]),
    lab('schmitt_trigger','Comparateur à hystérésis',CATEGORY,
        'Faire monter puis descendre une tension : les deux seuils donnent au circuit une mémoire.',[
        s('r1','Résistance sortie–entrée positive',1,100,1,20,'kΩ'),s('r2','Résistance entrée positive–masse',1,100,1,10,'kΩ'),
        s('vsat','Valeur absolue des niveaux de sortie',2,15,0.1,12,'V'),s('e','Amplitude de la rampe triangulaire',0.1,15,0.1,6,'V'),
        s('noise','Amplitude du bruit déterministe ajouté',0,2,0.05,0,'V'),s('f','Fréquence de la rampe',10,10000,10,1000,'Hz'),
        select('initial','État initial',[('haut','Sortie positive'),('bas','Sortie négative')],'haut')],
        [p('Deux seuils',r1=20,r2=10,e=6,noise=0),p('Mémoire sans basculement',e=1,noise=0),p('Rampe bruitée',e=6,noise=0.7)]),
    lab('astable','Oscillateur de relaxation',CATEGORY,
        'Suivre la charge d’un condensateur et les basculements de l’ALI ; une tension continue rend les deux durées inégales.',[
        s('r1','Résistance de charge du condensateur',1,100,1,10,'kΩ'),s('c','Capacité',1,1000,1,100,'nF'),
        s('r2','Résistance entrée positive–commande',1,100,1,10,'kΩ'),s('r3','Résistance entrée positive–sortie',1,100,1,20,'kΩ'),
        s('ve','Tension continue de commande',-12,12,0.1,0,'V'),s('vsat','Valeur absolue des niveaux de sortie',2,15,0.1,12,'V')],
        [p('Oscillation symétrique',ve=0,r2=10,r3=20),p('Deux durées différentes',ve=5),p('Oscillations arrêtées',ve=12,vsat=10)]),
    lab('wien','Oscillateur à pont de Wien',CATEGORY,
        'Trouver la fréquence sélectionnée par le pont, puis passer de l’extinction au démarrage des oscillations.',[
        s('r1','Résistance de la branche série',1,100,1,10,'kΩ'),s('r2','Résistance de la branche parallèle',1,100,1,10,'kΩ'),
        s('c1','Capacité de la branche série',1,100,1,10,'nF'),s('c2','Capacité de la branche parallèle',1,100,1,10,'nF'),
        s('margin','Rapport gain / gain critique',0.8,1.2,0.005,1.02),s('vsat','Échelle de limitation d’amplitude',2,15,0.1,12,'V'),
        s('seed','Petite perturbation initiale',0.001,0.2,0.001,0.02,'V')],
        [p('Extinction',margin=0.95),p('Seuil linéaire',margin=1),p('Démarrage et limitation',margin=1.02),p('Pont dissymétrique',r1=20,r2=10,c1=10,c2=20,margin=1.02)]),
    lab('redresseur_precision','Redresseur de précision : valeur absolue',CATEGORY,
        'Comparer un pont de diodes et un ALI qui compense le seuil des diodes, surtout pour une petite tension.',[
        s('e','Amplitude de l’entrée',0.01,5,0.01,0.2,'V'),s('f','Fréquence de l’entrée',10,10000,10,1000,'Hz'),
        s('vd','Seuil d’une diode',0,0.9,0.01,0.6,'V'),s('vsat','Limite de tension de l’ALI',2,15,0.1,12,'V')],
        [p('Petite tension',e=0.2,vd=0.6),p('Diodes idéales',vd=0,e=1),p('Compensation limitée par l’alimentation',e=5,vsat=3,vd=0.6)]),
    lab('filtre_etat','Filtre actif à trois ALI',CATEGORY,
        'Choisir une bande de fréquences, puis isoler des harmoniques d’un créneau et suivre les deux tensions internes.',[
        s('r1','Résistance d’entrée R₁',1,100,1,10,'kΩ'),s('r2','Résistance de rétroaction R₂',1,100,1,30,'kΩ'),
        s('r3','Résistance de retour R₃',1,100,1,10,'kΩ'),s('r4','Résistance de l’inverseur R₄',1,100,1,10,'kΩ'),
        s('r5','Résistance de l’inverseur R₅',1,100,1,10,'kΩ'),s('r6','Résistance de l’intégrateur R₆',1,100,1,10,'kΩ'),
        s('c','Capacité commune aux deux condensateurs',1,100,1,10,'nF'),s('e','Amplitude de l’entrée',0.1,3,0.1,1,'V'),
        s('f','Fréquence fondamentale de l’entrée',10,100000,10,530,'Hz'),
        select('signal','Signal d’entrée',[('sinus','Sinusoïde'),('creneau','Créneau alternatif impair')],'creneau'),
        s('harmonics','Nombre d’harmoniques impaires calculées',1,60,1,30,integer=True)],
        [p('Isoler le troisième harmonique',f=530,r2=30,signal='creneau'),p('Sinusoïde à la résonance',f=1590,signal='sinus'),p('Bande plus étroite',r2=100,signal='creneau',f=530)]),
    lab('transistor_polarisation','Transistor : polarisation et petits signaux',CATEGORY,
        'Prolongement accompagné : placer le point de repos d’un transistor NPN, puis amplifier une petite variation.',[
        s('vcc','Tension d’alimentation',5,15,0.1,12,'V'),s('rb1','Résistance base–masse',5,100,1,10,'kΩ'),
        s('rb2','Résistance alimentation–base',10,100,1,47,'kΩ'),s('rc','Résistance de collecteur',1,10,0.1,2.2,'kΩ'),
        s('re','Résistance d’émetteur',0.1,2,0.1,1,'kΩ'),s('beta','Gain en courant β',50,300,1,100),
        s('rg','Résistance du générateur',0.1,10,0.1,1,'kΩ'),s('rl','Résistance de charge en alternatif',1,100,1,10,'kΩ'),
        s('c1','Capacité de liaison d’entrée',0.1,100,0.1,1,'µF'),s('ce','Capacité de découplage d’émetteur',0.1,1000,0.1,100,'µF'),
        select('bypass','Condensateur de découplage',[('oui','Connecté'),('non','Déconnecté')],'oui'),
        s('e','Amplitude de la petite variation d’entrée',0.001,0.1,0.001,0.01,'V'),s('f','Fréquence de cette variation',10,100000,10,1000,'Hz')],
        [p('Régime actif',rb1=10,rb2=47,re=1,rc=2.2,e=0.01),p('Contre-réaction d’émetteur',bypass='non'),p('Saturation au repos',rb1=47,rb2=10,re=0.1,rc=10),p('Blocage',vcc=5,rb1=5,rb2=100)])
]
