"""Structures et bilans des réactions du recueil (p. 524–528).

Les contributeurs mésomères sont des représentations d'une même espèce.
Les bornes stœchiométriques ne sont ni des rendements ni des cinétiques.
L'unique loi temporelle nouvelle est celle de l'E1 : sa constante apparente
et son branchement sont explicitement des données choisies par l'utilisateur.
"""
from __future__ import annotations
import copy
import math
import re
import numpy as np
from commun import (atom, bond, molecule, electron_arrow as arrow, metric as m,
                    chart as ch, series as se, scene, mechanism_scene as ms,
                    reaction_scene as rs)


def result(metrics, charts, drawing, steps, assumptions, **extra):
    return dict(metrics=metrics, charts=charts, scene=drawing, steps=steps,
                assumptions=assumptions, **extra)


def formula_atoms(formula):
    """Formules brutes uniquement : pas de groupes condensés ni de parenthèses."""
    tokens=re.findall(r'([A-Z][a-z]?)(\d*)',formula)
    if ''.join(a+b for a,b in tokens)!=formula:
        raise ValueError('Formule brute non reconnue.')
    counts={}
    for element,number in tokens:
        counts[element]=counts.get(element,0)+int(number or 1)
    return counts


def species(label, formula, charge=0, coefficient=1):
    return dict(label=label, formula=formula, charge=charge, coefficient=coefficient)


def equation(reactants,products):
    """Chaque espèce est donnée explicitement, indépendamment des sommets dessinés."""
    return dict(reactants=reactants,products=products)


def shifted(graph,dx=0,dy=0,prefix=''):
    value=copy.deepcopy(graph)
    for a in value['atoms']:
        a['id']=prefix+str(a['id']);a['x']+=dx;a['y']+=dy
    for b in value['bonds']:
        b['a']=prefix+str(b['a']);b['b']=prefix+str(b['b'])
    for e in value.get('arrows',[]):
        for key in ('start','end','control'):
            e[key]=[e[key][0]+dx,e[key][1]+dy]
    return value


def combine(name,*graphs,arrows=(),caption=''):
    atoms=[];bonds=[];curves=[]
    for graph in graphs:
        atoms.extend(copy.deepcopy(graph['atoms']));bonds.extend(copy.deepcopy(graph['bonds']))
        curves.extend(copy.deepcopy(graph.get('arrows',[])))
    return molecule(name,atoms,bonds,curves+list(arrows),caption=caption)


def ring(prefix='r',cx=0,cy=0,radius=1,aromatic=True):
    atoms=[atom(prefix+str(i),'C',cx+radius*math.cos(i*math.pi/3),
                cy+radius*math.sin(i*math.pi/3),label='CH') for i in range(6)]
    bonds=[bond(prefix+str(i),prefix+str((i+1)%6),2 if aromatic and i%2==0 else 1) for i in range(6)]
    return atoms,bonds


def carbonyl_fragment(prefix='a',x=0,y=0,acyl='acetyl',leaving='Cl',leaving_charge=0,oxygen_charge=0,order=2):
    """R–C(=O)–Z, R entièrement explicité pour le benzoyle."""
    aa=[atom(prefix+'c','C',x,y),atom(prefix+'o','O',x,y+1.05,charge=oxygen_charge)]
    bb=[bond(prefix+'c',prefix+'o',order)]
    if acyl=='acetyl':
        aa.append(atom(prefix+'r','C',x-1.15,y,label='CH₃'));bb.append(bond(prefix+'r',prefix+'c'))
    else:
        ra,rb=ring(prefix+'r',x-2.05,y,radius=.9)
        ra[0]['label']='C';aa+=ra;bb+=rb+[bond(prefix+'r0',prefix+'c')]
    if leaving:
        element='Cl' if leaving=='Cl' else 'N' if leaving.startswith('N') else 'O'
        aa.append(atom(prefix+'z',element,x+1.15,y,label=leaving,charge=leaving_charge));bb.append(bond(prefix+'c',prefix+'z'))
    return molecule('',aa,bb)


def dihedral_free_chain(name,labels,orders=None):
    aa=[atom(str(i),'C',i,.20*(i%2),label=label) for i,label in enumerate(labels)]
    return molecule(name,aa,[bond(str(i),str(i+1),(orders or [1]*(len(labels)-1))[i]) for i in range(len(labels)-1)])


def effect_arene(group,stage):
    """Contributeurs ortho puis para : charges et ordres de liaison explicites."""
    aa,bb=ring()
    aa[0]['label']='C'
    curves=[]
    if group=='alkyl':
        aa.append(atom('s','C',2.05,0,label='CH₃'));bb.append(bond('r0','s'))
        return molecule('Toluène : +I ; hyperconjugaison possible',aa,bb,caption='Un groupe alkyle ne fournit pas le doublet non liant d’un groupe +M classique.')
    if group in ('methoxy','chloro'):
        aa.append(atom('s','O' if group=='methoxy' else 'Cl',2.05,0,charge=1 if stage else 0))
        bb.append(bond('r0','s',2 if stage else 1))
        if group=='methoxy':
            aa.append(atom('m','C',3.0,.5,label='CH₃'));bb.append(bond('s','m'))
        if stage:
            aa[1]['charge']=-1;bb[0]['order']=1
            if stage==2:
                aa[1]['charge']=0;aa[3]['charge']=-1
                bb[1]['order']=2;bb[2]['order']=1
        if stage==0:
            curves=[arrow((2.0,.25),(1.45,.0),(1.65,.65),label='doublet → liaison π'),
                    arrow((.75,.43),(.55,.94),(.95,1.0),label='π → carbone ortho')]
        elif stage==1:
            curves=[arrow((.45,1.02),(.0,.87),(.08,1.4),label='doublet → π'),
                    arrow((-.75,.44),(-1.0,.1),(-1.2,.8),label='π → carbone para')]
        return molecule(('Anisole' if group=='methoxy' else 'Chlorobenzène')+[' : contributeur neutre',' : contributeur ortho',' : contributeur para'][stage],aa,bb,curves,
                        caption='⇄ représente la mésomérie, sans déplacement des noyaux. Ces formes chargées ne sont pas des intermédiaires isolables.')
    aa += [atom('n','N',2.05,0,charge=1),atom('o1','O',2.8,.8,charge=-1 if stage else 0),atom('o2','O',2.8,-.8,charge=-1)]
    bb += [bond('r0','n',2 if stage else 1),bond('n','o1',1 if stage else 2),bond('n','o2')]
    if stage:
        aa[1]['charge']=1;bb[0]['order']=1
        if stage==2:
            aa[1]['charge']=0;aa[3]['charge']=1;bb[1]['order']=2;bb[2]['order']=1
    if stage==0:
        curves=[arrow((.75,.43),(1.5,.0),(1.15,.6),label='π arène → liaison C–N'),
                arrow((2.43,.4),(2.82,.9),(2.9,.15),label='π N=O → O')]
    elif stage==1:
        curves=[arrow((-.75,.44),(.0,.87),(-.5,1.3),label='π → liaison adjacente')]
    return molecule('Nitrobenzène'+[' : contributeur de départ',' : déficit ortho',' : déficit para'][stage],aa,bb,curves,
                    caption='N conserve quatre unités de liaison et la charge +1 ; les deux oxygènes portent −1 dans le contributeur chargé.')


def effects(p):
    system=p['system'];group=p['group'];stage=int(p['stage'])
    inductive={'alkyl':'+I','methoxy':'−I','chloro':'−I','nitro':'−I'}[group]
    mesomeric={'alkyl':'pas de +M par doublet','methoxy':'+M','chloro':'+M','nitro':'−M'}[group]
    if system=='inductive':
        lab={'alkyl':('C','CH₃δ⁺'),'methoxy':('O','Oδ⁻'),'chloro':('Cl','Clδ⁻'),'nitro':('N','NO₂δ⁻')}[group]
        sign='δ⁻' if group=='alkyl' else 'δ⁺'
        aa=[atom('s',lab[0],0,0,label=lab[1]),atom('c1','C',1.2,.2,label='CH₂'+sign),
            atom('c2','C',2.4,0,label='CH₂'),atom('c3','C',3.6,.2,label='CH₃')]
        bb=[bond('s','c1'),bond('c1','c2'),bond('c2','c3')]
        if group=='methoxy': aa.append(atom('m','C',-.9,.5,label='CH₃'));bb.append(bond('m','s'))
        drawing=ms('Polarisation transmise par les liaisons σ','δ désigne une charge partielle qualitative ; aucune charge formelle n’est créée.',
                   [molecule('Groupe et chaîne : '+inductive,aa,bb,caption='L’effet inductif s’atténue avec la distance. Le curseur ne représente pas une réaction.')],0)
        rule='Polarisation σ : '+inductive+' ; ce groupe présente '+mesomeric+' seulement si un système π adapté est conjugué.'
        metrics=[m('Effet inductif',inductive),m('Effet mésomère possible',mesomeric),m('Charge formelle de la molécule',0,'e')]
        notes=['Les lettres δ ne sont pas des charges entières. Le signe I caractérise le sens de polarisation relativement au carbone.',
               'La mésomérie exige un recouvrement orbital : un groupe OCH₃ séparé de l’arène par CH₂ ne délocalise pas son doublet jusqu’à l’arène.']
        extra=dict(inductive=inductive,mesomeric=mesomeric,formal_charge=0)
    elif system=='mesomeric':
        frames=[effect_arene(group,i) for i in range(3)]
        drawing=ms('Relier I, M et orientation','Même connectivité dans tous les contributeurs ; ⇄ est une relation de représentation.',frames,stage)
        orientation='ortho/para' if group!='nitro' else 'méta'
        rule=f'{inductive} ; {mesomeric} ; orientation SEA généralement {orientation}.'
        metrics=[m('Effet I',inductive),m('Effet M',mesomeric),m('Orientation SEA usuelle',orientation),
                 m('Activation globale','désactivant' if group in ('chloro','nitro') else 'activant')]
        notes=['Une charge dans un contributeur rend visible une délocalisation ; elle n’est pas la charge partielle réelle de ce carbone.',
               'Le chlore cumule −I et +M : l’arène est désactivé mais orienté ortho/para. Confondre orientation et activation conduit à une mauvaise prédiction.',
               'Le méthyle est +I ; son activation et son orientation impliquent aussi l’hyperconjugaison, distincte du doublet d’un donneur +M.']
        extra=dict(inductive=inductive,mesomeric=mesomeric,orientation=orientation)
    elif system=='markovnikov':
        alternative=p['conditions']=='alternative'
        aa=[atom('c0','C',0,0,label='CH₂'),atom('c1','C',1.2,.2,label='CH'),atom('c2','C',2.4,0,label='CH₂'),atom('c3','C',3.6,.2,label='CH₃')]
        bb=[bond('c0','c1',2),bond('c1','c2'),bond('c2','c3')]
        start=molecule('But-1-ène : double liaison dissymétrique',aa,bb)
        if not alternative:
            start=molecule('But-1-ène + HBr : protoner C=C',copy.deepcopy(aa)+[atom('h','H',-.7,-1),atom('br','Br',-1.9,-1)],
                           copy.deepcopy(bb)+[bond('h','br')],
                           [arrow((.6,.1),(-.7,-1),(-.5,.1),label='π → H'),arrow((-1.3,-1),(-1.9,-.9),(-1.7,-.3),label='H–Br → Br⁻')])
            a1=copy.deepcopy(aa);a1[0]['label']='CH₂';a1[1]['charge']=1
            a1 += [atom('h','H',-.7,-.7),atom('br','Br',1.2,-1.3,charge=-1)]
            b1=[bond('c0','c1'),bond('c1','c2'),bond('c2','c3'),bond('c0','h')]
            middle=molecule('Carbocation secondaire + Br⁻',a1,b1,[arrow((1.3,-1.1),(1.2,.2),(2.2,-.3),label='doublet Br⁻ → C⁺')])
            a2=copy.deepcopy(a1);a2[1]['charge']=0;a2[-1]['charge']=0
            last=molecule('2-bromobutane : produit de Markovnikov',a2,b1+[bond('c1','br')])
            product='2-bromobutane';rule='HBr sans peroxydes : H sur C1, Br sur C2 via le carbocation secondaire.'
        else:
            start['atoms']=copy.deepcopy(aa)+[atom('b','B',-.7,-1,label='BH₃')]
            a1=copy.deepcopy(aa);a1[0]['label']='CH₂';a1[1]['label']='CH₂'
            a1.append(atom('b','B',-.9,-.6,label='BH₂'));b1=[bond('c0','c1'),bond('c1','c2'),bond('c2','c3'),bond('c0','b')]
            middle=molecule('Première hydroboration : C1–B ; addition concertée syn',a1,b1,
                            caption='Un alkylborane partiel est schématisé ; BH₃ peut hydroborer trois alcènes, selon la stœchiométrie.')
            a2=copy.deepcopy(a1);a2[-1].update(id='b',element='O',label='OH')
            last=molecule('Butan-1-ol après H₂O₂ / HO⁻',a2,b1,
                          caption='C–B devient C–O avec conservation de la configuration ; sous-produits borés non représentés.')
            product='butan-1-ol';rule='Hydroboration puis oxydation : régiosélectivité anti-Markovnikov et addition syn, sans carbocation libre.'
        drawing=ms('Une règle dépend du mécanisme',rule,[start,middle,last],stage)
        metrics=[m('Produit attendu',product),m('Régiochimie','anti-Markovnikov' if alternative else 'Markovnikov'),m('Carbocation libre',not alternative)]
        notes=[rule,'Le but-1-ène possède deux carbones différents dans C=C. L’intermédiaire secondaire explique l’orientation de HBr ; cette justification ne s’applique pas à la hydroboration.']
        extra=dict(product_name=product,carbocation=not alternative)
    else:
        alternative=p['conditions']=='alternative'
        if alternative:
            aa=[atom('c0','C',0,0,label='CH₂'),atom('c1','C',1.2,.2,label='CH'),atom('c2','C',2.4,0,label='CH₂'),atom('c3','C',3.6,.2,label='CH₂'),atom('c4','C',4.8,0,label='CH₃'),
                atom('h','H',0,1),atom('br','Br',1.2,-.9),atom('o','O',-1.4,1,label='tBuO',charge=-1)]
            bb=[bond('c0','c1'),bond('c1','c2'),bond('c2','c3'),bond('c3','c4'),bond('c0','h'),bond('c1','br')]
            graph=molecule('2-bromopentane : Hβ anti au Br',aa,bb,[arrow((-1.25,1),(0,1),(-.6,1.7),label='base → Hβ'),
                arrow((0,.5),(.6,.1),(.25,-.4),label='C–H → π'),arrow((1.2,-.4),(1.2,-1),(1.9,-.5),label='C–Br → Br⁻')],
                caption='Base encombrée : possibilité de favoriser l’alcène moins substitué ; la géométrie anti doit être réalisable.')
            prod=dihedral_free_chain('Pent-1-ène : branche moins substituée',['CH₂','CH','CH₂','CH₂','CH₃'],[2,1,1,1])
            frames=[graph,graph,prod];product='pent-1-ène : favorisation possible';rule='Base encombrée et groupe partant Br : la compétition peut privilégier le Hβ le plus accessible.'
        else:
            frames=e1_frames('secondary');product='pent-2-ène (E/Z) : usuellement majoritaire';rule='Déshydratation acide du pentan-2-ol : Zaïtsev favorise généralement l’alcène plus substitué.'
        drawing=ms('Zaïtsev n’est pas une loi sans conditions',rule,frames,min(stage,len(frames)-1))
        metrics=[m('Branche mise en avant',product),m('Mécanisme','E2' if alternative else 'E1'),m('Condition discriminante','base encombrée / halogénure' if alternative else 'alcool / acidité / chauffage')]
        notes=[rule,'Changer d’alcool acide en halogénure avec base change le groupe partant et le mécanisme. HO⁻ est un mauvais groupe partant : on ne déshydrate pas l’alcool par une simple E2 avec tBuO⁻.',
               'La règle de Zaïtsev prédit une tendance ; un rapport numérique demande des données de cinétique, de température et de conformation.']
        extra=dict(mechanism='E2' if alternative else 'E1',product_name=product)
    return result(metrics,[],drawing,[rule]+notes,
        ['Structures semi-développées : les groupes CH₂/CH₃ contiennent leurs H implicites.',
         'Les commandes « groupe » concernent I/M ; les commandes « conditions » concernent les règles. Aucune distribution numérique universelle n’est attribuée.'],**extra)


def e1_source_frames():
    """Exercice p. 531/533 : C5H11Cl + H2O, charge totale zéro."""
    aa=[atom('c0','C',0,0,label='CH₃'),atom('c1','C',1.1,.18,label='CH'),
        atom('c2','C',2.2,0,label='CH'),atom('c3','C',3.3,.18,label='CH₃'),
        atom('c4','C',2.2,1.15,label='CH₃'),atom('cl','Cl',1.1,-.9),
        atom('w','O',0,-1.8,label='H₂O')]
    bb=[bond('c0','c1'),bond('c1','c2'),bond('c2','c3'),bond('c2','c4'),bond('c1','cl')]
    f0=molecule('1. 2-chloro-3-méthylbutane : départ de Cl⁻',copy.deepcopy(aa),copy.deepcopy(bb),
                [arrow((1.1,-.36),(1.1,-1.0),(1.8,-.5),label='C–Cl → Cl⁻')],
                caption='Milieu ionisant approprié : le doublet C–Cl part avec Cl. Aucune protonation préalable de l’halogénure n’est requise.')
    a1=copy.deepcopy(aa);b1=[b for b in copy.deepcopy(bb) if not {b['a'],b['b']}=={'c1','cl'}]
    a1[1]['charge']=1;a1[5].update(x=-1.2,y=-.9,charge=-1)
    f1=molecule('2. Carbocation secondaire + Cl⁻',copy.deepcopy(a1),copy.deepcopy(b1),
                caption='Une rotation et une migration 1,2 peuvent être discutées ; cette banque suit les deux éliminations directes, sans imposer de migration.')
    a2=copy.deepcopy(a1);a2[2]['label']='C';a2.append(atom('hb','H',3.15,-.85));b2=copy.deepcopy(b1)+[bond('c2','hb')]
    f2=molecule('3. Hβ sur C3 : former l’alcène plus substitué',a2,b2,
                [arrow((.12,-1.7),(3.15,-.85),(1.75,-2.1),label='H₂O → Hβ'),
                 arrow((2.675,-.425),(1.65,.1),(2.0,-.9),label='Cβ–H → π')],
                caption='L’autre Hβ est porté par le CH₃ de C1 et donnerait 3-méthylbut-1-ène. La branche représentée donne 2-méthylbut-2-ène.')
    a3=copy.deepcopy(a2);a3[1]['charge']=0;a3[6]['charge']=1;a3[-1].update(x=.8,y=-1.8)
    b3=[b for b in copy.deepcopy(b1)] + [bond('w','hb')]
    for b in b3:
        if {b['a'],b['b']}=={'c1','c2'}:b['order']=2
    f3=molecule('4. 2-méthylbut-2-ène + H₃O⁺ + Cl⁻',a3,b3,
                caption='Le carbone portant deux CH₃ ne permet pas E/Z sur cet alcène. H₂O devenue H₃O⁺ et Cl⁻ conservent la charge globale zéro.')
    return [f0,f1,f2,f3]


def e1_frames(substrate):
    """Acide catalytique inclus : chaque image conserve C5 H15 O2 et +1."""
    if substrate=='source':return e1_source_frames()
    primary=substrate=='primary';tertiary=substrate=='tertiary'
    alcohol_c=0 if primary else 1
    labels=['CH₂','CH₂','CH₂','CH₂','CH₃'] if primary else ['CH₃','C' if tertiary else 'CH','CH₂','CH₃' if tertiary else 'CH₂']+([] if tertiary else ['CH₃'])
    # Tertiaire : chaîne de quatre C plus un CH3 branché (c4).
    aa=[atom(f'c{i}','C',i*1.1,.18*(i%2),label=label) for i,label in enumerate(labels)]
    bb=[bond(f'c{i}',f'c{i+1}') for i in range(len(labels)-1)]
    if tertiary:
        aa.append(atom('c4','C',1.1,1.2,label='CH₃'));bb.append(bond('c1','c4'))
    x=alcohol_c*1.1;y=.18*(alcohol_c%2)
    aa += [atom('o','O',x,y-1,label='OH'),atom('w','O',x-1.3,y-1.8,label='H₃O',charge=1)]
    bb += [bond(f'c{alcohol_c}','o')]
    f0=molecule('1. Protoner l’alcool',aa,bb,[arrow((x+.12,y-1),(x-1.1,y-1.7),(x+.1,y-1.9),label='doublet O → H⁺')],caption='H₃O⁺ donne un proton et devient H₂O. Le doublet de l’alcool reste sur O.')
    a1=copy.deepcopy(aa);a1[-2].update(label='OH₂',charge=1);a1[-1].update(label='H₂O',charge=0)
    f1=molecule('2. Départ de H₂O : rupture C–O',a1,bb,[arrow((x,y-.5),(x,y-1.1),(x+.65,y-.8),label='C–O → O')])
    a2=copy.deepcopy(a1);a2[alcohol_c]['charge']=1;a2[alcohol_c]['label']='C' if tertiary else 'CH'
    a2[-2].update(label='H₂O',charge=0)
    b2=[b for b in bb if not (b['a']==f'c{alcohol_c}' and b['b']=='o')]
    f2=molecule('3. Carbocation ; choisir un H en β',a2,b2,
                [arrow((x,y-1.0),(x+1.1,y+.45),(x+1.3,y-.55),label='H₂O prélève Hβ'),
                 arrow((x+1.1,y+.3),(x+.55,y),(x+.55,y+.8),label='Cβ–H → liaison π')],
                caption='Un hydrogène β est implicite sur le groupe CH₂ ; les deux flèches créent C=C et régénèrent H₃O⁺.')
    a3=copy.deepcopy(a2);a3[alcohol_c]['charge']=0
    a3[2]['label']='CH';a3[-2].update(label='H₃O',charge=1)
    b3=copy.deepcopy(b2)
    for b in b3:
        if b['a']=='c1' and b['b']=='c2':b['order']=2
    f3=molecule('4. Alcène plus substitué + H₂O ; acide régénéré',a3,b3,
                caption='Pent-2-ène E/Z ou 2-méthylbut-2-ène ; le dessin de chaîne ne choisit pas une proportion E/Z.')
    # Le proton catalytique est visible : les flèches partent d'un doublet
    # ou d'une liaison et aboutissent au H réellement transféré.
    for index,f in enumerate([f0,f1,f2,f3]):
        f['bonds']=copy.deepcopy(f['bonds'])
        acid_h=(x-.45,y-1.8) if index==0 else (x,y-1.7)
        f['atoms'].append(atom('ha','H',*acid_h))
        f['bonds'].append(bond('w' if index==0 else 'o','ha'))
        for a in f['atoms']:
            if a['id']=='w' and index==0:a['label']='OH₂'
            if a['id']=='o' and index>=1:a['label']='OH'
    f0['arrows']=[arrow((x+.12,y-1),(x-.45,y-1.8),(x+.15,y-1.9),label='O alcool → H'),
                  arrow((x-.875,y-1.8),(x-1.3,y-1.7),(x-1.15,y-1.2),label='O–H acide → O')]
    if not primary:
        beta_x=2.2;beta_y=.9
        for f in [f2,f3]:
            f['atoms'].append(atom('hb','H',beta_x if f is f2 else x+.75,beta_y if f is f2 else y-1.4))
            f['bonds'].append(bond('c2' if f is f2 else 'o','hb'))
            if f is f2:
                for a in f['atoms']:
                    if a['id']=='c2':a['label']='CH'
        f2['arrows']=[arrow((x+.15,y-1),(beta_x,beta_y),(x+1.75,y-.6),label='H₂O → Hβ'),
                      arrow((beta_x,beta_y/2),(x+.55,y),(x+.6,y+.85),label='Cβ–H → π')]
    if primary:
        f0['name']='Pentan-1-ol : E1 classique non retenue'
        f0['arrows']=[]
        f0['caption']='Pas de carbocation primaire libre dans le modèle. Une déshydratation primaire peut suivre une voie concertée sous conditions adaptées.'
        return [f0]
    return [f0,f1,f2,f3]


def e1(p):
    source=p['substrate']=='source';allowed=p['substrate']!='primary';k=float(p['k_ion']) if allowed else 0.;z=float(p['branch_z'])/100
    t=np.linspace(0,float(p['time']),241);remaining=np.exp(-k*t);total=1-remaining
    names=['2-méthylbut-2-ène','3-méthylbut-1-ène'] if source else ['pent-2-ène (E/Z)','pent-1-ène'] if p['substrate']!='tertiary' else ['2-méthylbut-2-ène','2-méthylbut-1-ène']
    frames=e1_frames(p['substrate'])
    eq=equation([species('2-Chloro-3-méthylbutane','C5H11Cl'),species('Eau','H2O')],
                [species('Alcènes','C5H10'),species('Hydronium','H3O',1),species('Chlorure','Cl',-1)]) if source else \
       equation([species('Alcool','C5H12O')],[species('Alcènes','C5H10'),species('Eau','H2O')])
    text='Carbocation secondaire/tertiaire admissible ; la déprotonation β suit le départ d’eau.' if allowed else 'L’E1 via un carbocation primaire isolé est exclue ; le modèle laisse l’alcool inchangé.'
    return result([m('E1 dans le modèle',allowed),m('Conversion calculée',100*total[-1],'%'),m('Ionisation apparente choisie',k,'s⁻¹'),
        m('Branchement choisi vers le plus substitué',p['branch_z'],'%'),m(names[0],total[-1]*z,'équiv.'),m(names[1],total[-1]*(1-z),'équiv.'),m('Acide','H₃O⁺ formé au bilan' if source else 'catalytique, régénéré')],
        [ch('Une ionisation, deux branches déclarées','t / s','Quantité / quantité initiale',se('Alcool',t,remaining),se(names[0],t,total*z),se(names[1],t,total*(1-z)))],
        ms('Deux événements distincts : départ, puis Hβ',text,frames,min(int(p['stage']),len(frames)-1)),
        [text,'Le chlorure de l’exercice se sépare en Cl⁻ ; la rupture C–Cl est hétérolytique et le carbone devient secondaire cationique.' if source else 'La protonation transforme OH en H₂O, groupe partant convenable. La rupture C–O est hétérolytique : O garde le doublet.',
         'Le carbocation possède une orbitale p vacante. H₂O prélève ensuite un Hβ ; le doublet C–H forme C=C.',
         'Le modèle réduit les étapes rapides et utilise A(t)/A₀ = exp(−k₍ion₎t). k₍ion₎ dépendrait du solvant, de la température et, pour l’alcool, de l’acidité.',
         'Le réglage de branchement est une donnée d’expérience fictive déclarée, pas une prédiction de Zaïtsev. '+('Les deux alcènes du cas source sont des isomères de constitution ; aucun E/Z ne s’applique au plus substitué.' if source else 'Les pent-2-ènes E et Z sont regroupés.')],
        ['Milieu ionisant approprié ; la solvolyse concurrente et les migrations 1,2 ne sont pas intégrées dans la banque des éliminations directes.' if source else 'Milieu acide chauffé ; la solvolyse concurrente et les réarrangements ne sont pas intégrés dans ce modèle isolé.',
         'La vitesse lente d’ionisation est assimilée à une loi de premier ordre apparente ; les intermédiaires ne sont pas quantifiés.',
         'Chaque image conserve C₅H₁₃ClO et la charge totale zéro.' if source else 'Chaque image inclut le catalyseur : C₅H₁₅O₂⁺ est conservé, avec une charge totale +1.'],
        allowed=allowed,time=t,remaining=remaining,total_alkene=total,product_z=total*z,product_h=total*(1-z),reaction=eq,
        frame_inventory=[dict(formula='C5H13ClO' if source else 'C5H15O2',charge=0 if source else 1) for _ in frames],substrate=p['substrate'])


def enolate_graph(donor,site,form,electrophile,product=False,arrows_on=False):
    """C/O constituent des nucléophiles différents sur la même connectivité initiale."""
    malonate=donor=='malonate'
    # O-forme : CH2=C(O−)CH3, ou EtO–C(O−)=CH–COOEt.
    o_form=site=='O' if product else form=='O'
    aa=[atom('alpha','C',0,0,label='CH' if malonate else 'CH₂',charge=-1 if not o_form and not product else 0),
        atom('acyl','C',1.15,.2),atom('o','O',1.15,1.3,charge=-1 if o_form and not product else 0),
        atom('r','O' if malonate else 'C',2.3,.2,label='OEt' if malonate else 'CH₃')]
    bb=[bond('alpha','acyl',2 if o_form else 1),bond('acyl','o',1 if o_form else 2),bond('acyl','r')]
    if malonate:
        aa+=[atom('acyl2','C',-1.15,.2),atom('o2','O',-1.15,1.3),atom('r2','O',-2.3,.2,label='OEt')]
        bb+=[bond('alpha','acyl2'),bond('acyl2','o2',2),bond('acyl2','r2')]
    alkyl={'methyl':'CH₃','ethyl':'CH₂CH₃','tertbutyl':'C(CH₃)₃'}[electrophile]
    point=(1.15,1.3) if site=='O' else (0,0)
    aa.append(atom('e','C',point[0]+.8 if product else point[0]+.3,point[1]-1.4 if product else point[1]-2.2,label=alkyl))
    aa.append(atom('br','Br',point[0]+1.8 if product else point[0]+1.4,point[1]-1.4 if product else point[1]-2.2,charge=-1 if product else 0))
    if product:bb.append(bond('o' if site=='O' else 'alpha','e'))
    else:bb.append(bond('e','br'))
    curves=[]
    if arrows_on:
        curves=[arrow((point[0]+.05,point[1]+.1),(point[0]+.3,point[1]-2.1),(point[0]-.9,point[1]-1),label=('Cα' if site=='C' else 'O')+' → C de RX'),
                arrow((point[0]+.85,point[1]-2.2),(point[0]+1.4,point[1]-2.05),(point[0]+1.4,point[1]-1.5),label='C–Br → Br⁻')]
    name=('Malonate' if malonate else 'Propanone')+(' : produit alkylé en '+site if product else ' : contributeur '+('O⁻' if o_form else 'Cα⁻'))
    return molecule(name,aa,bb,curves,caption='Groupes OEt = OCH₂CH₃. C-alkylation et O-alkylation donnent des connectivités différentes, pas deux contributeurs mésomères.')


def enolatealkyl(p):
    donor=p['donor'];site=p['site'];electrophile=p['electrophile'];allowed=electrophile!='tertbutyl'
    x=min(1.,float(p['equivalents'])) if allowed else 0.
    opposite='O' if site=='C' else 'C'
    frames=[enolate_graph(donor,site,opposite,electrophile),enolate_graph(donor,site,site,electrophile,arrows_on=allowed)]
    if opposite=='O':
        frames[0]['arrows']=[arrow((1.15,1.4),(1.15,.7),(.55,1.1),label='doublet O⁻ → π'),
                             arrow((.575,.1),(0,.1),(.2,.8),label='π → Cα')]
    else:
        frames[0]['arrows']=[arrow((0,.1),(.575,.1),(.35,-.55),label='doublet Cα → π'),
                             arrow((1.15,.75),(1.2,1.4),(1.75,1.1),label='π → O')]
    if allowed:frames.append(enolate_graph(donor,site,site,electrophile,product=True))
    else:
        frames[1]['name']='SN2 interdite au carbone tertiaire : discuter E2'
        frames[1]['caption']='L’énolate est aussi une base ; un Hβ et un groupe partant sont présents sur tBuBr. La voie E2 n’est pas intégrée au bilan SN2.'
    carbon_count=1 if electrophile=='methyl' else 2 if electrophile=='ethyl' else 4
    donor_formula='C7H11O4' if donor=='malonate' else 'C3H5O'
    rx_formula={1:'CH3Br',2:'C2H5Br',4:'C4H9Br'}[carbon_count]
    product_formula=('C'+str(7+carbon_count)+'H'+str(11+2*carbon_count+1)+'O4') if donor=='malonate' else ('C'+str(3+carbon_count)+'H'+str(5+2*carbon_count+1)+'O')
    product_name=('Malonate de diéthyle α-'+('méthylé' if electrophile=='methyl' else 'éthylé')) if donor=='malonate' and site=='C' else \
        ('butan-2-one' if electrophile=='methyl' else 'pentan-2-one') if site=='C' else 'Éther d’énol / cétène-acétal de voie O'
    ratios=np.linspace(0,2,101);bounds=np.minimum(1,ratios) if allowed else np.zeros_like(ratios)
    eq=equation([species('Énolate',donor_formula,-1),species('RX',rx_formula)],
                [species('Produit alkylé',product_formula),species('Bromure','Br',-1)])
    return result([m('Voie SN2',allowed),m('Site sélectionné',site),m('Produit de la voie choisie',product_name if allowed else 'aucun produit SN2'),
        m('Borne de produit SN2',x,'équiv.'),m('Énolate non consommé',1-x,'équiv.'),m('RX non consommé',p['equivalents']-x,'équiv.'),m('Charge globale',-1,'e')],
        [ch('Stœchiométrie 1 énolate + 1 RX','RX / énolate initial','Borne de produit / énolate initial',se('Voie SN2 sélectionnée',ratios,bounds))],
        ms('Contributeur, nucléophile et carbone électrophile','Un centre tertiaire bloque la SN2 ; le contre-ion alcalin de l’énolate est spectateur.',frames,min(int(p['stage']),len(frames)-1)),
        ['L’énolate possède deux contributeurs utiles : charge portée par O ou par Cα. Le nucléophile est une seule espèce délocalisée.',
         'Voie C : le doublet de Cα forme C–C et C–Br cède son doublet à Br. Voie O : une liaison O–C forme un éther d’énol.',
         'Un RX méthylique ou primaire est compatible avec cette SN2. Sur tBuBr, la SN2 classique est exclue ; une élimination E2 peut concurrencer.',
         'La courbe donne seulement min(n₀ énolate, n₀ RX), sous hypothèse d’achèvement de la voie isolée. Les conditions C/O ne sont pas prédites par cette borne.'],
        ['Énolate préparé auparavant ; contre-ion et solvant non représentés, monoalkylation isolée.',
         'La commande C/O impose une voie à comparer : solvant, métal, température et réactif gouvernent expérimentalement leur compétition.',
         'L’excès de RX peut produire d’autres réactions sur un composé encore énolisable ; elles sont exclues, donc la borne est celle de la monoalkylation.'],
        allowed=allowed,extent=x,site=site,product_name=product_name,product_formula=product_formula,reaction=eq)


def ammonium_frame(amine,electrophile,product=False,arrows_on=False):
    ethyl=amine=='triethyl';benzyl=electrophile=='benzyl'
    aa=[atom('n','N',0,0,charge=1 if product else 0)]
    bb=[]
    for i,(x,y) in enumerate([(-1.1,.8),(-1.1,-.8),(0,1.2)]):
        aa.append(atom('a'+str(i),'C',x,y,label='CH₂CH₃' if ethyl else 'CH₃'));bb.append(bond('n','a'+str(i)))
    aa += [atom('e','C',1.3 if product else 2.1,0,label='CH₂' if benzyl else 'CH₃'),
           atom('br','Br',3.6,0,charge=-1 if product else 0)]
    if benzyl:
        ra,rb=ring('r',3.05 if product else 3.85,-1.35,.75);ra[2]['label']='C'
        aa+=ra;bb+=rb+[bond('e','r2')]
    if product:bb.append(bond('n','e'))
    else:bb.append(bond('e','br'))
    curves=[arrow((.1,-.1),(2.05,0),(1.0,-1.1),label='doublet N → C'),
            arrow((2.85,0),(3.6,.15),(3.25,.7),label='C–Br → Br⁻')] if arrows_on else []
    return molecule('Sel d’ammonium quaternaire' if product else 'Amine tertiaire et RX : '+('flèches concertées SN2' if arrows_on else 'repérer N et C–Br'),aa,bb,curves,
                    caption='N possède trois liaisons et un doublet avant réaction ; quatre liaisons et la charge +1 après. Br⁻ est toujours visible.')


def aminealkyl(p):
    ethyl=p['amine']=='triethyl';benzyl=p['electrophile']=='benzyl';q=float(p['equivalents']);x=min(1,q)
    amine_formula='C6H15N' if ethyl else 'C3H9N';rx_formula='C7H7Br' if benzyl else 'CH3Br'
    c=(6 if ethyl else 3)+(7 if benzyl else 1);h=(15 if ethyl else 9)+(7 if benzyl else 3)
    product_formula=f'C{c}H{h}N'
    frames=[ammonium_frame(p['amine'],p['electrophile']),ammonium_frame(p['amine'],p['electrophile'],arrows_on=True),ammonium_frame(p['amine'],p['electrophile'],product=True)]
    ratios=np.linspace(0,3,121)
    eq=equation([species('Amine tertiaire',amine_formula),species('Bromure organique',rx_formula)],
                [species('Ammonium quaternaire',product_formula,1),species('Bromure','Br',-1)])
    return result([m('Liaisons de N avant / après','3 / 4'),m('Charge de l’azote final',1,'e'),m('Charge du sel total',0,'e'),
        m('Borne de sel formé',x,'équiv.'),m('Amine tertiaire restante',1-x,'équiv.'),m('RX restant',q-x,'équiv.'),m('Cinquième alkylation','aucun doublet sur N⁺')],
        [ch('Quaternisation : consommation 1:1','RX / amine tertiaire initiale','Borne de sel / amine initiale',se('Sel ammonium',ratios,np.minimum(1,ratios)),se('RX non consommé',ratios,np.maximum(0,ratios-1)))],
        ms('Former N–C sans perdre le contre-ion','Les deux flèches appartiennent à une même substitution concertée ; la vue intermédiaire expose leur trajet, sans créer un intermédiaire de SN2.',frames,int(p['stage'])),
        ['N donne son doublet au carbone portant Br ; la liaison C–Br cède un doublet à Br. L’électrophile méthylique ou benzylique est compatible avec la SN2.',
         'Le produit possède quatre substituants et la charge +1 sur N. Br⁻ compense cette charge : le sel total est neutre.',
         'L’amine tertiaire initiale ne comporte pas N–H. Il n’y a donc pas de déprotonation qui donnerait une amine neutre après la quaternisation.',
         'Au-delà d’un équivalent RX, N⁺ n’a plus de doublet à fournir. La courbe est une borne stœchiométrique, pas un rendement mesuré.'],
        ['Réaction de Menshutkin isolée ; absence de voie concurrente et de problème de solubilité dans le bilan maximal.',
         'Les amines primaires et secondaires peuvent s’alkyler plusieurs fois ; ce laboratoire choisit une amine tertiaire pour rendre une seule quaternisation non ambiguë.'],
        extent=x,nitrogen_initial_charge=0,nitrogen_final_charge=1,nitrogen_final_bonds=4,product_formula=product_formula,reaction=eq)


def anhydride_graph(acyl='acetyl',product=False,tetra=False,variant='formation',acidtrap='secondamine'):
    """Une substitution acyle complète, avec les fragments et charges conservés."""
    if variant=='chloridealcohol':
        left=carbonyl_fragment('a',0,0,acyl,'Cl')
        aa=left['atoms']+[atom('nu','O',0,-1.5,label='HOEt')];bb=left['bonds']
        if not tetra and not product:
            return molecule('Chlorure d’acyle + éthanol',aa,bb,[arrow((.1,-1.35),(0,0),(-.8,-.55),label='O de EtOH → C acyle'),arrow((0,.5),(.1,1.15),(-.5,.9),label='π → O')],caption='Le chlorure d’acyle est activé ; l’alcool neutre donne son doublet, puis le carbonyle se reforme.')
        bb.append(bond('ac','nu'))
        for a in aa:
            if a['id']=='ao':a['charge']=-1 if tetra else 0
            if a['id']=='nu':a.update(label='HOEt' if tetra else 'OEt',charge=1 if tetra else 0)
            if a['id']=='az' and product:a.update(label='HCl',x=2.2,y=-1.0)
        for b in bb:
            if b['a']=='ac' and b['b']=='ao':b['order']=1 if tetra else 2
        if product:bb=[b for b in bb if not (b['a']=='ac' and b['b']=='az')]
        return molecule('Intermédiaire tétraédrique zwitterionique' if tetra else 'Ester + HCl',aa,bb,
                        [arrow((0,1.15),(0,.5),(-.65,.9),label='O⁻ reforme π'),arrow((.6,0),(1.2,.1),(.9,.8),label='C–Cl → Cl⁻')] if tetra else [],
                        caption='Le départ de Cl⁻ et la déprotonation de OEtH⁺ livrent l’ester. HCl est un coproduct, souvent capté par une base dans la synthèse réelle.')
    if variant=='formation':
        left=carbonyl_fragment('a',0,0,acyl,'Cl')
        right=carbonyl_fragment('b',4.0,0,acyl,'O',leaving_charge=-1)
        for a in right['atoms']:a['x']=8.0-a['x']
        if not tetra and not product:
            return combine('Chlorure d’acyle + carboxylate',left,right,
                arrows=[arrow((2.9,.15),(0,.05),(1.4,-1.4),label='O⁻ → C acyle'),
                        arrow((0,.5),(.1,1.15),(-.5,.95),label='π C=O → O')],
                caption='L’oxygène chargé du carboxylate porte le doublet nucléophile ; le carbone du chlorure d’acyle est l’électrophile.')
        aa=left['atoms']+right['atoms'];bb=left['bonds']+right['bonds']
        for a in aa:
            if a['id']=='bz':a['charge']=0;a['x']=1.4;a['y']=-.65
        # Le second fragment se rapproche sans changer sa connectivité.
        for a in aa:
            if a['id'].startswith('b') and a['id']!='bz':a['x']-=.8;a['y']-=.65
        bb.append(bond('ac','bz'))
        for a in aa:
            if a['id']=='ao':a['charge']=-1 if tetra else 0
            if a['id']=='az' and product:a.update(x=-1.0,y=-1.7,charge=-1)
        for b in bb:
            if b['a']=='ac' and b['b']=='ao':b['order']=1 if tetra else 2
        if product:bb=[b for b in bb if not (b['a']=='ac' and b['b']=='az')]
        curves=[arrow((.0,1.2),(0,.45),(-.7,.8),label='O⁻ reforme C=O'),
                arrow((.6,0),(1.2,.1),(.95,.8),label='C–Cl → Cl⁻')] if tetra else []
        return molecule('Intermédiaire tétraédrique' if tetra else 'Anhydride + Cl⁻',aa,bb,curves,
                        caption='Le pont est C(=O)–O–C(=O). La charge négative quitte O pour Cl lors de l’élimination.')
    # Anhydride symétrique initial : linker O, deux carbonyles et R explicites.
    left=carbonyl_fragment('a',0,0,acyl,None)
    right=carbonyl_fragment('b',4.0,0,acyl,None)
    # Retournement du second fragment : R est à droite et le pont est entre les acyles.
    for a in right['atoms']:a['x']=8.0-a['x']
    for a in right['atoms']:a['x']-=4.0
    bridge=atom('bridge','O',2.0,0)
    aa=left['atoms']+right['atoms']+[bridge];bb=left['bonds']+right['bonds']+[bond('ac','bridge'),bond('bridge','bc')]
    if variant=='hydrolysis':nu_label='H₂O';nu_element='O';product_label='OH';extra_label='OH'
    elif variant=='alcoholysis':nu_label='HOEt';nu_element='O';product_label='OEt';extra_label='OH'
    else:nu_label='H₂NEt';nu_element='N';product_label='NHEt';extra_label='O'
    aa.append(atom('nu',nu_element,0,-1.4,label=nu_label))
    if variant=='amidation':aa.append(atom('base','N',-1.8,-2.0,label='H₂NEt' if acidtrap=='secondamine' else 'NEt₃'))
    if not tetra and not product:
        return molecule('Anhydride + '+nu_label+(' ; base présente' if variant=='amidation' else ''),aa,bb,
            [arrow((.15,-1.3),(0,0),(-.8,-.7),label='doublet Nu → C'),arrow((0,.55),(.1,1.15),(-.5,.8),label='π → O')],
            caption='L’eau, l’alcool ou l’amine neutre donne un doublet. Les transferts de proton déterminent les espèces finales.')
    bb.append(bond('ac','nu'))
    for a in aa:
        if a['id']=='nu':a.update(label=nu_label if tetra else product_label,charge=1 if tetra else 0)
        if a['id']=='ao':a['charge']=-1 if tetra else 0
    for b in bb:
        if b['a']=='ac' and b['b']=='ao':b['order']=1 if tetra else 2
    if product:
        bb=[b for b in bb if not (b['a']=='ac' and b['b']=='bridge')]
        for a in aa:
            if a['id']=='bridge':a.update(x=2.8,y=-.5,label=extra_label,charge=-1 if variant=='amidation' else 0)
            if a['id']=='base':a.update(label='H₃NEt' if acidtrap=='secondamine' else 'HNEt₃',charge=1)
    curves=[arrow((.05,1.15),(0,.5),(-.6,.9),label='O⁻ → π'),arrow((1,0),(2,.15),(1.55,.8),label='liaison acyle–O → O')] if tetra else []
    return molecule('Intermédiaire tétraédrique zwitterionique' if tetra else {'hydrolysis':'Deux acides carboxyliques','alcoholysis':'Ester + acide carboxylique','amidation':'Amide + carboxylate ; acide piégé'}[variant],aa,bb,curves,
                    caption='Les transferts de proton rapides sont regroupés dans la dernière vue. L’amine ou la base capte le proton de l’acide libéré.' if variant=='amidation' else 'L’élimination rétablit C=O ; la vue finale regroupe aussi les transferts de proton.')


def anhydride(p):
    v=p['variant'];acyl=p['acyl'];q=float(p['equivalents']);trap=p['acidtrap']
    n_required=2 if v=='amidation' and trap=='secondamine' else 1
    x=min(1,q/n_required)
    # R=CH3 ou C6H5 ; tous les coproducts sont inclus dans les équations.
    acetyl=acyl=='acetyl'
    acid='C2H4O2' if acetyl else 'C7H6O2';carboxylate='C2H3O2' if acetyl else 'C7H5O2'
    chloride='C2H3ClO' if acetyl else 'C7H5ClO';anh='C4H6O3' if acetyl else 'C14H10O3'
    ester='C4H8O2' if acetyl else 'C9H10O2';amide='C4H9NO' if acetyl else 'C9H11NO'
    if v=='formation':eq=equation([species('Chlorure d’acyle',chloride),species('Carboxylate',carboxylate,-1)],[species('Anhydride',anh),species('Chlorure','Cl',-1)])
    elif v=='chloridealcohol':eq=equation([species('Chlorure d’acyle',chloride),species('Éthanol','C2H6O')],[species('Ester',ester),species('HCl','HCl')])
    elif v=='hydrolysis':eq=equation([species('Anhydride',anh),species('Eau','H2O')],[species('Acide carboxylique',acid,coefficient=2)])
    elif v=='alcoholysis':eq=equation([species('Anhydride',anh),species('Éthanol','C2H6O')],[species('Ester',ester),species('Acide',acid)])
    else:
        reactants=[species('Anhydride',anh),species('Éthylamine','C2H7N',coefficient=n_required)]
        products=[species('Amide',amide),species('Carboxylate',carboxylate,-1)]
        if trap=='secondamine':products.append(species('Éthylammonium','C2H8N',1))
        else:
            reactants.append(species('Triéthylamine externe','C6H15N'));products.append(species('Triéthylammonium','C6H16N',1))
        eq=equation(reactants,products)
    frames=[anhydride_graph(acyl,variant=v,acidtrap=trap),anhydride_graph(acyl,tetra=True,variant=v,acidtrap=trap),anhydride_graph(acyl,product=True,variant=v,acidtrap=trap)]
    ratios=np.linspace(0,3,121)
    return result([m('Famille','addition–élimination sur l’acyle'),m('Nucléophile',{'formation':'carboxylate','chloridealcohol':'éthanol','hydrolysis':'H₂O','alcoholysis':'éthanol','amidation':'éthylamine'}[v]),
        m('Nucléophile requis dans le bilan choisi',n_required,'équiv.'),m('Borne d’avancement',x,'équiv.'),m('Nucléophile restant',q-n_required*x,'équiv.'),
        m('Coproduct',{'formation':'Cl⁻','chloridealcohol':'HCl','hydrolysis':'second acide','alcoholysis':'acide','amidation':'carboxylate et sel ammonium' if trap=='secondamine' else 'carboxylate et triéthylammonium'}[v])],
        [ch('Borne stœchiométrique de la transformation','Nucléophile / réactif acyle initial','ξ / réactif acyle initial',se('Bilan sélectionné',ratios,np.minimum(1,ratios/n_required)))],
        ms('Addition, intermédiaire, élimination','Le carbone acyle reçoit le doublet ; C=O devient provisoirement C–O ; son rétablissement expulse le groupe partant.',frames,int(p['stage'])),
        ['Le carboxylate réagit sur le chlorure d’acyle pour donner C(=O)–O–C(=O) et Cl⁻. Les deux fragments acyles restent reconnaissables.',
         'Le chlorure d’acyle et EtOH donnent ester + HCl, distinct de l’alcoolyse de l’anhydride qui donne ester + acide. HCl peut être capté par une base dans la synthèse réelle.',
         'L’anhydride peut transférer un acyle à H₂O, EtOH ou EtNH₂. Les produits sont respectivement deux acides, ester + acide, amide + acide avant neutralisation.',
         'En amidation avec neutralisation intégrale, une seconde amine capte le proton de l’acide coproduct. Avec Et₃N externe, une seule amine primaire est comptée pour la liaison C–N.',
         'La courbe est une borne de bilan, sans modèle de vitesse ni de rendement. Une seule équivalence d’amine ne signifie pas absence absolue d’amide ; elle ne suffit pas au bilan imposant aussi la neutralisation complète.'],
        ['Une seule substitution acyle ; mêmes fragments RCO sélectionnés de part et d’autre dans l’anhydride symétrique.',
         'Transferts de proton regroupés dans la dernière vue. L’eau / alcool en excès et les facteurs cinétiques sont des conditions expérimentales à préciser.',
         'Pour l’amidation, « base externe » désigne un équivalent de triéthylamine ; son sel Et₃NH⁺ accompagne le carboxylate dans le bilan isolé.',
         'Le choix du piège à acide n’est utilisé que dans l’amidation.'],
        extent=x,required_nucleophile=n_required,reaction=eq,variant=v)


def hydrolysis_frames(derivative,medium):
    """Éthanoyle commun, états acide/base corrects ; étapes de proton regroupées."""
    basic=medium=='base';leaving={'chloride':'Cl','ester':'OEt','amide':'NH₂'}[derivative]
    graph=carbonyl_fragment('a',0,0,'acetyl',leaving)
    aa=graph['atoms'];bb=graph['bonds']
    aa.append(atom('nu','O',0,-1.4,label='HO' if basic else 'H₂O',charge=-1 if basic else 0))
    if not basic:
        aa.append(atom('cat','O',-1.7,-1.6,label='H₃O',charge=1))
    else:
        # Le chlorure nécessite un second HO− si le produit final est le carboxylate.
        if derivative=='chloride':aa.append(atom('base','O',2.6,-1.4,label='HO',charge=-1))
    f0=molecule('Réactifs : '+('nucléophile HO⁻' if basic else 'activation acide du carbonyle'),aa,bb,
        [arrow((.1,-1.25),(0,0),(-.8,-.55),label='Nu → carbone acyle'),arrow((0,.5),(.05,1.15),(-.6,.9),label='π → O')] if basic else [],
        caption='En acide, protoner O augmente l’électrophilie ; en base, HO⁻ est directement le nucléophile.')
    a1=copy.deepcopy(aa);b1=copy.deepcopy(bb)
    if not basic:
        for a in a1:
            if a['id']=='ao':a.update(label='OH',charge=1)
            if a['id']=='cat':a.update(label='H₂O',charge=0)
        f1=molecule('O protoné : carbonyle activé',a1,b1,[arrow((.1,-1.25),(0,0),(-.8,-.55),label='H₂O → C'),arrow((0,.5),(.1,1.1),(-.6,.9),label='π → O')])
        a2=copy.deepcopy(a1);b2=copy.deepcopy(b1);b2.append(bond('ac','nu'))
        for a in a2:
            if a['id']=='ao':a['charge']=0
            if a['id']=='nu':a.update(label='OH₂',charge=1)
        for b in b2:
            if b['a']=='ac' and b['b']=='ao':b['order']=1
        f2=molecule('Intermédiaire tétraédrique puis transferts H⁺',a2,b2,
                    caption='Le groupe partant OEt / NH₂ est protoné avant son départ sous forme EtOH / NH₃. Les transferts sont rapides dans ce schéma de principe.')
    else:
        b1.append(bond('ac','nu'))
        for a in a1:
            if a['id']=='ao':a['charge']=-1
            if a['id']=='nu':a['charge']=0
        for b in b1:
            if b['a']=='ac' and b['b']=='ao':b['order']=1
        f1=molecule('Intermédiaire tétraédrique anionique',a1,b1,[arrow((.0,1.2),(0,.5),(-.6,.9),label='O⁻ reforme π'),arrow((.6,0),(1.2,.1),(.9,.8),label='C–Z → Z')])
        a2=copy.deepcopy(a1);b2=copy.deepcopy(bb)+[bond('ac','nu')]
        b2=[b for b in b2 if not (b['a']=='ac' and b['b']=='az')]
        for a in a2:
            if a['id']=='ao':a['charge']=0
            if a['id']=='az':a.update(x=2.6,y=.2,charge=-1)
        f2=molecule('Acide carboxylique + groupe partant, avant transfert H',a2,b2,
                    caption='OEt⁻ ou NH₂⁻ ne reste pas en présence de l’acide : il prélève son proton. Cette étape est une représentation de principe, pas l’affirmation d’un intermédiaire libre durable.')
    a3=copy.deepcopy(aa);b3=[b for b in bb if not (b['a']=='ac' and b['b']=='az')]+[bond('ac','nu')]
    for a in a3:
        if a['id']=='nu':a.update(label='O' if basic else 'OH',charge=-1 if basic else 0)
        if a['id']=='az':
            if derivative=='chloride':a.update(x=2.6,y=.2,label='Cl' if basic else 'HCl',charge=-1 if basic else 0)
            elif derivative=='ester':a.update(x=2.6,y=.2,label='HOEt',charge=0)
            else:a.update(x=2.6,y=.2,label='NH₃' if basic else 'NH₄',charge=0 if basic else 1)
        if a['id']=='cat' and derivative=='amide':a.update(label='H₂O',charge=0)
        if a['id']=='base':a.update(label='H₂O',charge=0)
    f3=molecule('État final : '+('carboxylate' if basic else 'acide carboxylique'),a3,b3,
                caption='Milieu basique : COO⁻ ; milieu acide : COOH. L’amide donne NH₃ en base et NH₄⁺ en milieu acide.')
    return [f0,f1,f2,f3]


def hydrolyseacyle(p):
    d=p['derivative'];base=p['medium']=='base';q=float(p['equivalents'])
    req=2 if base and d=='chloride' else 1
    limit=min(1,q/req)
    df={'chloride':'C2H3ClO','ester':'C4H8O2','amide':'C2H5NO'}[d]
    reactants=[species('Dérivé acyle',df),species('HO⁻','HO',-1,req)] if base else [species('Dérivé acyle',df),species('H₂O','H2O')]
    if base:
        products=[species('Acétate','C2H3O2',-1)]
        products+={'chloride':[species('Cl⁻','Cl',-1),species('Eau','H2O')],
                   'ester':[species('Éthanol','C2H6O')],'amide':[species('Ammoniac','H3N')]}[d]
    else:
        products=[species('Acide éthanoïque','C2H4O2')]
        if d=='chloride':products.append(species('HCl','HCl'))
        elif d=='ester':products.append(species('Éthanol','C2H6O'))
        else:
            # Le proton du bain acide est consommé pour NH4+ dans le bilan net.
            reactants.append(species('Proton du bain acide','H',1));products.append(species('Ammonium','H4N',1))
    frames=hydrolysis_frames(d,p['medium'])
    reactivity={'chloride':'très réactif : hydrolyse facile','ester':'réactif sous catalyse acide / base, temps et chauffage à préciser','amide':'résonance stabilisante : hydrolyse exigeante, chauffage / conditions adaptées'}[d]
    ratios=np.linspace(0,2,101)
    return result([m('Produit acyle en fin de milieu','CH₃COO⁻' if base else 'CH₃COOH'),m('Coproduct azoté','NH₃' if base else 'NH₄⁺') if d=='amide' else m('Coproduct','Cl⁻ / HCl' if d=='chloride' else 'EtOH'),
        m('Réactivité comparative',reactivity),m('Borne stœchiométrique',limit,'équiv.'),m('HO⁻ / H₂O requis dans le bilan',req,'équiv.'),
        m('Conversion réelle','non calculée : cinétique / équilibre requis')],
        [ch('Borne de matière : ne pas confondre avec conversion','HO⁻ ou H₂O / dérivé initial','Borne ξ / dérivé initial',se('Bilan choisi',ratios,np.minimum(1,ratios/req)))],
        ms('Le milieu décide des espèces finales',reactivity,frames,int(p['stage'])),
        ['Identifier l’électrophile commun R–C(=O)–Z, puis le nucléophile : HO⁻ en base, H₂O sur le carbonyle activé en acide.',
         'Addition puis rétablissement de C=O : le groupe Z part après les transferts de proton nécessaires. Les amides sont moins réactifs que les esters et chlorures d’acyle.',
         'La saponification forme un carboxylate qui ne reste pas un électrophile acyle comparable à l’ester. Une acidification ultérieure donnerait l’acide, étape distincte.',
         'Hydrolyse acide d’un ester : équilibre réversible, eau en excès utile. Hydrolyse d’une amide : conditions plus exigeantes ; aucun taux ou temps identique aux chlorures n’est supposé.',
         'Pour le chlorure en base : un HO⁻ réalise l’hydrolyse, un second neutralise l’acide ; le bilan final comporte acétate + Cl⁻ + H₂O.'],
        ['Les graphes montrent une seule famille éthanoyle afin d’isoler l’effet de Z et du milieu.',
         'Les transferts H⁺ sont regroupés ; le départ d’un amide en milieu acide est précédé de la protonation appropriée, et ne signifie pas expulsion de NH₂⁻ dans l’acide.',
         'L’avancement affiché est une limite stœchiométrique atteignable dans le bilan choisi, pas une conversion prédite. En milieu acide l’eau est usuellement le solvant.',
         'L’acide du bain est catalytique pour l’ester ; un équivalent H⁺ demeure capté dans NH₄⁺ pour l’hydrolyse acide de l’amide.'],
        extent_limit=limit,required_nucleophile=req,reaction=equation(reactants,products),carboxyl_charge=-1 if base else 0,reactivity=reactivity)


def photo_ring(product=False,sea=False):
    aa,bb=ring(aromatic=not product or sea)
    if product:
        for i,a in enumerate(aa[:6]):
            if not sea or i==0:
                if sea:a['label']='C'
                x=a['x']*1.8;y=a['y']*1.8
                aa.append(atom('cl'+str(i),'Cl',x,y));bb.append(bond('r'+str(i),'cl'+str(i)))
                if sea:break
        if sea:
            aa+=[atom('h','H',2.8,-1),atom('clh','Cl',3.8,-1)];bb.append(bond('h','clh'))
    return molecule('Chlorobenzène + HCl' if product and sea else 'Hexachlorocyclohexane : stéréoisomères non distingués' if product else 'Benzène : trois liaisons π conjuguées',aa,bb,
                    caption='La représentation plane ne spécifie aucune configuration des six centres CHCl : elle n’identifie pas le seul isomère γ (lindane).' if product and not sea else 'Une substitution conserve l’aromaticité ; une photoaddition complète conduit à un cycle saturé.')


def photochlore(p):
    sea=p['mode']=='sea';active=sea or p['light']=='on';q=float(p['chlorine']);req=1 if sea else 3
    extent=min(1,q/req) if active else 0.
    start=photo_ring()
    if sea:
        middle=copy.deepcopy(start);middle['name']='Cl₂ / FeCl₃ : électrophile chlorant, puis SEA'
        middle['caption']='Le complexe σ perd H⁺, puis l’aromaticité est restaurée. Ce cadre compare les bilans ; le mécanisme SEA détaillé figure dans le laboratoire Aromatique.'
    else:
        middle=copy.deepcopy(start);middle['name']='hν : addition sur le noyau, trois Cl₂ au bilan complet' if active else 'Sans hν : pas de photoaddition dans ce modèle'
        middle['caption']='La première photoaddition et les suivantes ne sont pas assimilées à une SEA ni à trois réactions indépendantes de même vitesse.'
    finish=photo_ring(product=True,sea=sea) if active else copy.deepcopy(start)
    if not active:finish['name']='Benzène conservé : photoaddition non activée'
    curve=np.linspace(0,4,161);total=np.minimum(1,curve/req) if active else np.zeros_like(curve)
    rx=equation([species('Benzène','C6H6'),species('Dichlore','Cl2',coefficient=req)],
                [species('Chlorobenzène','C6H5Cl'),species('Chlorure d’hydrogène','HCl')] if sea else [species('Hexachlorocyclohexane','C6H6Cl6')])
    return result([m('Nature','substitution électrophile aromatique' if sea else 'photoaddition'),m('Cl₂ requis par bilan complet',req,'équiv.'),
        m('Borne de produit complet',extent,'équiv.'),m('Cl₂ non alloué au produit complet',q-req*extent,'équiv.'),m('Aromaticité du produit',sea),
        m('Isomère γ sélectionné','aucune sélection stéréochimique ici' if not sea else 'sans objet')],
        [ch('Même Cl₂, stœchiométrie différente','Cl₂ / benzène initial','Borne du produit complet',se('SEA' if sea else 'Photoaddition',curve,total))],
        ms('Lire les conditions au-dessus de la flèche','FeCl₃ sans hν mène à une substitution ; l’irradiation permet une addition qui sature le cycle.',[start,middle,finish],int(p['stage'])),
        ['Photoaddition : C₆H₆ + 3 Cl₂ → C₆H₆Cl₆. Les six H sont conservés ; les trois unités π disparaissent.',
         'SEA : C₆H₆ + Cl₂ → C₆H₅Cl + HCl. Un H est remplacé par Cl ; les six carbones restent aromatiques.',
         'La courbe divise la quantité disponible de Cl₂ par le coefficient 3 ou 1 : c’est une borne de stœchiométrie, sans prédiction de rendement.',
         'Avec moins de trois Cl₂, une photoaddition partielle et plusieurs espèces sont possibles : la borne de produit complet ne décrit pas leur distribution.',
         'Le composé C₆H₆Cl₆ comporte plusieurs stéréoisomères. Un dessin plat et la formule brute ne suffisent pas à conclure « lindane ».'],
        ['Une seule monochloration SEA est retenue ; à forte conversion ou excès de Cl₂, des substitutions supplémentaires peuvent intervenir.',
         'La commande lumière porte uniquement sur la photoaddition ; le mode SEA impose FeCl₃ et l’absence de hν.',
         'Aucun mécanisme radicalaire détaillé de photoaddition ni distribution de stéréoisomères n’est inventé.'],
        extent=extent,chlorine_required=req,active=active,aromatic_product=sea,reaction=rx)


def grignard_fragment(group,halide,state):
    """RX, RMgX ou RH : Mg et X restent explicitement dessinés."""
    if group=='phenyl':
        aa,bb=ring();aa[0]['label']='C' if state!='rh' else 'CH';attach='r0';x=1
    else:
        aa=[atom('c0','C',-1.1,0,label='CH₃'),atom('c1','C',0,.2,label='CH₃' if state=='rh' else 'CH₂')]
        bb=[bond('c0','c1')];attach='c1';x=0
    if state=='rx':
        aa += [atom('x',halide,x+1.2,0),atom('mg','Mg',x+2.6,-1.2)]
        bb += [bond(attach,'x')]
    elif state=='rmgx':
        aa += [atom('mg','Mg',x+1.1,0),atom('x',halide,x+2.25,0)]
        bb += [bond(attach,'mg'),bond('mg','x')]
    else:
        aa += [atom('mg','Mg',x+2.0,-.9),atom('x',halide,x+3.1,-.9),atom('o','O',x+2.0,-2.0,label='OH')]
        bb += [bond('mg','x'),bond('mg','o')]
    return molecule({'rx':'RX + Mg : insertion en éther anhydre','rmgx':'RMgX : carbone nucléophile, liaison polarisée','rh':'RH + MgXOH : réactif détruit par un proton'}[state],aa,bb,
                    caption='R–Mg–X est une écriture de bilan : le solvant coordonne Mg et les espèces agrégées / équilibres de Schlenk ne sont pas détaillés.')


def grignardprep(p):
    group=p['group'];halide=p['halide'];mg=float(p['magnesium']);water=float(p['water']);progress=float(p['progress'])
    formed=min(1,mg)*progress;destroyed=min(formed,water);available=formed-destroyed
    scan=np.linspace(0,2,161);available_scan=np.maximum(0,formed-scan);lost_scan=np.minimum(formed,scan)
    r='C2H5' if group=='ethyl' else 'C6H5';rh='C2H6' if group=='ethyl' else 'C6H6'
    insertion=equation([species('RX',r+halide),species('Magnésium','Mg')],[species('RMgX',r+'Mg'+halide)])
    quench=equation([species('RMgX',r+'Mg'+halide),species('Eau','H2O')],[species('RH',rh),species('Hydroxyhalogénure de Mg','Mg'+halide+'OH')])
    first=grignard_fragment(group,halide,'rx');second=grignard_fragment(group,halide,'rmgx')
    if water>0 and formed>0:
        second['atoms'] += [atom('water','O',-.5,-1.6,label='OH'),atom('wh','H',.4,-1.6)]
        second['bonds'].append(bond('water','wh'))
        source_x=1.55 if group=='phenyl' else .55
        second['arrows']=[arrow((source_x,.05),(.4,-1.6),(source_x+.4,-.7),label='doublet C–Mg → H de H₂O'),
                          arrow((-.05,-1.6),(-.5,-1.5),(-.3,-.9),label='O–H → O')]
        second['caption']='Le doublet polarisé de la liaison C–Mg prélève un proton ; l’eau parasite consomme le réactif avant toute attaque d’un carbonyle.'
    elif formed==0:
        second=copy.deepcopy(first);second['name']='Aucun RMgX formé : pas de nucléophile disponible'
    else:
        second['name']='Milieu anhydre : RMgX est préservé'
    third=grignard_fragment(group,halide,'rh') if destroyed>0 else grignard_fragment(group,halide,'rmgx') if formed>0 else copy.deepcopy(first)
    if destroyed>0:
        if available>0:
            third=combine('RH parasite et RMgX encore disponible',shifted(third,prefix='q'),
                          shifted(grignard_fragment(group,halide,'rmgx'),dx=6.2,prefix='u'),
                          caption='Les deux espèces coexistent dans le bilan ; leurs quantités sont chiffrées séparément. MgXOH accompagne la fraction détruite.')
        else:third['name']='RMgX totalement détruit : RH + MgXOH'
    elif formed==0:
        third['name']='Pas d’insertion accomplie : RX / Mg non engagé'
    inventory=[dict(label='RX',formula=r+halide,initial=1.,final=1-formed),
               dict(label='Mg',formula='Mg',initial=mg,final=mg-formed),
               dict(label='H₂O',formula='H2O',initial=water,final=water-destroyed),
               dict(label='RMgX',formula=r+'Mg'+halide,initial=0.,final=available),
               dict(label='RH',formula=rh,initial=0.,final=destroyed),
               dict(label='MgXOH',formula='Mg'+halide+'OH',initial=0.,final=destroyed)]
    return result([m('RMgX formé par insertion idéale',formed,'équiv.'),m('RMgX détruit par l’eau',destroyed,'équiv.'),
        m('RMgX disponible',available,'équiv.'),m('RX restant',1-formed,'équiv.'),m('Mg non engagé',mg-formed,'équiv.'),m('Eau restante',water-destroyed,'équiv.'),
        m('Hydrolyse finale d’un alcoolate','étape différente, après addition C–C')],
        [ch('L’eau parasite retire un équivalent par proton fourni ici','H₂O initial / RX initial','Quantité / RX initial',se('RMgX disponible',scan,available_scan),se('RH parasite',scan,lost_scan))],
        ms('Deux opérations : préparer, puis préserver','RX + Mg → RMgX ; RMgX + H₂O → RH + MgXOH. L’éther doit être sec, le montage protégé de l’humidité.',[first,second,third],int(p['stage'])),
        ['Former RMgX par insertion de Mg dans R–X en solvant éthéré anhydre ; l’apparence R–Mg–X n’est pas un mécanisme concerté d’insertion.',
         'L’insertion accomplie vaut p × min(n₀ RX, n₀ Mg), où p est la fraction imposée. Aucun temps ou taux universel n’est associé à p.',
         'Chaque H₂O consomme ici un RMgX : le carbone lié à Mg reçoit H, donnant RH ; MgXOH reçoit O et l’autre H.',
         'Les quantités finales RX, Mg, H₂O, RMgX, RH et MgXOH conservent chaque élément. Elles sont fournies individuellement dans les bilans.',
         'Après attaque d’un carbonyle, on hydrolyse volontairement l’alcoolate pour isoler l’alcool. Une hydrolyse avant cette attaque détruit au contraire le nucléophile et la synthèse C–C.'],
        ['Un RX initial vaut un équivalent ; la fraction d’insertion p est une donnée imposée, pas une prédiction expérimentale.',
         'L’eau ne passivait pas le Mg dans ce bilan isolé : elle attaque seulement le RMgX formé. En réalité l’humidité peut aussi bloquer l’amorçage et aggraver la perte.',
         'Une seule déprotonation de H₂O est comptée ; les sels sont représentés par MgXOH sans modéliser leurs agrégats ni leur solvatation.',
         'La préparation d’un chlorure peut demander des conditions d’amorçage différentes d’un bromure ; aucune égalité de vitesse n’est supposée.'],
        formed=formed,destroyed=destroyed,available=available,remaining_rx=1-formed,remaining_mg=mg-formed,remaining_water=water-destroyed,
        inventory=inventory,insertion_reaction=insertion,quench_reaction=quench)


FUNCTIONS={'effets':effects,'e1':e1,'enolatealkyl':enolatealkyl,'aminealkyl':aminealkyl,
           'anhydride':anhydride,'hydrolyseacyle':hydrolyseacyle,'photochlore':photochlore,'grignardprep':grignardprep}


def calculate(lab_id,params):
    return FUNCTIONS[lab_id](params)
