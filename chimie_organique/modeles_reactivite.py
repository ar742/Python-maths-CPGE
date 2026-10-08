"""Réactivité CPGE : mécanismes documentés et modèles quantitatifs déclarés.

Les graphes utilisent des groupes semi-développés. Leurs nombres de sommets
ne sont pas des nombres d'atomes : les bilans sont établis séparément.
Les constantes, barrières et pondérations réglables sont des données de modèle,
pas des prédictions universelles de rendement ou de composition expérimentale.
"""
from __future__ import annotations
import math
import numpy as np
from commun import (R, atom, bond, electron_arrow as arrow, molecule, chain,
                    benzene, metric as m, chart as ch, series as se, scene,
                    reaction_scene as rs, mechanism_scene as ms, energy_profile)

KB = 1.380649e-23
H = 6.62607015e-34

def result(metrics, charts, drawing, steps, assumptions, **extra):
    return dict(metrics=metrics, charts=charts, scene=drawing, steps=steps,
                assumptions=assumptions, **extra)

def eyring(dh, ds, temperature):
    """k pour une étape unimoléculaire, κ=1 ; dh kJ/mol, ds J/mol/K."""
    return KB*temperature/H * math.exp(ds/R-dh*1000/(R*temperature))

def fractions_from_barriers(barriers, temperature, multiplicities=None):
    energies=np.asarray(barriers,dtype=float)
    weights=np.ones(len(energies)) if multiplicities is None else np.asarray(multiplicities,dtype=float)
    weights=weights*np.exp(-(energies-energies.min())*1000/(R*temperature))
    return weights/weights.sum()

def acid_extent(delta_pka, ratio):
    """x/HA₀ ; équation stable en logarithmes et stœchiométrie exacte."""
    lo,hi=0.,min(1.,float(ratio))
    for _ in range(100):
        x=(lo+hi)/2
        # Les quotients aux limites peuvent être indistinguables en flottants.
        if 1-x<=0 or ratio-x<=0: hi=x; continue
        logq=2*math.log10(max(x,1e-300))-math.log10(1-x)-math.log10(ratio-x)
        if logq<delta_pka: lo=x
        else: hi=x
    return (lo+hi)/2

def second_order(a0,b0,k,t):
    """A+B→P, concentrations égales ou inégales, sans excès imposé."""
    t=np.asarray(t,dtype=float)
    if k==0: return np.full_like(t,a0),np.full_like(t,b0),np.zeros_like(t)
    if abs(a0-b0)<=1e-12*max(a0,b0):
        a=a0/(1+k*a0*t);x=a0-a
    else:
        delta=b0-a0
        if delta>0:
            z=np.exp(-k*delta*t)
            a=a0*delta*z/(b0-a0*z);x=a0-a
        else:
            z=np.exp(k*delta*t)
            b=b0*(-delta)*z/(a0-b0*z);x=b0-b
    return a0-x,b0-x,x

def consecutive(k1,k2,t):
    """A→I→P avec concentrations normalisées initiales (1,0,0)."""
    t=np.asarray(t,dtype=float);a=np.exp(-k1*t)
    if abs(k1-k2)<1e-10*max(k1,k2,1): i=k1*t*a
    else: i=k1*(np.exp(-k1*t)-np.exp(-k2*t))/(k2-k1)
    product=np.maximum(0,1-a-i)
    return a,i,product

def geom_sn2(stage, substrate='secondary'):
    """Graphes avec inversion dessinée ; aucun calcul d'étiquette CIP."""
    left=-2 if stage<2 else 0
    atoms=[atom('c','C',0,0,label='Cα'),atom('a','C',-.6,1,label='CH₃'),
           atom('b','C',-.6,-1,label='CH₂CH₃'),atom('h','H',-1.1,.35,label='H'),
           atom('nu','O',left-1.1,0,label='HO',charge=-1 if stage==0 else 0),
           atom('br','Br',1.5 if stage<2 else 2.5,0,charge=-1 if stage==2 else 0)]
    if substrate=='methyl':
        for a in atoms:
            if a['id'] in ('a','b'): a.update(element='H',label='H')
    elif substrate=='primary':
        atoms[2].update(element='H',label='H')
    elif substrate=='tertiary': atoms[3].update(element='C',label='CH₃')
    if stage==2:
        atoms[1]['x']=.6;atoms[2]['x']=.6;atoms[3]['x']=1.1
        atoms[4]['x']=-1.3
    if stage==1:
        atoms[1]['x']=0;atoms[2]['x']=0;atoms[3].update(x=.6,y=.5)
    bonds=[bond('c','a',style='wedge' if stage!=1 else 'line'),
           bond('c','b',style='dash' if stage!=1 else 'line'),bond('c','h')]
    if stage==0: bonds.append(bond('c','br'))
    elif stage==1:
        atoms[4].update(x=-1.3,charge=0,label='HOδ⁻');atoms[5]['label']='Brδ⁻'
        bonds.extend([bond('c','nu',style='dashed'),bond('c','br',style='dashed')])
    else: bonds.append(bond('c','nu'))
    arrows=[]
    if stage==0: arrows=[arrow((-2.8,.1),(0,.05),(-1.4,.8),label='doublet de O'),arrow((.75,0),(1.5,.2),(1.3,.8),label='liaison C–Br')]
    return molecule(['Réactifs : attaque arrière','État de transition : liaisons partielles','Produit : inversion géométrique'][stage],atoms,bonds,arrows,
                    caption='Groupes semi-développés ; perspective qualitative. Inversion ≠ changement R/S garanti.')

def carbonyl(name='Propanone',left='CH₃',right='CH₃',oxygen='O',charge=0,order=2):
    def element(label):
        return 'H' if label=='H' else 'O' if label.startswith('O') else 'Cl' if label=='Cl' else 'N' if label.startswith('N') else 'C'
    return molecule(name,[atom('c','C',0,0),atom('o','O',0,1.1,label=oxygen,charge=charge),
                           atom('l',element(left),-1,0,label=left),atom('r',element(right),1,0,label=right)],
                    [bond('c','o',order),bond('l','c'),bond('c','r')])

def tetrahedral(name,left,right,nucleophile,protonated=False):
    def element(label):
        return 'H' if label=='H' else 'O' if label.startswith('O') else 'Cl' if label=='Cl' else 'N' if label.startswith('N') else 'C'
    return molecule(name,[atom('c','C',0,0),atom('o','O',0,1.1,label='OH' if protonated else 'O',charge=0 if protonated else -1),
                           atom('l',element(left),-1,0,label=left),atom('r',element(right),1,0,label=right),atom('nu',element(nucleophile),0,-1,label=nucleophile)],
                    [bond('c','o'),bond('l','c'),bond('c','r'),bond('c','nu')])

def electrons(p):
    reaction=p['reaction'];stage=min(int(p['stage']),1)
    if reaction=='acid':
        g0=molecule('HO⁻ + CH₃COOH',[atom('b','O',-1.8,0,label='HO',charge=-1),atom('h','H',-.4,0),
            atom('o','O',.5,0),atom('r','C',1.5,0,label='CH₃CO')],[bond('h','o'),bond('o','r')],
            [arrow((-1.6,.1),(-.4,0),(-1,.7),label='doublet → H'),arrow((.05,0),(.5,.15),(.3,.6),label='liaison O–H → O')])
        g1=molecule('H₂O + CH₃COO⁻',[atom('b','O',-1.5,0,label='OH'),atom('h','H',-.5,0),
            atom('o','O',.6,0,charge=-1),atom('r','C',1.6,0,label='CH₃CO')],[bond('b','h'),bond('o','r')])
        zsum=41;charge=-1;moving=4;text='Deux flèches de doublet : O de HO⁻ donne vers H ; la liaison O–H cède vers O.'
    elif reaction=='sn2':
        g0=geom_sn2(0,'methyl');g1=geom_sn2(2,'methyl');zsum=53;charge=-1;moving=4
        text='Deux doublets se déplacent simultanément : O → C et liaison C–Br → Br.'
    elif reaction=='homolysis':
        g0=molecule('Br₂ : rupture homolytique',[atom('a','Br',-.8,0),atom('b','Br',.8,0)],[bond('a','b')],
            [arrow((-.05,.06),(-.8,.15),(-.5,.7),electrons=1),arrow((.05,-.06),(.8,-.15),(.5,-.7),electrons=1)])
        g1=molecule('Deux radicaux Br•',[atom('a','Br',-1,0,label='Br•'),atom('b','Br',1,0,label='Br•')],[])
        zsum=70;charge=0;moving=2;text='Les flèches à demi-pointe transportent un électron chacune. Chaque Br conserve un électron de la liaison.'
    else:
        def carbox(first):
            o1=1 if first else 2;o2=2 if first else 1
            return molecule('CH₃COO⁻ : contributeur '+('A' if first else 'B'),
                [atom('c','C',0,0),atom('l','C',-1,0,label='CH₃'),atom('o1','O',.8,.8,charge=-1 if first else 0),
                 atom('o2','O',.8,-.8,charge=0 if first else -1)],
                [bond('l','c'),bond('c','o1',o1),bond('c','o2',o2)],
                [arrow((.8,.9),(0,.1),(.1,1),label='doublet O → liaison π'),arrow((.4,-.4),(.9,-.8),(1,-.2),label='π → O')] if first else [])
        g0,g1=carbox(True),carbox(False);zsum=31;charge=-1;moving=4
        text='La mésomérie change la représentation électronique, pas la connectivité des noyaux : ce n’est pas une réaction entre deux espèces.'
    x,y=energy_profile([0,0 if reaction=='resonance' else -15],[p['barrier']])
    if reaction=='homolysis':
        x=np.linspace(0,5,201);y=194*(1-np.exp(-x))**2
    profile_note='Coordonnée fictive de représentation, sans barrière de résonance réelle.' if reaction=='resonance' else 'Barrière et énergie finale pédagogiques, non données mesurées.'
    if reaction=='homolysis': profile_note='Dissociation de Br₂ : énergie de liaison gazeuse D≈194 kJ/mol ; potentiel de Morse illustratif, coordonnée a(r−rₑ). Le réglage de barrière n’est pas appliqué.'
    return result([m('Charge totale initiale',charge,'e'),m('Charge totale finale',charge,'e'),m('Électrons totaux conservés',zsum-charge),
                   m('Électrons sur les flèches',moving),m('Étape réelle',stage),m('Nature','mésomérie' if reaction=='resonance' else 'transformation')],
        [ch('Inventaire des électrons : avant et après','Étape','Nombre d’électrons',se('Électrons totaux',[0,1],[zsum-charge]*2))] +
        ([] if reaction=='resonance' else [ch('Dissocier une liaison coûte de l’énergie' if reaction=='homolysis' else 'Profil énergétique déclaré',
            'a(r−rₑ), adimensionnel' if reaction=='homolysis' else 'Coordonnée réactionnelle','U / kJ·mol⁻¹' if reaction=='homolysis' else 'G / kJ·mol⁻¹',se('Potentiel de Morse illustratif' if reaction=='homolysis' else 'Profil modèle',x,y))]),
        ms('Déplacer des électrons sans en créer',text,[g0,g1],stage),
        [text,'Contrôler toutes les charges formelles avant et après. Les groupes CH₃ et CH₃CO contiennent des atomes implicites.',profile_note],
        ['Groupes semi-développés ; bilans d’atomes établis indépendamment du nombre de sommets.',profile_note],electron_inventory=zsum-charge,charge_balance=0)

def acidebase(p):
    d=p['pka_base']-p['pka_acid'];b=p['base_ratio'];c=p['concentration'];x=acid_extent(d,b)
    ds=np.linspace(-20,20,241);xs=np.array([acid_extent(v,b) for v in ds])
    concentrations=[c*(1-x),c*(b-x),c*x,c*x]
    return result([m('ΔpKₐ = pKₐ(BH⁺) − pKₐ(HA)',d),m('log₁₀ K',d),m('Conversion de HA',100*x,'%'),m('Limite stœchiométrique',100*min(1,b),'%'),
                   m('HA restant',concentrations[0],'mol·L⁻¹'),m('Base restante',concentrations[1],'mol·L⁻¹')],
        [ch('Avancement d’équilibre : constantes et stœchiométrie','ΔpKₐ','Fraction HA transformée',se('Équilibre',ds,xs),se('Limite',[ds[0],ds[-1]],[min(1,b)]*2))],
        scene('bars','HA + B ⇌ A⁻ + BH⁺','Activités assimilées aux concentrations dans le même solvant ; contre-ions non représentés.',
              labels=['HA','B','A⁻','BH⁺'],values=concentrations,unit='mol·L⁻¹'),
        ['K = 10^[pKₐ(BH⁺) − pKₐ(HA)].','Avec x = ξ/n₀(HA), K = x² / [(1−x)(b−x)].',
         'Même un K très élevé ne consomme pas davantage de HA que la base disponible. Un alcyne terminal exige une base suffisamment forte.'],
        ['Tous les pKₐ doivent être comparés dans un même solvant et aux mêmes conventions.',
         'Solution idéale ; HA et B initialement seuls, ni précipitation, ni dégagement gazeux, ni équilibre secondaire.'],extent=x,concentrations=concentrations,stoichiometric_limit=min(1,b))

def sn2(p):
    allowed=p['substrate'] not in ('tertiary','vinyl');k=p['k'] if allowed else 0
    t=np.linspace(0,p['time'],241);a,b,x=second_order(p['a0'],p['b0'],k,t)
    stage=int(p['stage']) if allowed else 0
    nu=np.linspace(0,2,161);v=k*p['a0']*nu
    explanation='SN2 classique envisageable ; le k choisi n’est pas prédit par la structure.' if allowed else 'SN2 classique exclue dans ce modèle : encombrement tertiaire ou carbone vinylique sp².'
    return result([m('Voie SN2', 'admissible' if allowed else 'bloquée'),m('Vitesse initiale',k*p['a0']*p['b0'],'mol·L⁻¹·s⁻¹'),
        m('RX transformé',x[-1],'mol·L⁻¹'),m('RX final',a[-1],'mol·L⁻¹'),m('Nu⁻ final',b[-1],'mol·L⁻¹'),m('Ordres partiels','1 en RX ; 1 en Nu⁻'),m('Étiquette R/S','à recalculer par CIP')],
        [ch('Intégration bimoléculaire sans réservoir','t / s','c / mol·L⁻¹',se('RX',t,a),se('Nu⁻',t,b),se('Produit',t,x)),
         ch('Vitesse initiale et nucléophile','[Nu⁻]₀ / mol·L⁻¹','v₀ / mol·L⁻¹·s⁻¹',se('v₀ = k₂[RX]₀[Nu⁻]₀',nu,v))],
        ms('Attaque arrière et inversion',explanation,[geom_sn2(i,p['substrate']) for i in range(3)] if allowed else [geom_sn2(0,p['substrate'])],stage),
        [explanation,'v = k₂[RX][Nu⁻]. Les deux réactifs diminuent d’une même quantité ξ/V ; le produit augmente de cette quantité.',
         'Le schéma inverse la géométrie des trois groupes conservés. R/S dépend des priorités du nucléophile et du groupe partant.'],
        ['Une seule SN2, milieu homogène ; constantes fixées, aucune voie concurrente dans cette expérience.',
         'Carbone secondaire : mécanisme possible sans garantir qu’il domine E2 ; k₂ est une donnée choisie.'],
        allowed=allowed,time=t,a=a,b=b,product=x,initial_rate=k*p['a0']*p['b0'],inversion=allowed)

def sn1_graph(stage, substrate):
    if substrate=='rearrange':
        # 2-bromo-3-méthylbutane : migration 1,2 d'hydrure vers C2+.
        moved=stage>=2
        atoms=[atom('m','C',-1.7,0,label='CH₃'),atom('c2','C',-.7,0,label='CH',charge=1 if stage==1 else 0),
               atom('c3','C',.7,0,label='C(CH₃)₂',charge=1 if stage==2 else 0),
               atom('h','H',-.7 if moved else .7,.9),atom('br','Br',-1.2,-1,charge=0 if stage==0 else -1)]
        bonds=[bond('m','c2'),bond('c2','c3'),bond('h','c2' if moved else 'c3')]
        if stage==0: bonds.append(bond('c2','br'))
        arrows=[]
        if stage==0: arrows=[arrow((-.95,-.5),(-1.2,-1),(-1.7,-.6),label='C–Br → Br')]
        elif stage==1: arrows=[arrow((.7,.45),(-.7,.1),(0,1.2),label='C3–H → C2⁺ : migration 1,2')]
        elif stage==2:
            atoms.append(atom('o','O',2.2,0,label='H₂O'));arrows=[arrow((2,.1),(.7,.1),(1.3,.8),label='eau → C3⁺')]
        elif stage>=3:
            atoms.append(atom('o','O',1.5,-.8,label='OH₂' if stage==3 else 'OH',charge=1 if stage==3 else 0));bonds.append(bond('c3','o'))
            if stage==4: atoms.append(atom('hp','H',2.7,-.8,charge=1))
        names=['Substrat : 2-bromo-3-méthylbutane','Carbocation C2⁺ secondaire : l’hydrure migre',
               'Carbocation C3⁺ tertiaire réarrangé','Capture : oxonium réarrangé','Alcool réarrangé après déprotonation']
        return molecule(names[stage],atoms,bonds,arrows)
    center='PhCH₂' if substrate=='benzyl' else 'R₂CH' if substrate=='secondary' else 'RCH₂' if substrate=='primary' else 'R₃C'
    if stage==0:
        return molecule('Ionisation : C–Br → Br', [atom('c','C',0,0,label=center),atom('br','Br',1.1,0)], [bond('c','br')],
                        [arrow((.55,0),(1.1,.15),(.9,.8),label='doublet de liaison')])
    if stage==1:
        return molecule('Carbocation plan + Br⁻', [atom('c','C',0,0,label=center,charge=1),atom('br','Br',1.8,0,charge=-1),
                atom('nu','O',-1.7,0,label='H₂O')], [],[arrow((-1.5,.1),(0,0),(-.8,.8),label='doublet → C⁺')],
                caption='Si une migration 1,2 est possible : la liaison migrante apporte son doublet au centre déficitaire.')
    if stage==2:
        return molecule('Capture : oxonium', [atom('c','C',0,0,label=center),atom('o','O',1,0,label='OH₂',charge=1),
                        atom('br','Br',2.3,0,charge=-1)], [bond('c','o')],caption='L’oxygène à trois liaisons porte +1 ; l’hydrolyse libère ensuite un proton.')
    return molecule('Alcool + H⁺ + Br⁻', [atom('c','C',0,0,label=center),atom('o','O',1,0,label='OH'),
                     atom('h','H',2,0,charge=1),atom('br','Br',3,0,charge=-1)], [bond('c','o')])

def sn1(p):
    allowed=p['substrate'] not in ('primary','vinyl');k1=p['k1'] if allowed else 0;k2=p['k2']
    t=np.linspace(0,p['time'],301);a,i,product=consecutive(k1,k2,t)
    back=.5+p['bias']/100 if allowed else 0;front=1-back if allowed else 0
    stage=min(int(p['stage']),4 if p['substrate']=='rearrange' else 3) if allowed else 0
    x,y=energy_profile([0,20,-15],[65,42])
    rearrange=p['substrate']=='rearrange'
    return result([m('Ionisation', 'possible' if allowed else 'non retenue'),m('RX restant',100*a[-1],'%'),m('Carbocation apparent',100*i[-1],'%'),
        m('Produit capturé',100*product[-1],'%'),m('Face arrière parmi le produit',100*back,'%'),m('Réarrangement','possible : migration 1,2' if rearrange else 'non représenté'),m('Étape réelle',stage)],
        [ch('Ionisation puis capture : deux temps distincts','t / s','Fraction molaire',se('RX',t,a),se('R⁺',t,i),se('Produit',t,product)),
         ch('Deux barrières et un minimum intermédiaire','Coordonnée réactionnelle','G modèle / kJ·mol⁻¹',se('Profil déclaré',x,y))],
        ms('Un carbocation n’est pas un état de transition','La planéité permet les deux faces ; une paire d’ions peut rendre leur capture inégale.',
           [sn1_graph(j,p['substrate']) for j in range(5 if rearrange else 4)] if allowed else [sn1_graph(0,p['substrate'])],stage),
        ['Ionisation : v = k₁[RX]. Capture par l’eau en grand excès : constante apparente k₂.',
         'Le produit comprend ici l’alcool après déprotonation rapide. Les concentrations normalisées vérifient RX + R⁺ + produit = 1.',
         '50/50 est le cas idéal sans mémoire de face ; le curseur d’excès impose un biais expérimental hypothétique, sans le prédire.',
         'Un carbocation secondaire adjacent à un centre plus substitué peut subir une migration 1,2 ; les proportions des isomères ne sont pas prédites.'],
        ['Solvolyse à constantes imposées ; eau en excès, déprotonation rapide, pas d’élimination dans cette intégration. Migration éventuelle supposée rapide devant la capture.',
         'Énergies du profil pédagogiques. Primaire non stabilisé et vinylique : ionisation SN1 classique écartée.'],
        allowed=allowed,time=t,a=a,intermediate=i,product=product,back_fraction=back,front_fraction=front,rearrangement=rearrange)

def competition(p):
    substrate=p['substrate'];sn2ok=substrate not in ('tertiary','vinyl');ionok=substrate in ('secondary','tertiary');e2ok=substrate not in ('methyl','vinyl')
    ion=p['k_ion'] if ionok else 0;capture=p['capture']/100
    rates=np.array([p['k_sn2']*p['nu'] if sn2ok else 0,ion*capture,ion*(1-capture),p['k_e2']*p['base'] if e2ok else 0])
    total=float(rates.sum());t=np.linspace(0,p['time'],201);remaining=np.exp(-total*t)
    shares=rates/total if total>0 else np.zeros(4);products=shares[:,None]*(1-remaining)
    nu=np.linspace(0,2,101);v_sn2=p['k_sn2']*nu if sn2ok else nu*0
    curves=[se('RX',t,remaining)]+[se(label,t,v) for label,v in zip(['SN2','SN1','E1','E2'],products)]
    return result([m('Constante apparente totale',total,'s⁻¹'),m('Conversion',100*(1-remaining[-1]),'%')]+[m('Part '+label,100*v,'%') for label,v in zip(['SN2','SN1','E1','E2'],shares)],
        [ch('Quatre voies avec réservoirs imposés','t / s','Fraction molaire',*curves),
         ch('SN2 et concentration du nucléophile','[Nu] / mol·L⁻¹','k apparent / s⁻¹',se('SN2',nu,v_sn2))],
        scene('bars','Composition calculée, pas classement arbitraire','SN1 et E1 partagent l’ionisation commune ; capture/(capture+élimination) est imposé.',
              labels=['RX','SN2','SN1','E1','E2'],values=np.r_[remaining[-1],products[:,-1]],unit='fraction'),
        ['kapp(SN2)=k₂[Nu] ; kapp(E2)=k₂[base].','L’ionisation commune est répartie entre SN1 et E1 par une fraction de capture choisie : elle n’est pas comptée deux fois.',
         'Sous réservoirs, RX(t)=RX₀ exp(−Σkapp t). Chaque produit vaut sa part de vitesse multipliée par la conversion.'],
        ['Nucléophile et base maintenus en excès ; constantes et fraction de capture choisies, non prédites par le substrat.',
         'Méthyle sans Hβ : E2 exclue ; tertiaire : SN2 exclue ; halogénure vinylique : ces mécanismes classiques ne sont pas retenus.'],rates=rates,shares=shares,time=t,remaining=remaining,products=products)

def elimination(p):
    phi=p['dihedral'];anti=abs(((phi-180+180)%360)-180)<1e-9
    T=p['temperature'];pop=1/(1+math.exp(p['chair_gap']*1000/(R*T)))
    cyc=p['system']=='cyclohexane';reactive=pop if cyc else (1. if anti else 0.)
    fractions=fractions_from_barriers([p['barrier_z'],p['barrier_h']],T)
    if cyc: fractions=np.array([0.,1.])
    angles=np.linspace(0,360,241);# conformational energy is illustrative, not a rate prefactor
    conform=3*(1+np.cos(np.radians(3*angles)))
    ts=np.linspace(250,420,151);populations=1/(1+np.exp(p['chair_gap']*1000/(R*ts)))
    g=molecule('Élimination concertée : trois doublets',
        [atom('b','O',-2.2,.9,label='B',charge=-1),atom('h','H',-1.3,.8),atom('cb','C',-.6,0,label='Cβ'),
         atom('ca','C',.6,0,label='Cα'),atom('br','Br',1.3,-.8),atom('r1','C',-1.5,-.7,label='CH₃'),atom('r2','C',1.5,.7,label='CH₃')],
        [bond('h','cb'),bond('cb','ca'),bond('ca','br'),bond('cb','r1'),bond('ca','r2')],
        [arrow((-2,.8),(-1.3,.8),(-1.6,1.6),label='base → Hβ'),arrow((-.95,.4),(0,.1),(-.4,.8),label='C–H → C=C'),
         arrow((.95,-.4),(1.4,-.8),(1.5,0),label='C–Br → Br')])
    label='Chaise diaxiale : Br et CH₃ axiaux. Au Cβ substitué, CH₃ occupe l’axe : seul l’autre Hβ anti est disponible.' if cyc else ('Conformation anti exacte disponible.' if anti else 'Conformation instantanée non anti : E2 anti non représentée à ce dièdre.')
    return result([m('Accessibilité instantanée', 'trans-diaxiale' if cyc else ('anti' if anti else 'non anti')),m('Fraction de conformère réactif',100*reactive,'%'),
        m('Chaise diaxiale, population',100*pop,'%'),m('Produit plus substitué, parmi produits',100*fractions[0] if reactive>0 else 0,'%'),
        m('Produit moins substitué, parmi produits',100*fractions[1] if reactive>0 else 0,'%'),m('Critère','géométrie avant stabilité')],
        [ch('Énergie conformationnelle illustrative','Dièdre / °','Énergie modèle / kJ·mol⁻¹',se('Trois alternances',angles,conform)),
         ch('Population de la chaise diaxiale','T / K','Fraction',se('Boltzmann',ts,populations))],
        rs('E2 anti et contrainte de conformation',label,[g,chain('Produit : alcène',['CH₃','CH','CH','CH₃'],[1,2,1])]),
        [label,'Anti-périplanaire signifie dièdre Hβ–Cβ–Cα–Br de 180°, pas seulement « H et Br sur deux carbones voisins ».','Chaise réactive : p = 1/(1+exp(ΔG/RT)).',
         'La comparaison des barrières Zaïtsev/Hofmann est un modèle choisi pour les voies accessibles ; une voie géométriquement absente reçoit zéro.'],
        ['Chaîne : conformation figée ; on ne prétend pas qu’une molécule en solution ne puisse pas tourner pour devenir anti.',
         'Cyclohexane : trans-1-bromo-2-méthyl ; interconversion des chaises à l’équilibre. Pas de prédiction numérique de vitesse E2 réelle.'],
        anti=anti,reactive_fraction=reactive,chair_population=pop,product_shares=fractions if reactive>0 else np.zeros(2))

def alkene_graph(substrate):
    if substrate=='propene': return chain('Propène',['CH₂','CH','CH₃'],[2,1])
    if substrate=='rearrange': return chain('3-méthylbut-1-ène',['CH₂','CH','CH(CH₃)','CH₃'],[2,1,1])
    # Two original geometries with substituents on actual sides of C=C.
    e=substrate=='butene_E'
    return molecule('(E)-but-2-ène' if e else '(Z)-but-2-ène',
        [atom('c1','C',-.5,0,label='CH'),atom('c2','C',.5,0,label='CH'),atom('r1','C',-1.2,.8,label='CH₃'),
         atom('r2','C',1.2,-.8 if e else .8,label='CH₃')],[bond('c1','c2',2),bond('c1','r1'),bond('c2','r2')])

def alcene(p):
    sub,rx=p['substrate'],p['reagent'];internal=sub.startswith('butene');rearrange=sub=='rearrange' and rx in ('hbr','water')
    name='';selectivity='';stereo='';note='';change=-1
    if rx=='borane':
        name='Butan-2-ol' if internal else ('3-méthylbutan-1-ol' if sub=='rearrange' else 'Propan-1-ol')
        selectivity='OH sur le carbone le moins substitué (alcène terminal)';stereo='H et OH ajoutés syn'
        product=chain(name,['CH₃','CH(OH)','CH₂','CH₃'] if internal else ['HOCH₂','CH₂','CH₃'] if sub=='propene' else ['HOCH₂','CH₂','CH(CH₃)','CH₃'])
        note='Hydroboration concertée, puis oxydation avec rétention au carbone portant B ; pas de carbocation libre.'
    elif rx in ('hbr','water'):
        group='Br' if rx=='hbr' else 'OH'
        name=('2-bromo-2-méthylbutane' if rx=='hbr' else '2-méthylbutan-2-ol') if rearrange else ('2-bromobutane' if internal and rx=='hbr' else 'Butan-2-ol' if internal else '2-bromopropane' if rx=='hbr' else 'Propan-2-ol')
        product=chain(name,['CH₃',f'C({group})(CH₃)','CH₂','CH₃'] if rearrange else ['CH₃',f'CH({group})','CH₂','CH₃'] if internal else ['CH₃',f'CH({group})','CH₃'])
        selectivity='Carbocation le plus stabilisé ; règle de Markovnikov pour le cas simple';stereo='Pas stéréospécifique ; deux faces accessibles'
        note='Migration 1,2 de H possible : le carbocation secondaire devient tertiaire avant capture.' if rearrange else 'Carbocation intermédiaire ; l’eau conduit à un oxonium puis à un alcool.'
    elif rx=='bromine':
        name='meso-(2R,3S)-2,3-dibromobutane' if sub=='butene_E' else 'Racémique (2R,3R)/(2S,3S)-2,3-dibromobutane' if sub=='butene_Z' else '1,2-dibromopropane' if sub=='propene' else '1,2-dibromo-3-méthylbutane'
        product=chain(name,['CH₃','CHBr','CHBr','CH₃'] if internal else ['CH₂Br','CHBr','CH₃'] if sub=='propene' else ['CH₂Br','CHBr','CH(CH₃)','CH₃'])
        selectivity='Deux carbones de la double liaison';stereo='Addition anti via bromonium';note='Le pont bromonium interdit la face de Br⁻ du même côté.'
    elif rx=='hydrogen':
        name='Butane' if internal else 'Propane' if sub=='propene' else '2-méthylbutane';product=chain(name,['CH₃','CH₂','CH₂','CH₃'] if internal else ['CH₃','CH₂','CH₃'] if sub=='propene' else ['CH₃','CH₂','CH(CH₃)','CH₃'])
        selectivity='C=C réduite';stereo='Addition syn sur une surface métallique';note='La catalyse intervient sans être consommée au bilan.'
    elif rx=='epoxide':
        name='Époxyde correspondant';product=molecule(name,[atom('c1','C',-.6,0,label='CHR'),atom('c2','C',.6,0,label='CHR′'),atom('o','O',0,.9)], [bond('c1','c2'),bond('c1','o'),bond('c2','o')])
        selectivity='Transfert concerté d’un O';stereo='Conservation de la relation E/Z dans l’époxyde';note='Peracide → acide carboxylique ; les deux liaisons C–O se forment sur la même face.'
    elif rx=='diol':
        name='meso-butane-2,3-diol' if sub=='butene_Z' else 'Butane-2,3-diol racémique' if internal else 'Propane-1,2-diol' if sub=='propene' else '3-méthylbutane-1,2-diol'
        product=chain(name,['CH₃','CHOH','CHOH','CH₃'] if internal else ['HOCH₂','CHOH','CH₃'] if sub=='propene' else ['HOCH₂','CHOH','CH(CH₃)','CH₃'])
        selectivity='Diol vicinal';stereo='Addition syn';note='Conditions douces déclarées ; une oxydation forte peut couper C–C.'
    else:
        name='Deux éthanals' if internal else 'Méthanal + éthanal' if sub=='propene' else 'Méthanal + 2-méthylpropanal'
        product=carbonyl(name,left='H',right='CH₃' if sub!='rearrange' else 'CH(CH₃)₂');selectivity='Coupure de C=C';stereo='Stéréochimie E/Z effacée';change=0
        note='Traitement réducteur : les fragments aldéhydes ne sont pas oxydés en acides. Le second fragment est HCHO ou un second éthanal.'
    initial=alkene_graph(sub);intermediate=initial
    atoms_by_id={a['id']:a for a in initial['atoms']};pi_bond=next(b for b in initial['bonds'] if b['order']==2)
    ca,cb=atoms_by_id[pi_bond['a']],atoms_by_id[pi_bond['b']]
    pi_mid=((ca['x']+cb['x'])/2,(ca['y']+cb['y'])/2)
    if rx in ('hbr','water'):
        if rx=='hbr':
            initial['atoms'].extend([atom('h','H',.4,1.7),atom('hx','Br',1.7,1.7)])
            initial['bonds'].append(bond('h','hx'))
            initial['arrows']=[arrow(pi_mid,(.4,1.7),(-.2,1),label='π → H'),arrow((1.05,1.7),(1.7,1.8),(1.4,2.3),label='H–Br → Br')]
        else:
            initial['atoms'].append(atom('h','H',.4,1.7,charge=1))
            initial['arrows']=[arrow(pi_mid,(.4,1.7),(-.2,1),label='π → H⁺')]
    elif rx=='bromine':
        initial['atoms'].extend([atom('br1','Br',.2,1.6),atom('br2','Br',1.6,1.6)])
        initial['bonds'].append(bond('br1','br2'))
        initial['arrows']=[arrow(pi_mid,(.2,1.6),(-.3,.8),label='π → Br'),arrow((.9,1.6),(1.6,1.7),(1.2,2.2),label='Br–Br → Br'),
                           arrow((.2,1.7),(cb['x'],cb['y']),(1.1,1.2),label='doublet Br → autre C')]
    elif rx=='borane':
        initial['atoms'].extend([atom('bo','B',0,1.6,label='BH₂'),atom('h','H',1,1.6)])
        initial['bonds'].append(bond('bo','h'))
        initial['arrows']=[arrow(pi_mid,(0,1.6),(-.3,.8),label='π → B'),arrow((.5,1.6),(cb['x'],cb['y']),(1.5,1),label='B–H → C substitué')]
    if rx=='bromine':
        c1label='CH(CH₃)' if internal else 'CH₂';c2label='CH(CH₃)' if internal or sub=='propene' else 'CH[CH(CH₃)₂]'
        intermediate=molecule('Bromonium + Br⁻',[atom('c1','C',-.6,0,label=c1label),atom('c2','C',.6,0,label=c2label),atom('br','Br',0,.9,charge=1),atom('b','Br',1.8,0,charge=-1)],
                              [bond('c1','c2'),bond('c1','br'),bond('c2','br')],[arrow((1.7,.1),(.6,0),(1.1,-.6)),arrow((.3,.45),(0,1),(1,.8))])
    elif rx in ('hbr','water'):
        intermediate=molecule('Carbocation '+('réarrangé tertiaire' if rearrange else 'de Markovnikov'),[atom('c','C',0,0,label='R₂C' if rearrange else 'RCH',charge=1),atom('nu','Br' if rx=='hbr' else 'O',-1.7,0,label='Br' if rx=='hbr' else 'H₂O',charge=-1 if rx=='hbr' else 0)],[],[arrow((-1.5,.1),(0,0),(-.8,.8))])
    elif rx=='borane':
        intermediate=molecule('Organoborane avant oxydation (monoaddition représentée)',
            [atom('b','B',-1,0,label='BH₂'),atom('c1','C',0,0,label='CH₂' if not internal else 'CH(CH₃)'),atom('c2','C',1,0,label='CH₂'),atom('r','C',2,0,label='CH₃' if sub=='propene' or internal else 'CH(CH₃)₂')],
            [bond('b','c1'),bond('c1','c2'),bond('c2','r')])
        if internal: intermediate['atoms'][2]['label']='CH₂';intermediate['atoms'][3]['label']='CH₃'
    frames=[initial,intermediate,product];stage=int(p['stage'])
    x,y=energy_profile([0,20,-30],[60,45]) if rx in ('hbr','water','bromine') else energy_profile([0,-30],[55])
    diagrams=[initial,product]
    if rx=='ozone' and not internal: diagrams.append(carbonyl('Méthanal : second fragment','H','H'))
    if rx=='ozone' and internal: diagrams.append(carbonyl('Éthanal : second fragment','H','CH₃'))
    drawing=rs('Identifier le produit, puis justifier',note,diagrams) if stage==2 and rx=='ozone' else ms('Addition et choix des conditions',note,frames,stage)
    return result([m('Produit principal du cas',name),m('Régiosélectivité',selectivity),m('Stéréochimie',stereo),m('Réarrangement','possible' if rearrange else 'non requis'),m('Étape affichée',stage)],
        [ch('Topologie du mécanisme : profil illustratif','Coordonnée réactionnelle','G modèle / kJ·mol⁻¹',se('Profil déclaré',x,y))],drawing,
        [selectivity,stereo,note,'Les noms et règles concernent les substrats proposés. Le graphe semi-développé ne porte pas toutes les configurations : les noms meso/racémique les explicitent.'],
        ['Cas documentés, sans prédiction de rendement ni de proportion minoritaire.','Énergies de profil choisies uniquement pour distinguer voie concertée et intermédiaire.'],product_name=name,regio=selectivity,stereo=stereo,rearrangement=rearrange)

def alcyne(p):
    sub,rx=p['substrate'],p['reagent'];terminal=sub=='propyne';initial=chain('Propyne' if terminal else 'But-2-yne',['CH₃','C','CH' if terminal else 'C','CH₃'] if not terminal else ['CH₃','C','CH'],[1,3,1] if not terminal else [1,3])
    stereo='sans objet';name='';equiv=1;intermediate=initial
    if rx in ('lindlar','dissolving'):
        name='Propène' if terminal else '(Z)-but-2-ène' if rx=='lindlar' else '(E)-but-2-ène'
        stereo='syn : alcène Z si deux groupes distincts' if rx=='lindlar' else 'anti : alcène E si deux groupes distincts'
        product=alkene_graph('propene' if terminal else 'butene_Z' if rx=='lindlar' else 'butene_E')
    elif rx=='hydrogen':
        name='Propane' if terminal else 'Butane';equiv=2;product=chain(name,['CH₃','CH₂','CH₃'] if terminal else ['CH₃','CH₂','CH₂','CH₃'])
    elif rx in ('mercury','borane'):
        aldehyde=terminal and rx=='borane';name='Propanal' if aldehyde else 'Propanone' if terminal else 'Butan-2-one'
        product=carbonyl(name,'H' if aldehyde else 'CH₃','CH₂CH₃' if aldehyde or not terminal else 'CH₃')
        intermediate=chain('Énol avant tautomérie',['CH₃','CH','CH(OH)'] if aldehyde else ['CH₃','C(OH)','CH₂'] if terminal else ['CH₃','C(OH)','CH','CH₃'],[1,2] if terminal else [1,2,1])
        stereo='Énol → carbonyle : tautomérie, pas mésomérie'
    elif rx.startswith(('hbr','hcl')):
        twice=rx in ('hbr2','hcl2');equiv=2 if twice else 1;name=('2,2-dibromopropane' if terminal else '2,2-dibromobutane') if twice else ('2-bromoprop-1-ène' if terminal else '2-bromobut-2-ène (E/Z)')
        product=chain(name,['CH₃','CBr₂' if twice else 'CBr','CH₃' if twice else 'CH₂'] if terminal else ['CH₃','CBr₂' if twice else 'CBr','CH₂' if twice else 'CH','CH₃'],[1,1] if twice and terminal else [1,2] if terminal else [1,1,1] if twice else [1,2,1])
        if rx.startswith('hcl'):
            name=name.replace('bromo','chloro')
            product['name']=name
            for a in product['atoms']:a['label']=a['label'].replace('Br','Cl')
        stereo='Geminal après deux additions ; Markovnikov dans le cas terminal'
    else:
        twice=rx=='br2';equiv=2 if twice else 1;name='1,1,2,2-tétrabromopropane' if terminal and twice else '2,2,3,3-tétrabromobutane' if twice else 'Dibromoalcène : addition anti favorisée'
        product=chain(name,['CH₃','CBr₂','CHBr₂'] if terminal and twice else ['CH₃','CBr₂','CBr₂','CH₃'] if twice else ['CH₃','CBr','CHBr'] if terminal else ['CH₃','CBr','CBr','CH₃'],[1,1] if terminal and twice else [1,1,1] if twice else [1,2] if terminal else [1,2,1])
        stereo='Anti favorisée à la première addition ; l’alcyne n’a pas de configuration E/Z'
    note='Un borane encombré est requis pour limiter à une hydroboration de l’alcyne ; BH₃ seul n’est pas une garantie de sélectivité.' if rx=='borane' else 'Le produit carbonylé est isolé après tautomérie.' if rx=='mercury' else 'Choix des conditions et quantité stœchiométrique explicités.'
    if rx in ('hbr2','hcl2','br2'):
        intermediate=chain('Première addition : alcène halogéné',
            ['CH₃','CBr','CH₂' if rx in ('hbr2','hcl2') else 'CHBr'] if terminal else ['CH₃','CBr','CH' if rx in ('hbr2','hcl2') else 'CBr','CH₃'],
            [1,2] if terminal else [1,2,1])
        if rx=='hcl2':
            for a in intermediate['atoms']:a['label']=a['label'].replace('Br','Cl')
    elif rx=='hydrogen':
        intermediate=alkene_graph('propene' if terminal else 'butene_Z');intermediate['name']='Alcène intermédiaire avant seconde hydrogénation'
    frames=[initial,intermediate,product] if rx in ('mercury','borane','hydrogen','hbr2','hcl2','br2') else [initial,product]
    stage=min(int(p['stage']),len(frames)-1)
    x,y=energy_profile([0,5,-30],[55,40]) if rx in ('mercury','borane') else energy_profile([0,-30],[60])
    return result([m('Produit du cas',name),m('Stéréochimie / règle',stereo),m('Équivalents au bilan',equiv),m('Fonction isolée','carbonyle' if rx in ('mercury','borane') else 'alcène' if rx in ('lindlar','dissolving','hbr1','hcl1','br1') else 'saturée'),m('Étape réelle',stage)],
        [ch('Profil illustratif : distinguer énol et carbonyle','Coordonnée réactionnelle','G modèle / kJ·mol⁻¹',se('Profil déclaré',x,y))],ms('Changer de réactif change la cible',note,frames,stage),
        [stereo,note,'Une hydrogénation complète consomme deux H₂ par C≡C. Lindlar et métal dissous s’arrêtent à des alcènes de géométries différentes.',
         'Propyne hydraté avec Hg²⁺ → propanone ; hydroboration sélective/oxydation → propanal.'],
        ['Sous-ensemble documenté : alcyne terminal simple ou alcyne interne symétrique.','Profils énergétiques qualitatifs, sans constantes ou rendements prédits.',
         'Lindlar/métal dissous : bilan avant/après, pas mécanisme détaillé de surface ou transfert électronique. L’index est arrêté au dernier état disponible.'],product_name=name,stereo=stereo,equivalents=equiv,stage=stage,tautomerism=rx in ('mercury','borane'))

def radical(p):
    per=p['mode']=='peroxide';hal=p['halogen'];factor=p['selectivity'];weights=np.array([9.,factor]);shares=weights/weights.sum()
    radical_c=math.sqrt(p['initiation']/(2*p['termination']))
    sources=np.linspace(.00001,.01,201);steady=np.sqrt(sources/(2*p['termination']))
    # Gas-phase approximate bond enthalpies, used only to reason about propagation signs.
    # Jeu d'énergies de liaison moyennes déclaré : π≈266, C–Cl≈350,
    # C–Br≈293, C–I≈233 ; C–H secondaire≈410 ; HCl≈431, HBr≈366, HI≈298.
    # Approximation illustrative : différence de moyennes, pas donnée calorimétrique.
    dh1={'hbr':266.-293.,'hcl':266.-350.,'hi':266.-233.}.get(hal,266.-293.)
    dh2={'hbr':366.-410.,'hcl':431.-410.,'hi':298.-410.}.get(hal,366.-410.)
    chain_ok=hal=='hbr' if per else hal in ('cl','br')
    if per:
        frames=[molecule('Amorçage : RO–OR → 2 RO•',[atom('a','O',-.8,0,label='RO'),atom('b','O',.8,0,label='OR')],[bond('a','b')],
                         [arrow((0,.05),(-.8,.1),(-.4,.7),electrons=1),arrow((0,-.05),(.8,-.1),(.4,-.7),electrons=1)]),
                molecule('Br• + CH₂=CH–CH₃ → BrCH₂–CH•–CH₃',[atom('br','Br',-1.7,0,label='Br•'),atom('a','C',-.5,0,label='CH₂'),atom('b','C',.5,0,label='CH'),atom('r','C',1.5,0,label='CH₃')],
                         [bond('a','b',2),bond('b','r')],[arrow((-1.5,.1),(-.5,.1),(-1,.7),electrons=1),arrow((0,.08),(-.5,.1),(-.4,.7),electrons=1),arrow((0,-.08),(.5,-.1),(.4,-.7),electrons=1)]),
                molecule('Propagation : radical + HBr → produit + Br•',[atom('a','C',-.5,0,label='BrCH₂–CH•–CH₃'),atom('h','H',.8,0),atom('br','Br',1.8,0)],
                         [bond('h','br')],[arrow((-.5,.1),(.8,.1),(0,.8),electrons=1),arrow((1.3,.05),(.8,.1),(1,.7),electrons=1),arrow((1.3,-.05),(1.8,-.1),(1.8,-.7),electrons=1)]),
                molecule('Terminaison : deux radicaux se combinent',[atom('a','Br',-.8,0,label='Br•'),atom('b','Br',.8,0,label='Br•')],[],
                         [arrow((-.8,.1),(0,0),(-.4,.7),electrons=1),arrow((.8,.1),(0,0),(.4,.7),electrons=1)])]
        desc='HBr / peroxydes : Br sur le carbone terminal, radical secondaire ; propagation de chaîne favorable.' if chain_ok else 'Cette chaîne anti-Markovnikov classique ne se soutient pas : une étape de propagation est endothermique pour HCl ou HI.'
        metrics=[m('Effet peroxyde classique','oui : HBr' if chain_ok else 'non pour ce HX'),m('ΔH propagation 1 estimée',dh1,'kJ·mol⁻¹'),m('ΔH propagation 2 estimée',dh2,'kJ·mol⁻¹'),m('Radicaux stationnaires, modèle',radical_c,'mol·L⁻¹'),m('Produit HBr du cas','1-bromopropane' if chain_ok else 'non prédit par cette chaîne')]
        quantitative=ch('Énergétique approximative des deux propagations','Étape','ΔH / kJ·mol⁻¹',se('Approximation par énergies de liaison',[1,2],[dh1,dh2]))
    else:
        frames=[molecule('Amorçage : X₂ → 2 X•',[atom('a','Br' if hal=='br' else 'Cl',-.8,0,label='X'),atom('b','Br' if hal=='br' else 'Cl',.8,0,label='X')],[bond('a','b')],
                          [arrow((0,.05),(-.8,.1),(-.4,.7),electrons=1),arrow((0,-.05),(.8,-.1),(.4,-.7),electrons=1)]),
                chain('Propagation 1 : X• + R–H → HX + R•',['X•','H','R'],[1,1]),
                chain('Propagation 2 : R• + X₂ → RX + X•',['R•','X','X'],[1,1]),
                chain('Terminaison : R• + R• → R–R',['R','R'])]
        desc='Isobutane : 9 hydrogènes primaires équivalents et 1 hydrogène tertiaire ; nombres de sites et réactivité par site se multiplient.'
        metrics=[m('H primaires',9),m('H tertiaires',1),m('Produit primaire, modèle',100*shares[0],'%'),m('Produit tertiaire, modèle',100*shares[1],'%'),m('Radicaux stationnaires, modèle',radical_c,'mol·L⁻¹'),m('Réactif valable','Cl₂ ou Br₂' if chain_ok else 'choisir Cl₂ ou Br₂ pour ce mode')]
        factors=np.geomspace(1,2000,201);quantitative=ch('Sélectivité corrigée du nombre d’hydrogènes','k₃/k₁ choisi','Fraction du produit tertiaire',se('k₃/(9k₁+k₃)',factors,factors/(9+factors)),x_scale='log')
    return result(metrics,[quantitative,ch('État stationnaire radicalaire','Rᵢ / mol·L⁻¹·s⁻¹','[R•] / mol·L⁻¹',se('√(Rᵢ/2kₜ)',sources,steady))],
        ms('Amorçage, propagation, terminaison',desc,frames,int(p['stage'])),
        [desc,'Rᵢ = 2kₜ[R•]² : la source est définie comme le nombre de radicaux créés par unité de volume et temps.',
         'Le facteur de sélectivité est choisi. Les préréglages illustrent forte sélectivité de bromation et faible sélectivité de chloration ; il varie avec température et substrat.',
         'Jeu d’énergies moyennes déclaré, en kJ/mol : π(C=C)≈266 ; C–Cl≈350, C–Br≈293, C–I≈233 ; C–H secondaire≈410 ; HCl≈431, HBr≈366, HI≈298. ΔH ≈ liaisons rompues − liaisons formées.',
         'Cette approximation des ΔH éclaire le signe ; elle ne donne ni une calorimétrie précise, ni une cinétique en solution.'],
        ['Monohalogénation à faible conversion, sites d’isobutane uniquement ; pas de polyhalogénation.',
         'État stationnaire avec terminaison bimoléculaire, pas de diffusion ni inhibiteur dans le modèle.','Pour l’effet peroxyde, seules les séquences HBr sont dessinées : HCl et HI servent de contre-exemples énergétiques.'],
        primary_fraction=float(shares[0]),tertiary_fraction=float(shares[1]),radical_concentration=radical_c,chain_supported=chain_ok,propagation_enthalpies=[dh1,dh2])

def carbonyle(p):
    rx=p['reaction'];initial=carbonyl('Éthanal','CH₃','H');steps=[];k=p['equilibrium'];water=p['water'];
    descriptions={
        'addition':('Éthanol','H⁻ → C ; π(C=O) → O ; hydrolyse de l’alcoolate.'),
        'ester':('Éthanoate d’éthyle','Acide + éthanol ⇌ ester + eau ; catalyse acide, addition puis élimination.'),
        'amide':('N-méthyléthanamide','Chlorure d’éthanoyle + 2 CH₃NH₂ → amide + CH₃NH₃⁺Cl⁻.'),
        'aldol':('3-hydroxybutanal','L’énolate de l’éthanal attaque le C du carbonyle d’un autre éthanal.'),
        'croton':('But-2-énal','Déshydratation du β-hydroxyaldéhyde ; formation d’une conjugaison C=C–C=O.'),
        'acetal':('1,1-diéthoxyéthane','Éthanal + 2 EtOH ⇌ acétal + H₂O ; H⁺ catalytique.'),
        'michael':('Adduit 1,4 : liaison C–C en β','Un énolate stabilisé attaque le carbone β d’une énone ; protonation du nouvel énolate.'),
        'wittig':('2-méthylpropène','Propanone + Ph₃P=CH₂ → 2-méthylpropène + Ph₃P=O.'),
        'epoxide':('Éthane-1,2-diol','HO⁻ ouvre l’oxyde d’éthylène ; rupture C–O, puis protonation.')}
    name,explanation=descriptions[rx]
    if rx=='addition':
        initial=carbonyl('Éthanal','CH₃','H');initial['atoms'].append(atom('nu','H',-1,-1,label='H',charge=-1));initial['arrows']=[arrow((-1,-.9),(0,0),(-1,.2)),arrow((0,.55),(.15,1.1),(.8,.8))]
        mid=tetrahedral('Alcoolate','CH₃','H','H');final=chain(name,['CH₃','CH₂','OH'])
        frames=[initial,mid,final]
    elif rx in ('ester','amide'):
        initial=carbonyl('Acide éthanoïque' if rx=='ester' else 'Chlorure d’éthanoyle','CH₃','OH' if rx=='ester' else 'Cl')
        if rx=='ester':
            initial['atoms'][1].update(label='OH',charge=1)
            initial['name']='Acide éthanoïque protoné au carbonyle'
        initial['atoms'].append(atom('nu','O' if rx=='ester' else 'N',1.8,-.8,label='EtOH' if rx=='ester' else 'CH₃NH₂'))
        initial['arrows']=[arrow((1.8,-.7),(0,0),(.5,-1)),arrow((0,.55),(.15,1.1),(.8,.8))]
        mid=tetrahedral('Intermédiaire tétraédrique','CH₃','OH' if rx=='ester' else 'Cl','OEt' if rx=='ester' else 'NHCH₃')
        # neutral amine attack has N+ until deprotonation; O- and N+ sum to zero
        if rx=='amide': mid['atoms'][-1].update(element='N',label='NH₂CH₃',charge=1)
        else:
            mid['atoms'][1].update(label='OH',charge=0)
            mid['atoms'][-1].update(element='O',label='OHEt',charge=1)
        final=carbonyl(name,'CH₃','OEt' if rx=='ester' else 'NHCH₃')
        frames=[initial,mid,final]
    elif rx in ('aldol','croton'):
        initial=molecule('Énolate + éthanal',[atom('a','C',-1.5,-.5,label='CH₂',charge=-1),atom('r','C',-2.4,-.5,label='CHO'),
            atom('c','C',0,0,label='CH'),atom('o','O',0,1.1),atom('m','C',1,0,label='CH₃')],[bond('a','r'),bond('c','o',2),bond('c','m')],
            [arrow((-1.4,-.4),(0,0),(-.8,.6),label='C nucléophile → C carbonyle'),arrow((0,.55),(.15,1.1),(.8,.8))])
        mid=chain('Alcoolate aldol',['CHO','CH₂','CH(O⁻)','CH₃']);mid['atoms'][2]['charge']=-1
        aldol=chain('3-hydroxybutanal',['CHO','CH₂','CH(OH)','CH₃']);final=chain(name,['CHO','CH','CH','CH₃'],[1,2,1]) if rx=='croton' else aldol
        frames=[initial,mid,aldol,final] if rx=='croton' else [initial,mid,final]
    elif rx=='acetal':
        mid=chain('Hémiacétal',['CH₃','CH(OH)','OEt']);final=chain(name,['CH₃','CH(OEt)','OEt']);frames=[initial,mid,final]
    elif rx=='michael':
        initial=molecule('Énone : repérer α et β',
            [atom('m','C',-1,0,label='CH₃'),atom('c','C',0,0),atom('o','O',0,1),atom('a','C',1,0,label='CHα'),
             atom('b','C',2,0,label='CH₂β'),atom('nu','C',3,-.5,label='CH(CO₂Et)₂',charge=-1)],
            [bond('m','c'),bond('c','o',2),bond('c','a'),bond('a','b',2)],
            [arrow((3,-.4),(2,.1),(2.8,.8),label='énolate → Cβ'),arrow((1.5,.05),(.5,.05),(1,.8),label='π(Cα=Cβ) → C–Cα'),
             arrow((0,.5),(.1,1),(-.8,.8),label='π(C=O) → O')])
        mid=chain('Énolate issu de l’addition 1,4',['CH₃C(O⁻)','CH','CH₂','CH(CO₂Et)₂'],[2,1,1]);mid['atoms'][0]['charge']=-1
        final=chain(name,['CH₃CO','CH₂','CH₂','CH(CO₂Et)₂']);frames=[initial,mid,final]
    elif rx=='wittig':
        initial=carbonyl('Propanone','CH₃','CH₃');initial['atoms'].append(atom('nu','C',-1,-1,label='CH₂',charge=-1))
        initial['atoms'].append(atom('p','P',-2,-1,label='PPh₃',charge=1));initial['bonds'].append(bond('nu','p'))
        initial['arrows']=[arrow((-1,-.9),(0,0),(-1,.2)),arrow((0,.55),(.1,1.1),(.8,.8))]
        mid=molecule('Oxaphosphetane : cycle à quatre centres',[atom('c','C',0,0,label='C(CH₃)₂'),atom('o','O',0,1),atom('p','P',1,1,label='PPh₃'),atom('a','C',1,0,label='CH₂')],
                     [bond('c','o'),bond('o','p'),bond('p','a'),bond('a','c')]);final=chain(name,['CH₂','C(CH₃)₂'],[2]);frames=[initial,mid,final]
    else:
        initial=molecule('Oxyde d’éthylène + HO⁻',[atom('a','C',-.6,0,label='CH₂'),atom('b','C',.6,0,label='CH₂'),atom('o','O',0,.9),atom('nu','O',-1.7,-.3,label='HO',charge=-1)],
                         [bond('a','b'),bond('a','o'),bond('b','o')],[arrow((-1.6,-.2),(-.6,0),(-1.3,.8)),arrow((-.3,.45),(0,1),(-.8,1))])
        mid=chain('Alcoolate après ouverture',['HO','CH₂','CH₂','O']);mid['atoms'][-1]['charge']=-1;final=chain(name,['HO','CH₂','CH₂','OH']);frames=[initial,mid,final]
    stage=min(int(p['stage']),len(frames)-1)
    aw=np.geomspace(.01,3,201);f=k/(k+aw);eq_fraction=k/(k+water)
    x,y=energy_profile([0,15,-20],[65,45])
    charts=[ch('Intermédiaire tétraédrique ou carboné : profil choisi','Coordonnée réactionnelle','G modèle / kJ·mol⁻¹',se('Profil illustratif',x,y))]
    if rx in ('ester','acetal'): charts.append(ch('Réservoirs : retirer l’eau déplace l’équilibre','Activité relative de H₂O','Fraction convertie, modèle',se('K/(K+aH₂O)',aw,f),x_scale='log'))
    return result([m('Transformation',name),m('Étape réelle',stage),m('Nombre d’étapes représentées',len(frames)),m('Déplacement d’équilibre','retirer H₂O' if rx in ('ester','acetal') else 'selon conditions'),
                   m('Fraction convertie sous réservoirs',100*eq_fraction if rx in ('ester','acetal') else 'non calculée','%' if rx in ('ester','acetal') else '')],charts,
        ms('Nommer chaque étape avant le produit',explanation,frames,stage),
        [explanation,'Addition carbonyle : le nucléophile donne à C ; le doublet π va vers O. Une substitution acyle exige aussi la sortie d’un groupe partant.',
         'Aldolisation : liaison C–C puis protonation. Crotonisation : élimination d’eau et conjugaison. Michael : addition au carbone β.',
         'Acide + amine donne d’abord un sel ammonium carboxylate ; une amidation efficace requiert activation ou conditions adaptées.'],
        ['Mécanismes simplifiés avec groupes explicites, protonations rapides regroupées ; pas toutes les espèces du catalyseur.',
         'Équilibre estérification/acétal : alcool et catalyseur en réservoir, activités standardisées ; K choisi intègre l’activité de l’alcool. Aucun rendement isolé prédit.'],
        product_name=name,stage=stage,frames_count=len(frames),equilibrium_fraction=eq_fraction if rx in ('ester','acetal') else None)

def grignard(p):
    sub,alkyl=p['substrate'],p['alkyl'];group={'methyl':'CH₃','ethyl':'CH₂CH₃','phenyl':'Ph'}[alkyl]
    protons=1 if sub=='protic' else 0;available=max(0,p['equivalents']-p['water']-protons);need=2 if sub=='ester' else 1
    full=available>=need;destroyed=min(p['equivalents'],p['water']+protons)
    names={'methanal':'Alcool primaire R–CH₂OH','aldehyde':'Alcool secondaire CH₃–CH(OH)–R','ketone':'Alcool tertiaire (CH₃)₂C(OH)R',
           'ester':'Alcool tertiaire CH₃C(OH)R₂','co2':'Acide carboxylique R–COOH','epoxide':'Alcool primaire R–CH₂–CH₂OH','protic':'Diol après addition et hydrolyse (si RMgBr supplémentaire)'}
    name=names[sub] if full else ('Addition impossible : RMgBr consommé par les protons' if destroyed>0 else 'Aucun RMgBr disponible') if available==0 else 'Mélange / conversion partielle : produit pur non garanti'
    status='excès disponible' if full and available>need else 'stœchiométrie suffisante' if full else 'quantité insuffisante'
    if sub in ('methanal','aldehyde','ketone','ester','protic'):
        left='H' if sub=='methanal' else 'CH₃';right='H' if sub in ('methanal','aldehyde') else 'OEt' if sub=='ester' else 'CH₂OH' if sub=='protic' else 'CH₃'
        initial=carbonyl('Électrophile : '+sub,left,right);initial['atoms'].append(atom('nu','C',-1.3,-1,label=group,charge=-1));initial['atoms'].append(atom('mg','Mg',-2.4,-1,label='MgBr',charge=1))
        initial['arrows']=[arrow((-1.2,-.9),(0,0),(-1,.1)),arrow((0,.55),(.15,1.1),(.8,.8))]
        mid=tetrahedral('Alcoolate magnésien',left,group if sub=='ester' else right,group)
        mid['atoms'].append(atom('mg','Mg',-2,1,label='MgBr',charge=1))
        final=tetrahedral(names[sub],left,group if sub=='ester' else right,group,True)
    elif sub=='co2':
        initial=chain('CO₂ + RMgBr',['O','C','O'],[2,2]);initial['atoms'].append(atom('nu','C',1,-1,label=group,charge=-1));initial['arrows']=[arrow((1,-.9),(1,.1),(.4,-.3)),arrow((.5,.1),(0,.2),(.2,.8))]
        initial['atoms'].append(atom('mg','Mg',-1,-1,label='MgBr',charge=1))
        mid=carbonyl('Carboxylate magnésien',group,'O⁻');mid['atoms'][3]['charge']=-1;mid['atoms'].append(atom('mg','Mg',-2,1,label='MgBr',charge=1));final=carbonyl(names[sub],group,'OH')
    else:
        initial=molecule('Oxyde d’éthylène + RMgBr',[atom('a','C',-.6,0,label='CH₂'),atom('b','C',.6,0,label='CH₂'),atom('o','O',0,.9),atom('nu','C',-1.8,-.4,label=group,charge=-1)],
                         [bond('a','b'),bond('a','o'),bond('b','o')],[arrow((-1.7,-.3),(-.6,0),(-1.3,.8)),arrow((-.3,.45),(0,1),(-.8,1))])
        initial['atoms'].append(atom('mg','Mg',-2,1,label='MgBr',charge=1))
        mid=chain('Alcoolate allongé de deux carbones',[group,'CH₂','CH₂','O⁻']);mid['atoms'][-1]['charge']=-1;mid['atoms'].append(atom('mg','Mg',-1,1,label='MgBr',charge=1))
        final=chain(names[sub],[group,'CH₂','CH₂','OH'])
    if not full and available>0:
        final['name']='Produit visé, au sein d’un mélange possible — conversion non prédite'
    frames=[initial,mid,final];stage=int(p['stage']) if available>0 else 0
    if available==0:
        # Ne pas dessiner une attaque C=O si le réactif a déjà été détruit.
        initial['arrows']=[]
        if destroyed>0:
            initial['name']='Électrophile sans RMgBr disponible : protons prioritaires'
            initial['atoms']=[a for a in initial['atoms'] if a['id'] not in ('nu','mg')]
            initial['bonds']=[b for b in initial['bonds'] if b['a'] not in ('nu','mg') and b['b'] not in ('nu','mg')]
    eqs=np.linspace(0,4,161);avail=np.maximum(0,eqs-p['water']-protons);capacity=np.minimum(1,avail/need)
    upper=min(1,available/need)
    return result([m('Produit visé après hydrolyse',name),m('RMgBr consommé par protons',destroyed,'équiv.'),m('RMgBr restant pour addition',available,'équiv.'),
        m('Besoin par électrophile',need,'équiv.'),m('Statut',status),m('Borne stœchiométrique de formation',100*upper,'%')],
        [ch('Borne de bilan, pas rendement isolé','RMgBr ajouté / équiv.','Borne de fraction convertie',se('Après consommation protique',eqs,capacity))],
        ms('Séquence anhydre puis hydrolyse',
           'Le carbone du RMgBr est nucléophile et fortement basique. Solvant éthéré anhydre ; hydrolyse seulement après addition.',frames,stage),
        ['Avant toute attaque carbonyle : un proton d’eau, d’alcool, d’acide ou d’alcyne terminal consomme un équivalent RMgBr et donne RH.',
         'Un ester subit addition, élimination d’alcoolate, puis addition à la cétone formée, plus réactive. Un équivalent ne constitue pas une recette de cétone pure.',
         'La borne de fraction convertie est un maximum stœchiométrique ; elle n’est ni une distribution de produits, ni une conversion calculée cinétiquement.',
         'Le CO₂ donne un carboxylate puis un acide ; l’oxyde d’éthylène allonge le squelette de deux carbones.'],
        ['Contaminants quantifiés comme équivalents de protons ; consommation protique prioritaire et complète.',
         'RMgBr représenté comme R⁻ / MgBr⁺ pour lire les flèches, sans prétendre décrire son agrégation ou sa structure réelle en éther.'],
        available_equivalents=available,destroyed_equivalents=destroyed,required_equivalents=need,stoichiometric_upper_bound=upper,full_stoichiometry=full,product_name=name)

REDOX_START={'alcohol1':('Éthanol',-1),'alcohol2':('Propan-2-ol',0),'alcohol3':('2-méthylpropan-2-ol',1),
             'aldehyde':('Éthanal',1),'ketone':('Propanone',2),'ester':('Éthanoate d’éthyle',3),'acid':('Acide éthanoïque',3),'nitro':('Nitrobenzène',3)}

def oxydoreduction(p):
    sub,rx=p['substrate'],p['reagent'];name,oxidation=REDOX_START[sub];product_name=name;end=oxidation;reacts=False;extra=''
    if rx in ('pcc','aqueous'):
        if sub=='alcohol1': product_name,end=('Éthanal',1) if rx=='pcc' else ('Acide éthanoïque',3);reacts=True
        elif sub=='alcohol2': product_name,end='Propanone',2;reacts=True
        elif sub=='aldehyde' and rx=='aqueous': product_name,end='Acide éthanoïque',3;reacts=True
        elif sub=='alcohol3': extra='Pas de H sur le carbone carbinol : pas d’oxydation usuelle conservant le squelette.'
    elif rx in ('nabh4','lialh4'):
        if sub in ('aldehyde','ketone'): product_name,end=('Éthanol',-1) if sub=='aldehyde' else ('Propan-2-ol',0);reacts=True
        elif rx=='lialh4' and sub in ('ester','acid'): product_name,end='Éthanol',-1;reacts=True;extra='L’ester fournit aussi l’alcool du groupe OR après hydrolyse.' if sub=='ester' else 'Un acide consomme aussi de l’hydrure par réaction acido-basique.'
        elif rx=='lialh4' and sub=='nitro': product_name,end='Aniline',-3;reacts=True
        elif sub in ('alcohol1','alcohol2','alcohol3') and rx=='lialh4': extra='Réaction acido-basique avec O–H ; ce n’est pas une réduction du carbone.'
    elif rx=='metal' and sub=='nitro': product_name,end='Aniline',-3;reacts=True;extra='ArNO₂ + 6 H⁺ + 6 e⁻ → ArNH₂ + 2 H₂O ; neutralisation finale.'
    electrons=abs(end-oxidation) if reacts else 0
    start=carbonyl(name,'CH₃','H' if sub=='aldehyde' else 'OEt' if sub=='ester' else 'OH' if sub=='acid' else 'CH₃') if sub in ('aldehyde','ketone','ester','acid') else benzene(name,{0:'NO₂'}) if sub=='nitro' else chain(name,['CH₃','CH₂OH'] if sub=='alcohol1' else ['CH₃','CH(OH)','CH₃'] if sub=='alcohol2' else ['CH₃','C(OH)(CH₃)','CH₃'])
    if product_name=='Aniline': final=benzene(product_name,{0:'NH₂'})
    elif product_name=='Éthanol': final=chain(product_name,['CH₃','CH₂','OH'])
    elif product_name=='Propan-2-ol': final=chain(product_name,['CH₃','CH(OH)','CH₃'])
    elif product_name=='Éthanal': final=carbonyl(product_name,'CH₃','H')
    elif product_name=='Acide éthanoïque': final=carbonyl(product_name,'CH₃','OH')
    elif product_name=='Propanone': final=carbonyl(product_name)
    else: final=start
    note='Transformation retenue dans les conditions usuelles.' if reacts else 'Pas de transformation rédox usuelle retenue pour cette fonction/réactif.'
    return result([m('Fonction de départ',name),m('Produit',product_name),m('Rédox du centre suivi','oui' if reacts else 'non'),m('Nombre d’oxydation initial',oxidation),
        m('Nombre d’oxydation final',end),m('Électrons par centre',electrons),m('Centre suivi','N' if sub=='nitro' else 'C fonctionnel')],
        [ch('Échelle d’oxydation du centre fonctionnel','Avant / après','Nombre d’oxydation',se('Centre suivi',[0,1],[oxidation,end]))],
        rs('Chimiosélectivité et bilan électronique',note+' '+extra,[start,final]),
        [note,extra or 'Un réactif est défini par ses conditions : NaBH₄ réduit usuellement aldéhydes/cétones ; LiAlH₄ réduit aussi esters et acides.',
         'Pour le carbone : liaison C–O compte +1 (double liaison +2), C–H compte −1, C–C compte 0. Nitrobenzène : le centre suivi est N, pas le carbone du cycle.',
         'Une variation de nombre d’oxydation indique un bilan électronique, pas des électrons libres effectivement transférés lors d’une addition d’hydrure.'],
        ['Tableau de conditions usuelles CPGE ; substrats simples, sans autres fonctions concurrençant le réactif.',
         'Absence de transformation dans ce modèle n’exclut pas des conditions spécialisées ; pas de rupture C–C oxydante étudiée ici.'],
        reacts=reacts,oxidation_initial=oxidation,oxidation_final=end,electrons_per_center=electrons,product_name=product_name)

def aromatique(p):
    sub,rx=p['substituent'],p['reaction'];directors={'h':'aucune orientation préalable','methyl':'ortho / para','oh':'ortho / para','methoxy':'ortho / para','chloro':'ortho / para','nitro':'méta','acyl':'méta'}
    effect={'h':'référence','methyl':'activant','oh':'fortement activant','methoxy':'activant','chloro':'désactivant','nitro':'fortement désactivant','acyl':'désactivant'}
    fc=rx in ('alkylation','acylation');allowed=not (fc and sub in ('nitro','acyl'))
    # Phenols can undergo O chemistry / Lewis acid complexation; do not call FC a simple prediction.
    qualified=fc and sub in ('oh','methoxy')
    weights=fractions_from_barriers([p['go'],p['gm'],p['gp']],p['temperature'],[2,2,1]) if allowed else np.zeros(3)
    group={'h':None,'methyl':'CH₃','oh':'OH','methoxy':'OCH₃','chloro':'Cl','nitro':'NO₂','acyl':'COCH₃'}[sub]
    e={'nitration':'NO₂','bromination':'Br','chlorination':'Cl','sulfonation':'SO₃H','alkylation':'R','acylation':'COR'}[rx]
    e_element={'nitration':'N','bromination':'Br','chlorination':'Cl','sulfonation':'S','alkylation':'C','acylation':'C'}[rx]
    site=2 if directors[sub]=='méta' else 1
    # Représentation de l'électrophile activé : Br/Cl liés au catalyseur ;
    # HSO3+ est un modèle limite en milieu acide, pas un ion libre universel.
    donating_bond=2 if site==2 else 0
    charge_site=3 if site==2 else 0
    initial=benzene('Aromatique substitué',{} if group is None else {0:group});initial['atoms'].append(atom('e',e_element,2.5,1,label=e,charge=1))
    a=initial['atoms'][donating_bond];b=initial['atoms'][(donating_bond+1)%6]
    # π donation from a bond midpoint, not from a bare carbon.
    initial['arrows']=[arrow(((a['x']+b['x'])/2,(a['y']+b['y'])/2),(2.5,1),(1.3,1.8),label='doublet π → E⁺')]
    sigma=benzene('Complexe σ (contributeur)',{} if group is None else {0:group});sigma['atoms'].append(atom('e',e_element,1.8*math.cos(site*math.pi/3),1.8*math.sin(site*math.pi/3),label=e));sigma['bonds'].append(bond(site,'e'))
    sigma['bonds'][donating_bond]['order']=1;sigma['atoms'][charge_site]['charge']=1
    final=benzene('Produit ortho (un exemple)' if directors[sub]!='méta' else 'Produit méta (un exemple)',{**({} if group is None else {0:group}),site:e})
    frames=[initial,sigma,final] if allowed else [initial];stage=min(int(p['stage']),len(frames)-1)
    temps=np.linspace(250,450,151);pop=np.array([fractions_from_barriers([p['go'],p['gm'],p['gp']],v,[2,2,1]) for v in temps])
    x,y=energy_profile([0,35,-15],[90,43])
    description='Friedel–Crafts usuelle non retenue sur ce cycle fortement désactivé.' if not allowed else 'L’orientation chimique qualitative et les fractions du modèle de barrières sont séparées.'
    return result([m('Orientation qualitative',directors[sub]),m('Effet sur la réactivité',effect[sub]),m('Applicabilité','non : cycle trop désactivé' if not allowed else 'conditions à préciser / complexation possible' if qualified else 'cas classique'),
        m('Part ortho, barrières choisies',100*weights[0],'%'),m('Part méta, barrières choisies',100*weights[1],'%'),m('Part para, barrières choisies',100*weights[2],'%')],
        [ch('Cinq sites : multiplicité et barrières déclarées','T / K','Fraction du modèle',*[se(label,temps,pop[:,j] if allowed else np.zeros(len(temps))) for j,label in enumerate(['Ortho (2 sites)','Méta (2 sites)','Para (1 site)'])]),
         ch('Addition puis restauration de l’aromaticité','Coordonnée réactionnelle','G modèle / kJ·mol⁻¹',se('Profil déclaré',x,y))],
        ms('SEA : le cycle est nucléophile',description,frames,stage),
        [description,('Sulfonation réversible : SO₃ / H₂SO₄ ; le schéma suit HSO₃⁺ en milieu très acide. Le choix du milieu peut aussi conduire à une voie avec SO₃ neutre.' if rx=='sulfonation' else 'L’électrophile du schéma représente une espèce activée par le milieu ou le catalyseur ; les halogènes ne sont pas ajoutés comme ions libres stables.'),'Halogène : −I désactive, donation mésomère oriente ortho/para. NO₂ : forte désactivation et orientation méta.',
         'Fractions calculées : pᵢ ∝ nᵢ exp(−ΔG‡ᵢ/RT), avec n = (2,2,1). Barrières réglables choisies, sans estimation à partir d’un moment dipolaire.',
         'Ordre de synthèse : une Friedel–Crafts doit usuellement précéder une nitration qui désactive le cycle ; l’alkylation peut réarranger et polyalkyler.',
         'Phénol et anisole : leur réaction avec un acide de Lewis et les possibilités de réaction sur O imposent de préciser les conditions avant une Friedel–Crafts.'],
        ['Complexe σ dessiné comme un contributeur, pas un carbocation uniformément réparti.',
         'Produit dessiné : une position exemplaire ; le graphique montre des fractions d’un modèle dont les barrières sont imposées, pas une analyse de mélange réel.'],
        allowed=allowed,orientation=directors[sub],activation=effect[sub],shares=weights,multiplicities=[2,2,1],qualified_conditions=qualified)

def huckel(system,beta,torsion=0):
    n=6 if system=='benzene' else 4;cycle=system in ('benzene','cyclobutadiene')
    mat=np.zeros((n,n))
    for i in range(n-1):
        coupling=-beta*(math.cos(math.radians(torsion)) if not cycle and i==1 else 1)
        mat[i,i+1]=mat[i+1,i]=coupling
    if cycle: mat[0,n-1]=mat[n-1,0]=-beta
    energies,coefficients=np.linalg.eigh(mat)
    # Equal occupation in exactly degenerate frontier subspaces: invariant to basis choice.
    occupations=np.zeros(n);remaining=n
    groups=[];i=0
    while i<n:
        j=i+1
        while j<n and abs(energies[j]-energies[i])<1e-9: j+=1
        group_size=j-i;occ=min(2*group_size,remaining)/group_size
        occupations[i:j]=occ;remaining-=occ*group_size;groups.append((i,j));i=j
    return energies,coefficients,occupations,mat

def orbitales(p):
    system=p['system'];S=p['overlap'];beta=p['beta'];torsion=p['torsion']
    if system=='lcao':
        energies=np.array([-beta/(1+S),beta/(1-S)])
        coeff=np.array([[1/math.sqrt(2*(1+S)),1/math.sqrt(2*(1-S))],[1/math.sqrt(2*(1+S)),-1/math.sqrt(2*(1-S))]])
        overlap=np.array([[1,S],[S,1]]);norm=np.diag(coeff.T@overlap@coeff);occupations=np.array([2.,0.]);pos=[[-1,0],[1,0]]
        charge=np.array([1.,1.]);classification='OM σ liante / σ* antiliante, modèle symétrique';gap=energies[1]-energies[0];HOm=0;BV=1
        matrix=None;electron_count=2
    else:
        actual='butadiene' if system=='diels' else system
        energies,coeff,occupations,matrix=huckel(actual,beta,torsion if actual=='butadiene' else 0)
        norm=np.sum(coeff**2,axis=0);charge=(coeff**2)@occupations;n=len(energies);electron_count=n
        pos=[[math.cos(2*math.pi*j/n),math.sin(2*math.pi*j/n)] for j in range(n)] if system in ('benzene','cyclobutadiene') else [[j,0] for j in range(n)]
        occupied=np.where(occupations>0)[0];unfilled=np.where(occupations<2)[0];HOm=int(occupied[-1]);BV=int(unfilled[0]);gap=max(0.,float(energies[BV]-energies[HOm]))
        classification='Aromatique : cycle plan conjugué, 6 π' if system=='benzene' else '4 π : antiaromatique sous hypothèse de planéité ; modèle dégénéré' if system=='cyclobutadiene' else 'Chaîne conjuguée : ni aromaticité ni antiaromaticité cyclique'
    index=min(int(p['orbital'])-1,len(energies)-1)
    levels=[dict(energy=float(en),label=f'OM {i+1}'+(' · HO' if i==HOm else '')+(' · BV' if i==BV else ''),occupation=float(occ),coefficients=coeff[:,i].tolist()) for i,(en,occ) in enumerate(zip(energies,occupations))]
    xs=np.arange(1,len(energies)+1);ss=np.linspace(0,.8,161)
    curves=[ch('Spectre des OM : énergie relative à α = 0','OM par énergie croissante','E / eV',se('Valeurs propres',xs,energies))]
    if system=='lcao': curves.append(ch('Normalisation avec le recouvrement','S','Coefficient',se('c liante',ss,1/np.sqrt(2*(1+ss))),se('|c antiliante|',ss,1/np.sqrt(2*(1-ss)))))
    else: curves.append(ch('Population π totale par centre','Centre π','Électrons π',se('Σ occupation × |coefficient|²',xs,charge)))
    cis=abs(torsion)<1e-9
    diels_note='Diels–Alder : le conformère s-cis permet de fermer les deux liaisons ; s-trans ne réagit pas directement et doit d’abord se convertir.' if system=='diels' else 'Les signes indiquent une phase d’orbitales ; changer globalement le signe d’une OM ne change aucun observable.'
    return result([m('Système',classification),m('Électrons π / σ du modèle',electron_count),m('HO',HOm+1),m('BV',BV+1),m('Écart HO–BV',gap,'eV'),
        m('Erreur de normalisation',float(np.max(np.abs(norm-1)))),m('OM réellement affichée',index+1),m('Diène s-cis','oui' if cis else 'non, conformation figée')],curves,
        scene('orbitals','Phases, occupations et niveaux d’énergie',diels_note,levels=levels,positions=pos,selected=index,energy_unit='eV',
              color_note='Deux couleurs = signes/phases opposés ; taille du lobe proportionnelle à |c|. La densité dépend de |Ψ|², pas du signe seul.'),
        ['CLOA : Ψ± = (φA ± φB)/√[2(1±S)], pour deux OA réelles normalisées et un recouvrement S.',
         'Hückel : Hii=α=0, Hij=−|β| entre voisins ; les OA π sont orthonormées (S=0). Diagonalisation réelle, occupations explicites.',
         'Dans un niveau dégénéré partiellement occupé, l’occupation égale des OM évite de faire dépendre les populations de la base arbitraire choisie par le solveur.',
         diels_note,'Diels–Alder n’est pas simulée comme un rendement proportionnel à une superposition de lobes : la compatibilité de phase est nécessaire, pas suffisante.'],
        ['Modèles CLOA et Hückel distincts : on ne mélange pas recouvrement réglable des deux OA et Hückel orthogonal.',
         'Énergies en eV, β choisi ; Hückel ignore répulsion électronique, relaxation géométrique et solvant. Cyclobutadiène réel se distord : cycle carré plan ici idéalisé.',
         'Diène : couplage central β cos(dièdre), approximation qualitative ; s-cis et s-trans sont tous deux conjugués, mais une Diels–Alder requiert s-cis.'],
        energies=energies,coefficients=coeff,occupations=occupations,norms=norm,populations=charge,selected=index,homo=HOm,lumo=BV,gap=gap,matrix=matrix,diels_geometry_allowed=cis if system=='diels' else None)

def cinetique(p):
    T=p['temperature'];ka=eyring(p['ha'],p['sa'],T);kb=eyring(p['hb'],p['sb'],T);total=ka+kb
    kinetic=np.array([ka,kb])/total;thermo=fractions_from_barriers([p['ga'],p['gb']],T)
    times=np.linspace(0,p['time'],241);reactant=np.exp(-total*times);products=kinetic[:,None]*(1-reactant)
    temps=np.linspace(250,450,151);ks=np.array([[eyring(p['ha'],p['sa'],t),eyring(p['hb'],p['sb'],t)] for t in temps])
    kinetic_T=ks[:,0]/ks.sum(axis=1);thermo_T=np.array([fractions_from_barriers([p['ga'],p['gb']],t)[0] for t in temps])
    ga_dagger=p['ha']-T*p['sa']/1000;gb_dagger=p['hb']-T*p['sb']/1000
    xa,ya=energy_profile([0,p['ga']],[ga_dagger]);xb,yb=energy_profile([0,p['gb']],[gb_dagger]);
    return result([m('k vers A',ka,'s⁻¹'),m('k vers B',kb,'s⁻¹'),m('A : fraction cinétique',100*kinetic[0],'%'),m('A : fraction à l’équilibre des produits',100*thermo[0],'%'),
        m('ΔG‡A',ga_dagger,'kJ·mol⁻¹'),m('ΔG‡B',gb_dagger,'kJ·mol⁻¹'),m('Produit cinétique','A' if ka>kb else 'B' if kb>ka else 'égalité'),m('Produit thermodynamique','A' if p['ga']<p['gb'] else 'B' if p['gb']<p['ga'] else 'égalité')],
        [ch('Voies concurrentes irréversibles : formation','t / s','Fraction',se('R',times,reactant),se('A',times,products[0]),se('B',times,products[1])),
         ch('Deux questions : vite formé ou stable ?','T / K','Fraction de A parmi produits',se('Cinétique',temps,kinetic_T),se('Équilibre A ⇌ B',temps,thermo_T)),
         ch('Profils d’énergie libre au T choisi','Coordonnée réactionnelle','G / kJ·mol⁻¹',se('Voie A',xa,ya),se('Voie B',xb,yb))],
        scene('energy','Barrières et niveaux ont des rôles distincts','ΔG‡ fixe les vitesses ; ΔG des produits fixe leur équilibre si une interconversion est possible.',
              x=xa,y=ya,curves=[dict(label='A',x=xa,y=ya),dict(label='B',x=xb,y=yb)],
              states=[dict(x=0,y=0,label='R'),dict(x=1,y=ga_dagger,label='TS A'),dict(x=2,y=p['ga'],label='A'),dict(x=2,y=p['gb'],label='B')]),
        ['Eyring : k=(kBT/h) exp(ΔS‡/R) exp(−ΔH‡/RT), coefficient de transmission κ=1.',
         'Part cinétique A = kA/(kA+kB). Part thermodynamique A = exp(−GA/RT)/[exp(−GA/RT)+exp(−GB/RT)].',
         'L’intégration affichée est irréversible. La composition d’équilibre est une comparaison séparée, atteignable seulement si A et B peuvent s’interconvertir.',
         'L’entropie d’activation peut inverser le classement des vitesses quand on chauffe ; les niveaux finaux sont ici fixés en énergie libre.'],
        ['Deux étapes unimoléculaires concurrentes ; valeurs de ΔH‡, ΔS‡ et G choisies, pas calculées à partir d’une molécule.',
         'G(A) et G(B) fixés sur la plage de T : modèle pédagogique distinct d’une mesure de ΔH et ΔS de réaction. Pas de cinétique de rééquilibration simulée.'],
        rates=[ka,kb],kinetic_shares=kinetic,thermodynamic_shares=thermo,time=times,reactant=reactant,products=products,activation_free_energies=[ga_dagger,gb_dagger])

CALCULATORS={name:globals()[name] for name in ['electrons','acidebase','sn2','sn1','competition','elimination','alcene','alcyne','radical','carbonyle','grignard','oxydoreduction','aromatique','orbitales','cinetique']}

def calculate(lab_id,params):
    return CALCULATORS[lab_id](params)
