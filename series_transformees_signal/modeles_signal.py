"""Modèles spectraux et numériques : conventions en Hz et facteurs explicites."""
from __future__ import annotations
import math
import numpy as np
from commun import metric as m, chart as c, series as s, scene, result, integrate

def alias_frequency(f,F):
    return (f+F/2)%F-F/2

def window_values(name,N):
    phase=2*np.pi*np.arange(N)/N
    if name=='hann':return .5-.5*np.cos(phase)
    if name=='blackman':return .42-.5*np.cos(phase)+.08*np.cos(2*phase)
    return np.ones(N)

def amplitude_spectrum(y,F,window='rect',padding=1):
    N=len(y);w=window_values(window,N);z=np.fft.rfft(y*w,n=N*int(padding))
    amp=np.abs(z)/w.sum();amp[1:]*=2
    if N*int(padding)%2==0:amp[-1]/=2
    return np.fft.rfftfreq(N*int(padding),1/F),amp

def pack(metrics,charts,title,description,steps,assumptions,kind='signal',**data):
    return result(metrics,charts,scene(kind,title,description,**data),steps,assumptions)

def poisson_gaussienne(p):
    sigma,T,N=p['sigma'],p['T'],int(p['N']);t=np.linspace(-T,T,601)
    K=max(N,int(math.ceil(10*sigma/T+3)))
    direct=sum(np.exp(-((t+k*T)/sigma)**2/2) for k in range(-K,K+1))
    k=np.arange(1,N+1);coef=np.sqrt(2*np.pi)*sigma/T*np.exp(-2*np.pi**2*sigma**2*k*k/T**2)
    dual=np.sqrt(2*np.pi)*sigma/T+2*np.sum(coef[:,None]*np.cos(2*np.pi*k[:,None]*t/T),axis=0)
    return pack([m('Écart maximal des troncatures',float(np.max(abs(direct-dual)))),m('Coefficient moyen c₀',np.sqrt(2*np.pi)*sigma/T),m('Termes directs de chaque côté',K)],
    [c('Poisson : même signal, deux constructions','t / s','Amplitude',s('Somme de gaussiennes',t,direct),s('N raies de Fourier',t,dual)),c('Spectre discret','k / T / Hz','|cₖ|',s('Coefficients positifs',np.arange(N+1)/T,np.r_[np.sqrt(2*np.pi)*sigma/T,coef]))],
    'Une identité temps-fréquence','Périodiser dans le temps produit des raies dans le spectre.',
    ['Partir de la TF d’une gaussienne en Hz.','Calculer cₖ = ŝ(k/T)/T.','Comparer les sommes puis augmenter N quand les impulsions sont étroites.'],
    ['Identité de Poisson appliquée à une gaussienne de Schwartz : les échanges sont justifiés.','Somme directe tronquée à au moins 10σ de distance ; somme spectrale tronquée à |k| ≤ N.'],kind='comb',period=T)

def shannon(p):
    F,B,f0,M=p['F'],p['B'],p['f0'],int(p['M']);t=np.linspace(-1.5,1.5,601)
    fun=lambda x:np.sinc(B*x)**2*np.cos(2*np.pi*f0*x)
    n=np.arange(-M,M+1);tn=n/F;yn=fun(tn)
    rec=np.sinc(F*t[:,None]-n)@yn
    nu=np.linspace(-max(2*F,25),max(2*F,25),601)
    tri=lambda x:np.maximum(1-abs(x)/B,0)/B
    spec=lambda x:.5*(tri(x-f0)+tri(x+f0))
    original=spec(nu);K=int(math.ceil((float(np.max(abs(nu)))+f0+B)/F));replicas=sum(spec(nu-k*F) for k in range(-K,K+1))
    error=float(np.max(abs(rec-fun(t))));nyquist=F>2*(f0+B);visible=abs(tn)<=1.5
    return pack([m('Borne du support spectral',f0+B,'Hz'),m('Seuil strict 2(f₀+B)',2*(f0+B),'Hz'),m('Bandes sans chevauchement','Oui' if nyquist else 'Seuil ou chevauchement'),m('Erreur sur la fenêtre affichée',error),m('Nombre d’échantillons',2*M+1)],
    [c('Reconstruire le paquet','t / s','Amplitude',s('Signal exact',t,fun(t)),s('Somme sinc tronquée',t,rec),dict(s('Mesures',tn[visible],yn[visible]),style='dots')),c('Spectre et copies dues au peigne','ν / Hz','TF (unités de temps)',s('ŝ(ν)',nu,original),s('TF du signal échantillonné / F',nu,replicas))],
    'De la mesure au signal continu','Le critère spectral précède la reconstruction.',
    ['s(t)=sinc²(Bt)cos(2πf₀t), avec sinc(u)=sin(πu)/(πu).','TF[sinc²(Bt)] = max(1−|ν|/B,0)/B.','Avec a=1/F : TF du peigne = F Σδ(ν−kF).','Reconstruire Σs(n/F)sinc(Ft−n) ; augmenter M pour distinguer troncature et repliement.'],
    ['Signal continu appartenant à L¹ et L² ; support spectral inclus dans [−(f₀+B), f₀+B].','Le théorème utilise une somme infinie. L’expérience emploie 2M+1 mesures. L’écart est mesuré sur [−1,5 ; 1,5] : il peut provenir de la troncature et, sous le seuil, du repliement.'],kind='sampling',samples_t=tn,samples_y=yn,rate=F,band=f0+B)

def aliasing(p):
    F,f,phi=p['F'],p['f'],np.deg2rad(p['phase']);fa=alias_frequency(f,F)
    t=np.linspace(0,.8,601);tn=np.arange(int(.8*F)+1)/F
    true=np.sin(2*np.pi*f*t+phi);app=np.sin(2*np.pi*fa*t+phi);yn=np.sin(2*np.pi*f*tn+phi)
    return pack([m('Fréquence réelle',f,'Hz'),m('Fréquence apparente signée',fa,'Hz'),m('Erreur aux instants de mesure',float(np.max(abs(yn-np.sin(2*np.pi*fa*tn+phi))))),m('Échantillons',len(tn))],
    [c('Des courbes différentes, des points identiques','t / s','Amplitude',s('Sinusoïde réelle',t,true),s('Représentant de Nyquist',t,app),dict(s('Mesures communes',tn,yn),style='dots'))],
    'Une ambiguïté de mesure','Les phases sont égales modulo 2π aux instants k/F.',
    ['Ramener f modulo F dans [−F/2,F/2[.','Écrire 2π(f−fₐ)k/F = 2πℓk.','À f=F/2, sin(πk+φ)=(-1)ᵏsin φ : toutes les phases ne sont pas identifiables.'],
    ['Sinusoïdes idéales, signal périodique d’énergie infinie : illustration de l’ambiguïté, distincte du paquet L¹∩L² du TP Shannon.','Une fréquence apparente négative encode un changement de phase ; sa valeur absolue donne la fréquence du motif.'],kind='sampling',rate=F,samples_t=tn,samples_y=yn)

def butterworth_response(f,fc,n):
    poles=np.exp(1j*np.pi*(2*np.arange(n)+1+n)/(2*n))
    return np.prod(-poles[:,None]/(1j*np.atleast_1d(f)[None,:]/fc-poles[:,None]),axis=0)

def anti_repliement(p):
    F,fc,f,A,n=p['F'],p['fc'],p['noise_f'],p['amplitude'],int(p['order']);fu=3
    hu,hn=butterworth_response(np.array([fu,f]),fc,n);fa=alias_frequency(f,F)
    t=np.linspace(0,1,601);tn=np.arange(int(F)+1)/F
    raw=np.cos(2*np.pi*fu*t)+A*np.cos(2*np.pi*f*t)
    filtered=(hu*np.exp(2j*np.pi*fu*t)+A*hn*np.exp(2j*np.pi*f*t)).real
    nu=np.geomspace(.5,160,500);gain=abs(butterworth_response(nu,fc,n))
    return pack([m('Fréquence parasite repliée',abs(fa),'Hz'),m('Gain à la perturbation',abs(hn)),m('Atténuation du parasite',20*math.log10(abs(hn)),'dB'),m('Gain utile à 3 Hz',abs(hu)),m('Coupure / Nyquist',fc/(F/2))],
    [c('Chaîne analogique puis mesure','t / s','Amplitude',s('Sans filtre',t,raw),s('Après filtre analogique',t,filtered),dict(s('Mesures filtrées',tn,(hu*np.exp(2j*np.pi*fu*tn)+A*hn*np.exp(2j*np.pi*f*tn)).real),style='dots')),c('Sélectivité de Butterworth','ν / Hz','Gain / dB',s('20 log₁₀|H|',nu,20*np.log10(gain)),x_scale='log')],
    'Filtrer avant de perdre l’information','Une fois les bandes repliées, un filtre numérique ne sépare pas des fréquences indiscernables.',
    ['Pôles unitaires de Butterworth dans le demi-plan gauche ; H(0)=1.','Calculer les gains complexes à 3 Hz et à la fréquence perturbatrice.','Échantillonner ensuite les sinusoïdes atténuées et déphasées.'],
    ['Filtre analogique idéal de Butterworth, régime permanent ; transitoire de mise en marche absent.','Le filtre n’a pas de coupure spectrale abrupte : il atténue le repliement sans garantir une bande strictement limitée.'],kind='filter',poles=np.column_stack((np.exp(1j*np.pi*(2*np.arange(n)+1+n)/(2*n)).real*2*np.pi*fc,np.exp(1j*np.pi*(2*np.arange(n)+1+n)/(2*n)).imag*2*np.pi*fc)))

def fenetres_fft(p):
    N,F,pad=int(p['N']),128,int(p['padding']);t=np.arange(N)/F;y=np.cos(2*np.pi*p['f']*t+.3)
    w=window_values(p['window'],N);nu,a=amplitude_spectrum(y,F,p['window'],pad);mask=nu<=50
    # Limit exported plot size without changing the computation or peak metric.
    ids=np.flatnonzero(mask);ids=ids[::max(1,math.ceil(len(ids)/640))]
    enbw=F*np.sum(w*w)/np.sum(w)**2
    return pack([m('Durée T=N/F',N/F,'s'),m('Espacement des cases natives',F/N,'Hz'),m('Pas de la courbe interpolée',F/(N*pad),'Hz'),m('Gain cohérent de fenêtre',float(np.mean(w))),m('Bande équivalente de bruit',enbw,'Hz'),m('Amplitude au maximum interpolé',float(np.max(a)))],
    [c('Signal et fenêtre','t / s','Amplitude',s('Signal',t,y),s('Fenêtre w',t,w),s('Produit y·w',t,y*w)),c('Amplitude monolatérale corrigée','ν / Hz','Amplitude',s('FFT / Σw (×2 hors DC et Nyquist)',nu[ids],a[ids]))],
    'Une FFT sur une durée finie','Multiplier par une fenêtre convolue le spectre avec celui de cette fenêtre.',
    ['T=N/F avec F=128 Hz ; N mesures, dernier instant (N−1)/F.','Amplitude normalisée par Σw ; doubler les raies positives hors DC et Nyquist.','Le gain cohérent corrige une raie isolée sur une case, sans supprimer le biais hors case.','Ajouter des zéros échantillonne davantage le même spectre fenêtré.'],
    ['Fenêtres périodiques adaptées à la FFT ; aucun zéro supplémentaire n’est une nouvelle mesure.','Amplitudes de pics hors case et de raies non résolues restent dépendantes de la fenêtre.'],kind='spectrum',frequencies=nu[ids],amplitudes=a[ids])

def resolution(p):
    N,F,pad=int(p['N']),128,int(p['padding']);delta=p['delta'];t=np.arange(N)/F
    y=np.cos(2*np.pi*18*t)+np.cos(2*np.pi*(18+delta)*t)
    nu,a=amplitude_spectrum(y,F,'hann',pad);mask=(nu>=10)&(nu<=30)
    return pack([m('Durée d’observation',N/F,'s'),m('Écart Δf',delta,'Hz'),m('Espacement natif 1/T',F/N,'Hz'),m('Δf·T',delta*N/F),m('Pas après ajout de zéros',F/(N*pad),'Hz')],
    [c('Battements observés sur la durée de mesure','t / s','Amplitude',s('Deux sinusoïdes',t,y),s('Enveloppe positive',t,2*abs(np.cos(np.pi*delta*t)))),c('Deux raies et un lobe de fenêtre','ν / Hz','Amplitude',s('FFT avec fenêtre de Hann',nu[mask],a[mask]))],
    'Une durée d’acquisition compte','La séparation dépend de la largeur des lobes, donc de T et de la fenêtre.',
    ['cos(2πf₁t)+cos(2πf₂t)=2cos(πΔft)cos(2π(f₁+f₂)t/2).','La largeur entre les premiers zéros du lobe de Hann vaut environ 4/T.','Comparer une durée multipliée par huit à huit fois plus de zéros.'],
    ['Signal sans bruit, amplitudes égales et phases initiales nulles.','1/T est le pas natif ; la séparation réelle des pics dépend aussi du fenêtrage et du rapport des amplitudes.'],kind='spectrum')

def spectrogramme(p):
    F,N,L=128,384,int(p['length']);t=np.arange(N)/F;duration=N/F
    rate=(p['f1']-p['f0'])/duration
    y=np.cos(2*np.pi*(p['f0']*t+.5*rate*t*t));w=window_values('hann',L)
    starts=np.arange(0,N-L+1,8);centers=(starts+(L-1)/2)/F;nu=np.fft.rfftfreq(256,1/F)
    power=np.array([abs(np.fft.rfft(y[j:j+L]*w,n=256))**2/(F*np.sum(w*w)) for j in starts]).T
    db=10*np.log10(np.maximum(power,1e-10));db-=db.max();db=np.maximum(db,-65)
    ridge=p['f0']+rate*centers
    return pack([m('Fenêtre temporelle L/F',L/F,'s'),m('Pas natif F/L',F/L,'Hz'),m('Pente du chirp',rate,'Hz/s'),m('Nombre de tranches',len(starts))],
    [c('Un signal dont la fréquence évolue','t / s','Amplitude',s('Chirp',t,y)),c('Fréquence instantanée','t / s','ν / Hz',s('f₀ + kt',t,p['f0']+rate*t))],
    'Localiser l’énergie dans le temps et les fréquences','La carte affiche une STFT fenêtrée, en décibels relatifs au maximum.',
    ['Dériver la phase : ν(t)=f₀+kt.','Découper le signal avec une fenêtre de Hann de L points, déplacement de 8 points.','Calculer les FFT locales ; l’ajout de zéros à 256 points densifie la carte.','Une fenêtre courte suit les variations ; une fenêtre longue sépare mieux des raies stationnaires.'],
    ['Chirp réel de trois secondes, échantillonné à 128 Hz, fréquences sous 64 Hz.','Carte relative : PSD bilatérale positive |FFT|²/(FΣw²), normalisée à son maximum ; plancher −65 dB.'],kind='spectrogram',times=centers,frequencies=nu,db=db,ridge=ridge)

def modulation(p):
    t=np.linspace(0,2,601);fm,fc,depth=p['fm'],p['fc'],p['m'];phase=np.deg2rad(p['phase'])
    message=np.cos(2*np.pi*fm*t);env=1+depth*message
    mod=env*np.cos(2*np.pi*fc*t)
    demod=env*np.cos(2*np.pi*p['offset']*t+phase)
    return pack([m('Porteuse',fc,'Hz'),m('Bandes latérales',f'{fc-fm:g} et {fc+fm:g}','Hz'),m('Amplitude de chaque bande',depth/2),m('Surmodulation','Oui' if depth>1 else 'Non'),m('Gain synchrone cos φ',math.cos(phase))],
    [c('Message, enveloppe et porteuse modulée','t / s','Amplitude',s('Signal AM',t,mod),s('Enveloppe signée',t,env),s('− enveloppe',t,-env)),c('Après multiplication et passe-bas idéal','t / s','Amplitude',s('1 + m·message',t,env),s('Basses fréquences démodulées',t,demod)),c('Raies du spectre positif','ν / Hz','Amplitude',dict(s('Porteuse et bandes latérales',[fc-fm,fc,fc+fm],[depth/2,1,depth/2]),style='stems'))],
    'Multiplier pour déplacer des fréquences','Une porteuse transforme un message lent en bandes latérales.',
    ['Développer cos(2πfₘt)cos(2πf꜀t) en somme de deux cosinus.','Multiplier le signal reçu par 2cos(2π(f꜀+Δf)t+φ).','Un passe-bas idéal enlève les termes autour de 2f꜀ ; il reste (1+m cos2πfₘt)cos(2πΔft+φ).'],
    ['AM réelle, porteuse transmise, canal idéal ; fréquences normalisées pour voir les courbes.','Passe-bas idéal de la démodulation : les termes rapides sont supprimés analytiquement.','m>1 inverse le signe de l’enveloppe ; un simple détecteur d’enveloppe devient ambigu.'],kind='modulation')

def correlation_retard(p):
    F=200;t=np.arange(600)/F;delay=p['delay'];sigma=.075
    pulse=lambda x:np.exp(-((x-.4)/sigma)**2/2)*np.cos(2*np.pi*17*(x-.4))
    g=pulse(t);signal=pulse(t-delay);rng=np.random.default_rng(int(p['seed']));f=signal+p['noise']*rng.standard_normal(len(t))
    corr=np.correlate(f,g,'full')/F;lags=np.arange(-len(g)+1,len(f))/F
    norm=math.sqrt(float(np.sum(g*g)*np.sum(f*f)))/F
    corr/=norm if norm else 1
    mask=(lags>=0)&(lags<=1.4);peak=int(np.argmax(corr[mask]));estimated=lags[mask][peak]
    sample_ids=np.arange(0,len(t),2)
    return pack([m('Retard imposé',delay,'s'),m('Retard estimé',estimated,'s'),m('Distance aller-retour estimée',p['speed']*estimated/2,'m'),m('Maximum de corrélation normalisée',float(corr[mask][peak])),m('Pas de recherche',1/F,'s')],
    [c('Émission et réception','t / s','Amplitude',s('Impulsion codée émise g',t[sample_ids],g[sample_ids]),s('Réception f',t[sample_ids],f[sample_ids])),c('Chercher le retard','τ / s','C_fg / (‖f‖₂‖g‖₂)',s('Corrélation normalisée',lags[mask],corr[mask]))],
    'Un écho retrouvé dans le bruit','C_fg(τ)=∫conj(g(t))f(t+τ)dt : l’écho retardé donne un pic à τ positif.',
    ['Employer la convention de corrélation de la page 108.','Sommer les produits sur toute la fenêtre, avec Δt=1/F.','Normaliser par les énergies totales ; Cauchy-Schwarz borne le module par 1.','Pour un trajet aller-retour, d=cτ/2 ; le bruit peut déplacer le maximum.'],
    ['Deux signaux réels à énergie finie tronqués sur trois secondes, bruit gaussien reproductible.','La recherche se fait sur une grille de 5 ms ; le pic n’est pas une garantie de précision en bruit fort.'],kind='correlation')

def causal_filter(y,name,width):
    width=int(width)
    if name=='mean':return np.convolve(y,np.ones(width)/width,'full')[:len(y)]
    pole=math.exp(-1/width);out=np.empty_like(y);previous=0.
    for j,value in enumerate(y):previous=pole*previous+(1-pole)*value;out[j]=previous
    return out

def debruitage(p):
    F=128;t=np.arange(512)/F;ideal=np.sin(2*np.pi*p['f']*t)+.25*np.sin(2*np.pi*2*p['f']*t)
    rng=np.random.default_rng(int(p['seed']));noise=p['noise']*rng.standard_normal(len(t));raw=ideal+noise
    filtered=causal_filter(raw,p['filter'],p['width']);target=causal_filter(ideal,p['filter'],p['width'])
    start=min(int(5*p['width']),200);sl=slice(start,None)
    rms=lambda a:math.sqrt(float(np.mean(a[sl]**2)))
    distortion=rms(target-ideal);residual=rms(filtered-target);nu=np.linspace(0,F/2,401);omega=2*np.pi*nu/F
    if p['filter']=='mean':
        H=np.mean(np.exp(-1j*omega[:,None]*np.arange(int(p['width']))),axis=1)
        variance_factor=1/p['width']
    else:
        pole=math.exp(-1/p['width']);H=(1-pole)/(1-pole*np.exp(-1j*omega));variance_factor=(1-pole)/(1+pole)
    return pack([m('Bruit avant : RMS mesuré',rms(noise)),m('Bruit après : RMS mesuré',residual),m('Distorsion du signal utile : RMS',distortion),m('Facteur théorique de variance du bruit',variance_factor),m('Échantillons exclus du bilan',start)],
    [c('Signal utile, mesure et sortie','t / s','Amplitude',s('Signal utile',t,ideal),s('Signal bruité',t,raw),s('Sortie filtrée',t,filtered),s('Signal utile filtré',t,target)),c('Réponse fréquentielle numérique','ν / Hz','|H|',s('Module du filtre',nu,abs(H)))],
    'Réduire le bruit a un coût','La sortie idéale du même filtre distingue bruit résiduel et déformation du signal.',
    ['Écrire le filtre causal et sa réponse impulsionnelle.','Pour du bruit blanc indépendant : Var(sortie)=σ²Σh[k]².','Calculer séparément sortie(signal+bruit)−sortie(signal) et sortie(signal)−signal.','Écarter le transitoire initial du bilan RMS ; comparer aux facteurs de variance.'],
    ['Bruit blanc gaussien ; une réalisation finie fluctue autour du bilan théorique.','Filtre récursif de pôle exp(−1/largeur), associé à une constante de temps largeur/F ; repos initial nul.'],kind='filter')

MODELS={name:globals()[name] for name in ['poisson_gaussienne','shannon','aliasing','anti_repliement','fenetres_fft','resolution','spectrogramme','modulation','correlation_retard','debruitage']}
def calculate(lab_id,p):return MODELS[lab_id](p)
