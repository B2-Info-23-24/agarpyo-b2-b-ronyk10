# Roro.io

Roro.io est le projet final du cours de Python réalisé à Lyon Ynov Campus, pour les deuxièmes années de bachelor informatique.
C'est un dérivé du célèbre jeu Agar.io, en mode solo.

## Prérequis

Assurez-vous d'avoir les versions spécifiées des packages suivants installées sur votre système, ainsi que Python et Miniconda.

- Python (version utilisée pour le développement : 3.10.13)
- Pygame (version utilisée pour le développement : 2.5.2)

## Installation

Clonez le dépôt sur votre machine locale.

```bash
git clone https://github.com/B2-Info-23-24/agarpyo-b2-b-ronyk10.git
```

Accédez au répertoire du projet.

```bash
cd ./agarpyo-b2-b-ronyk10
```

Créez et activez un environnement virtuel à partir d'un fichier d'import environnement.yml
```bash
conda env create -f roroio.yaml
conda activate roroio
```


## Lancer le jeu
```bash
python menu.py
```

## Utilisation
Lors du lancement de Roro.io, le choix est laissé à l'utilisateur de pouvoir sélectionner son mode de jeu, avec le clavier (via les touches Z,Q,S,D), ainsi que la difficulté qu'il souhaite parmi 3 distinctes : 
Facile, Moyen et Difficile. 
Il vous est possible de quitter la partie à tout moment en appuyant sur la touche "Echap" de votre clavier.

![image](https://github.com/B2-Info-23-24/agarpyo-b2-b-ronyk10/assets/115625855/010f3c2c-9ff6-473a-84c5-e216178bfb0a)


## Contribution

Si vous souhaitez contribuer à ce projet, veuillez suivre les étapes suivantes :

1. Forkez le projet.
2. Créez une branche pour votre fonctionnalité (**git checkout -b fonctionnalite/ma-fonctionnalite**).
3. Committez vos changements (**git commit -m 'Ajouter une nouvelle fonctionnalité'**).
4. Poussez la branche sur votre fork (**git push origin fonctionnalite/ma-fonctionnalite**).
5. Ouvrez une pull request.


