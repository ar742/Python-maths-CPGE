# Fluides & Ondes : un parcours sup / spé

Commencer par pression, force et bilan d’énergie. En spé, relier les profils aux conditions aux limites et les ondes aux hypothèses de propagation. Les modèles de couche limite, de tourbillons et de MHD viennent ensuite.

Prévoir 60 à 90 minutes par séance prioritaire, avec un bilan rédigé. Les prolongements peuvent être étudiés séparément après les techniques qu’ils réutilisent.

Repères PCSI, PC et PSI. Le socle commun du parcours porte sur pression, conservation, forces, énergie et ondes. PC utilise Navier–Stokes incompressible ; PSI exclut l’utilisation d’Euler et de Navier–Stokes. Les équations fournies des TP ne créent donc pas une obligation identique pour toutes les filières. Taylor–Green, Blasius complet et MHD sont des prolongements.

[Guide de lancement](LISEZ_MOI.md) · [Retour à l’atelier](README.md)

## Avant de commencer

- Notations communes : g est l’accélération de la pesanteur. Les bilans utilisent les unités SI ; convertir les mm, mPa·s et autres unités des curseurs avant un calcul.
- Sup : mécanique du point, pression, gaz parfait et bilans d’énergie.
- Sup : dérivation, intégration, oscillations et équations différentielles linéaires.
- Spé : débits, diffusion, ondes, nombres complexes et conditions aux limites ; calcul vectoriel lorsqu’il est introduit dans la filière.

## Pour chaque séance

1. Définir le système et préciser si le bilan est de masse, de quantité de mouvement ou d’énergie.
2. Convertir les unités puis prévoir un signe ou un facteur d’échelle.
3. Modifier une seule grandeur et contrôler une limite ou un bilan.
4. Séparer le résultat du modèle de son domaine de validité physique.

## Sup : trois séances de pression et de forces

Les lois de profil et de traînée nécessaires sont fournies ; les justifications commencent par des bilans simples.

### 1. Une pression sous l’eau et dans l’air

**Techniques incontournables** · Sup · statique et gaz parfait

Distinguer pression absolue, différence de pression et effet de compressibilité.

**À faire :** Noter z l’altitude, ρ la masse volumique et p la pression. Comparer le liquide incompressible et l’atmosphère isotherme. Doubler la profondeur dans le premier cas, puis modifier T dans le second.

**Acquis attendu :** Retrouver le signe de dp/dz=−ρg ; distinguer variation affine du liquide et loi exponentielle de l’atmosphère.

**Limites et compléments :** Température constante et gravité uniforme sont des hypothèses. Le modèle atmosphérique n’est pas une prévision météorologique.

**TP associés :** Pression, profondeur et atmosphère

### 2. Une paroi transmet une force visqueuse

**Techniques incontournables** · Sup → Spé · cisaillement et bilan de forces

Comprendre ce que mesure une viscosité et retrouver un profil élémentaire.

**À faire :** Noter η la viscosité dynamique, h la distance entre plaques et U₀,U₁ leurs vitesses. Choisir Couette sans gradient de pression ; augmenter η et comparer profil et contrainte. Comparer ensuite cisaillement et rotation solide dans le TP newtonien.

**Acquis attendu :** Relier contrainte à η∂u/∂y ; expliquer pourquoi une rotation solide ne produit pas la même déformation qu’un cisaillement.

**Limites et compléments :** La loi newtonienne est donnée ; les tenseurs généraux et l’étude complète du gradient de vitesse sont facultatifs. Convertir mPa·s en Pa·s.

**TP associés :** La viscosité mesure une déformation ; Couette–Poiseuille entre deux parois

### 3. Chute et traînée d’une sphère

**Techniques incontournables** · Sup · dynamique et vitesse limite

Écrire le bilan de forces avant de choisir une loi de traînée.

**À faire :** Noter R le rayon, U la vitesse relative, ρ et ρs les masses volumiques du fluide et de la sphère. Comparer poids, poussée et traînée ; calculer le Reynolds avec le diamètre 2R. Tester le régime lent.

**Acquis attendu :** Justifier une vitesse limite par la compensation des forces ; expliquer quand une traînée proportionnelle à U devient insuffisante.

**Limites et compléments :** Les expressions de Stokes et de traînée inertielle sont fournies. Le modèle d’interpolation n’est pas une loi universelle de tous les écoulements.

**TP associés :** Une sphère entre Stokes et inertie

## Spé : quatre séances de conservation et de propagation

Choisir les hypothèses puis appliquer les équations adaptées à la filière.

### 4. Lire un champ sans perdre la masse

**Techniques incontournables** · Spé · continuité et description eulérienne

Relier un champ de vitesse à la conservation du volume dans un cas incompressible.

**À faire :** Noter v le champ de vitesse, a le taux d’étirement et Ω la vitesse angulaire. Comparer les champs permanents de rotation et d’étirement ; vérifier la somme des dérivées diagonales de v et interpréter le bilan de flux d’un petit domaine.

**Acquis attendu :** Justifier la divergence nulle dans l’exemple et distinguer ligne de courant à un instant et trajectoire d’une particule.

**Limites et compléments :** L’équation locale dépend de la filière. La description lagrangienne détaillée, la fonction de courant et la décomposition générale du gradient sont des compléments, pas tout le travail prioritaire.

**TP associés :** Suivre une particule, lire un champ

### 5. Une conduite échange de l’énergie

**Techniques incontournables** · Spé · Bernoulli, pertes et pompe

Contrôler un bilan d’énergie en présence de changement de section et de hauteur.

**À faire :** Noter Q le débit, D₁,D₂ les diamètres, Δz la différence d’altitude et Δp la différence de pression. Commencer sans pertes ni pompe ; retrouver les vitesses par conservation du débit. Ajouter les pertes puis la pompe.

**Acquis attendu :** Attribuer un signe à chaque contribution et relier puissance hydraulique et puissance fournie avec le rendement annoncé.

**Limites et compléments :** La relation de Bernoulli idéale demande ses hypothèses. Les corrélations de pertes fournies ne couvrent pas toutes les conduites ni tous les régimes.

**TP associés :** Bernoulli généralisé : pertes et pompe

### 6. Un tube relie débit et pression

**Techniques incontournables** · Spé · écoulement laminaire et profil fourni

Passer d’un profil de vitesse à un débit et contrôler une forte dépendance géométrique.

**À faire :** Noter R le rayon du tube, L sa longueur, Δp la pression motrice et η la viscosité. Intégrer le profil parabolique sur la section ; doubler R à L,Δp,η fixés puis recalculer le Reynolds.

**Acquis attendu :** Retrouver Q proportionnel à R⁴ et distinguer vitesse maximale et vitesse moyenne ; vérifier que l’hypothèse laminaire reste adaptée.

**Limites et compléments :** PC peut établir le profil avec Navier–Stokes ; une autre filière utilise la loi fournie et le bilan. Développement d’entrée et turbulence ne sont pas décrits.

**TP associés :** Poiseuille : le rayon à la puissance quatre ; Couette–Poiseuille entre deux parois

### 7. Une onde sonore transporte un flux

**Techniques incontournables** · Spé · acoustique et thermodynamique

Relier pression acoustique, vitesse et propriété thermodynamique du milieu.

**À faire :** Noter ρ la masse volumique, c la célérité et Z=ρc l’impédance. Comparer deux milieux à une interface et vérifier les flux. Dans le gaz parfait, comparer compressions isotherme et adiabatique puis changer la fréquence.

**Acquis attendu :** Expliquer le rôle de l’impédance et de la compressibilité ; distinguer coefficients d’amplitude et rapports de puissance.

**Limites et compléments :** Linéarisation et petites amplitudes sont nécessaires. La comparaison thermique donne des échelles, sans résoudre toutes les pertes visqueuses et thermiques.

**TP associés :** Pression, vitesse et interface acoustique ; Pourquoi le son est-il adiabatique ?

## Approfondissements : trois familles d’ondes et de circulation

Ces applications utilisent les outils CPGE avec des relations complémentaires fournies.

### 8. Une vague n’emporte pas toute l’eau

**Approfondissement CPGE** · Spé · dispersion et ondes de surface

Distinguer propagation de phase et mouvement des particules.

**À faire :** Noter λ la longueur d’onde, h la profondeur et k=2π/λ. Comparer kh≪1 et kh≫1, puis diminuer λ pour examiner la tension superficielle. Contrôler aussi la petitesse de l’amplitude.

**Acquis attendu :** Lire les orbites et expliquer les deux limites de la relation de dispersion fournie ; distinguer vitesse de phase et de groupe.

**Limites et compléments :** Le modèle de houle linéaire est accompagné. Déferlement, écoulement moyen et théorie non linéaire ne sont pas déduits des orbites affichées.

**TP associés :** Houle, rides et orbites des particules

### 9. Conduit et fente sélectionnent des directions

**Approfondissement CPGE** · Spé · conditions aux limites et diffraction

Comparer une coupure de propagation et une ouverture diffractante.

**À faire :** Noter c la célérité, f la fréquence et m,n les indices du conduit. Comparer f à la coupure du mode choisi. Dans la fente, noter a la largeur et λ=c/f ; changer a/λ avant de prévoir les premiers zéros.

**Acquis attendu :** Distinguer propagation, évanescence et élargissement angulaire ; vérifier les limites des approximations de petits angles.

**Limites et compléments :** Les modèles de conduit et de fente sont fournis. Une onde évanescente n’a pas le même transport axial qu’un mode propagatif.

**TP associés :** Un conduit sélectionne les modes ; Diffraction : une fente devient une antenne

### 10. Une circulation creuse la pression et donne une portance

**Approfondissement CPGE** · Spé · tourbillon et Magnus guidés

Relier rotation, vitesse tangentielle et différence de pression.

**À faire :** Dans Rankine, noter R le rayon du cœur et Ω sa vitesse angulaire ; comparer intérieur et extérieur. Dans Magnus, noter Γ la circulation, U la vitesse lointaine et ρ la masse volumique ; inverser Γ.

**Acquis attendu :** Justifier le signe de la dépression et de la portance ; contrôler la continuité au bord du cœur du vortex.

**Limites et compléments :** Circulation et modèles de potentiel sont introduits ici. La rotation réelle d’un objet ne détermine pas automatiquement la Γ prescrite dans le modèle Magnus.

**TP associés :** Rankine : circulation et dépression ; Magnus : la portance vient de la circulation

## Au-delà : trois branches sur les équations du fluide

Les modèles suivants dépassent le socle commun et se lisent avec leurs hypothèses.

### A. Diffusion visqueuse et couche limite

**Au-delà du programme** · Au-delà du socle commun · approfondissement PC possible

Comparer pénétration transitoire et épaississement le long d’une plaque.

**À faire :** Noter ν la viscosité cinématique, t le temps, x la distance le long de la plaque et U∞ la vitesse loin de celle-ci. Dans le démarrage de paroi, quadrupler t ; dans Blasius, quadrupler x à U∞ fixée.

**Acquis attendu :** Retrouver les longueurs en √(νt) et √(νx/U∞) ; distinguer couche limite et tout l’écoulement.

**Limites et compléments :** La notion de couche limite est au programme PC ; la solution complète de Blasius, sa similarité et ses coefficients sont des prolongements fournis.

**TP associés :** Démarrage d’une paroi et diffusion visqueuse ; Blasius : une couche limite qui s’épaissit

### B. Taylor–Green : contrôler une solution exacte

**Au-delà du programme** · Au-delà · Navier–Stokes et bilan d’énergie

Utiliser une solution particulière pour vérifier les termes d’une équation.

**À faire :** Noter L la période spatiale, k=2π/L, ν la viscosité cinématique et t le temps. Calculer divergence et décroissance de la vitesse de Taylor–Green ; comparer énergie perdue et dissipation affichée.

**Acquis attendu :** Vérifier le bilan pour cette solution et distinguer convection, diffusion et pression.

**Limites et compléments :** L’utilisation locale de Navier–Stokes incompressible relève de PC, est exclue en PSI. Cette solution ne résout pas le problème général d’existence et de régularité du millénaire.

**TP associés :** Taylor–Green : un bilan exact de Navier–Stokes ; Suivre une particule, lire un champ

### C. Un champ magnétique agit sur le fluide

**Au-delà du programme** · Au-delà · Hartmann et Alfvén

Associer force de Lorentz, dissipation et vitesse d’une onde couplée.

**À faire :** Noter B le champ, σ la conductivité, j le courant, ρ la masse volumique et μ₀ la perméabilité du vide. Comparer Hartmann avec B faible et fort ; passer à Alfvén et modifier B puis ρ.

**Acquis attendu :** Relier le freinage à j×B et la célérité à B/√(μ₀ρ) dans le modèle annoncé.

**Limites et compléments :** MHD, Hartmann et Alfvén sont des prolongements. Conductivité, fermeture électrique et régime dissipatif doivent être ceux du modèle choisi.

**TP associés :** Hartmann et Alfvén : le fluide rencontre B

## Repères de programme

- [PCSI 2021 · statique et thermodynamique (annexe 2)](https://cache.media.education.gouv.fr/file/SPE1-MEN-MESRI-4-2-2021/65/0/spe780_annexe_1373650.pdf#page=34)
- [PC 2021 · mécanique des fluides, §4 (annexe 2)](https://cache.media.education.gouv.fr/file/31/23/0/ensecsup703_annexes_1417230.pdf#page=42)
- [PSI 2021 · fluides, exclusion Euler/NS (BO complet)](https://www.enseignementsup-recherche.gouv.fr/sites/default/files/imported_files/documents/BO_31_MESRI_1417448.pdf#page=269)
