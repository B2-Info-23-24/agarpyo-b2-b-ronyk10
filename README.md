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
conda env create -f roroio.yml
conda activate roroio
```

## Contenu de roroio.yml
```bash
name: roroio
channels:
  - defaults
dependencies:
  - bzip2=1.0.8=he774522_0
  - ca-certificates=2023.12.12=haa95532_0
  - libffi=3.4.4=hd77b12b_0
  - openssl=3.0.13=h2bbff1b_0
  - pip=23.3.1=py310haa95532_0
  - python=3.10.13=he1021f5_0
  - setuptools=68.2.2=py310haa95532_0
  - sqlite=3.41.2=h2bbff1b_0
  - tk=8.6.12=h2bbff1b_0
  - tzdata=2023d=h04d1e81_0
  - vc=14.2=h21ff451_1
  - vs2015_runtime=14.27.29016=h5e58377_2
  - wheel=0.41.2=py310haa95532_0
  - xz=5.4.5=h8cc25b3_0
  - zlib=1.2.13=h8cc25b3_0
  - pip:
      - pygame==2.5.2

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


