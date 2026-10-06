# Lecture scientifique du recueil et conventions de l’atelier

Le recueil fournit les situations expérimentales et les questions de départ. L’atelier développe leurs calculs en explicitant les hypothèses, les unités et les limites des modèles. Les remarques ci-dessous portent sur les pages de l’extrait privé `MemoCPGEScientifAR2027-mecaFluides.pdf` ; elles ne remettent pas en cause l’intérêt pédagogique des situations proposées. La pagination imprimée est accompagnée de la page dans le PDF, comptée à partir de 1. Les points de signe et de dimension des pages 315, 316, 321, 323 et 326 ont aussi été vérifiés sur les pages rendues, au-delà de l’extraction du texte.

## 1. Distinguer onde mécanique et onde électromagnétique

**Page 291, PDF 1.** Une onde mécanique exige un milieu matériel. Une onde électromagnétique peut être transverse et se propager dans le vide : elle ne devient pas pour autant une onde mécanique. Pour une onde stationnaire de forme `A(x) cos(ωt)`, deux ventres séparés par un nœud vibrent en opposition de phase lorsque `A(x)` change de signe. Les points ne sont donc pas tous en phase ; un nœud ne vibre pas.

**Dans l’atelier :** séparer oscillation locale, déplacement de la phase et transport d’énergie, notamment dans `houle`, `acoustique` et `conduit`.

## 2. Une image stroboscopique fixe n’identifie pas une fréquence unique

**Page 293, PDF 3.** Des éclairs de fréquence `fe` prélèvent le mouvement aux instants `n/fe`. Des fréquences différentes peuvent produire les mêmes phases échantillonnées. Une image fixe à 50 Hz, puis deux phases alternées à 100 Hz, ne suffit donc pas à prouver à elle seule une fréquence de mouvement égale à 50 Hz : d’autres multiples impairs conviennent aussi pour une oscillation sinusoïdale.

**Dans l’atelier :** la galerie `diffraction.svg` montre le même échantillonnage à 50 Hz pour deux oscillations à 25 et 75 Hz. Il faut une information indépendante, une mesure temporelle ou un protocole de variation contrôlé pour lever l’ambiguïté.

## 3. Dans un guide, célérité du milieu et vitesses axiales diffèrent

**Pages 297–299, PDF 7–9.** Pour des parois rigides rectangulaires, `kz²=(ω/c)²−(mπ/a)²−(nπ/b)²`. Un mode transverse a une coupure `fc`. Au-dessus de celle-ci, `vφ=ω/kz` et `vg=dω/dkz=c²kz/ω`, donc `vφ vg=c²`. La vitesse de phase axiale dépasse `c`, tandis que la vitesse de groupe lui est inférieure. Le mode uniforme `(0,0)` fait exception : il n’a pas de coupure et ses deux vitesses valent `c`.

**Dans l’atelier :** `conduit` affiche séparément les deux vitesses et le régime évanescent ; la décroissance sous coupure n’est pas assimilée à une absorption visqueuse.

## 4. Rotation d’un récipient : le terme centrifuge a une dimension d’accélération

**Page 310, PDF 14.** Dans le référentiel tournant à vitesse angulaire constante, l’accélération centrifuge est `Ω²r er`, orientée vers l’extérieur. Son potentiel est `−Ω²r²/2`. Le facteur `1/2` appartient au potentiel, pas à l’accélération. La surface libre est bien une paraboloïde : `zs=zc+Ω²r²/(2g)`.

**Dans l’atelier :** l’illustration `hydrostatique.svg` fixe également `zc` par le volume conservé. Une constante d’intégration est déterminée par une donnée physique.

## 5. Potentiel des vitesses : il faut préciser le domaine

**Page 314, PDF 18.** Un champ de rotationnel nul admet un potentiel local. Pour un potentiel global univoque, des hypothèses topologiques supplémentaires, par exemple un domaine simplement connexe, sont nécessaires. À l’extérieur d’un cœur de vortex, le champ en `1/r` a un rotationnel nul mais une circulation non nulle sur les cercles entourant le cœur.

**Dans l’atelier :** `vortex` distingue vorticité locale et circulation intégrale. La fonction de courant scalaire utilisée en dimension deux ne devient pas automatiquement une description par surfaces des lignes de courant en dimension trois.

## 6. Bernoulli instationnaire : signe de ∂tφ et fonction d’intégration

**Page 315, PDF 19 ; rappel page 321, PDF 25.** Avec la convention `v=grad φ`, un fluide parfait homogène et un champ irrotationnel vérifient

`∂tφ + |v|²/2 + p/ρ + gz = C(t)`.

Le signe devant `∂tφ` est positif. L’intégration spatiale donne une fonction du temps, constante dans l’espace sur chaque composante connexe. La remplacer par une constante absolue demande une justification de jauge. Pour Bernoulli stationnaire le long d’une ligne de courant, une autre ligne peut porter une autre constante si l’écoulement est rotationnel.

**Dans l’atelier :** le bilan entre sections ajoute explicitement pompe, pertes de charge et coefficient d’énergie cinétique `α`. Un fluide incompressible peut avoir un écoulement rotationnel ; l’incompressibilité n’autorise pas à elle seule un Bernoulli global.

## 7. Reynolds : préciser la géométrie avant de citer un seuil

**Page 315, PDF 19.** Les valeurs proches de 2 000–3 000 sont des repères pour certaines conduites, avec une vitesse et une longueur conventionnelles. Elles ne constituent pas des seuils universels pour toutes les géométries. Perturbations, rugosité, entrée et stabilité de l’écoulement comptent.

**Dans l’atelier :** `Re=UL/ν` est d’abord le rapport des temps diffusif et advectif. Le tube utilise le diamètre et la vitesse moyenne ; `blasius` utilise la distance au bord d’attaque. Une solution laminaire formelle peut rester affichée alors que ses conditions de réalisation doivent être discutées.

## 8. Contrainte visqueuse : employer η, et non ν

**Page 316, PDF 20.** La viscosité dynamique `η` a l’unité Pa·s ; la viscosité cinématique `ν=η/ρ` a l’unité m²·s⁻¹. Une contrainte de cisaillement vaut `τxy=η ∂yu`. Le coefficient d’un tenseur de contrainte ne peut donc pas être `ν` si celui-ci conserve sa définition cinématique.

Pour un fluide newtonien isotrope incompressible, `τ=2ηD`, avec `D=(grad v+grad vᵀ)/2`. La rotation rigide ne dissipe pas. Pour un fluide compressible, une viscosité volumique doit aussi être considérée.

**Dans l’atelier :** `newtonien` vérifie le bilan `τ:grad v=2ηD:D≥0`, en W·m⁻³, et la distinction des deux viscosités.

## 9. Diffusion visqueuse : √t et conditions aux deux parois

**Page 316, PDF 20.** La longueur caractéristique du premier problème de Stokes est `δ=2√(νt)`, et non `2√ν × t`. L’analyse des unités permet déjà de trancher : `√ν` a l’unité m·s⁻¹ᐟ². Cette longueur n’est pas un front net.

La solution `u/U=erfc[y/(2√νt)]` décrit un **demi-espace** dont une paroi démarre à vitesse `U`. Si une seconde paroi fixe est située à `y=h`, elle doit satisfaire `u(h,t)=0`. La solution est alors une série de Fourier, ou une série d’images équivalente, qui tend vers `U(1−y/h)`.

**Dans l’atelier :** `diffusion` propose les deux domaines séparément et compare leurs limites. Une référence primaire indépendante est la [résolution du premier problème de Stokes par le MIT](https://ocw.mit.edu/courses/2-25-advanced-fluid-mechanics-fall-2013/6c64b72340cd5b5da9a0d59516b63aec_MIT2_25F13_SolutionStokes1.pdf).

## 10. Poiseuille : la chute positive de pression fixe le signe du débit

**Page 321, PDF 25.** Si l’on définit `Δp=p(L)−p(0)`, une pression décroissante donne `Δp<0`, et le profil positif vers `+x` vaut `−Δp(R²−r²)/(4ηL)`. L’atelier choisit plutôt `Δpdrop=p(0)−p(L)>0`, d’où

`u(r)=Δpdrop(R²−r²)/(4ηL)`, `Q=πR⁴Δpdrop/(8ηL)`.

Dans un tube incliné, le gradient moteur porte sur `p+ρgz`. Le bilan dissipatif utilise la chute de cette charge mécanique. La moyenne `ū=u_max/2` provient de l’intégrale cylindrique `2π∫u(r)r dr`, pas d’une moyenne uniforme des rayons.

## 11. Magnus : la circulation ne se déduit pas de la seule rotation du cylindre idéal

**Page 321, PDF 25.** Un fluide parfait impose l’imperméabilité de la paroi, et non l’adhérence. Le problème potentiel autour d’un cylindre admet une circulation `Γ` à spécifier. Une loi telle que `Γ=2πR²Ω` est une hypothèse supplémentaire ; elle n’est pas une conséquence universelle de la vitesse de rotation de l’objet.

**Dans l’atelier :** `Γ` est le paramètre du laboratoire `magnus`. Avec `U∞` vers `+x` et `Γ` positive antihoraire, la force par unité de longueur vaut `Fy′=−ρU∞Γ`. Le signe est contrôlé par l’intégration des pressions, et la traînée idéale est nulle. Pour un objet réel, viscosité et décollement interviennent. Voir le [cours primaire du MIT sur cylindre et circulation](https://ocw.mit.edu/courses/16-01-unified-engineering-i-ii-iii-iv-fall-2005-spring-2006/52b148916995923bec75c35a36deedd0_f16_fall.pdf).

## 12. Bruit et analyse spectrale

**Page 322, PDF 26.** Un bruit peut être analysé spectralement. L’absence de périodicité empêche généralement de le décrire par une série discrète d’harmoniques d’une période unique ; elle n’interdit ni la transformée de Fourier ni une densité spectrale de puissance.

**Conséquence pédagogique :** distinguer une sinusoïde, un signal périodique composé et un signal aléatoire avant d’interpréter son spectre.

## 13. Diffraction : aucun premier zéro lorsque λ>a

**Page 323, PDF 27.** Les données `f=25 kHz`, `c=340 m/s` et `a=1 cm` donnent `λ=13,6 mm>a`. Dans le modèle de fente uniforme en champ lointain,

`I(θ)/I(0)=[sin(πa sinθ/λ)/(πa sinθ/λ)]²`.

Le premier zéro exigerait `sinθ=λ/a>1` : il n’existe pas dans l’hémisphère propagatif. On ne peut pas convertir `λ/a=1,36` en un petit angle de premier zéro. Le lobe est large ; une largeur à mi-hauteur ou un seuil de détection peut définir un autre critère, à annoncer explicitement.

**Dans l’atelier :** `diffraction` trace la loi avec `sinθ`, précise l’absence de zéro et réserve `θ≈λ/a` aux petits rapports.

## 14. Atténuation acoustique : le signe dépend de la convention temporelle

**Page 326, PDF 30.** Avec `p∝exp[i(kx−ωt)]` et l’équation `p_tt/c²−Δp−τ ∂tΔp=0`, où `τ=4η/(3ρc²)` dans le modèle visqueux donné, la substitution fournit

`k²(1−iωτ)=ω²/c²`.

Le signe est donc `−iωτ` pour cette convention. La branche `Im(k)>0` donne une amplitude décroissante vers `+x`. Avec la convention temporelle opposée, les signes complexes doivent être changés ensemble. Une atténuation visqueuse, un mode sous coupure et une diminution de pression dans un tube sont trois phénomènes différents.

## Choix explicites des prolongements

Le modèle de Stokes autour d’une sphère exige `Re≪1` ; une corrélation de traînée à Reynolds fini n’est pas sa démonstration. Blasius est un modèle laminaire de couche limite plane, sans gradient de pression extérieur. La MHD de Hartmann impose ici un circuit transverse court-circuité `Ez=0` et un faible Reynolds magnétique. L’onde d’Alfvén utilise un autre modèle, idéal. Le TP `thermo` compare les limites isotherme et isentropique du gaz parfait, sans fabriquer de loi de relaxation intermédiaire.

Le [cours primaire de transport du MIT](https://live.ocw.mit.edu/courses/3-185-transport-phenomena-in-materials-engineering-fall-2003/6e459228e4e97c9c29e50c481b262c5c_lectures.pdf) fournit une référence indépendante pour la similitude de Blasius et son coefficient `f″(0)≈0,332`.

Pour les autres prolongements, consulter la [leçon de MHD de l’université du Wisconsin](https://magnetohydrodynamics.physics.wisc.edu/lecture5.html) pour Hartmann et la fermeture électrique, le [cours du MIT sur les vagues](https://ocw.mit.edu/courses/2-017j-design-of-electromechanical-robotic-systems-fall-2009/resources/mit2_017jf09_ch06/) pour la dispersion, et la [documentation et le code de référence OpenFOAM](https://cpp.openfoam.org/v12/classFoam_1_1dragModels_1_1SchillerNaumann.html) pour la corrélation de Schiller–Naumann. Ces références complètent les démonstrations présentes dans l’atelier.

## Navier–Stokes : information datée

Vérification le **6 octobre 2026** : dans son [annonce du 11 septembre 2026](https://www.claymath.org/news/navier-stokes-announcement/), le Clay Mathematics Institute indique que le problème a « apparently been settled » et décrit une évaluation progressive selon ses règles. Cette page ne confirme pas l’attribution d’un prix. Le laboratoire illustre une solution exacte particulière en dimension deux, Taylor–Green, et son bilan d’énergie ; il n’évalue pas la preuve annoncée ni le problème général en dimension trois.
