# Formules de l’extrait M10–M11

Corrections limitées aux formules, conformément à l’autorisation de l’auteur pour cet atelier. Les pages citées sont les pages imprimées de l’extrait ; les conventions de Fourier sont celles fixées à la page 106.

## Page 105 · Exercice 10 : dérivées du binôme généralisé

Avec `f_p(u)=(1−u)^−(2p+1)/2`, les dérivées sont :

```text
f_p′(u) = (2p+1)/2 · f_(p+1)(u)
f_p^(k)(u) = [(2p+1)(2p+3)…(2p+2k−1)]/2^k · f_(p+k)(u).
```

Ces formules remplacent les signes négatifs et les indices décroissants imprimés. Pour p=0, la dérivée vaut `+(1/2)(1−u)^−3/2`. Le développement binomial final et l’intégrale elliptique finale de cette page restent corrects.

## Page 107 · TP RC : inversion du terme de la rampe

Pour l’entrée `u_E(t)=at+b`, au repos initial, la décomposition imprimée est correcte. La réponse s’écrit :

```text
u_S(t) = at+b−τa+(τa−b)e^(−t/τ), t≥0.
```

Le coefficient exponentiel imprimé `τ²a−τb` doit être divisé par τ, puisque `L⁻¹[1/(1+τp)]=(1/τ)e^(−t/τ)`. La formule ci-dessus vérifie `u_S(0+)=0` et `τu_S′+u_S=at+b`. Les réponses au pas et à l’impulsion données dans le même TP sont correctes.

## Page 108 · Peigne, échantillonnage et reconstruction

Pour le peigne **non pondéré** défini dans l’extrait, `P_a(t)=Σ_k δ(t−ka)`, et la transformée en Hz :

```text
TF(P_a)(ν) = (1/a) Σ_k δ(ν−k/a) = P(aν), avec P=P_1.
φ(t) = f(t) P_a(t)  ⇒  φ̂(ν) = (1/a) Σ_k f̂(ν−k/a).
f̂(ν) = a φ̂(ν) Π(aν), si la bande est contenue dans ]−1/(2a),1/(2a)[.
f(t) = φ * [t ↦ sin(πt/a)/(πt/a)].
```

Ces expressions restaurent les facteurs du peigne et du filtre de reconstruction. À `t=ja`, la reconstruction donne bien `f(ja)`, puisque le sinus cardinal vaut 1 à zéro et 0 aux autres entiers. **La formule finale de Shannon imprimée est correcte.**

Dans la formule de Poisson, après `c_n=ŝ(n/T)/T`, la somme des coefficients reconstruit la fonction périodisée **f(t)** ; le membre de gauche imprimé `f̂(t)` doit donc être `f(t)`.

Dans l’identité précédant Shannon, le membre spectral utilise **ŝ(ν+kF)**, avec le chapeau, à la place de `s(ν+kF)`. L’indicatrice `T(ν)=1_[−F/2,F/2](ν)` vaut **1 dans la bande et 0 hors de la bande** : cette expression corrige l’inversion des deux valeurs dans la ligne qui la développe. Elle donne bien `h(t)=F sin(πFt)/(πFt)`.

## Page 109 · Calculs de Fourier en pulsation

En conservant la convention unitaire de la page 106 :

```text
F_ω⁻¹[F_ω(f)](t) = (1/√(2π)) ∫ F_ω(f)(ω)e^(iωt)dω
                 = (1/(2π)) ∬ f(u)e^(−iωu)e^(iωt)du dω = f(t).
F_ω²(f)(t)       = (1/(2π)) ∬ f(u)e^(−iω(u+t))du dω = f(−t).
∫ exp(−iωx)dω   = 2πδ(x), au sens des distributions.
```

Les facteurs `1/√(2π)`, `1/(2π)` et `2π` doivent être rétablis dans les étapes intermédiaires imprimées. Les résultats finaux `f(t)` et `f(−t)` sont corrects. Le dernier membre intitulé `F_ω²(f̂)` correspond au calcul de **F_ω²(f)** commencé à la ligne précédente.
