# QUIZ
## Lancement de l'application

### Lancer la machine virtuel
Normalement une machine virtuel est déjà disponible. Si ce n'est pas le cas créez la avec la commande 
    `virtualenv -p python3 venv` ensuite lancez la machine virtuel python avec la commande
    `source venv/bin/activate`

Installer les dépendences avec la commande
    `pip install -r server/requirements.txt`

### Creer la base de données
Une base de données est déjà disponible répertoire. Si ce n'est pas le cas créez un fichier **questionnaire.db** puis populez la base de données avec la commande
    `flask loaddb`

### Lancer le serveur
Allumer le serveur avec la commande
    `flask run`

### Accéder au site
Dans le terminal allez dans le dossier **projetquiz** puis faite les commandes
    `npm install`
    `npm run dev --host`

## Ce qui à été fait

## Ce qui n'a pas été fait