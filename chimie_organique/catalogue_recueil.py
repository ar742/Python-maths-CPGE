"""Expériences centrées sur les tableaux de réactions du recueil, p. 524–528."""
from commun import slider as s, select as q, preset as p, lab

LABS = [
    lab('effets', 'Effets I/M et règles : justifier avant de nommer', 'Règles et déplacements d’électrons',
        'Expliquer une orientation de réaction à partir de la structure plutôt que réciter une règle. Repérer polarisation, conjugaison et géométrie permet de préciser les conditions d’application de Markovnikov et de Zaïtsev.', [
        q('system','Objet à comparer',[('inductive','Effet inductif dans une chaîne'),('mesomeric','Mésomérie d’un arène substitué'),('markovnikov','Addition HBr / hydroboration du but-1-ène'),('zaitsev','Déshydratation du pentan-2-ol')],'mesomeric'),
        q('group','Groupe pour l’étude I/M',[('alkyl','CH₃'),('methoxy','OCH₃'),('chloro','Cl'),('nitro','NO₂')],'methoxy'),
        q('conditions','Conditions des règles',[('ordinary','Acide / sans peroxydes'),('alternative','BH₃ puis oxydation / base encombrée')],'ordinary'),
        s('stage','Structure ou contributeur',0,2,1,0,integer=True)], [
        p('Méthoxy : −I et +M',system='mesomeric',group='methoxy',stage=1),
        p('Chlore : −I mais +M',system='mesomeric',group='chloro',stage=1),
        p('Nitro : −I et −M',system='mesomeric',group='nitro',stage=1),
        p('CH₃ : +I, pas de doublet +M',system='inductive',group='alkyl'),
        p('HBr : carbocation secondaire',system='markovnikov',conditions='ordinary',stage=1),
        p('Hydroboration : alcool primaire',system='markovnikov',conditions='alternative',stage=2),
        p('Zaïtsev a des conditions',system='zaitsev',conditions='ordinary',stage=2)]),
    lab('e1', 'E1 : départ de Cl ou d’eau, puis choix du H en β', 'Éliminations',
        'Construire une élimination en deux étapes : départ du groupe partant, puis perte d’un proton voisin. Comparer halogénure et alcool activé permet de relier carbocation, vitesse de transformation et répartition des produits.', [
        q('substrate','Substrat et groupe partant',[('source','2-chloro-3-méthylbutane : exercice p. 531/533'),('secondary','Pentan-2-ol : secondaire'),('tertiary','2-méthylbutan-2-ol : tertiaire'),('primary','Pentan-1-ol : E1 classique non retenue')],'source'),
        s('k_ion','Constante apparente d’ionisation choisie',.001,.2,.001,.02,'s⁻¹'),
        s('time','Temps observé',1,500,1,150,'s'),
        s('branch_z','Fraction vers l’alcène le plus substitué, donnée choisie',0,100,1,80,'%'),
        s('stage','Réactif → carbocation → Hβ → alcène',0,3,1,1,integer=True)], [
        p('Pentan-2-ol : deux positions β',substrate='secondary',stage=2),
        p('Exercice : Cl part, deux alcènes possibles',substrate='source',stage=3),
        p('Tertiaire : carbocation admissible',substrate='tertiary',stage=2),
        p('Primaire : ne pas inventer un carbocation',substrate='primary'),
        p('Même mécanisme, branchement différent',branch_z=55,stage=3)]),
    lab('enolatealkyl', 'Énolate ambident : alkylation en C ou en O', 'Construire une liaison C–C',
        'Un énolate possède deux sites susceptibles d’attaquer un électrophile. Suivre les doublets et comparer les liaisons créées permet de distinguer alkylation sur le carbone et sur l’oxygène, selon les conditions fournies.', [
        q('donor','Énolate préparé',[('acetone','Énolate de la propanone'),('malonate','Énolate du malonate de diéthyle')],'malonate'),
        q('electrophile','Halogénure',[('methyl','Bromométhane'),('ethyl','Bromoéthane primaire'),('tertbutyl','Bromure de tert-butyle : SN2 bloquée')],'ethyl'),
        q('site','Voie sélectionnée, sans prédiction de sélectivité',[('C','Alkylation du carbone α'),('O','Alkylation de l’oxygène')],'C'),
        s('equivalents','RX par équivalent d’énolate',0,2,.1,1,'équiv.'),
        s('stage','Contributeur → flèches SN2 → produit',0,2,1,1,integer=True)], [
        p('Malonate : prolonger le squelette',donor='malonate',electrophile='ethyl',site='C',stage=2),
        p('Propanone : butan-2-one',donor='acetone',electrophile='methyl',site='C',stage=2),
        p('Autre connectivité : éther d’énol',donor='acetone',electrophile='ethyl',site='O',stage=2),
        p('Tertiaire : élimination concurrente à discuter',electrophile='tertbutyl'),
        p('RX limitant',equivalents=.4)]),
    lab('aminealkyl', 'Alkylation d’une amine : former un sel quaternaire', 'Substitutions nucléophiles',
        'Ajouter un groupe carboné à une amine tertiaire avec son doublet libre. Compter les liaisons et les charges explique la formation d’un ammonium quaternaire et le rôle du contre-ion.', [
        q('amine','Amine tertiaire',[('trimethyl','Triméthylamine'),('triethyl','Triéthylamine')],'trimethyl'),
        q('electrophile','Halogénure SN2',[('methyl','Bromométhane'),('benzyl','Bromure de benzyle')],'benzyl'),
        s('equivalents','RX par équivalent d’amine',0,3,.1,1,'équiv.'),
        s('stage','Repérage → flèches concertées → sel',0,2,1,2,integer=True)], [
        p('Sel de benzyltriméthylammonium',amine='trimethyl',electrophile='benzyl',stage=2),
        p('Tétraméthylammonium',amine='trimethyl',electrophile='methyl',stage=2),
        p('Excès de RX : l’azote est déjà quaternaire',equivalents=2.5),
        p('Moins d’un équivalent : borne stœchiométrique',equivalents=.5)]),
    lab('anhydride', 'Anhydride : le carboxylate attaque, puis l’acyle se transfère', 'Addition–élimination sur l’acyle',
        'Former un anhydride puis transférer un groupe acyle à un nucléophile. Suivre les deux fragments et les équivalents de base permet de prévoir la fonction obtenue et de vérifier le bilan du piège à acide.', [
        q('variant','Transformation',[('formation','Chlorure d’acyle + carboxylate'),('chloridealcohol','Chlorure d’acyle + éthanol'),('hydrolysis','Hydrolyse de l’anhydride'),('alcoholysis','Alcoolyse de l’anhydride par l’éthanol'),('amidation','Amidation de l’anhydride par l’éthylamine')],'formation'),
        q('acyl','Famille de l’acyle',[('acetyl','Éthanoyle : CH₃CO'),('benzoyl','Benzoyle : PhCO')],'benzoyl'),
        q('acidtrap','Piège à acide, pour l’amidation',[('secondamine','Deuxième équivalent d’éthylamine'),('external','Triéthylamine externe, un équivalent fourni')],'secondamine'),
        s('equivalents','Nucléophile par chlorure / anhydride',0,3,.1,1,'équiv.'),
        s('stage','Réactifs → intermédiaire tétraédrique → produits',0,2,1,1,integer=True)], [
        p('Deux fragments benzoyle',variant='formation',acyl='benzoyl',stage=2),
        p('Chlorure de benzoyle → benzoate d’éthyle',variant='chloridealcohol',acyl='benzoyl',equivalents=1,stage=2),
        p('Deux acides après hydrolyse',variant='hydrolysis',equivalents=1,stage=2),
        p('Un ester et un acide',variant='alcoholysis',equivalents=1,stage=2),
        p('Amide : réserver la seconde amine',variant='amidation',equivalents=2,stage=2),
        p('Amide : base externe',variant='amidation',acidtrap='external',equivalents=1,stage=2)]),
    lab('hydrolyseacyle', 'Hydrolyser un dérivé d’acyle : acide ou base ?', 'Addition–élimination sur l’acyle',
        'Hydrolyser un chlorure d’acyle, un ester ou un amide, en milieu acide ou basique. Les flèches et le bilan acido-basique permettent de déterminer les fonctions et les charges présentes à la fin du traitement.', [
        q('derivative','Dérivé éthanoyle',[('chloride','Chlorure d’éthanoyle'),('ester','Éthanoate d’éthyle'),('amide','Éthanamide')],'ester'),
        q('medium','Milieu',[('acid','Hydrolyse acide'),('base','Hydrolyse basique')],'base'),
        s('equivalents','Eau / HO⁻ fourni, borne de bilan',0,2,.1,1,'équiv.'),
        s('stage','Activation → addition → élimination → état final',0,3,1,3,integer=True)], [
        p('Saponification : acétate et éthanol',derivative='ester',medium='base',stage=3),
        p('Acide : ester, réaction réversible',derivative='ester',medium='acid',stage=3),
        p('Amide : chauffage requis',derivative='amide',medium='base',stage=3),
        p('Amide acide : ammonium',derivative='amide',medium='acid',stage=3),
        p('Chlorure : deux HO⁻ jusqu’au carboxylate',derivative='chloride',medium='base',equivalents=2,stage=3)]),
    lab('photochlore', 'Benzène et Cl₂ : lumière ou catalyseur ?', 'Aromatique : addition ou substitution',
        'Comparer l’action du dichlore sur le benzène sous lumière ou avec un catalyseur de Lewis. Les conditions, les liaisons et le bilan des atomes distinguent substitution aromatique et photoaddition.', [
        q('mode','Conditions',[('addition','Photoaddition : hν'),('sea','Substitution : FeCl₃, sans hν')],'addition'),
        s('chlorine','Cl₂ par équivalent de benzène',0,4,.1,3,'équiv.'),
        q('light','Irradiation dans le cas photoaddition',[('on','Lumière présente'),('off','Sans lumière')],'on'),
        s('stage','Comparer réactif → nature de la transformation → bilan',0,2,1,2,integer=True)], [
        p('3 Cl₂ : cyclohexane hexachloré',mode='addition',chlorine=3,light='on',stage=2),
        p('1 Cl₂ ne suffit pas au bilan complet',mode='addition',chlorine=1,stage=2),
        p('Sans lumière : photoaddition arrêtée',mode='addition',light='off'),
        p('FeCl₃ : chlorobenzène + HCl',mode='sea',chlorine=1,stage=2)]),
    lab('grignardprep', 'Préparer RMgX : le proton détruit avant l’addition', 'Organomagnésiens',
        'Préparer un organomagnésien puis mesurer ce qu’il reste en présence de traces d’eau. Le bilan des quantités explique pourquoi l’anhydrie est nécessaire et distingue destruction du réactif et hydrolyse finale de l’alcoolate.', [
        q('group','Halogénure organique',[('ethyl','Éthyle : CH₃CH₂X'),('phenyl','Phényle : C₆H₅X')],'phenyl'),
        q('halide','Halogène',[('Br','Brome'),('Cl','Chlore')],'Br'),
        s('magnesium','Mg par équivalent de RX',0,2,.05,1,'équiv.'),
        s('water','Eau parasite par équivalent de RX',0,2,.05,0,'équiv.'),
        s('progress','Fraction de l’insertion idéale accomplie',0,1,.05,1),
        s('stage','Insertion → eau parasite → matière disponible',0,2,1,0,integer=True)], [
        p('Milieu anhydre : PhMgBr disponible',group='phenyl',halide='Br',water=0,stage=2),
        p('Une demi-équivalence d’eau perdue',water=.5,stage=1),
        p('Toute la préparation détruite',water=1,stage=2),
        p('Mg limitant',magnesium=.4,water=0,stage=2),
        p('Insertion partielle, pas une durée fictive',progress=.4,water=.1,stage=2)])
]
