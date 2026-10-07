"""Quinze expériences de réactivité : commandes, cas et limites publiques."""
from commun import slider as s, select as q, preset as p, lab

LABS = [
    lab('electrons', 'Flèches : où vont réellement les électrons ?', 'Comprendre la réactivité',
        'Distinguer déplacement de doublet, transfert de proton, substitution, homolyse et mésomérie ; contrôler charges et inventaire électronique.', [
        q('reaction', 'Transformation à suivre', [('acid','Transfert de proton'),('sn2','Substitution nucléophile'),('homolysis','Homolyse de Br₂'),('resonance','Mésomérie du carboxylate')], 'acid'),
        s('stage','Étape du schéma',0,2,1,0,integer=True), s('barrier','Barrière pédagogique choisie',10,100,1,45,'kJ·mol⁻¹')], [
        p('Le doublet attaque H',reaction='acid',stage=0),p('La liaison C–Br cède son doublet',reaction='sn2',stage=0),
        p('Deux électrons séparés',reaction='homolysis',stage=0),p('Une structure, deux contributeurs',reaction='resonance',stage=0)]),
    lab('acidebase', 'Acidité, basicité et avancement : choisir avant d’attaquer', 'Comprendre la réactivité',
        'Résoudre HA + B ⇌ A⁻ + BH⁺ à partir des pKₐ dans un même solvant, avec bilans de matière et limite stœchiométrique.', [
        s('pka_acid','pKₐ de HA',-5,50,.1,10),s('pka_base','pKₐ de BH⁺',-5,50,.1,11),
        s('base_ratio','Quantité initiale B / HA',.1,3,.05,1),s('concentration','Concentration initiale HA',.01,1,.01,.1,'mol·L⁻¹')], [
        p('Phénol et amine : équilibre',pka_acid=10,pka_base=11,base_ratio=1),
        p('Alcool et amidure : déprotonation',pka_acid=16,pka_base=38,base_ratio=1),
        p('Alcyne terminal et amine : insuffisant',pka_acid=25,pka_base=11,base_ratio=1),
        p('Base limitante malgré K immense',pka_acid=5,pka_base=30,base_ratio=.4)]),
    lab('sn2', 'SN2 : cinétique bimoléculaire et inversion de Walden', 'Substituer ou éliminer',
        'Suivre une substitution concertée, son état de transition et son inversion géométrique ; tester les cas tertiaire et vinylique où ce mécanisme classique échoue.', [
        q('substrate','Carbone portant le groupe partant',[('methyl','Méthyle'),('primary','Primaire'),('secondary','Secondaire'),('tertiary','Tertiaire'),('vinyl','Vinylique')],'secondary'),
        s('k','Constante k₂ choisie',.001,2,.001,.15,'L·mol⁻¹·s⁻¹'),s('a0','Concentration initiale RX',.01,1,.01,.2,'mol·L⁻¹'),
        s('b0','Concentration initiale Nu⁻',.01,2,.01,.3,'mol·L⁻¹'),s('time','Durée d’observation',1,300,1,80,'s'),
        s('stage','Réactifs, état de transition, produits',0,2,1,0,integer=True)], [
        p('Inversion sur un centre secondaire',substrate='secondary',stage=0,a0=.2,b0=.3),
        p('Même quantité des deux réactifs',substrate='primary',a0=.2,b0=.2),p('Nucléophile en grand excès',substrate='primary',a0=.1,b0=2),
        p('Carbone tertiaire : obstruction',substrate='tertiary'),p('Halogénure vinylique : autre chimie',substrate='vinyl')]),
    lab('sn1', 'SN1 : intermédiaire, solvolyse et mémoire stéréochimique', 'Substituer ou éliminer',
        'Résoudre RX → R⁺ → ROH avec deux constantes apparentes ; distinguer carbocation plan, racémisation idéale, paire d’ions et possibilité de réarrangement.', [
        q('substrate','Substrat',[('tertiary','Halogénure tertiaire'),('benzyl','Halogénure benzylique'),('secondary','Halogénure secondaire'),('rearrange','Secondaire pouvant se réarranger'),('primary','Primaire non stabilisé'),('vinyl','Vinylique')],'tertiary'),
        s('k1','Ionisation k₁ choisie',.001,.2,.001,.02,'s⁻¹'),s('k2','Capture k₂ apparente choisie',.005,1,.005,.1,'s⁻¹'),
        s('time','Durée d’observation',1,500,1,150,'s'),s('bias','Excès de capture par la face arrière, modèle',0,40,1,0,'points de %'),
        s('stage','Étape : ionisation, migration éventuelle, capture',0,4,1,1,integer=True)], [
        p('Carbocation puis produit',substrate='tertiary',bias=0,k1=.02,k2=.1),p('Accumuler l’intermédiaire',k1=.1,k2=.01),
        p('Paire d’ions : racémisation incomplète',substrate='secondary',bias=20),p('Migration 1,2 possible',substrate='rearrange',stage=1),
        p('Primaire sans stabilisation',substrate='primary')]),
    lab('competition', 'SN1 / SN2 / E1 / E2 : une compétition explicite', 'Substituer ou éliminer',
        'Séparer critères structuraux et cinétiques. Les fractions sont calculées uniquement à partir de constantes choisies, avec nucléophile et base maintenus en excès.', [
        q('substrate','Famille du substrat',[('primary','Primaire'),('secondary','Secondaire'),('tertiary','Tertiaire'),('methyl','Méthyle'),('vinyl','Vinylique')],'secondary'),
        s('nu','Concentration Nu',0,2,.05,.5,'mol·L⁻¹'),s('base','Concentration base',0,2,.05,.5,'mol·L⁻¹'),
        s('k_sn2','k₂ de SN2 choisi',0,1,.01,.2,'L·mol⁻¹·s⁻¹'),s('k_e2','k₂ de E2 choisi',0,1,.01,.1,'L·mol⁻¹·s⁻¹'),
        s('k_ion','Ionisation commune SN1/E1 choisie',0,.2,.001,.005,'s⁻¹'),s('capture','Fraction du carbocation capturée, modèle',0,100,1,80,'%'),
        s('time','Durée',1,200,1,50,'s')], [
        p('Nucléophile, faible basicité',substrate='primary',nu=1,base=.05,k_ion=0),
        p('Base forte : E2 favorisée',substrate='secondary',nu=.2,base=1.5,k_e2=.5,k_ion=0),
        p('Solvolyse tertiaire',substrate='tertiary',nu=0,base=0,k_ion=.05,capture=85),
        p('Méthyle : aucun H en β',substrate='methyl',nu=1,base=1),p('Toutes les voies arrêtées',nu=0,base=0,k_ion=0)]),
    lab('elimination', 'E2 : anti-périplanarité et verrou cyclohexanique', 'Substituer ou éliminer',
        'Relier dièdre H–C–C–Br, accessibilité anti et population des chaises ; voir pourquoi la géométrie peut imposer un produit avant Zaïtsev.', [
        q('system','Squelette',[('acyclic','Chaîne : 2-bromobutane'),('cyclohexane','trans-1-bromo-2-méthylcyclohexane')],'acyclic'),
        s('dihedral','Dièdre Hβ–Cβ–Cα–Br',0,360,5,180,'°'),s('temperature','Température',250,420,5,298,'K'),
        s('chair_gap','G(chaise diaxiale) − G(diéquatoriale)',0,20,.5,8,'kJ·mol⁻¹'),
        s('barrier_z','Barrière vers le plus substitué, modèle',40,110,1,65,'kJ·mol⁻¹'),
        s('barrier_h','Barrière vers le moins substitué, modèle',40,110,1,70,'kJ·mol⁻¹')], [
        p('Conformation anti disponible',system='acyclic',dihedral=180),p('Conformation syn : non retenue ici',system='acyclic',dihedral=0),
        p('Chaise majoritaire non réactive',system='cyclohexane',chair_gap=8),
        p('Encombrement : barrière de Hofmann abaissée',system='acyclic',dihedral=180,barrier_z=80,barrier_h=60)]),
    lab('alcene', 'Alcènes : régiochimie, stéréochimie et réarrangements', 'Ajouter et transformer',
        'Comparer les familles d’additions sur un même squelette : électrophile, bromonium, hydroboration, hydrogénation, époxydation et coupure oxydante.', [
        q('substrate','Alcène',[('propene','Propène'),('butene_E','(E)-but-2-ène'),('butene_Z','(Z)-but-2-ène'),('rearrange','3-méthylbut-1-ène')],'propene'),
        q('reagent','Conditions documentées',[('hbr','HBr sans peroxydes'),('water','H₂O / H⁺'),('borane','1. BH₃ ; 2. H₂O₂ / HO⁻'),('bromine','Br₂ sans lumière'),('hydrogen','H₂ / métal'),('epoxide','Peracide'),('diol','Oxydation douce : diol syn'),('ozone','1. O₃ ; 2. traitement réducteur')],'borane'),
        s('stage','Avancement du mécanisme ou bilan',0,2,1,2,integer=True)], [
        p('Propène → propan-1-ol',substrate='propene',reagent='borane'),p('Propène → propan-2-ol',substrate='propene',reagent='water'),
        p('Bromonium : addition anti',substrate='butene_E',reagent='bromine',stage=1),p('Réarrangement après protonation',substrate='rearrange',reagent='hbr',stage=1),
        p('Coupure : reconnaître les fragments',substrate='butene_E',reagent='ozone')]),
    lab('alcyne', 'Alcynes : deux additions, réduction et tautomérie', 'Ajouter et transformer',
        'Le choix des réactifs distingue alcène E, alcène Z, alcane et dérivé carbonylé ; suivre l’énol sans le confondre avec le produit isolé.', [
        q('substrate','Alcyne',[('propyne','Propyne terminal'),('butyne','But-2-yne interne')],'butyne'),
        q('reagent','Conditions',[('lindlar','H₂ / Lindlar'),('dissolving','Na / NH₃ liquide'),('hydrogen','H₂ en excès / métal'),('mercury','H₂O / H⁺ / Hg²⁺'),('borane','Hydroboration sélective puis oxydation'),('hbr1','Un équivalent HBr'),('hbr2','Deux équivalents HBr'),('br1','Un équivalent Br₂'),('br2','Deux équivalents Br₂')],'lindlar'),
        s('stage','Alcyne, intermédiaire, produit',0,2,1,2,integer=True)], [
        p('Alcène Z',substrate='butyne',reagent='lindlar'),p('Alcène E',substrate='butyne',reagent='dissolving'),
        p('Alcyne terminal → cétone',substrate='propyne',reagent='mercury',stage=2),p('Alcyne terminal → aldéhyde',substrate='propyne',reagent='borane',stage=2),
        p('Deux additions HBr : dibromure geminal',substrate='propyne',reagent='hbr2')]),
    lab('radical', 'Radicaux : chaîne, effet peroxyde et sélectivité', 'Ajouter et transformer',
        'Distinguer amorçage, propagation et terminaison ; pondérer les sites par leurs hydrogènes plutôt que compter seulement les carbones.', [
        q('mode','Expérience',[('halogenation','Monohalogénation de l’isobutane'),('peroxide','Addition radicalaire sur le propène')],'halogenation'),
        q('halogen','Réactif',[('cl','Cl₂'),('br','Br₂'),('hbr','HBr / peroxydes'),('hcl','HCl / peroxydes'),('hi','HI / peroxydes')],'br'),
        s('selectivity','k(H tertiaire) / k(H primaire), choisi',1,2000,1,1600),s('initiation','Source radicalaire Rᵢ, modèle',.0001,.01,.0001,.001,'mol·L⁻¹·s⁻¹'),
        s('termination','Constante de terminaison kₜ choisie',1e5,1e8,1e5,1e7,'L·mol⁻¹·s⁻¹'),s('stage','Étape de chaîne',0,3,1,1,integer=True)], [
        p('Chloration, faible sélectivité',mode='halogenation',halogen='cl',selectivity=5),p('Bromation, forte sélectivité',mode='halogenation',halogen='br',selectivity=1600),
        p('Effet peroxyde : HBr seulement',mode='peroxide',halogen='hbr'),p('HCl : propagation défavorable',mode='peroxide',halogen='hcl'),
        p('HI : première propagation défavorable',mode='peroxide',halogen='hi')]),
    lab('carbonyle', 'Carbonyles : addition, substitution acyle et énolates', 'Construire une synthèse',
        'Comparer des transformations documentées, étape par étape : AN, addition–élimination, aldolisation, crotonisation, acétal, Michael, Wittig et ouverture d’époxyde.', [
        q('reaction','Transformation',[('addition','NaBH₄ : addition d’hydrure'),('ester','Estérification de Fischer'),('amide','Chlorure d’acyle + amine'),('aldol','Aldolisation de l’éthanal'),('croton','Crotonisation de l’aldol'),('acetal','Acétalisation de l’éthanal'),('michael','Addition 1,4 d’un énolate'),('wittig','Wittig sur la propanone'),('epoxide','Ouverture d’époxyde par HO⁻')],'aldol'),
        s('stage','Étape représentée',0,4,1,0,integer=True),s('water','Activité de l’eau relative, modèle d’équilibre',.01,3,.01,1),
        s('equilibrium','K choisi pour estérification/acétalisation',.1,20,.1,4)], [
        p('Aldol : construire C–C',reaction='aldol',stage=1),p('Crotonisation : former la conjugaison',reaction='croton',stage=2),
        p('Amide : activer l’acide',reaction='amide',stage=1),p('Acétal : retirer l’eau',reaction='acetal',water=.05),
        p('Michael : attaque en β',reaction='michael',stage=0)]),
    lab('grignard', 'Organomagnésiens : former C–C et survivre aux protons', 'Construire une synthèse',
        'Choisir un électrophile, compter les équivalents et tester une fonction protique ; un ester requiert deux additions et ne livre pas une cétone pure avec un seul équivalent.', [
        q('substrate','Électrophile',[('methanal','Méthanal'),('aldehyde','Éthanal'),('ketone','Propanone'),('ester','Éthanoate d’éthyle'),('co2','CO₂'),('epoxide','Oxyde d’éthylène'),('protic','Hydroxypropanone non protégée')],'ketone'),
        q('alkyl','Groupe transféré',[('methyl','CH₃MgBr'),('ethyl','EtMgBr'),('phenyl','PhMgBr')],'methyl'),
        s('equivalents','Équivalents RMgBr ajoutés',0,4,.1,1),s('water','Équivalents de contaminants protoniques',0,3,.1,0),
        s('stage','Addition puis hydrolyse',0,2,1,2,integer=True)], [
        p('Méthanal → alcool primaire',substrate='methanal',alkyl='ethyl',equivalents=1),p('Cétone → alcool tertiaire',substrate='ketone',equivalents=1),
        p('Ester : deux équivalents nécessaires',substrate='ester',equivalents=2),p('Ester : un équivalent ne garantit pas la cétone',substrate='ester',equivalents=1),
        p('Fonction OH : destruction prioritaire',substrate='protic',equivalents=1)]),
    lab('oxydoreduction', 'Oxydoréduction : choisir une fonction et un réactif', 'Construire une synthèse',
        'Contrôler le nombre d’oxydation du carbone et la chimiosélectivité : alcools, carbonyles, esters, acides et nitroaromatiques.', [
        q('substrate','Fonction de départ',[('alcohol1','Alcool primaire'),('alcohol2','Alcool secondaire'),('alcohol3','Alcool tertiaire'),('aldehyde','Aldéhyde'),('ketone','Cétone'),('ester','Ester'),('acid','Acide carboxylique'),('nitro','Nitrobenzène')],'ester'),
        q('reagent','Réactif / conditions',[('pcc','Oxydant doux anhydre, type PCC'),('aqueous','Oxydant fort aqueux'),('nabh4','NaBH₄, conditions usuelles'),('lialh4','LiAlH₄ anhydre puis hydrolyse'),('metal','Fe / H⁺ puis neutralisation')],'lialh4'),
        s('stage','Avant / après transformation',0,1,1,1,integer=True)], [
        p('Alcool primaire → aldéhyde',substrate='alcohol1',reagent='pcc'),p('Alcool primaire → acide',substrate='alcohol1',reagent='aqueous'),
        p('NaBH₄ laisse l’ester',substrate='ester',reagent='nabh4'),p('LiAlH₄ réduit l’ester',substrate='ester',reagent='lialh4'),
        p('Nitrobenzène → aniline',substrate='nitro',reagent='metal')]),
    lab('aromatique', 'SEA : orientation, activation et ordre de synthèse', 'Comprendre la réactivité',
        'Séparer orientation et vitesse : les halogènes désactivent tout en orientant ortho/para ; une forte désactivation interdit les Friedel–Crafts usuelles.', [
        q('substituent','Groupe déjà présent',[('h','H : benzène'),('methyl','CH₃'),('oh','OH'),('methoxy','OCH₃'),('chloro','Cl'),('nitro','NO₂'),('acyl','COCH₃')],'chloro'),
        q('reaction','SEA envisagée',[('nitration','Nitration'),('bromination','Bromation avec FeBr₃'),('alkylation','Friedel–Crafts : alkylation'),('acylation','Friedel–Crafts : acylation')],'nitration'),
        s('temperature','Température, modèle de barrières',250,450,5,298,'K'),
        s('go','Barrière par site ortho choisie',40,120,1,75,'kJ·mol⁻¹'),s('gm','Barrière par site méta choisie',40,120,1,90,'kJ·mol⁻¹'),
        s('gp','Barrière par site para choisie',40,120,1,72,'kJ·mol⁻¹'),s('stage','Électrophile, complexe σ, produit',0,2,1,0,integer=True)], [
        p('Halogène : ortho/para mais désactivant',substituent='chloro',go=75,gm=90,gp=72),
        p('NO₂ : orientation méta',substituent='nitro',go=105,gm=90,gp=110),
        p('CH₃ : orientation ortho/para',substituent='methyl',go=65,gm=80,gp=63),
        p('Friedel–Crafts sur nitrobenzène : arrêt',substituent='nitro',reaction='acylation'),
        p('Deux ortho, deux méta, un para : compter',substituent='h',go=80,gm=80,gp=80)]),
    lab('orbitales', 'Orbitales : CLOA, Hückel et Diels–Alder', 'Comprendre la réactivité',
        'Normaliser des combinaisons d’orbitales puis diagonaliser un système π ; reconnaître HO/BV, aromaticité sous hypothèses et géométrie s-cis d’un diène.', [
        q('system','Système',[('lcao','Deux OA réelles normalisées'),('butadiene','Butadiène : chaîne π'),('benzene','Benzène : cycle π'),('cyclobutadiene','Cyclobutadiène plan idéalisé'),('diels','Butadiène + éthène : Diels–Alder')],'butadiene'),
        s('overlap','Recouvrement S des deux OA',0,.8,.02,.2),s('beta','|β| : couplage π choisi',.5,4,.1,2.5,'eV'),
        s('torsion','Dièdre central du diène',0,180,5,0,'°'),s('orbital','OM affichée, par énergie croissante',1,6,1,2,integer=True)], [
        p('Liante et antiliante normalisées',system='lcao',overlap=.2,orbital=1),p('HO du butadiène',system='butadiene',orbital=2),
        p('Benzène : couche fermée',system='benzene',orbital=3),p('Cycle à 4 π : dégénérescence',system='cyclobutadiene',orbital=2),
        p('Diels–Alder : diène s-trans',system='diels',torsion=180,orbital=2)]),
    lab('cinetique', 'Cinétique ou thermodynamique : deux sélectivités', 'Comprendre la réactivité',
        'Relier Eyring, profils d’énergie libre, produits concurrents et équilibre ; la température agit sur des barrières et niveaux déclarés, jamais sur un score.', [
        s('temperature','Température',250,450,5,298,'K'),s('ha','ΔH‡ vers A',40,110,1,60,'kJ·mol⁻¹'),s('sa','ΔS‡ vers A',-150,80,5,-40,'J·mol⁻¹·K⁻¹'),
        s('hb','ΔH‡ vers B',40,110,1,68,'kJ·mol⁻¹'),s('sb','ΔS‡ vers B',-150,80,5,-30,'J·mol⁻¹·K⁻¹'),
        s('ga','G(A) − G(R), fixé dans ce modèle',-40,0,1,-8,'kJ·mol⁻¹'),s('gb','G(B) − G(R), fixé dans ce modèle',-40,0,1,-16,'kJ·mol⁻¹'),
        s('time','Durée',.01,20,.01,2,'s')], [
        p('A formé plus vite, B plus stable',ha=60,hb=68,sa=-40,sb=-30,ga=-8,gb=-16),
        p('Barrières égales : partage cinétique',ha=65,hb=65,sa=-40,sb=-40),
        p('Produits isoénergétiques : équilibre égal',ga=-12,gb=-12),
        p('Réchauffer une compétition entropique',temperature=420,ha=60,hb=70,sa=-80,sb=-20)])
]
