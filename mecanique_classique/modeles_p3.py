"""Calculs P3, SI ; intégration explicite contrôlée par les invariants."""
import math
import numpy as np
from commun import metric, series, chart, result

G = 9.81

def assembly(mass, stretch=1.8):
    points = np.array([[.65*stretch,0,0],[-.5*stretch,0,0],[0,.55,0],[0,-.4,0],[0,0,.35],[0,0,-.6]])
    weights = np.array([1.,2.,3.,1.5,.8,2.2]); weights *= mass/weights.sum()
    points -= np.average(points,axis=0,weights=weights)
    return points, weights

def inertia(points, masses):
    return sum(m*(np.dot(r,r)*np.eye(3)-np.outer(r,r)) for r,m in zip(points,masses))

def rk4(function, state, duration, dt=.002, project=None):
    n = max(400, int(math.ceil(duration/dt)))
    time = np.linspace(0,duration,n+1); h = time[1]-time[0]
    values = np.empty((n+1,len(state))); values[0] = state
    for i in range(n):
        y=values[i]; a=function(y); b=function(y+h*a/2); c=function(y+h*b/2); d=function(y+h*c)
        values[i+1]=y+h*(a+2*b+2*c+d)/6
        if project: values[i+1]=project(values[i+1])
    return time, values

def thinning(t, a, count=700):
    ix=np.unique(np.linspace(0,len(t)-1,min(count,len(t))).astype(int))
    return t[ix],a[ix]

def inertie_huygens(p):
    points,masses=assembly(p['mass'],p['stretch']); d=np.array([p['dx'],p['dy'],0.])
    ig=inertia(points,masses); io=inertia(points+d,masses)
    predicted=ig+p['mass']*(np.dot(d,d)*np.eye(3)-np.outer(d,d))
    theta,phi=np.radians([p['theta'],p['phi']]); u=np.array([np.sin(theta)*np.cos(phi),np.sin(theta)*np.sin(phi),np.cos(theta)])
    eig,axes=np.linalg.eigh(ig); az=np.linspace(0,360,361); q=np.array([np.sin(theta)*np.cos(np.radians(az)),np.sin(theta)*np.sin(np.radians(az)),np.full(len(az),np.cos(theta))]).T
    jg=np.einsum('ni,ij,nj->n',q,ig,q); jo=np.einsum('ni,ij,nj->n',q,io,q)
    return result([metric('Inertie de l’axe passant par G',float(u@ig@u),'kg·m²'),metric('Inertie de l’axe passant par O',float(u@io@u),'kg·m²'),metric('Plus petite inertie principale',float(eig[0]),'kg·m²'),metric('Plus grande inertie principale',float(eig[-1]),'kg·m²'),metric('Écart entre calcul direct et Huygens',float(np.max(np.abs(io-predicted))),'kg·m²')],
      [chart('Tourner l’axe tout en gardant sa même inclinaison','Azimut φ (°)','Moment d’inertie (kg·m²)',series('Axe par G',az,jg),series('Axe par O',az,jo)),chart('Les trois axes principaux','Numéro de l’axe','Moment d’inertie (kg·m²)',series('Valeurs propres de I_G',[1,2,3],eig))],
      dict(kind='inertia',title='Six masses autour de G, axe par O',description='Les directions principales sont les colonnes de la matrice des vecteurs propres.',points=points+d,masses=masses,tensor=io,principal_axes=axes,axis=u,center=d),
      ['Pour chaque masse mᵢ, calculer sa distance perpendiculaire à l’axe : I(u)=Σ mᵢ(|rᵢ|²−(rᵢ·u)²).','La matrice I_G=Σ mᵢ(|rᵢ|²Id−rᵢrᵢᵀ) est symétrique ; uᵀI_Gu donne l’inertie suivant u.','Avec d=OG, I_O=I_G+M(|d|²Id−ddᵀ). La distance entre les deux axes parallèles vaut |d×u|.','Diagonaliser I_G : les valeurs propres sont les inerties principales et les vecteurs propres donnent leurs axes.'],
      ['Six masses ponctuelles liées rigidement ; les coordonnées sont exprimées en mètres.','Les axes comparés ont la même direction. Huygens ne compare pas deux axes d’orientations différentes.'])

def konig(p):
    r,m=assembly(p['mass']); ig=inertia(r,m); vg=np.array([p['vx'],p['vy'],0.]); om=np.array([0.,0.,p['omega']]); pos=np.array([p['gx'],p['gy'],0.])
    vel=vg+np.cross(om,r); direct=float(np.sum(m*np.sum(vel*vel,axis=1))/2); trans=float(p['mass']*vg@vg/2); rot=float(om@ig@om/2)
    angular=np.sum(np.cross(r+pos,m[:,None]*vel),axis=0); orbit=np.cross(pos,p['mass']*vg); intrinsic=ig@om
    t=np.linspace(0,2,301); paths=[]
    for i,point in enumerate(r):
        c=np.cos(p['omega']*t); s=np.sin(p['omega']*t)
        paths.append(dict(label=f'Masse {i+1}',x=pos[0]+vg[0]*t+point[0]*c-point[1]*s,y=pos[1]+vg[1]*t+point[0]*s+point[1]*c))
    w=np.linspace(-8,8,321)
    return result([metric('Énergie de translation',trans,'J'),metric('Énergie de rotation',rot,'J'),metric('Énergie calculée par les six vitesses',direct,'J'),metric('Écart du second théorème de König',abs(direct-trans-rot),'J'),metric('Écart du premier théorème de König',float(np.linalg.norm(angular-orbit-intrinsic)),'kg·m²/s'),metric('Moment cinétique orbital suivant z',float(orbit[2]),'kg·m²/s')],
      [chart('Comment se répartit l’énergie si l’on change la rotation ?','Vitesse angulaire ω (rad/s)','Énergie (J)',series('Translation',w,np.full(len(w),trans)),series('Rotation',w,.5*ig[2,2]*w*w),series('Somme',w,trans+.5*ig[2,2]*w*w)),chart('Comparer les six vitesses au même instant','Numéro de la masse','Norme de la vitesse (m/s)',series('Vitesse dans le laboratoire',np.arange(1,7),np.linalg.norm(vel,axis=1)),series('Vitesse par rapport à G',np.arange(1,7),np.linalg.norm(np.cross(om,r),axis=1)))],
      dict(kind='trajectory',title='Translation de G et rotation autour de G',description='Les six trajectoires correspondent à des points d’un même solide.',time=t,paths=paths),
      ['Écrire vᵢ=v_G+Ω×rᵢ avec rᵢ=GMᵢ. Par définition de G, Σmᵢrᵢ=0.','Développer Σ½mᵢ|vᵢ|² : le terme croisé vaut v_G·(Ω×Σmᵢrᵢ)=0. Donc E_c=½M|v_G|²+½ΩᵀI_GΩ.','Développer ΣOMᵢ×mᵢvᵢ : L_O=OG×Mv_G+I_GΩ.','Les deux termes du moment cinétique s’ajoutent vectoriellement : ils peuvent se compenser, contrairement aux deux énergies positives.'],
      ['Cinématique prescrite d’un solide rigide ; aucune conservation n’est supposée pour un mouvement imposé.','Les positions relatives sont évaluées dans l’orientation initiale pour le bilan affiché.'])

def barre_bascule(p):
    mass,L=p['mass'],p['L']; a,b=np.radians([p['theta1'],p['theta2']]); c=math.sqrt(3*G/L)
    duration=2/c*math.log(math.tan(b/4)/math.tan(a/4)); t=np.linspace(0,duration,601); th=4*np.arctan(math.tan(a/4)*np.exp(c*t/2)); speed=c*np.sin(th/2); acc=3*G/(4*L)*np.sin(th)
    rr=mass*G*(5*np.cos(th)-3)/2; rt=-mass*G*np.sin(th)/4
    rx=rr*np.sin(th)+rt*np.cos(th); ry=rr*np.cos(th)-rt*np.sin(th)
    kinetic=.5*(4*mass*L*L/3)*speed*speed; potential=mass*G*L*np.cos(th)
    return result([metric('Durée entre les deux angles',duration,'s'),metric('Inertie autour du pivot',4*mass*L*L/3,'kg·m²'),metric('Vitesse angulaire finale',float(speed[-1]),'rad/s'),metric('Norme finale de la réaction',float(np.hypot(rx[-1],ry[-1])),'N'),metric('Variation numérique de E_c+E_p',float(np.ptp(kinetic+potential)),'J')],
      [chart('Basculement et accélération','Temps (s)','Angle (°)',series('θ',t,np.degrees(th))),chart('Le pivot exerce une force qui change de sens','Angle θ (°)','Force (N)',series('Composante radiale Rᵣ',np.degrees(th),rr),series('Composante tangentielle Rθ',np.degrees(th),rt),series('Norme de R',np.degrees(th),np.hypot(rx,ry))),chart('Le pivot ne fournit aucun travail','Temps (s)','Énergie (J)',series('Énergie cinétique',t,kinetic),series('Énergie potentielle',t,potential),series('Somme',t,kinetic+potential))],
      dict(kind='rod',title='Barre de longueur 2L, pivot fixe O',description='L’extrémité libre se situe à deux fois la position du centre de masse G.',time=t,theta=th,length=2*L,pivot=[0,0],tips=dict(x=2*L*np.sin(th),y=2*L*np.cos(th)),reaction=dict(x=rx,y=ry)),
      ['Huygens : I_O=M(2L)²/12+ML²=4ML²/3. L’angle θ part de la verticale ascendante.','Sur la trajectoire d’énergie MgL, ½I_Oθ̇²=MgL(1−cosθ), donc θ̇=√(3g/L)sin(θ/2).','Entre θ₁ et θ₂ strictement positifs : Δt=2√(L/(3g)) ln[tan(θ₂/4)/tan(θ₁/4)]. L’intégrale diverge lorsque θ₁ tend vers 0.','Projeter Ma_G=Mg+R avec a_G=−Lθ̇²eᵣ+Lθ̈eθ. On obtient Rᵣ=Mg(5cosθ−3)/2 et Rθ=−Mg sinθ/4.'],
      ['Barre homogène rigide ; pivot idéal sans frottement dans un référentiel galiléen.','Une barre exactement verticale et immobile reste immobile : la trajectoire étudiée est la limite d’une perturbation initiale, et non un départ sans vitesse à θ₁.'])

def barre_rotule(p):
    mass,L=p['mass'],p['L']; th=np.radians(p['theta']); n=np.array([np.sin(th),0.,np.cos(th)])
    w=p['theta_dot']*np.array([np.cos(th),0.,-np.sin(th)])+p['phi_dot']*np.cross([0,0,1],n)
    lam=3*G/(4*L); ez=np.array([0.,0.,1.]); inertia_o=4*mass*L*L/3
    def fun(y):
        q,v=y[:3],y[3:]; return np.r_[v,-lam*(ez-q[2]*q)-np.dot(v,v)*q]
    def project(y):
        q=y[:3]/np.linalg.norm(y[:3]); return np.r_[q,y[3:]-np.dot(y[3:],q)*q]
    t,y=rk4(fun,np.r_[n,w],p['duration'],project=project); n,w=y[:,:3],y[:,3:]; angular=inertia_o*np.cross(n,w); e=.5*inertia_o*np.sum(w*w,axis=1)+mass*G*L*n[:,2]
    theta=np.arccos(np.clip(n[:,2],-1,1)); phi=np.unwrap(np.arctan2(n[:,1],n[:,0])); ts,ns=thinning(t,n)
    return result([metric('Inertie transversale en O',inertia_o,'kg·m²'),metric('Énergie initiale',float(e[0]),'J'),metric('Écart maximal de l’énergie',float(np.max(np.abs(e-e[0]))),'J'),metric('Composante verticale du moment cinétique',float(angular[0,2]),'kg·m²/s'),metric('Écart maximal de cette composante',float(np.max(np.abs(angular[:,2]-angular[0,2]))),'kg·m²/s')],
      [chart('Inclinaison et azimut de la barre','Temps (s)','Angle (°)',series('Inclinaison θ',t,np.degrees(theta)),series('Azimut φ déroulé',t,np.degrees(phi))),chart('Deux invariants indépendants','Temps (s)','Énergie (J)',series('E_c+E_p',t,e)),chart('Le couple du poids n’a pas de composante verticale','Temps (s)','Moment cinétique (kg·m²/s)',series('L_O,z',t,angular[:,2]))],
      dict(kind='rigid3d',title='Barre sur rotule : orientation dans l’espace',description='Le vecteur unitaire n pointe de O vers l’extrémité libre ; G=L n.',time=ts,axis=ns,length=2*L),
      ['Convention : θ est l’angle à la verticale ascendante, φ l’azimut. OG=L(sinθ cosφ,sinθ sinφ,cosθ).','La barre est mince : I_O=I⊥(Id−nnᵀ), I⊥=4ML²/3. La composante de Ω parallèle à la barre n’est pas déterminée par le mouvement de son axe et ne contribue pas ici.','Avec n·n=1, L_O=I⊥n×ṅ et E_c=½I⊥|ṅ|². Le poids exerce le couple −MgL n×e_z.','L’équation intégrée est n̈=−(3g/(4L))(e_z−n_z n)−|ṅ|²n. Les erreurs sur E et L_z mesurent la précision de l’intégration.'],
      ['Barre homogène de rayon négligé ; rotule parfaite sans moment de réaction.','RK4 avec petit pas ; normalisation de n et projection de ṅ sur le plan tangent. Les bilans affichés contrôlent les erreurs restantes.'])

def cylindre_bord(p):
    m,R,fs=p['mass'],p['radius'],p['fs']; detach=math.acos(4/7)
    if fs==0: threshold=0.
    else:
        lo,hi=0.,detach
        for _ in range(70):
            mid=(lo+hi)/2
            if math.sin(mid)>fs*(7*math.cos(mid)-4): hi=mid
            else: lo=mid
        threshold=(lo+hi)/2
    a=min(math.radians(p['theta1']),threshold); th=np.linspace(a,threshold,401)
    normal=m*G*(7*np.cos(th)-4)/3; tangent=m*G*np.sin(th)/3; speed=np.sqrt(np.maximum(0,4*G/(3*R)*(1-np.cos(th)))); kinetic=.75*m*R*R*speed*speed; potential=m*G*R*np.cos(th)
    reference=np.linspace(0,detach,501); nr=m*G*(7*np.cos(reference)-4)/3; tr=m*G*np.sin(reference)/3
    return result([metric('Premier angle de glissement',math.degrees(threshold),'°'),metric('Angle N=0 si l’adhérence était maintenue',math.degrees(detach),'°'),metric('Réaction normale au seuil',float(normal[-1]),'N'),metric('Réaction tangentielle au seuil',float(tangent[-1]),'N'),metric('Variation de l’énergie pendant l’adhérence',float(np.ptp(kinetic+potential)),'J'),metric('Phase représentée','Adhérence uniquement, jusqu’au seuil')],
      [chart('Branche d’adhérence supposée : chercher |T|=fₛN','Angle θ (°)','Force (N)',series('T requis en adhérence',np.degrees(reference),tr),series('fₛ N disponible',np.degrees(reference),fs*nr),series('N',np.degrees(reference),nr),xMarker=math.degrees(threshold),xMarkerLabel='Premier glissement'),chart('La trajectoire calculée s’arrête au glissement','Angle θ (°)','Vitesse angulaire (rad/s)',series('θ̇ pendant l’adhérence',np.degrees(th),speed)),chart('Bilan avant le changement de régime','Angle θ (°)','Énergie (J)',series('Énergie totale',np.degrees(th),kinetic+potential))],
      dict(kind='rolling',title='Cylindre en contact avec l’arête',description='La scène s’arrête au premier seuil de glissement ; elle ne prolonge pas l’hypothèse d’adhérence.',theta=th,radius=R,center=dict(x=R*np.sin(th),y=R*np.cos(th)),contact=[0,0]),
      ['Pendant l’adhérence, le point de contact du cylindre est immobile. Huygens donne I_I=3mR²/2.','Énergie : ½I_Iθ̇²=mgR(1−cosθ), d’où θ̇²=(4g/(3R))(1−cosθ) et θ̈=(2g/(3R))sinθ.','Le PFD donne T=(mg/3)sinθ et N=(mg/3)(7cosθ−4). Pour rester en adhérence, il faut N≥0 et |T|≤fₛN.','Le rapport T/N diverge avant N=0. Pour tout fₛ fini positif, le glissement arrive donc avant arccos(4/7). Après ce seuil, une nouvelle équation de contact est nécessaire.'],
      ['Cylindre plein homogène ; arête idéalisée comme contact ponctuel ; mouvement plan.','Les courbes de réactions au-delà du seuil sont des valeurs requises par une adhérence hypothétique, pas les réactions du mouvement réel.','Si l’angle initial choisi dépasse le seuil, seule la configuration du seuil est montrée. Pour fₛ=0, l’adhérence cesse dès le départ.'])

def coulomb_motion(m,fs,fd,F,v0,duration):
    """Traction constante et événement v=0 traités exactement par morceaux."""
    bound=fs*m*G; kinetic_force=fd*m*G; t=np.linspace(0,duration,401); stop=None
    if v0==0:
        sliding=abs(F)>bound+1e-12
        force=-math.copysign(kinetic_force,F) if sliding else -F
        acceleration=(F+force)/m; v=acceleration*t; x=.5*acceleration*t*t
        friction=np.full(len(t),force); distance=np.abs(x)
        regime='Glissement' if sliding else 'Adhérence'
    else:
        force=-kinetic_force; acceleration=(F+force)/m
        if acceleration<0:
            stopping_time=-v0/acceleration
            if stopping_time<=duration: stop=stopping_time
        if stop is None:
            v=v0+acceleration*t; x=v0*t+.5*acceleration*t*t
            friction=np.full(len(t),force); distance=x.copy()
            regime='Glissement, freinage sans arrêt dans l’intervalle' if acceleration<0 else 'Glissement vers la droite'
        else:
            t=np.unique(np.r_[t,stop]); tau=np.maximum(0,t-stop); before=t<stop
            x_stop=v0*stop+.5*acceleration*stop*stop
            if abs(F)<=bound+1e-12:
                a2=0.; force2=-F; regime='Glissement puis adhérence'
            else:
                # Avec 0≤fd≤fs et v0>0, un arrêt ne peut être suivi
                # que d’une reprise vers la gauche sous une force F<−fsN.
                a2=(F+kinetic_force)/m; force2=kinetic_force
                regime='Glissement puis inversion du mouvement'
            v=np.where(before,v0+acceleration*t,a2*tau)
            x=np.where(before,v0*t+.5*acceleration*t*t,x_stop+.5*a2*tau*tau)
            friction=np.where(before,force,force2)
            distance=np.where(before,x,x_stop+np.abs(x-x_stop))
    return dict(time=t,x=x,v=v,friction=friction,distance=distance,acceleration=acceleration,stop=stop,regime=regime)

def coulomb_horizontal(p):
    m,fs,F=p['mass'],p['fs'],p['force']; fd=fs*p['ratio']; bound=fs*m*G
    v0=p['v0'] if p.get('initial','rest')=='moving' else 0.
    motion=coulomb_motion(m,fs,fd,F,v0,p['duration']); t,x,v=motion['time'],motion['x'],motion['v']; friction=motion['friction']
    f=np.linspace(-max(100,2*bound),max(100,2*bound),601); ff=np.where(np.abs(f)<=bound,-f,-np.sign(f)*fd*m*G)
    work=F*x; loss=fd*m*G*motion['distance']; kinetic=.5*m*v*v; change=kinetic-.5*m*v0*v0
    return result([metric('Régime',motion['regime']),metric('Seuil statique fₛmg',bound,'N'),metric('Coefficient dynamique f_d',fd),metric('Frottement à t=0⁺',float(friction[0]),'N'),metric('Accélération à t=0⁺',motion['acceleration'],'m/s²'),metric('Temps d’arrêt',motion['stop'] if motion['stop'] is not None else 'Aucun arrêt pendant l’observation','s' if motion['stop'] is not None else ''),metric('Énergie cinétique initiale',.5*m*v0*v0,'J'),metric('Chaleur dissipée à la fin',float(loss[-1]),'J'),metric('Écart du bilan W_F=ΔE_c+Q',float(np.max(np.abs(work-change-loss))),'J')],
      [chart('Essais indépendants à partir du repos','Force horizontale F (N)','Frottement algébrique (N)',series('Loi de réponse',f,ff)),chart('La position reste continue au changement de régime','Temps (s)','Position (m)',series('Position de la caisse',t,x)),chart('Arrêt et éventuelle reprise inverse','Temps (s)','Vitesse (m/s)',series('Vitesse de la caisse',t,v)),chart('Le frottement change de branche à l’arrêt','Temps (s)','Force (N)',series('Frottement',t,friction),series('Traction constante',t,np.full(len(t),F))),chart('Le bilan tient compte de l’énergie initiale','Temps (s)','Énergie (J)',series('Travail de la traction',t,work),series('Variation d’énergie cinétique',t,change),series('Énergie dissipée',t,loss))],
      dict(kind='friction',title='Traction constante : adhérence, freinage ou inversion',description='La vitesse est continue ; la force de frottement peut changer brutalement au passage v=0.',time=t,x=x,v=v,friction=friction,alpha=0,mass=m),
      ['Le bilan vertical donne N=mg. À v=0, tester |F|≤fₛN : si oui, F_frot=−F et la caisse reste immobile.','Tant que v>0, F_frot=−f_dN, même si F est négative. Le freinage donne a₁=(F−f_dN)/m et, si a₁<0, t_arrêt=−v₀/a₁.','Après l’arrêt, une force F<−fₛN provoque une reprise à gauche : F_frot=+f_dN et a₂=(F+f_dN)/m. La solution repart de x_arrêt avec v=0 ; x et v restent donc continus.','Le coefficient f_d est égal au rapport choisi multiplié par fₛ ; 0≤f_d≤fₛ. Le bilan exact est W_F=E_c(t)−E_c(0)+Q avec Q=f_dN×distance parcourue. Après une inversion, la distance parcourue diffère de |x|.'],
      ['Caisse sans basculement ; sol horizontal ; force horizontale constante appliquée suffisamment bas.','Le premier graphique compare des essais indépendants initialement au repos. Les graphiques en temps correspondent à l’état initial choisi, repos ou vitesse v₀ positive.','Une solution analytique par morceaux traite l’arrêt comme un événement et vérifie de nouveau la loi statique avant de poursuivre le mouvement.'])

def plan_incline(p):
    alpha=np.radians(p['alpha']); m,R,fs=p['mass'],p['radius'],p['fs']; fd=fs*p['ratio']; body=p['body']; k={'cylinder':.5,'sphere':.4,'ring':1.,'block':0}[body]; n=m*G*np.cos(alpha)
    if body=='block':
        stuck=math.tan(alpha)<=fs+1e-12; sliding=not stuck; acc=0. if stuck else G*(np.sin(alpha)-fd*np.cos(alpha)); angular=0.; force=m*G*np.sin(alpha) if stuck else fd*n; regime='Adhérence, caisse immobile' if stuck else 'Glissement de la caisse'
    else:
        required=m*G*np.sin(alpha)*k/(1+k); sliding=required>fs*n+1e-12; stuck=False
        if sliding: acc=G*(np.sin(alpha)-fd*np.cos(alpha)); angular=fd*G*np.cos(alpha)/(k*R); force=fd*n; regime='Roulement avec glissement'
        else: acc=G*np.sin(alpha)/(1+k); angular=acc/R; force=required; regime='Roulement sans glissement'
    t=np.linspace(0,p['duration'],401); v=acc*t; x=.5*acc*t*t; omega=angular*t; slip=x-.5*R*angular*t*t; kinetic=.5*m*v*v+.5*k*m*R*R*omega*omega; work=m*G*np.sin(alpha)*x; loss=force*slip if sliding else np.zeros_like(t)
    angles=np.linspace(0,65,261); threshold=fs if body=='block' else fs*(1+k)/k
    return result([metric('Régime',regime),metric('Accélération du centre de masse',acc,'m/s²'),metric('Réaction tangentielle (norme)',force,'N'),metric('Réaction normale',n,'N'),metric('Vitesse de glissement finale',float(v[-1]-R*omega[-1]),'m/s'),metric('Énergie dissipée',float(loss[-1]),'J'),metric('Écart du bilan énergétique',float(np.max(np.abs(work-kinetic-loss))),'J')],
      [chart('Vérifier la condition de contact avant le calcul','Angle du plan (°)','Rapport sans dimension',series('tan α',angles,np.tan(np.radians(angles))),series('Seuil d’adhérence ou de roulement',angles,np.full(len(angles),threshold))),chart('Translation, rotation et glissement','Temps (s)','Vitesse (m/s)',series('v_G',t,v),series('Rω',t,R*omega),series('v_contact=v_G−Rω',t,v-R*omega)),chart('Où va le travail du poids ?','Temps (s)','Énergie (J)',series('Travail du poids',t,work),series('Énergie cinétique totale',t,kinetic),series('Énergie dissipée',t,loss))],
      dict(kind='friction',title='Descente sur le plan incliné',description='x mesure le déplacement suivant la pente, positif vers le bas.',time=t,x=x,v=v,alpha=alpha,mass=m,radius=R,omega=omega,body=body),
      ['Pour une caisse, la condition de repos est mg sinα≤fₛmg cosα, soit tanα≤fₛ. Le frottement vaut alors mg sinα, pas nécessairement fₛN.','Pour un objet roulant, écrire ma=mg sinα−T et Iω̇=TR. Avec a=Rω̇ et I=kmR², a=g sinα/(1+k) et T=kmg sinα/(1+k).','Ce roulement demande [k/(1+k)]tanα≤fₛ. Sinon utiliser T=f_dN, calculer séparément a et ω̇, puis vérifier le sens de v_G−Rω.','Le frottement statique peut effectuer un travail −Tx_G sur le centre de masse tout en fournissant +T RΔrotation à la rotation. Sa puissance totale T·v_contact est nulle en roulement sans glissement.'],
      ['Plan fixe, objet initialement au repos, contact sans perte de contact ni résistance au roulement.','Après démarrage en glissement, les paramètres retenus gardent v_contact dirigée vers le bas. La force de frottement s’y oppose.'])

def gyroscope(p):
    m,ell,r=p['mass'],p['ell'],p['radius']; i3=.5*m*r*r; i1=m*(ell*ell+r*r/4); spin=2*math.pi*p['spin']; s=i3*spin; slow=m*G*ell/s; th=np.radians(p['theta']); n0=np.array([np.sin(th),0.,np.cos(th)]); ez=np.array([0.,0.,1.]); rate=slow if p['launch']=='slow' else 0.; ndot=rate*np.cross(ez,n0); l0=i1*np.cross(n0,ndot)+s*n0
    def fun(y):
        n,l=y[:3],y[3:]; return np.r_[np.cross(l,n)/i1,-m*G*ell*np.cross(n,ez)]
    def project(y):
        q=y[:3]/np.linalg.norm(y[:3]); l=y[3:]; l=l+(s-np.dot(l,q))*q; return np.r_[q,l]
    dt=min(.004,.08*i1/max(np.linalg.norm(l0),.001)); t,y=rk4(fun,np.r_[n0,l0],p['duration'],dt=dt,project=project); n,l=y[:,:3],y[:,3:]; transverse=l-s*n; energy=np.sum(transverse*transverse,axis=1)/(2*i1)+s*s/(2*i3)+m*G*ell*n[:,2]
    theta=np.arccos(np.clip(n[:,2],-1,1)); phi=np.unwrap(np.arctan2(n[:,1],n[:,0])); ts,ns=thinning(t,n); approx=np.c_[np.sin(th)*np.cos(slow*t),np.sin(th)*np.sin(slow*t),np.full(len(t),np.cos(th))]
    return result([metric('Précession lente approchée',slow,'rad/s'),metric('Rapport précession / rotation propre',slow/spin),metric('Écart entre inclinaisons extrêmes',float(np.degrees(np.ptp(theta))),'°'),metric('Écart maximal de l’énergie',float(np.max(np.abs(energy-energy[0]))),'J'),metric('Écart maximal de L_z',float(np.max(np.abs(l[:,2]-l[0,2]))),'kg·m²/s'),metric('Inertie axiale I₃',i3,'kg·m²'),metric('Inertie transversale en O I₁',i1,'kg·m²')],
      [chart('Comparer la précession réelle à l’approximation lente','Temps (s)','Azimut déroulé (°)',series('Intégration complète',t,np.degrees(phi)),series('Précession lente',t,np.degrees(slow*t))),chart('La nutation est une oscillation de l’inclinaison','Temps (s)','Inclinaison θ (°)',series('θ intégrée',t,np.degrees(theta)),series('θ supposée constante',t,np.full(len(t),p['theta']))),chart('Contrôler l’énergie du modèle complet','Temps (s)','Énergie (J)',series('Énergie totale',t,energy))],
      dict(kind='gyroscope',title='Axe de la toupie pesante',description='La courbe réelle est calculée avec le couple du poids. La précession lente n’est qu’une approximation.',time=ts,axis=ns,length=ell,approx_axis=approx[np.unique(np.linspace(0,len(t)-1,min(700,len(t))).astype(int))]),
      ['Le modèle est un solide de révolution fixé en O : I₃=mr²/2 et I₁=m(ℓ²+r²/4). Le poids s’applique en G=ℓn.','Poser s=L·n=I₃ω₃, constant. Les équations intégrées sont ṅ=(L×n)/I₁ et L̇=−mgℓ(n×e_z). Elles évitent les singularités des angles d’Euler.','Si L≈s n et si l’inclinaison varie peu, dL/dt≈Ω_p e_z×L donne Ω_p≈mgℓ/s. Augmenter la rotation propre ralentit la précession.','Le modèle complet conserve E=|L−sn|²/(2I₁)+s²/(2I₃)+mgℓn_z et L_z. Le lâcher sans précession initiale peut produire de la nutation. Comparer les courbes avant d’utiliser l’approximation.'],
      ['Pivot fixe sans frottement ; solide axisymétrique ; inerties indiquées définissent le modèle et ne prétendent pas représenter toutes les toupies.','La précision est contrôlée par E et L_z. Un petit rapport Ω_p/ω₃ est nécessaire mais ne suffit pas à supprimer toute nutation initiale.'])

COMPUTE={name:globals()[name] for name in ['inertie_huygens','konig','barre_bascule','barre_rotule','cylindre_bord','coulomb_horizontal','plan_incline','gyroscope']}
