##Aymeric BACHELET (BACA24060106) et Tom PIERRE (PIET08110102)

- Les articles, catégories et commentaires présents actuellement dans la base de données sont des textes "lorem ipsum" générés, ils n'ont aucune signification, ils sont là pour dnner une idée de la forme de l'application remplie.
- 


Les instructions pour lancer le projet correctement qui nous ont été données pour la base de cette application :
#### Conditions préalables:

Vous devez avoir déjà installé :

- python
- pip
- virtualenv

#### Mise en place du projet

1. Décompressez le fichier
2. Allez dans le dossier du projet et installez un dossier d'environnement virtuel : 
```
virtualenv .venv
```

3. Activez l'environnement virtuel :
```
source .venv/bin/activate (linux)
.venv\Scripts\activate.bat (windows)
```

4. Installez toutes les bibliothèques et extensions requises pour ce projet. Toutes les dépendances sont répertoriées dans le fichier requirements.txt. Exécutez la commande ci-dessous pour les installer tous en une seule commande (windows ou linux) :

```
pip install -r requirements.txt
```

#### Pour déployer la base de données

En utilisant Shell (linux ou Mac) ou CMD (windows), tapez les commandes suivantes :

```shell
$ flask db init
$ flask db migrate -m “Initial migration.”
$ flask db upgrade
```

#### Pour remplir la base de données :

Pour que nous ayons des données avec lesquelles nous pouvons effectuer certaines tâches, exécutez le script ci-dessous en utilisant le shell de votre système :

```shell
$ python populate_db.py 
```

#### Pour exécuter le projet :

exécutez la commande suivante dans votre terminal. Une autre option consiste à l'exécuter à partir de Visual Studio en cliquant sur l'icône "Play". Remarque : n'oubliez pas de vérifier l'interpréteur python installé dans votre environnement virtuel.

```
python3 run.py
```

ou

```
python run.py
```

#### Structure des répertoires de projet :

Le dossier **blueprints** contient le fichier default.py qui définit deux blueprints : default et users. Le blueprint 'users' crée les routes pour le CRUD d'utilisateur (créer, lire, mettre à jour et supprimer l'utilisateur). Le blueprint 'default' crée la route d'index (page d'accueil) et les routes de connexion et de déconnexion.

Le dossier '**controllers**' définit deux contrôles : un pour les utilisateurs et un pour les trois routes par défaut (index, login, logout). C'est dans les contrôleurs que la logique du système est exécutée.

Le dossier **ext** stocke toutes les extensions installées dans l'application : Bootstrap-flask (apparence, py), flask-sqlachemy (database.py), flask-login (login.py) et flask-migration (migration.py).

Le dossier de modèles (**models**) contient le modèle de tables de base de données (tables.py) et les objets Web Forms (forms.py).

Le dossier '**static**' est utilisé pour stocker les fichiers statiques couramment utilisés dans le front-end, tels que les fichiers CSS, les fichiers JS, les polices, les images, les vidéos, etc.

Le dossier '**templates**' contient tous les modèles utilisés pour rendre les écrans d'application. En particulier, base.html est un modèle utilisé comme base pour les autres modèles.

En dehors du dossier **app**, il y a le dossier tests, où nous conservons tous les fichiers de test. Nous exécutons ces tests via la commande "pytest tests". En plus du dossier tests, nous avons les fichiers run.py, qui est le premier fichier exécuté dans l'application, config.py, qui stocke les données de configuration de l'application, et populate_db.py. Ce dernier est un script spécial qui nous aide à créer des données dans la base de données pour tester l'application.

