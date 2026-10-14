# Chimie pour l’industrie — corrections de formules

Corrections vérifiées dans le contexte des fiches **C6, C7 et C8**, pages imprimées **545–570** du recueil de A. R. Les pages citées sont celles du recueil. Les formules ont été relues sur le PDF, puis contrôlées par substitution, bilan ou calcul indépendant.

## C6 — Cinétique

### 1. Page 546, TP — thiosulfate de sodium

La formule imprimée **Na₂SO₃** désigne le sulfite. Pour le thiosulfate employé dans le TP, écrire **Na₂S₂O₃** : deux ions Na⁺ compensent la charge de S₂O₃²⁻, présent dans le bilan de la réaction.

### 2. Page 548 — solution de A + B ⇌ C + D

Dans les conditions de la page, $`[A]_0=[B]_0=a`$, $`[C]_0=[D]_0=0`$ et $`x`$ est la concentration formée de C ou D. Les constantes des deux sens sont $`k_1>0`$ et $`k_{-1}>0`$.

L’expression imprimée

$$
x=x_{\mathrm{éq}}\left[1-2\left(1-\frac{x_{\mathrm{éq}}}{a}\right)
\exp\left(\frac{2a(x_{\mathrm{éq}}-a)k_1t}{x_{\mathrm{éq}}}\right)\right]
$$

doit être remplacée, comme solution exacte, par

$$
x(t)=x_{\mathrm{éq}}\,
\frac{1-e^{-\lambda t}}
{1+(1-2x_{\mathrm{éq}}/a)e^{-\lambda t}},
\qquad
x_{\mathrm{éq}}=\frac{a\sqrt{k_1}}{\sqrt{k_1}+\sqrt{k_{-1}}},
\qquad
\lambda=2a\sqrt{k_1k_{-1}}.
$$

La formule corrigée satisfait $`x(0)=0`$ et $`\dot x=k_1(a-x)^2-k_{-1}x^2`$. Pour $`a=1`$, $`k_1=1`$, $`k_{-1}=4`$, l’expression imprimée donne $`x(0)=-1/9`$. Elle correspond au premier terme de l’approche de l’équilibre à grand temps ; la page ne la présente pas comme une approximation asymptotique.

## C7 — Oxydo-réduction et électrochimie

### 3. Page 552 — seuil de corrosion sèche

Notons $`\nu_{\mathrm{O_2}}>0`$ le nombre de moles de dioxygène **consommées** dans la réaction d’oxydation, $`p^\circ`$ la pression standard et $`p_{\mathrm{O_2,éq}}`$ sa pression d’équilibre. Pour des phases condensées pures :

$$
\Delta_{\mathrm r}G^\circ(T)
=\nu_{\mathrm{O_2}}RT
\ln\left(\frac{p_{\mathrm{O_2,éq}}}{p^\circ}\right).
$$

Le signe **moins** imprimé doit être remplacé par **plus**. Pour une réaction normalisée à une mole de O₂, $`\nu_{\mathrm{O_2}}=1`$. En effet, $`Q=(p_{\mathrm{O_2}}/p^\circ)^{-\nu_{\mathrm{O_2}}}`$ et $`\Delta_{\mathrm r}G^\circ+RT\ln Q_{\mathrm{éq}}=0`$.

### 4. Page 552 — potentiel du calomel saturé

Pour $`\mathrm{Hg_2Cl_2(s)+2e^-\rightleftharpoons2Hg(l)+2Cl^-}`$, $`a_{\mathrm{Cl^-}}`$ désigne l’activité du chlorure. La loi générale est

$$
E=E^\circ_{\mathrm{Hg_2Cl_2/Hg}}
-\frac{RT}{2F}\ln(a_{\mathrm{Cl^-}}^2).
$$

Dans la formule imprimée $`E=0{,}244-0{,}03\log_{10}[\mathrm{Cl^-}]^2`$, **0,244 V est le potentiel saturé annoncé dans ce paragraphe**, et non le potentiel standard à activité unité. L’effet de la saturation ne doit pas être retranché une seconde fois.

Si $`E_{\mathrm{sat}}`$ et $`a_{\mathrm{Cl^-,sat}}`$ sont les valeurs à saturation KCl, une écriture utilisant cette référence est

$$
E=E_{\mathrm{sat}}-\frac{RT}{F}
\ln\left(\frac{a_{\mathrm{Cl^-}}}{a_{\mathrm{Cl^-,sat}}}\right).
$$

À saturation, elle restitue $`E=E_{\mathrm{sat}}`$, soit la valeur arrondie **0,244 V** de la fiche.

### 5. Page 553 — dérivation de Debye–Hückel

Conservons les objets de la page : $`V_i`$ est un potentiel électrique, $`q_i=k_i e`$ la charge de l’ion central, $`\varepsilon=\varepsilon_0\varepsilon_r`$, $`n_{j,0}`$ la densité d’ions de type $`j`$ loin de cet ion, et $`r_0`$ la distance minimale d’approche.

**Poisson et Boltzmann.** Le signe de Poisson et la charge dans l’exposant doivent être

$$
\Delta V_i=-\frac{\rho_i}{\varepsilon},
\qquad
n_j=n_{j,0}\exp\left(-\frac{k_j eV_i}{k_BT}\right),
$$

au lieu de $`\Delta V_i=+\rho_i/\varepsilon`$ et de l’exposant $`-V_i/(k_BT)`$. Avec $`\rho_i=\sum_j k_j e n_j`$, le membre droit de l’équation non linéaire porte donc aussi un signe global **moins**. L’énergie d’un ion est $`q_jV_i`$, ce qui rend l’exposant sans dimension.

La neutralité et la linéarisation conduisent bien à la relation imprimée

$$
\Delta V_i=\kappa^2V_i,\qquad
\kappa^2=\frac{e^2}{\varepsilon k_BT}\sum_j n_{j,0}k_j^2.
$$

**Solution radiale.** Comme $`\kappa`$ est une longueur inverse, les exponentielles sont $`e^{-\kappa r}`$ et $`e^{+\kappa r}`$, au lieu de $`e^{-r}`$ et $`e^r`$. La solution qui s’annule à l’infini et sa condition de contact sont

$$
V_i(r)=\frac{k_i e}{4\pi\varepsilon}
\frac{e^{-\kappa(r-r_0)}}{(1+\kappa r_0)r},
\qquad
V_i'(r_0)=-\frac{k_i e}{4\pi\varepsilon r_0^2}.
$$

Il faut donc remettre **$`\kappa`$ dans $`e^{-\kappa r}`$**, **$`r_0`$ dans $`1+\kappa r_0`$** et **$`4\pi`$ dans la condition de contact**. Une dérivation de $`V_i(r)`$ restitue cette condition et l’équation radiale.

**Soustraction du potentiel central.** Le terme coulombien à retrancher est $`k_i e/(4\pi\varepsilon r_0)`$, au lieu de $`k_i e/(\varepsilon r_0)`$. L’expression corrigée est

$$
V_i(r_0)-\frac{k_i e}{4\pi\varepsilon r_0}
=-\frac{k_i e\kappa}{4\pi\varepsilon(1+\kappa r_0)}.
$$

Ces corrections rétablissent les signes, les dimensions et les facteurs de la dérivation ; elles ne changent pas la loi finale des coefficients d’activité de la fiche.

### 6. Page 555 — potentiel standard et coefficient décimal de Nernst

Pour la demi-équation de réduction

$$
\nu_1\mathrm{Ox}+n e^-+m\mathrm{H^+}
\rightleftharpoons\nu_2\mathrm{Réd}+\nu_3\mathrm{H_2O},
$$

les $`\nu_i`$ sont les coefficients indiqués, $`n`$ le nombre d’électrons, et $`\Delta_{\mathrm f}G^\circ`$ les enthalpies libres standard de formation. Dans la convention de la page, $`\Delta_{\mathrm f}G^\circ_{\mathrm{H^+}}=0`$.

L’expression imprimée avec les trois termes **additionnés** doit être

$$
E^\circ=\frac{
\nu_1\Delta_{\mathrm f}G^\circ_{\mathrm{Ox}}
-\nu_2\Delta_{\mathrm f}G^\circ_{\mathrm{Réd}}
-\nu_3\Delta_{\mathrm f}G^\circ_{\mathrm{H_2O}}
}{nF}.
$$

La vérification est $`\Delta_{\mathrm r}G^\circ=\text{produits}-\text{réactifs}=-nFE^\circ`$.

Pour convertir le logarithme naturel en logarithme décimal, le coefficient correct à 298 K est

$$
\frac{RT}{F}\ln 10\simeq0{,}05916\ \mathrm V,
$$

au lieu de $`RT/(F\ln 10)\simeq0{,}059`$. En effet, $`\ln a=(\ln 10)\log_{10}a`$. Les formes générales de Nernst et la ligne utilisant $`0{,}059/n`$ déjà données sur cette page sont correctes.

### 7. Page 555 — pH de précipitation des hydroxydes

Avec $`h=a_{\mathrm{H^+}}`$, $`K_e`$ le produit ionique de l’eau, $`c`$ la concentration réduite à la référence de la fiche, et $`K_s,K_s'`$ les produits de solubilité respectifs, les deux seuils sont

$$
\mathrm{pH}_2=-\log_{10}\!\left[K_e(c/K_s)^{1/2}\right],
\qquad
\mathrm{pH}_3=-\log_{10}\!\left[K_e(c/K_s')^{1/3}\right].
$$

Le signe **moins** manque devant les deux logarithmes. Les expressions de $`h`$ qui les précèdent sont correctes : $`\mathrm{pH}=-\log_{10}h`$.

### 8. Page 555 — concentration de Fe²⁺ au-dessus du seuil

Pour $`\mathrm{Fe(OH)_2(s)\rightleftharpoons Fe^{2+}+2OH^-}`$, avec les mêmes concentrations réduites que la fiche :

$$
[\mathrm{Fe^{2+}}]=\frac{K_s h^2}{K_e^2},
$$

au lieu de $`K_s h^2/K_e^3`$. Substituer $`[\mathrm{OH^-}]=K_e/h`$ dans $`K_s=[\mathrm{Fe^{2+}}][\mathrm{OH^-}]^2`$ donne le **carré**. Au seuil, la formule corrigée restitue $`c`$.

### 9. Page 555 — coefficient du dioxygène dans le bilan affiché

En conservant les autres termes de la réaction imprimée, écrire

$$
\mathrm{Fe(OH)_3+\tfrac12H_2O
\rightleftharpoons Fe^{2+}+3OH^-+H^++\tfrac14O_2}.
$$

Le coefficient de O₂ est **1/4**, au lieu de **1/2** : il y a alors 3,5 atomes d’oxygène de chaque côté, quatre hydrogènes et une charge totale nulle.

### 10. Page 556 — somme des nombres d’oxydation

Pour une espèce de charge totale $`z`$ en unités de la charge élémentaire, $`N_i`$ étant le nombre d’atomes de type $`i`$ :

$$
\sum_i N_i\,\mathrm{no}(i)=z.
$$

Dans la ligne « composé ionique », la charge ne doit pas être **ajoutée à la somme**. Par exemple, dans SO₄²⁻, $`6+4(-2)=-2`$, déjà égal à la charge de l’ion.

### 11. Page 556 — limites de Tafel

Gardons la convention imprimée : $`\eta=E-E_{\mathrm{éq}}`$ et

$$
j=j_0\left[
e^{\alpha nF\eta/(RT)}
-e^{-(1-\alpha)nF\eta/(RT)}
\right],
\quad 0<\alpha<1,\quad j_0>0.
$$

Les deux limites, pour de fortes surtensions, sont

$$
\eta_a\simeq\frac{RT}{\alpha nF}\ln\left(\frac{j}{j_0}\right)
=\frac{RT\ln10}{\alpha nF}\log_{10}\left(\frac{j}{j_0}\right),
\quad j>0,
$$

$$
\eta_c\simeq-\frac{RT}{(1-\alpha)nF}
\ln\left(\frac{|j|}{j_0}\right),
\quad j<0.
$$

Les étiquettes anodique/cathodique et leurs formules doivent être mises en cohérence avec ces signes et coefficients. On garde respectivement la première ou la seconde exponentielle de Butler–Volmer ; le logarithme cathodique porte sur **$`|j|`$**.

### 12. Page 558, exercice 6 — potentiels libres du cuivre

Les deux signes de l’énoncé sont à corriger :

$$
E^\circ_{\mathrm{Cu^+/Cu}}=+0{,}51\ \mathrm V,
\qquad
E^\circ_{\mathrm{Cu^{2+}/Cu}}=+0{,}33\ \mathrm V.
$$

Le corrigé page 561 utilise précisément ces valeurs positives dans $`-FE^\circ`$ et $`-2FE^\circ`$. Elles donnent les résultats imprimés $`0{,}51-0{,}06(10{,}8)=-0{,}138`$ et $`0{,}33-0{,}03(11{,}8)=-0{,}024`$ V. La référence H⁺/H₂ à 0 V page 551 et le tableau page 561 confirment le sens réduction ; aucun changement de référence n’est nécessaire.

### 13. Page 560, exercice 4 — valeur de E₇°

Avec les données du corrigé :

$$
E_7^\circ=\frac{E_2^{\circ\prime}+2E_3^\circ}{3}
=\frac{0{,}11+2(0{,}45)}{3}
\simeq0{,}337\ \mathrm V,
$$

au lieu de **0,034 V**. Le quotient vaut $`1{,}01/3`$ ; les calculs qui suivent dans la fiche sont cohérents avec la valeur corrigée.

### 14. Page 561 — ordonnée du diagramme de Frost des complexes

L’axe doit porter **$`nE^\circ\ (\mathrm V)`$**, au lieu de **$`-nE^\circ\ (\mathrm V)`$**. Ici $`n`$ compte les électrons du couple avec Cu(s).

Les ordonnées tracées $`-0{,}138`$ pour Cu(I) et $`-0{,}048`$ pour Cu(II) sont bien $`1(-0{,}138)`$ et $`2(-0{,}024)`$. Le tracé et la conclusion de stabilité restent inchangés.

## C8 — Thermochimie

### 15. Page 563 — affinité de l’état réel

Avec $`\nu_i`$ les coefficients stœchiométriques algébriques et $`\mu_i`$ les potentiels chimiques **dans le mélange considéré** :

$$
\mathcal A=-\Delta_{\mathrm r}G=-\sum_i\nu_i\mu_i,
\qquad
\mathcal A^\circ=-\Delta_{\mathrm r}G^\circ.
$$

Le symbole standard **°** doit être retiré du premier $`\Delta_{\mathrm r}G`$ de l’égalité imprimée. La page 565 distingue déjà $`\mathcal A=\mathcal A^\circ-RT\ln Q`$.

### 16. Page 564 — état physique de ZnO dans le tableau

L’en-tête **ZnO(g)** doit être **ZnO(s)**. Le bilan, les réactions de réduction et le diagramme de cette même page utilisent le solide ; les valeurs $`-350{,}5\ \mathrm{kJ\,mol^{-1}}`$ et $`43{,}6\ \mathrm{J\,K^{-1}\,mol^{-1}}`$ sont employées pour ce même état.

### 17. Page 565 — constante d’équilibre

Avec $`a_{i,\mathrm{éq}}`$ les activités à l’équilibre et $`\nu_i`$ les coefficients algébriques :

$$
K^\circ=\prod_i a_{i,\mathrm{éq}}^{\nu_i},
\qquad
\ln K^\circ=\sum_i\nu_i\ln a_{i,\mathrm{éq}}.
$$

La ligne imprimée $`K^\circ=\ln\prod_i a_i^{\nu_i}`$ ajoute un logarithme à un seul côté. À l’équilibre, $`Q_{\mathrm{éq}}=K^\circ`$ ; si $`Q_{\mathrm{éq}}=1`$, la constante vaut 1, et non 0.

### 18. Page 569, exercice 2 — fonctions thermodynamiques de NO + ½ O₂ → NO₂

Le bilan calorimétrique de la fiche est correct :

$$
0{,}93\,\Delta_{\mathrm r}H^\circ(298)
=\Delta_{\mathrm r}H^\circ(298)+36(400-298).
$$

Les énergies étant ici en joules par mole, il donne

$$
\Delta_{\mathrm r}H^\circ(298)
=-\frac{36(400-298)}{0{,}07}
\simeq-52{,}457\ \mathrm{kJ\,mol^{-1}},
$$

au lieu de **−54,2 kJ·mol⁻¹**.

Les capacités thermiques données donnent

$$
C=\Delta_{\mathrm r}C_p^\circ=36-29-\tfrac12(29)
=-7{,}5\ \mathrm{J\,mol^{-1}\,K^{-1}}.
$$

Les coefficients de la formule imprimée $`-52-7{,}4T`$ sont à recalculer. Une expression cohérente, exprimée **ici en kJ·mol⁻¹**, est

$$
\Delta_{\mathrm r}H^\circ(T)
=-52{,}457-0{,}0075(T-298),
$$

avec $`T`$ exprimée numériquement en kelvins. Le facteur **$`10^{-3}`$**, le point de référence et l’enthalpie initiale doivent être cohérents.

Pour recalculer aussi les coefficients numériques de $`G`$ et $`S`$, notons $`T_0=800\ \mathrm K`$, $`H_0=\Delta_{\mathrm r}H^\circ(T_0)`$, $`G_0=\Delta_{\mathrm r}G^\circ(T_0)`$ et $`S_0=(H_0-G_0)/T_0`$. Une écriture cohérente, sans logarithme d’une grandeur dimensionnée, est

$$
\Delta_{\mathrm r}H^\circ(T)=H_0+C(T-T_0),
\qquad
\Delta_{\mathrm r}S^\circ(T)=S_0+C\ln(T/T_0),
$$

$$
\Delta_{\mathrm r}G^\circ(T)
=\Delta_{\mathrm r}H^\circ(T)-T\Delta_{\mathrm r}S^\circ(T).
$$

Employer la même unité d’énergie pour $`H_0,G_0,C`$ et $`S_0`$. En reprenant les données de pression en SI, $`8{,}2\ \mathrm{atm}=830\,865\ \mathrm{Pa}`$ : on retrouve $`x\simeq0{,}502`$ mol, $`K^\circ(800)\simeq0{,}782`$, $`G_0\simeq1{,}63`$ kJ·mol⁻¹, $`H_0\simeq-56{,}22`$ kJ·mol⁻¹ et $`S_0\simeq-72{,}32`$ J·mol⁻¹·K⁻¹. Les anciennes expressions numériques de $`G(T)`$ et $`S(T)`$ sont à recalculer avec ces mêmes données.

Contrôles : $`H'=C`$, $`S'=C/T`$, $`G'=-S`$ et $`H(298)=-52{,}457`$ kJ·mol⁻¹. Les relations intégrales de Gibbs imprimées restent correctes.

### 19. Pages 567 et 570 — signe de sublimation dans Born–Haber

La fiche définit l’enthalpie réticulaire comme la **dissociation** du solide en ions gazeux, et l’affinité électronique comme l’énergie d’arrachage de l’électron. En conservant ces conventions, avec $`E_{\mathrm i,Na}`$ l’énergie d’ionisation, $`AE_{\mathrm{Br}}`$ l’énergie d’arrachage, et les $`\Delta H^\circ`$ de sublimation, vaporisation, dissociation et formation :

$$
\Delta_{\mathrm{rétic}}H^\circ_{\mathrm{NaBr}}
=E_{\mathrm i,Na}-AE_{\mathrm{Br}}
+\tfrac12\Delta_{\mathrm{dis}}H^\circ_{\mathrm{Br_2}}
+\Delta_{\mathrm s}H^\circ_{\mathrm{Na}}
+\tfrac12\Delta_{\mathrm v}H^\circ_{\mathrm{Br_2}}
-\Delta_{\mathrm f}H^\circ_{\mathrm{NaBr}}.
$$

Le terme de sublimation du sodium porte **plus**, au lieu de **moins** dans la formule page 570.

Dans le cycle page 567, la flèche inverse $`\mathrm{Na(g)+\tfrac12Br_2(g)\to Na(s)+\tfrac12Br_2(l)}`$ porte

$$
-\Delta_{\mathrm s}H^\circ_{\mathrm{Na}}
-\tfrac12\Delta_{\mathrm v}H^\circ_{\mathrm{Br_2}},
$$

au lieu de $`+\Delta_{\mathrm s}H^\circ_{\mathrm{Na}}-\tfrac12\Delta_{\mathrm v}H^\circ_{\mathrm{Br_2}}`$. Les deux signes résultent du changement de sens de ces étapes du cycle.
