# Errata de formules — fiche M1, p.16

Ce document répond à l'autorisation donnée pour cet atelier. Il porte uniquement
sur les formules ci-dessous, vérifiées sur la page imprimée 16 du PDF dans leur
contexte. Il ne contient pas de remarques éditoriales ou pédagogiques.

## Groupe spécial linéaire et composantes réelles de GL

La page identifie `SLₙ(𝕂)` à `GLₙ⁺(𝕂)` puis emploie les conditions `det=+1`
et `det=−1` pour désigner les deux composantes réelles du groupe général linéaire.
Pour les matrices réelles, les formules sont :

```text
SLₙ(ℝ) = {A ∈ Mₙ(ℝ) : det A = 1}
GLₙ⁺(ℝ) = {A ∈ Mₙ(ℝ) : det A > 0}
GLₙ⁻(ℝ) = {A ∈ Mₙ(ℝ) : det A < 0}
GLₙ(ℝ) = GLₙ⁺(ℝ) ⊔ GLₙ⁻(ℝ)
SLₙ(ℝ) ⊊ GLₙ⁺(ℝ)
```

Les deux ensembles de signes sont les deux composantes connexes par arcs de
`GLₙ(ℝ)` pour les dimensions du contexte. Le déterminant peut varier au sein
d'une composante tout en gardant son signe. Par exemple,

```text
A = diag(2, 1, 1, 3)
det A = 6 > 0
A ∈ GL₄⁺(ℝ), mais A ∉ SL₄(ℝ).
```

Sur le corps complexe, la formule du groupe spécial reste
`SLₙ(ℂ)={A:det A=1}` ; les inégalités de signe ne définissent pas deux composantes
de `GLₙ(ℂ)`, qui est connexe par arcs.
