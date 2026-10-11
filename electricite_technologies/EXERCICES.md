# Électricité & Technologies — 108 exercices corrigés

## 01. Retrouver une valeur à une constante de temps

Sup · Laboratoire `laplace_initiales`

Prendre K=2, E=1 V, y₀=0 et τ=1 s. Calculer y(τ) et y(∞).

**Correction guidée**

La valeur finale est KE=2 V. À t=τ, y=2(1−e⁻¹)≈1,264 V, soit 63,2 % de la variation totale.

## 02. Démarrer au-dessus de l’équilibre

Sup · Laboratoire `laplace_initiales`

Prendre K=2, E=1 V et y₀=3 V. La sortie dépasse-t-elle son état initial ?

**Correction guidée**

y(t)=2+e⁻ᵗ/τ V. Elle décroît de 3 V vers 2 V sans dépasser 3 V. La dérivée initiale vaut (KE−y₀)/τ=−1/τ V/s.

## 03. Retrouver le terme initial en Laplace

Au-delà · Mathématiques · Laboratoire `laplace_initiales`

Pour τ=2 s, K=3, E=1 V et y₀=−1 V, écrire Y(p). Pourquoi Y(p)≠H(p)E/p ?

**Correction guidée**

(1+2p)Y=3/p−2, donc Y=(3/p−2)/(1+2p). Le terme −2/(1+2p) est la contribution de l’état initial ; H(p)E/p ne décrit que le départ au repos.

## 04. Lire le gain à la pulsation propre

Sup · Laboratoire `bode_second_ordre`

Prendre K=1, ζ=0,5. Calculer H(jω₀), son module et sa phase.

**Correction guidée**

À ω=ω₀, le dénominateur réduit vaut 2jζ=j. Donc H=1/j=−j, |H|=1 et la phase vaut −90°. Le gain est 0 dB.

## 05. Un dépassement sans pic de résonance

Spé · SI · Laboratoire `bode_second_ordre`

Le système a ζ=0,8. Y a-t-il un pic de résonance ? Quel est le dépassement après un échelon ?

**Correction guidée**

0,8>1/√2 : aucun pic de résonance. Mais 0,8<1 : le dépassement vaut 100 exp(−π·0,8/0,6)≈1,52 %. Les deux seuils diffèrent.

## 06. Comparer deux décades à haute fréquence

Sup · Laboratoire `bode_second_ordre`

Très au-dessus de ω₀, on multiplie ω par 100. Quelle variation de gain prévoir ?

**Correction guidée**

|H|≈K(ω₀/ω)². Multiplier ω par 100 divise le module par 10⁴ ; le gain varie de −80 dB. Cela correspond à deux décades de pente −40 dB/décade.

## 07. Calculer un gain fermé

Sup · SI · Laboratoire `retroaction_sensibilite`

μ=20 et β=0,1. Calculer G et la sensibilité Sμ.

**Correction guidée**

μβ=2. G=20/3≈6,667 et Sμ=1/3. Une petite variation relative de μ est divisée approximativement par 3 sur G.

## 08. Vérifier une variation de 20 %

Spé · SI · Laboratoire `retroaction_sensibilite`

Avec μ=20 et β=0,1, augmenter μ de 20 %. Comparer la variation exacte de G à l’approximation locale.

**Correction guidée**

μ₂=24 et G₂=24/3,4≈7,059. La hausse exacte est (G₂/G−1)≈5,882 %. L’approximation locale donne 20/3≈6,667 % ; elle surestime ici la variation.

## 09. Supprimer le capteur

Sup · SI · Laboratoire `retroaction_sensibilite`

Que deviennent G, Sμ et la constante de temps fermée si β=0 ?

**Correction guidée**

G=μ, Sμ=1 et la constante de temps reste τ. Le système ne bénéficie plus du retour ; une variation relative de μ se transmet intégralement au gain.

## 10. Retrouver les réglages initiaux

Sup · SI · Laboratoire `moteur_x`

Prendre E=5 V, μ=2, K₀=2 rad·s⁻¹/V, τ=1 s et β=0,5 V/(rad/s). Calculer les deux vitesses finales.

**Correction guidée**

T₀=4 rad·s⁻¹/V ; Ω∞=20 rad/s. Le facteur fermé vaut 1+μβK₀=3 ; T₀′=4/3 et Ω′∞=20/3≈6,667 rad/s. τ′=1/3 s.

## 11. Comparer les pentes au départ

Spé · SI · Laboratoire `moteur_x`

Au départ au repos, les pentes de Ω et Ω′ sont-elles différentes ? Justifier.

**Correction guidée**

Ω̇(0)=T₀E/τ. Pour la boucle fermée, Ω̇′(0)=T₀′E/τ′=T₀E/τ. Les pentes initiales sont égales : au tout premier instant, le capteur renvoie une vitesse nulle.

## 12. Interpréter un retour très fort

Spé · SI · Laboratoire `moteur_x`

Lorsque μβK₀ devient très grand, vers quelle valeur tend Ω′∞ ? Quelle limite réelle manque au modèle ?

**Correction guidée**

Ω′∞=μK₀E/(1+μβK₀) tend vers E/β. La constante de temps tend vers zéro dans le modèle idéal. Les retards, l’inductance et la saturation limitent cette accélération dans un moteur réel.

## 13. Calculer un fonctionnement à vide

Spé · SI · Laboratoire `moteur_mcc`

U=12 V, R=2 Ω, k=0,1, b=0,01 N·m·s et Cᵣ=0. Calculer Ω∞ et i∞.

**Correction guidée**

Rb+k²=0,03. Ω∞=1,2/0,03=40 rad/s ; i∞=(12−4)/2=4 A. Le couple moteur 0,4 N·m équilibre le frottement 0,01×40=0,4 N·m.

## 14. Ajouter une charge de 0,03 N·m

Spé · SI · Laboratoire `moteur_mcc`

Reprendre les valeurs précédentes avec Cᵣ=0,03 N·m. Calculer vitesse, courant et pertes Joule permanentes.

**Correction guidée**

Ω∞=(1,2−0,06)/0,03=38 rad/s ; i∞=(12−3,8)/2=4,1 A. Les pertes Joule valent Ri∞²=2×4,1²=33,62 W. Le couple moteur vaut 0,41 N·m, égal à 0,38+0,03.

## 15. Interpréter les pentes initiales

Sup · SI · Laboratoire `moteur_mcc`

Le moteur part de i=0 et Ω=0. Quelles sont les dérivées initiales si une charge constante Cᵣ est déjà appliquée ?

**Correction guidée**

i̇(0)=U/L et Ω̇(0)=−Cᵣ/J. À vide, la pente initiale mécanique est nulle. Avec la charge signée appliquée dès le départ, le modèle peut d’abord tourner légèrement dans le sens négatif ; aucune butée n’est prévue.

## 16. Comparer P et PI au régime permanent

Spé · SI · Laboratoire `correcteur_pi`

Sans saturation, un procédé a K=1 et un correcteur proportionnel Kₚ=2. Pour r=1, calculer l’erreur finale. Que change un PI stable et actif ?

**Correction guidée**

Avec P, y∞=KKₚr/(1+KKₚ)=2/3 et e∞=1/3. Avec un PI stable dont l’intégrale est active, e∞=0 et y∞=1, si la commande nécessaire est accessible.

## 17. Tester l’accessibilité

Spé · SI · Laboratoire `correcteur_pi`

K=1, uₘₐₓ=0,5 et r=3. Une intégrale peut-elle annuler l’erreur constante ?

**Correction guidée**

Non. La sortie permanente accessible est au plus Kuₘₐₓ=0,5. L’erreur reste au moins 2,5. Sans correction, v continue de croître : le manque de commande ne se résout pas par l’accumulation intégrale.

## 18. Comparer deux équilibres de l’intégrale

Au-delà · SI · Laboratoire `correcteur_pi`

Pendant une saturation haute, u=uₘₐₓ. Écrire la condition dv/dt=0 pour la correction proposée.

**Correction guidée**

0=(Kₚ/Tᵢ)e+[uₘₐₓ−Kₚe−v]/Tᵢ, donc v=uₘₐₓ. L’intégrale reste bornée à cet équilibre. Sans correction, dv/dt=(Kₚ/Tᵢ)e reste positif si e>0.

## 19. Retrouver la limite pour trois constantes égales

Spé · SI · Laboratoire `stabilite_marges`

Prendre τ₁=τ₂=τ₃=τ. À quelle pulsation la phase atteint-elle −180° ? Quel gain K donne alors |L|=1 ?

**Correction guidée**

La phase est −3 arctan(ωτ). Il faut arctan(ωτ)=60°, donc ωτ=√3. Chaque facteur a pour module 2 ; |L|=K/8. Le gain limite est K=8.

## 20. Calculer une marge de gain

Spé · SI · Laboratoire `stabilite_marges`

Pour trois constantes égales et K=4, calculer la marge de gain.

**Correction guidée**

À ωπ=√3/τ, |L|=4/8=0,5. La marge de gain vaut −20 log₁₀(0,5)=20 log₁₀2≈6,02 dB. Doubler K atteint la limite.

## 21. Interpréter un gain inférieur à 1

Spé · SI · Laboratoire `stabilite_marges`

K=0,5 et les trois constantes de temps sont positives. Pourquoi le logiciel n’affiche-t-il pas une marge de phase numérique ?

**Correction guidée**

Le module de L vaut K au continu et décroît avec ω. Il reste donc inférieur à 1 partout : aucun croisement à 0 dB n’existe. L’absence de marge de phase numérique ne signifie pas que la boucle est instable.

## 22. Reconstituer le transfert contrôlé

Spé · SI · Laboratoire `isolation_sismique`

Partir de x=I(x₀−αF), F=ηp(x−x₀) et I=ωᵣ²/(p²+ωᵣ²). Déterminer x/x₀.

**Correction guidée**

x(1+αηpI)=Ix₀(1+αηp). Donc G=I(1+αηp)/(1+αηpI)=(ωᵣ²+αηωᵣ²p)/(p²+αηωᵣ²p+ωᵣ²). Le numérateur est du premier degré.

## 23. Choisir un amortissement critique

Spé · SI · Laboratoire `isolation_sismique`

ωᵣ=8 rad/s et α=0,01 m/N. Déterminer η pour ζ=1.

**Correction guidée**

ζ=αηωᵣ/2. Donc η=2/(αωᵣ)=25 N·s/m. Le dénominateur devient (p+8)². Le transfert garde le numérateur 64+16p ; il n’est pas un simple passe-bas à numérateur constant.

## 24. Contrôler la cohérence mécanique

Sup · Physique · Laboratoire `isolation_sismique`

On définit α=l²/(C−Mgl) et ωᵣ²=(C−Mgl)/(Ml²). Calculer αωᵣ² et en déduire M pour α=0,01 m/N et ωᵣ=8 rad/s.

**Correction guidée**

Les facteurs l² et C−Mgl se simplifient : αωᵣ²=1/M. M=1/(0,01×64)=1,5625 kg. Les deux paramètres ne représentent pas une masse arbitraire indépendante.

## 25. Retrouver une fréquence repliée

Spé · Physique · Laboratoire `echantillonnage_adc`

Un signal de 800 Hz est échantillonné à 1000 Hz. Quelle fréquence apparaît dans la bande [0,500 Hz] ?

**Correction guidée**

800−1000=−200 Hz. Le module de la fréquence ramenée est 200 Hz. Le signe et la phase doivent être conservés pour reproduire exactement les échantillons.

## 26. Calculer le pas et l’erreur maximale

Spé · Physique · Laboratoire `echantillonnage_adc`

Un CAN bipolaire de 8 bits couvre −2 à +2 V. Calculer q et l’erreur maximale hors saturation du modèle à centres d’intervalles.

**Correction guidée**

q=4/256=0,015625 V, soit 15,625 mV. L’erreur maximale est q/2=7,8125 mV. La valeur +2 V est représentée par le centre du dernier intervalle, donc légèrement en dessous de +2 V.

## 27. Distinguer deux défauts

Spé · Physique · Laboratoire `echantillonnage_adc`

On mesure une sinusoïde de 1 kHz et d’amplitude 3 V avec fₑ=1500 Hz et une plage ±1 V. Doubler N résout-il les deux problèmes ?

**Correction guidée**

Non. fₑ<2f donne un repliement ; l’amplitude dépasse ±1 V et fait saturer les codes. Doubler N affine les intervalles dans la plage, sans augmenter fₑ ni la plage de tension.

## 28. Écrire une réponse impulsionnelle

Spé · Physique · Laboratoire `filtre_rif`

Pour N=4 et une mémoire vide, donner les six premiers termes de la réponse à x₀=1 puis 0.

**Correction guidée**

h₀=h₁=h₂=h₃=1/4, puis h₄=h₅=0. La somme vaut 1 et la réponse est finie ; aucune sortie précédente n’est réinjectée.

## 29. Annuler une fréquence de bruit

Spé · Physique · Laboratoire `filtre_rif`

fₑ=1000 Hz et N=10. Le bruit est une sinusoïde de 300 Hz. Pourquoi est-il annulé après le transitoire ?

**Correction guidée**

300=3 fₑ/N. Sur dix échantillons, les phases parcourent trois tours complets et leur somme complexe est nulle. Le filtre annule cette raie, sous réserve de stabilité de sa fréquence.

## 30. Calculer le retard

Au-delà · Traitement du signal · Laboratoire `filtre_rif`

N=9 et fₑ=1000 Hz. Quel retard de groupe possède la moyenne glissante ? Une entrée constante est-elle atténuée ?

**Correction guidée**

Le retard vaut (9−1)/(2×1000)=4 ms. Le gain au continu vaut la somme des neuf coefficients, donc 1 : une constante n’est pas atténuée après le transitoire de remplissage.

## 31. Retrouver l’impulsion

Sup · Mathématiques · Laboratoire `filtre_rii_z`

Pour a=0,8, calculer h₀, h₁ et h₂. Quelle est la somme de tous les hₖ ?

**Correction guidée**

h₀=0,2 ; h₁=0,16 ; h₂=0,128. La série géométrique donne Σhₖ=0,2/(1−0,8)=1. Le gain au continu vaut donc 1.

## 32. Observer un retour négatif discret

Au-delà · Temps discret · Laboratoire `filtre_rii_z`

Pour a=−0,8, calculer les trois premiers termes de h et le gain à la fréquence de Nyquist.

**Correction guidée**

h₀=1,8 ; h₁=−1,44 ; h₂=1,152. À f/fₑ=1/2, z⁻¹=−1 et H=(1−a)/(1+a)=1,8/0,2=9. Le filtre favorise la fréquence haute tout en restant stable.

## 33. Mesurer la durée de mémoire

Sup · Mathématiques · Laboratoire `filtre_rii_z`

Pour 0<a<1, au bout de combien d’échantillons le facteur aᵏ atteint-il e⁻¹ ? Calculer pour a=0,98.

**Correction guidée**

aᵏ=e⁻¹ donne k=−1/ln(a). Pour a=0,98, k≈49,5 échantillons. La durée réelle vaut ce nombre multiplié par Tₑ ; sans fréquence d’échantillonnage, on ne peut pas la donner en secondes.

## 34. Distinguer l’état initial de l’impulsion

Spé · Physique · Laboratoire `discretisation`

τ=1 ms et Tₑ=50 µs. Pour Euler implicite, calculer y₁ et y₂ si x₁=1 puis 0, d’abord avec y₀=1, puis avec y₀=0.

**Correction guidée**

Avec y₀=1 : y₁=20/21+1/21=1 ; y₂=20/21. Avec y₀=0 : y₁=1/21 ; y₂=20/441. Une entrée identique donne des sorties différentes à cause de l’état initial.

## 35. Trouver le bon numérateur bilinéaire

Au-delà · Temps discret · Laboratoire `discretisation`

Dans H(p)=1/(1+τp), remplacer p par (2/Tₑ)(1−z⁻¹)/(1+z⁻¹). Déterminer H(z).

**Correction guidée**

Après multiplication par 1+z⁻¹, H(z)=(1+z⁻¹)/[(1+2τ/Tₑ)+(1−2τ/Tₑ)z⁻¹]. La récurrence devient (1+2τ/Tₑ)yₖ+(1−2τ/Tₑ)yₖ₋₁=xₖ+xₖ₋₁.

## 36. Vérifier les pôles pour un grand pas

Au-delà · Temps discret · Laboratoire `discretisation`

Prendre Tₑ=3τ. Calculer les pôles Euler, bilinéaire et ZOH. Les trois méthodes proposées restent-elles stables ?

**Correction guidée**

Euler : a=1/4. Bilinéaire : aB=(2−3)/(2+3)=−1/5. ZOH : aZ=e⁻³≈0,0498. Leurs modules sont inférieurs à 1 : elles restent stables. Le pôle bilinéaire négatif donne une alternance artificielle pour un pas aussi grand.

## 37. Convertir un angle en fréquence

Sup · Mathématiques / au-delà · Laboratoire `polezero_z`

Les pôles ont θ=60° et la fréquence d’échantillonnage vaut 1200 Hz. Quelle fréquence d’oscillation représentent-ils ?

**Correction guidée**

60°=π/3 rad. La fréquence relative vaut (π/3)/(2π)=1/6 ; la fréquence réelle vaut 1200/6=200 Hz.

## 38. Lire une décroissance

Au-delà · Temps discret · Laboratoire `polezero_z`

Comparer l’enveloppe rᵏ après 20 échantillons pour r=0,8 et r=0,98.

**Correction guidée**

0,8²⁰≈0,01153 tandis que 0,98²⁰≈0,6676. Les deux rayons restent inférieurs à 1 ; les deux filtres sont stables, mais le second garde beaucoup plus longtemps la trace de l’impulsion.

## 39. Choisir les zéros pour une raie

Au-delà · Traitement du signal · Laboratoire `polezero_z`

Pour fₑ=1000 Hz, on veut annuler 100 Hz. Quel angle ψ choisir ? Où placer les deux zéros ?

**Correction guidée**

ψ=2π×100/1000=π/5=36°. Les zéros sont e±jπ/5, soit environ 0,8090±0,5878j. Ils sont conjugués et sur le cercle unité ; le filtre conserve des coefficients réels.

## 40. Calculer trois amplitudes

Spé · Physique · Laboratoire `modulation_am`

U=2 V, m=0,6, F=2000 Hz et f=100 Hz. Donner les fréquences et les amplitudes crête des trois raies.

**Correction guidée**

La porteuse est à 2000 Hz, amplitude 2 V. Les bandes latérales sont à 1900 Hz et 2100 Hz, chacune d’amplitude mU/2=0,6 V. Ces valeurs sont des amplitudes crête, pas des valeurs efficaces.

## 41. Choisir une constante de temps

Spé · Physique · Laboratoire `modulation_am`

Pour F=20 kHz et f=100 Hz, proposer un RC compatible avec une détection d’enveloppe.

**Correction guidée**

1/F=50 µs et 1/f=10 ms. Un RC de l’ordre de 1 ms se place entre ces deux échelles. Il faut ensuite vérifier l’ondulation et la décharge sur le signal réel : les inégalités sont des repères de choix.

## 42. Retrouver le message par démodulation synchrone

Spé · Physique PSI · Laboratoire `modulation_am`

Multiplier uAM par 2 cos(2πFt), avec une référence de même phase, puis filtrer les composantes rapides. Que reste-t-il ?

**Correction guidée**

2 cos²(2πFt)=1+cos(4πFt). Après passe-bas, il reste U[1+m cos(2πft)]. Retirer la composante constante U donne Um cos(2πft). Une erreur de phase de référence multiplie cette composante lente par le cosinus de l’erreur de phase.

## 43. Retrouver l’inconnue

Sup · Laboratoire `pont_wheatstone`

Les branches sont celles du schéma. R₁=2 kΩ, R₂=1 kΩ et R₃=6 kΩ. Quelle valeur de R₄ annule UBD ?

**Correction guidée**

R₂R₃=R₁R₄, donc R₄=3 kΩ. Les deux points milieux sont au potentiel E/3.

## 44. Prévoir un signe

Sup · Laboratoire `pont_wheatstone`

E=5 V et les quatre résistances valent 1 kΩ. On remplace R₄ par 1,1 kΩ. Quel est le signe et la valeur à vide de UBD ?

**Correction guidée**

VB=2,5 V et VD=5×1,1/2,1≈2,619 V. UBD≈−0,119 V : augmenter la résistance inférieure droite élève VD.

## 45. Une résistance de voltmètre finie

Spé · Laboratoire `pont_wheatstone`

Un pont présente une tension à vide U₀=100 mV et une résistance de Thévenin Rth=1 kΩ. Le voltmètre a Rm=9 kΩ. Que lit-il ? Un réglage à zéro est-il déplacé ?

**Correction guidée**

U=100×9/(9+1)=90 mV. Le zéro ne change pas, car le facteur de charge est strictement positif; la sensibilité diminue de 10 %.

## 46. Ordre de grandeur d’un câble

Sup · Laboratoire `ligne_transmission`

Une ligne sans pertes possède L=0,25 µH/m et C=100 pF/m. Calculer son impédance caractéristique et le retard sur 20 m.

**Correction guidée**

Z₀=√(L/C)=50 Ω. c=1/√(LC)=2×10⁸ m/s. Le retard d/c vaut 100 ns.

## 47. Comparer deux terminaisons

Spé · Laboratoire `ligne_transmission`

Pour Z₀=50 Ω réel, calculer Γ avec une charge de 50 Ω puis de 200 Ω. Quel pourcentage de la puissance incidente est réfléchi dans le second cas ?

**Correction guidée**

Γ=0 puis Γ=(200−50)/(200+50)=0,6. Pour une ligne sans pertes, la fraction de puissance réfléchie est |Γ|²=0,36, soit 36 %.

## 48. Vérifier une perte locale

Au-delà · Laboratoire `ligne_transmission`

En un point, les amplitudes crêtes sont |I|=0,10 A et |V|=5 V. R=0,02 Ω/m et G=2 µS/m. Calculer −dP/dx.

**Correction guidée**

−dP/dx=(R|I|²+G|V|²)/2=(0,02×0,01+2×10⁻⁶×25)/2=1,25×10⁻⁴ W/m. Les deux contributions sont positives.

## 49. Choisir le régime critique

Sup · Laboratoire `rlc_transitoire`

L=20 mH et C=10 µF. Calculer la résistance critique et la fréquence propre.

**Correction guidée**

Rcrit=2√(L/C)≈89,44 Ω. ω₀≈2236 rad/s et f₀=ω₀/(2π)≈355,9 Hz.

## 50. Lire un départ sans saut

Sup · Laboratoire `rlc_transitoire`

Un RLC série déchargé reçoit E=5 V à t=0. Peut-on avoir uC(0+)=5 V ou i(0+)≠0 ? Quelle dérivée démarre le courant ?

**Correction guidée**

La tension du condensateur et le courant de la bobine sont continus : uC(0+)=0 et i(0+)=0. La maille donne di/dt(0+)=E/L. Il peut y avoir un saut de dérivée, pas des variables de stockage.

## 51. Partager l’énergie de la source

Spé · Laboratoire `rlc_transitoire`

C=10 µF et E=5 V. Après établissement complet, calculer le travail fourni, l’énergie stockée et l’énergie dissipée.

**Correction guidée**

W=CE²=250 µJ. EC=CE²/2=125 µJ et EL=0. Le résistor a dissipé 125 µJ. Toute la charge injectée, CE, est passée sous la tension constante E.

## 52. Tension et courant à l’accord

Sup · Laboratoire `resonance_impedance`

À la résonance, Ueff=5 V et R=20 Ω. Trouver le courant efficace, son amplitude crête et la puissance active.

**Correction guidée**

Ieff=0,25 A, Icrête=√2 Ieff≈0,354 A et P=Ueff²/R=1,25 W. Le courant est en phase avec la tension.

## 53. Interpréter une impédance

Sup · Laboratoire `resonance_impedance`

Une mesure donne Z=30−40j Ω. Pour Ueff=10 V, calculer Ieff et la phase du courant par rapport à la tension.

**Correction guidée**

|Z|=50 Ω, donc Ieff=0,20 A. arg Z≈−53,13°, donc le courant avance de 53,13° sur la tension. La puissance active vaut R Ieff²=1,2 W.

## 54. Identifier une résistance totale

Spé · Laboratoire `resonance_impedance`

Une bobine de L=20 mH est en série dans un RLC. La largeur à mi-puissance est 160 Hz. Quelle résistance série totale en déduire ?

**Correction guidée**

R=2πLΔf≈20,11 Ω. Cette résistance comprend le résistor, les pertes de la bobine et toute résistance source série.

## 55. Un diviseur réel

Sup · Laboratoire `mesure_impedance`

R₀=1 kΩ. Les amplitudes en phase sont V₁=4 V et V₂=2 V. Les voies sont supposées idéales. Déduire Z.

**Correction guidée**

I=(4−2)/1000=2 mA, puis Z=2/(2×10⁻³)=1 kΩ. La formule utilise des amplitudes de même nature, toutes deux crêtes ou toutes deux efficaces.

## 56. Corriger la résistance d’entrée

Sup · Laboratoire `mesure_impedance`

Un résistor de 10 kΩ est mesuré par une voie d’entrée de 100 kΩ, capacité négligeable. Quelle résistance parallèle est obtenue ? Comment retrouver 10 kΩ ?

**Correction guidée**

Rmes=10×100/(10+100)=9,091 kΩ. La correction 1/R=1/Rmes−1/Rentrée donne 10 kΩ. Le biais est de −9,09 %, même avec une lecture sans bruit.

## 57. Préparer une mesure précise

Spé · Laboratoire `mesure_impedance`

Les voies sont en phase, V₁=4 V et V₂=3,8 V. Chaque amplitude a une incertitude-type relative indépendante de 0,5 %. Estimer l’incertitude relative sur le module déduit.

**Correction guidée**

√2×0,005×4/0,2≈0,141, soit 14,1 %. La tension différentielle de 0,2 V est trop petite pour ces lectures. Choisir R₀ pour obtenir une chute plus importante, sans rendre V₂ trop faible.

## 58. Moyenne et efficace

Sup · Laboratoire `pont_graetz`

Une tension sinusoïdale de crête 12 V et de fréquence 50 Hz alimente un pont idéal et une résistance de 100 Ω. Calculer la moyenne, la valeur efficace et la puissance de charge.

**Correction guidée**

⟨uR⟩=24/π≈7,64 V. Ueff=12/√2≈8,49 V. P=Ueff²/R=0,72 W. L’ondulation est à 100 Hz.

## 59. Compter les chutes de tension

Spé · Laboratoire `pont_graetz`

À un instant, |uAB|=5 V et chaque diode a un seuil de 0,7 V. Comparer les tensions de charge du pont et du point milieu à même tension de demi-enroulement.

**Correction guidée**

Le pont donne 5−2×0,7=3,6 V. Le point milieu donne 5−0,7=4,3 V. Ces résultats supposent que les tensions dépassent les seuils; sinon la sortie est nulle.

## 60. Fermer un bilan de puissance

Spé · Laboratoire `pont_graetz`

Un pont à seuil Vd=0,7 V débite un courant moyen de 0,10 A. La charge reçoit 2 W. Quelle puissance moyenne fournit la source ?

**Correction guidée**

Les deux diodes parcourues dissipent ensemble 2Vd⟨iR⟩=0,14 W. La source fournit donc 2,14 W. Un simple calcul avec la tension moyenne au carré ne remplace pas ⟨uR²⟩/R.

## 61. Limite à vide

Sup · Laboratoire `doubleur_tension`

Un doubleur de Delon reçoit une sinusoïde de crête E=12 V. Chaque diode a un seuil de 0,7 V. Donner les tensions établies à vide.

**Correction guidée**

Chaque condensateur atteint environ 11,3 V. La sortie vaut 22,6 V, après la charge sur les deux alternances. Ce résultat ne décrit pas le démarrage ni le fonctionnement sous charge.

## 62. Capacités différentes

Spé · Laboratoire `doubleur_tension`

Pendant un court intervalle, les deux diodes sont bloquées et le courant de charge est 2 mA. C₁=50 µF et C₂=100 µF. Donner les pentes des deux tensions.

**Correction guidée**

u₁′=−iR/C₁=−40 V/s et u₂′=−20 V/s. La sortie décroît à −60 V/s. La plus petite capacité présente la plus forte ondulation.

## 63. Estimer un stockage

Sup · Laboratoire `doubleur_tension`

À vide, deux condensateurs de 100 µF portent chacun 12 V. Quelle énergie totale stockent-ils ? Quelle capacité équivalente donnerait la même énergie sous 24 V ?

**Correction guidée**

Énergie totale : 2×(100×10⁻⁶×12²/2)=14,4 mJ. La capacité équivalente sous 24 V est 50 µF, puisque les deux capacités égales sont en série entre les extrémités.

## 64. Décharge entre deux recharges

Sup · Laboratoire `diode_rc`

Une diode est bloquée. R=1 kΩ, C=100 µF et la sortie vaut initialement 10 V. Calculer la tension 20 ms plus tard.

**Correction guidée**

τ=RC=0,10 s. uC=10 exp(−0,020/0,10)≈8,19 V. La décharge n’est pas linéaire sur une durée comparable à τ.

## 65. Vérifier l’état supposé

Spé · Laboratoire `diode_rc`

usource=8 V, uC=9 V, Rs=20 Ω et Vd=0,7 V. L’hypothèse de diode conductrice est-elle admissible ?

**Correction guidée**

Elle imposerait iD=(8−0,7−9)/20=−85 mA, interdit dans ce modèle. La diode est bloquée, et le condensateur alimente seul la résistance.

## 66. Le quart de période est-il un arrêt ?

Spé · Laboratoire `diode_rc`

Dans la limite source idéale et diode idéale, uC suit E sin(ωt) pendant la conduction. R est finie. Évaluer iD à t=T/4 et conclure.

**Correction guidée**

À T/4, uC=E et uC′=0 : iD=E/R>0. La diode ne se bloque donc pas exactement au maximum de la sinusoïde. Il faut attendre C usource′+usource/R=0 sur la branche descendante.

## 67. Triangle–étoile

Spé · Laboratoire `triphase_transformateur`

Le primaire est en triangle sous U₁=400 V. Le secondaire est en étoile et N₂/N₁=0,5. Calculer la tension d’un enroulement secondaire et la tension composée à vide.

**Correction guidée**

Chaque enroulement primaire reçoit 400 V; chaque secondaire fournit 200 V. La tension composée secondaire vaut √3×200≈346,4 V. Le rapport de tensions de ligne est 0,866, et non 0,5.

## 68. Puissance d’une charge équilibrée

Spé · Laboratoire `triphase_transformateur`

Une charge triphasée équilibrée reçoit U₂=400 V, I₂=10 A et cosφ=0,8. Trouver sa puissance active et apparente.

**Correction guidée**

S=√3×400×10≈6,928 kVA. P=S×0,8≈5,543 kW. Les valeurs de U₂ et I₂ sont composées et de ligne, toutes deux efficaces.

## 69. Rendement à partir des pertes

Spé · Laboratoire `triphase_transformateur`

Pu=10 kW, I₂=20 A, Rs=0,02 Ω par phase équivalente étoile et P₀=100 W. Calculer les pertes et le rendement.

**Correction guidée**

Pcuivre=3×0,02×20²=24 W. Pabs=10000+24+100=10124 W. η=10000/10124≈98,78 %. Le rapport de spires ne suffit pas à prévoir ce rendement.

## 70. Valeurs efficaces à T/4

Sup · Laboratoire `onduleur_spectre`

Un onduleur délivre E=175 V. La commande décalée vaut ±E pendant au total la moitié de la période et zéro le reste. Trouver les valeurs efficaces pleine onde et décalée.

**Correction guidée**

Pleine onde : Ueff=175 V. Commande décalée : Veff=175√(1/2)≈123,74 V. Ce sont des valeurs efficaces du signal complet, pas du seul fondamental.

## 71. Un THD calculé exactement

Spé · Laboratoire `onduleur_spectre`

Pour la pleine onde idéale de crête E, A₁=4E/π et Ueff=E. Calculer le THD total.

**Correction guidée**

U₁eff=4E/(π√2). THD=√(E²−8E²/π²)/(4E/(π√2))=√(π²/8−1)≈0,4834, soit 48,34 %. Le résultat est indépendant de E.

## 72. Rang 3 et commande décalée

Spé · Laboratoire `onduleur_spectre`

Avec δ=1/4, le troisième harmonique est-il annulé ? Quel est A₃/A₁ ?

**Correction guidée**

|cos(3π/4)|=cos(π/4)=1/√2. Donc A₃/A₁=1/3 : la raie de rang 3 reste présente. Une diminution de la valeur efficace totale ne prouve pas une diminution du THD.

## 73. Courant moyen en conduction continue

Spé · PSI · Laboratoire `hacheur_mcc`

E=48 V, Eₘ=20 V, R=2 Ω et α=0,6. Supposer la conduction continue. Calculer la tension et le courant moyens.

**Correction guidée**

⟨u⟩=0,6×48=28,8 V. ⟨i⟩=(28,8−20)/2=4,4 A. Il reste à vérifier, avec L et f, que le courant minimal est positif.

## 74. Calculer l’instant d’extinction

Spé · PSI · Laboratoire `hacheur_mcc`

À l’ouverture, i(0)=2 A, L=1 mH, R=2 Ω et Eₘ=10 V. La roue libre impose Li′+Ri+Eₘ=0. Quand le courant atteint-il zéro ?

**Correction guidée**

i(t)=−Eₘ/R+(2+Eₘ/R)exp(−Rt/L). Le zéro est t₀=(L/R)ln(1+Ri(0)/Eₘ)=0,5 ms×ln(1,4)≈0,168 ms. Après t₀, la diode se bloque.

## 75. Évaluer les pertes d’un courant ondulé

Spé · Laboratoire `hacheur_mcc`

Le courant d’induit a une moyenne de 4 A et un écart-type temporel de 1 A. R=2 Ω et Eₘ=20 V. Calculer les puissances cuivre et électromécanique.

**Correction guidée**

⟨i²⟩=⟨i⟩²+σi²=17 A². Pcuivre=34 W et Pconversion=Eₘ⟨i⟩=80 W. Avec des interrupteurs idéaux, la source fournit 114 W. Utiliser R⟨i⟩² aurait omis 2 W.

## 76. Puissance d’un courant en retard

Spé · Laboratoire `puissances_compensation`

Ueff=230 V, Ieff=5 A et le courant retarde de 36,87°. Calculer P, Q et S.

**Correction guidée**

cosφ=0,8 et sinφ=0,6. S=1150 VA, P=920 W et Q=690 var. Le facteur de puissance vaut 0,8; Q est positif pour la charge inductive.

## 77. Choisir un condensateur

Spé · Laboratoire `puissances_compensation`

Une charge absorbe Q=690 var sous 230 V à 50 Hz. Quelle capacité parallèle idéale annule cette puissance réactive ?

**Correction guidée**

Qc=−ωCU², donc C=690/(2π×50×230²)≈41,52 µF. Sa puissance active idéale est nulle; la source fournit toujours la puissance active de la charge.

## 78. Détecter une surcompensation

Spé · Laboratoire `puissances_compensation`

Sous U=230 V, une charge absorbe P=920 W et Q=690 var. Le condensateur fournit Qc=−1000 var. Calculer le nouveau courant de ligne.

**Correction guidée**

Qtotal=−310 var. S=√(920²+310²)≈970,8 VA et Iligne=S/U≈4,22 A. Le courant était 5 A sans compensation, mais son minimum à Q=0 serait P/U=4 A. Le courant est désormais en avance.

## 79. Calculer le produit gain–bande

Spé — physique PSI/PT · Laboratoire `ali_gain_bande`

Un ALI a un gain différentiel statique A₀ = 100 000 et une fréquence de transition fₜ = 1,00 MHz. Le diviseur de rétroaction impose un gain idéal G = 10. Calculer le gain statique bouclé G₀ et sa bande à −3 dB f_c, puis leur produit.

**Correction guidée**

La fréquence du pôle libre vaut fₚ = fₜ/A₀ = 10,0 Hz. Avec β = 1/G = 0,1 : G₀ = A₀/(1 + βA₀) = 9,9990 et f_c = fₚ(1 + βA₀) = 100 010 Hz. Le produit G₀f_c vaut exactement 1 000 000 Hz dans le modèle à un pôle. L’approximation G₀ ≈ G donne f_c ≈ 100 kHz.

## 80. Distinguer une limite de pente d’un rail

Spé — physique PSI/PT · Laboratoire `ali_gain_bande`

Une sortie sinusoïdale serait de 8,0 V crête à 10,0 kHz. Les rails valent ±12 V et la vitesse de balayage maximale SR vaut 0,050 V/µs. La sinusoïde peut-elle être reproduite ? Quelle amplitude maximale une sinusoïde à cette fréquence pourrait-elle avoir ?

**Correction guidée**

La pente maximale requise vaut 2πfS = 502 655 V/s = 0,503 V/µs : dix fois la pente disponible. Les rails permettent 8 V, mais la vitesse de balayage ne le permet pas. Une sinusoïde à 10 kHz doit satisfaire S ≤ SR/(2πf) = 0,796 V crête. Cette borne concerne une sinusoïde ; une sortie déformée peut avoir une autre amplitude et contenir des harmoniques.

## 81. Prévoir la limitation par une petite charge

Spé — physique PSI/PT · Laboratoire `ali_gain_bande`

Un ALI possède des rails ±12 V et un courant maximal de sortie Iₘₐₓ = 10 mA. Il alimente une résistance Rₗ = 100 Ω et devrait fournir 5 V crête. Quel plafond de tension impose la charge ?

**Correction guidée**

La loi d’Ohm impose |vₛ| ≤ IₘₐₓRₗ = 0,010 × 100 = 1,0 V. La prédiction de 5 V demanderait 50 mA. Le plafond effectif est min(12 V, 1 V) = 1 V : la saturation en courant apparaît avant les rails de tension. Remplacer Rₗ par 1 kΩ élève le plafond de courant à 10 V.

## 82. Comparer deux cellules identiques à leur fréquence propre

Sup — physique PTSI · Laboratoire `suiveur_cascade`

Deux cellules identiques possèdent une résistance R et une capacité C. À la pulsation ω = 1/(RC), calculer le module et la phase de la fonction de transfert avec et sans un suiveur idéal entre les cellules. On donne Hsans = 1/[1 + 3jωRC − (ωRC)²].

**Correction guidée**

À ωRC = 1, Hsans = 1/(3j) = −j/3 : son module vaut 1/3 et sa phase −90°. Avec suiveur, Havec = 1/(1 + j)² = 1/(2j) = −j/2 : son module vaut 1/2 et sa phase −90°. Les phases coïncident à cette fréquence, mais les amplitudes diffèrent de 50 %. La seconde cellule charge la première lorsqu’elles sont directement reliées.

## 83. Lire un capteur sans perdre sa tension

Sup — physique PTSI · Laboratoire `suiveur_cascade`

Un capteur possède une tension à vide de 2,00 V et une résistance interne Rₛ = 100 kΩ. L’appareil de lecture possède Rₗ = 10 kΩ. Calculer la lecture directe, puis la lecture avec un suiveur idéal.

**Correction guidée**

La lecture directe est 2 × 10/(100 + 10) = 0,1818 V, soit 9,09 % de la tension à vide. Le suiveur idéal ne prélève pas de courant sur le capteur et restitue 2,00 V. Il doit fournir à l’appareil 2/10 000 = 0,200 mA ; cette demande doit être compatible avec un suiveur réel.

## 84. Tester la multiplication des transferts

Spé — physique PSI/PT · Laboratoire `suiveur_cascade`

Deux filtres isolés ont pour transferts H₁ et H₂. Un étudiant écrit toujours Htotal = H₁H₂ lorsqu’il les relie. Quelle condition manque ? Comment un suiveur idéal la réalise-t-il ?

**Correction guidée**

Le premier filtre doit conserver son transfert sous la charge du second. Une forte impédance d’entrée du second devant l’impédance de sortie du premier permet cette approximation. Le suiveur idéal réalise une impédance d’entrée infinie et une impédance de sortie nulle : le premier ne fournit aucun courant au second, et les transferts se multiplient. La seule existence de deux étages ne suffit pas à justifier le produit.

## 85. Retrouver le signe d’une somme continue

Spé — ALI idéal · Laboratoire `sommateur_inverseur`

Un sommateur inverseur utilise R₁ = 10 kΩ, R₂ = 20 kΩ et Rf = 20 kΩ. Les entrées continues valent vₑ₁ = 0,30 V et vₑ₂ = −0,40 V. Calculer la sortie en régime linéaire.

**Correction guidée**

La loi des nœuds donne vₛ = −(20/10) × 0,30 − (20/20) × (−0,40) = −0,20 V. L’entrée négative fournit une contribution positive à la sortie ; l’entrée positive donne une contribution négative. Les poids sont −2 et −1, sans unité.

## 86. Choisir les poids par les résistances

Spé — montage accompagné · Laboratoire `sommateur_inverseur`

On souhaite vₛ = −3vₑ₁ − 2vₑ₂ avec une résistance de rétroaction Rf = 60 kΩ. Quelles résistances d’entrée R₁ et R₂ choisir ? Quel courant prélève la première entrée lorsque vₑ₁ = 1 V ?

**Correction guidée**

Les rapports imposent R₁ = Rf/3 = 20 kΩ et R₂ = Rf/2 = 30 kΩ. La borne inverseuse est au potentiel nul dans le régime linéaire idéal. La première source fournit donc 1/20 000 = 50 µA. L’impédance d’entrée de ce montage est finie : ce sommateur ne remplace pas un suiveur.

## 87. Repérer quand la formule linéaire cesse de s’appliquer

Spé — saturation · Laboratoire `sommateur_inverseur`

Un sommateur utilise R₁ = R₂ = 10 kΩ, Rf = 100 kΩ et des rails ±12 V. Les entrées continues valent 3,0 V et 0,50 V. Calculer la prédiction linéaire et la sortie du modèle quasi statique limité. Peut-on encore imposer v₋ = 0 dans le circuit réel ?

**Correction guidée**

La prédiction vaut −10(3,0 + 0,50) = −35 V. Le modèle limité affiche −12 V. Le circuit est saturé ; le gain infini ne permet plus d’égaliser les entrées. On ne doit donc pas continuer à utiliser une masse virtuelle pour obtenir tous les courants du circuit saturé. La courbe limitée illustre la perte de linéarité, sans décrire les états internes de l’ALI réel.

## 88. Conserver la constante d’intégration

Spé — physique PSI/PT · Laboratoire `integrateur_derivateur`

Un intégrateur idéal a R = 10 kΩ et C = 10 nF. Son entrée est vₑ(t) = E sin(2πft), avec E = 1,00 V et f = 1,00 kHz. La sortie est nulle à t = 0. Calculer sa valeur à un quart de période, puis à une demi-période.

**Correction guidée**

RC = 100 µs et 2πfRC = 0,628319. La sortie est vₛ(t) = E[cos(2πft) − 1]/(2πfRC). À T/4, elle vaut −1,5915 V ; à T/2, elle vaut −3,1831 V. La seule expression 1,5915 cos(2πft) omettrait la constante initiale et ne partirait pas de zéro.

## 89. Vérifier un dérivateur amélioré en basse fréquence

Spé — analyse du montage · Laboratoire `integrateur_derivateur`

Un dérivateur amélioré possède R = 10 kΩ, C = 10 nF, R′ = 100 kΩ et C′ = 1 nF. L’entrée a une amplitude de 1 V et une fréquence f = 100 Hz. Calculer l’amplitude de sortie et la comparer à la dérivée approchée.

**Correction guidée**

Les deux temps valent RC = R′C′ = 100 µs et R′C = 1,00 ms. Le transfert est −j2πfR′C/(1 + j2πfRC)². Son module vaut 0,628319/[1 + 0,0628319²] = 0,62585. La sortie fait donc 0,62585 V crête. La dérivée approchée donnerait 0,62832 V. Sa phase exacte vaut −90° − 2 arctan(0,0628319) = −97,19° : le signe inverseur doit être conservé.

## 90. Expliquer l’atténuation à très haute fréquence

Spé — filtrage · Laboratoire `integrateur_derivateur`

On donne H(s) = −R′Cs/[(1 + RCs)(1 + R′C′s)]. Les résistances sont en ohms, les capacités en farads. Trouver l’équivalent de H(jω) lorsque les deux produits ωRC et ωR′C′ sont très grands. Quelle pente de gain en décibels en déduire ?

**Correction guidée**

Le dénominateur devient RCR′C′s². Ainsi H(s) ≈ −1/(RC′s), donc H(jω) ≈ j/(RC′ω). Le module décroît comme 1/ω : chaque multiplication par dix de la fréquence réduit le gain de 20 dB. Les deux protections remplacent la croissance illimitée du dérivateur idéal par une atténuation à haute fréquence.

## 91. Calculer les seuils et leur largeur

Spé — physique PSI/PT · Laboratoire `schmitt_trigger`

R₁ = 20 kΩ relie la sortie à l’entrée positive ; R₂ = 10 kΩ relie cette entrée à la masse. Les niveaux de sortie sont ±12 V et l’entrée est appliquée à la borne négative. Trouver les seuils en montée et en descente.

**Correction guidée**

La fraction de sortie est β = 10/(20 + 10) = 1/3. En montée, une sortie +12 V bascule à vₑ = +4,0 V vers −12 V. En descente, une sortie −12 V bascule à vₑ = −4,0 V vers +12 V. La largeur de l’hystérésis est 8,0 V.

## 92. Deux sorties possibles pour une même entrée

Spé — mémoire · Laboratoire `schmitt_trigger`

Les seuils d’un Schmitt sont −4 V et +4 V. L’entrée triangulaire reste entre −3 V et +3 V. Prévoir la sortie si l’état initial vaut +12 V, puis si l’état initial vaut −12 V.

**Correction guidée**

Le signal n’atteint aucun seuil de basculement. Une sortie initiale +12 V demeure +12 V ; une sortie initiale −12 V demeure −12 V. Les deux expériences possèdent la même entrée, mais des sorties différentes. L’état initial constitue la mémoire indispensable à la description du circuit.

## 93. Garantir l’absence de commutations parasites

Spé — manipulation accompagnée · Laboratoire `schmitt_trigger`

Les seuils sont ±4 V. Une entrée de valeur absolue au plus 1,0 V reçoit une perturbation de valeur absolue au plus 0,7 V. Un basculement est-il possible, quel que soit l’état initial ?

**Correction guidée**

L’inégalité triangulaire donne |vₑ| ≤ 1,0 + 0,7 = 1,7 V, strictement inférieur à 4 V. Aucun seuil ne peut être atteint. L’état initial est donc conservé, que la perturbation soit sinusoïdale ou quelconque sous la borne fournie. Ce résultat dépend d’une borne d’amplitude, et non d’une fréquence supposée pour le bruit.

## 94. Trouver la période à commande nulle

Spé — physique PSI/PT · Laboratoire `astable`

Un astable possède R₁ = 10 kΩ, C = 100 nF, R₂ = 10 kΩ et R₃ = 20 kΩ. La commande est nulle et les niveaux de sortie valent ±12 V. Calculer la période et la fréquence.

**Correction guidée**

τ = R₁C = 1,00 ms et β = R₂/(R₂ + R₃) = 1/3. La période est T = 2τ ln[(1 + β)/(1 − β)] = 2 ms × ln 2 = 1,3863 ms. La fréquence vaut 721,35 Hz. Les deux demi-périodes valent 0,69315 ms. Le niveau de saturation fixe les seuils, mais se simplifie dans cette expression de T.

## 95. Décaler les durées avec une commande continue

Spé — physique PSI/PT · Laboratoire `astable`

Reprendre τ = 1 ms, β = 1/3 et Vₛₐₜ = 12 V, avec une commande Vₑ = 5 V. Calculer les seuils, les deux durées et la fraction du temps au niveau positif.

**Correction guidée**

h = (1 − β)Vₑ = 10/3 V. Les seuils sont L = −2/3 V et U = 22/3 V. La charge positive dure t₊ = 1 ms × ln(19/7) = 0,99853 ms ; la charge négative dure t₋ = 1 ms × ln(29/17) = 0,53408 ms. T = 1,53261 ms et t₊/T = 65,15 %. Une commande positive prolonge ici l’état de sortie positif.

## 96. Comprendre l’arrêt au seuil de commande

Spé — relaxation · Laboratoire `astable`

Pourquoi la formule de période ne doit-elle plus être appliquée comme un nombre fini lorsque |Vₑ| atteint Vₛₐₜ ? Que montre la simulation au-delà de cette limite ?

**Correction guidée**

Un seuil devient égal à la tension vers laquelle charge le condensateur. Une charge exponentielle approche sa cible sans l’atteindre en temps fini : une des durées diverge. Au-delà, le seuil est hors de l’intervalle accessible et le cycle s’arrête. La simulation affiche une sortie saturée constante et une fréquence égale à zéro, valeur qui signale l’absence d’oscillation.

## 97. Calculer le seuil pour un pont identique

Spé — physique PSI/PT · Laboratoire `wien`

Les deux résistances du pont valent R = 10 kΩ et ses deux capacités valent C = 10 nF. Trouver la fréquence sélectionnée et le gain critique. Pour un amplificateur non inverseur de gain 1 + Rf/Rg, choisir le rapport Rf/Rg au seuil.

**Correction guidée**

La fréquence est f₀ = 1/(2πRC) = 1591,55 Hz. Le gain critique vaut 1 + 1 + 1 = 3. L’amplificateur doit donc avoir Rf/Rg = 2 au seuil. Pour démarrer à partir d’une petite perturbation, son gain initial doit être légèrement supérieur à 3 ; une non-linéarité doit ensuite stabiliser l’amplitude.

## 98. Vérifier un pont dissymétrique

Spé — montage accompagné · Laboratoire `wien`

Le pont a R₁ = 20 kΩ, R₂ = 10 kΩ, C₁ = 10 nF et C₂ = 20 nF. Calculer f₀ et Gcrit. La règle « gain égal à 3 » reste-t-elle valable ?

**Correction guidée**

√(R₁R₂C₁C₂) = 200 µs, donc f₀ = 1/(2π × 200 µs) = 795,77 Hz. Le gain critique vaut 1 + R₁/R₂ + C₂/C₁ = 1 + 2 + 2 = 5. Le gain 3 conviendrait seulement à deux branches identiques. À gain 3, ce pont dissymétrique ne peut pas démarrer une oscillation dans le modèle linéaire.

## 99. Séparer condition de démarrage et amplitude finale

Spé — non-linéarités · Laboratoire `wien`

Pour un pont identique avec RC = 100 µs, le gain est G = 3,06. Estimer le taux de croissance initial γ près du seuil. Le modèle linéaire permet-il de prévoir une amplitude finale ?

**Correction guidée**

On a a = 3RC, b = RC et d = (RC)². Donc γ ≈ (G − 3)/(2RC) = 0,06/(200 µs) = 300 s⁻¹. L’enveloppe est multipliée par e en environ 3,33 ms au début. Le modèle linéaire continue à croître sans sélectionner d’amplitude. Le plateau du laboratoire vient d’une loi d’enveloppe non linéaire explicitement fournie ; il n’est pas déduit du gain critique.

## 100. Redresser une tension plus petite que le seuil

Sup — diodes ; spé — ALI · Laboratoire `redresseur_precision`

Une entrée sinusoïdale a E = 0,20 V crête. Les diodes ont Vᴅ = 0,60 V. Comparer un pont passif et le redresseur de précision à trois résistances égales ; les rails de l’ALI valent ±12 V.

**Correction guidée**

Le pont passif exige deux seuils, soit 1,20 V : il ne conduit jamais et sa sortie est nulle dans ce modèle. Le redresseur de précision fournit |e|, donc 0,20 V crête. Son ALI doit produire jusqu’à E + Vᴅ = 0,80 V en interne, valeur compatible avec les rails ±12 V. Ce raisonnement est quasi statique.

## 101. Retrouver la sortie différentielle par alternance

Spé — montage accompagné · Laboratoire `redresseur_precision`

Les trois résistances sont égales. En régime compensé, calculer vₛ₁, vₛ₂ et vₛ₂ − vₛ₁ pour e = +0,40 V, puis pour e = −0,40 V.

**Correction guidée**

Pour e = +0,40 V, la branche négative donne vₛ₁ = −0,40 V et vₛ₂ = 0 : la différence vaut +0,40 V. Pour e = −0,40 V, l’autre branche donne vₛ₁ = 0 et vₛ₂ = +0,40 V : la différence vaut encore +0,40 V. Le résultat utile est une différence de deux tensions, et non la seule sortie interne de l’ALI.

## 102. Évaluer la marge de compensation

Spé — limites d’ALI · Laboratoire `redresseur_precision`

Les rails de sortie valent ±3,0 V, le seuil de chaque diode vaut 0,60 V et l’entrée atteint 5,0 V crête. Quelle amplitude reste compensable ? Quelle crête montre le modèle quasi statique ?

**Correction guidée**

La compensation exige |e| + 0,60 ≤ 3,0 V, donc |e| ≤ 2,40 V. La crête utile du modèle limité vaut 2,40 V au lieu des 5,0 V idéaux. Augmenter la fréquence ne corrige pas ce manque de marge ; une expérience rapide peut ajouter une autre erreur, liée à la vitesse ou à la récupération de l’ALI.

## 103. Calculer les caractéristiques du filtre à trois ALI

Spé — physique PSI/PT, montage accompagné · Laboratoire `filtre_etat`

R₁ = R₃ = R₄ = R₅ = R₆ = 10 kΩ, R₂ = 30 kΩ et C = 10 nF. Calculer H₀, ω₀, Q et la largeur de bande en hertz.

**Correction guidée**

H₀ = R₂R₅/(R₁R₄) = 3. Avec des résistances de 10 kΩ dans la formule de fréquence, ω₀ = 1/(10 kΩ × 10 nF) = 10 000 rad/s, soit f₀ = 1591,55 Hz. Q = R₂Cω₀ = 3. Δω = 1/(R₂C) = 3333,33 rad/s ; Δf = Δω/(2π) = 530,52 Hz. Une largeur exprimée en rad/s ne doit pas être confondue avec celle en hertz.

## 104. Isoler le troisième harmonique du créneau

Sup — spectre fourni ; spé — filtre actif · Laboratoire `filtre_etat`

Un créneau impair a une crête E = 1 V. Sa fondamentale vaut fₑ = f₀/3. Le filtre a H₀ = 3 et Q = 3 ; on suppose que seul le troisième harmonique appartient à sa bande à −3 dB. Trouver la sortie obtenue en ne gardant que ce terme.

**Correction guidée**

Le coefficient du troisième harmonique est A₃ = 4E/(3π) = 0,42441 V. Il est exactement à la fréquence centrale, où H = H₀ = 3, réel positif. La sortie approchée est donc vₛ(t) ≈ (4/π) sin(2πf₀t) V, de crête 1,27324 V. La sortie calculée avec toutes les harmoniques comporte aussi les contributions atténuées hors de la bande ; elles ne sont pas nulles.

## 105. Modifier la bande sans déplacer le centre

Spé — réglage de filtre · Laboratoire `filtre_etat`

Dans ce filtre, on double uniquement R₂. Que deviennent ω₀, H₀, Q et Δω ? Peut-on dire que seul le facteur de qualité change ?

**Correction guidée**

La formule de ω₀ ne contient pas R₂ : le centre est inchangé. H₀ est proportionnel à R₂ et double ; Q = R₂Cω₀ double également ; Δω = 1/(R₂C) est divisée par deux. La bande se resserre, mais le gain central augmente aussi. Comparer des sorties sans prendre en compte cette amplification ferait attribuer à tort tout l’effet à la sélection fréquentielle.

## 106. Calculer le repos avant le petit signal

Au-delà — modèle fourni · Laboratoire `transistor_polarisation`

Un NPN a Vcc = 12 V, Rb₁ = 10 kΩ vers la masse, Rb₂ = 47 kΩ vers l’alimentation, Re = 1 kΩ, Rc = 2,2 kΩ et β = 100. On fournit Vbe = 0,7 V et le seuil de saturation Vce,sat = 0,2 V. Calculer le courant de collecteur et vérifier le régime.

**Correction guidée**

Vth = 12 × 10/57 = 2,10526 V et Rth = 10 × 47/57 = 8,24561 kΩ. Ib = (2,10526 − 0,7)/(8,24561 kΩ + 101 kΩ) = 12,863 µA. Ic ≈ 1,2863 mA, Ve ≈ 1,2992 V et Vc ≈ 9,1701 V. Vce ≈ 7,871 V, très supérieur à 0,2 V : le régime actif supposé est cohérent. La résistance du pont n’a pas été négligée.

## 107. Comparer gain découplé et gain avec Re

Au-delà — modèle petit signal fourni · Laboratoire `transistor_polarisation`

Le courant de repos vaut Ic = 1,00 mA, β = 100 et Rc = 2,00 kΩ ; la sortie n’est pas chargée. On fournit Uₜ = 25,85 mV. Le générateur impose directement la petite tension de base. Trouver le gain avec émetteur découplé, puis avec Re = 1,00 kΩ non découplée.

**Correction guidée**

gm = Ic/Uₜ = 0,038685 S et rπ = β/gm = 2585 Ω. Avec découplage idéal, le gain vaut −gmRc = −77,37. Sans découplage, il vaut −βRc/[rπ + (β + 1)Re] = −200 000/(2585 + 101 000) = −1,9308. Le découplage augmente beaucoup le gain ; cette comparaison suppose un générateur idéal, sans atténuation au pont de base ni au condensateur de liaison.

## 108. Refuser un petit signal autour d’un repos saturé

Au-delà — validation du modèle · Laboratoire `transistor_polarisation`

Un calcul avec Ic = βIb donne Vc − Ve = −0,5 V pour un NPN et une alimentation positive. Peut-on utiliser ce courant pour calculer gm = Ic/Uₜ et prédire une amplification ? Quelle démarche suivre ?

**Correction guidée**

Cette tension contredit le régime actif supposé : le transistor est saturé avant ce point. On ne doit pas calculer un amplificateur petit signal autour de cette solution fictive. Il faut résoudre le repos avec les tensions de jonction du modèle saturé, puis modifier le pont, Rc ou Re pour retrouver un régime actif avec de la marge de tension. Le laboratoire désactive sa réponse petit signal quand le repos est bloqué ou saturé.
