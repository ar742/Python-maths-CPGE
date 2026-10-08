# Premiers pas — Réactions de chimie organique

1. Installer Python 3.10 ou plus récent, puis double-cliquer sur `Lancer_Chimie_Organique.cmd`. L’installation initiale de NumPy demande une connexion ; les expériences fonctionnent ensuite hors ligne.
2. Ouvrir <http://127.0.0.1:8775>. L’accueil **Réactions du recueil** contient 61 fiches centrées sur les pages 524–528 et 531–534.
3. Filtrer par type ou rubrique, ou chercher « énolate », « Zaitsev », « aniline », « époxyde », un substrat ou un produit. Avant d’ouvrir le TP, prévoir les liaisons modifiées et le produit.
4. Cliquer **Prévoir le produit et explorer**. Lire le dossier réaction et son diagnostic, puis le but du TP, les variables et hypothèses. Les réglages correspondent à la fiche choisie ; une modification explore une variante.
5. Parcourir les étapes du mécanisme. Justifier départ et arrivée des électrons, charges, sous-produits, régiochimie et stéréochimie. Confronter votre prédiction au résultat avant de déplier la correction.
6. Suivre un [parcours du recueil](PARCOURS_REACTIONS.md), ouvrir la leçon associée et chercher les exercices avant leurs corrigés. Les repères **sup / spé / au-delà** et la [matrice du programme](MATRICE_PROGRAMME.md) situent les techniques.

Trois bons départs : **E2 et configurations R/S → E/Z**, **nitrobenzène et stratégie aromatique**, **énolate et alkylation C/O**. Les outils complémentaires IR/RMN, structures, CCM et extraction restent accessibles sur l’accueil.

[Présentation](README.md) · [Réactions, cours et corrections](REACTIONS_DU_RECUEIL.md) · [Cours complémentaire](COURS.md) · [42 illustrations](illustrations/README.md).

## Si le démarrage échoue

Le lanceur affiche le problème rencontré. Vérifier Python et l’installation de NumPy. Un port déjà utilisé se contourne avec :

```sh
python -X utf8 chimie_organique.py --port 8780
```

Ouvrir alors <http://127.0.0.1:8780>. Fermer la fenêtre de lancement termine le serveur.
