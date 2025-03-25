# QUIZ
## Lancement de l'application

### Lancer la machine virtuel
Normalement une machine virtuel est déjà disponible. Si ce n'est pas le cas créez la avec la commande 
    `virtualenv -p python3 venv` ensuite installez les dépendences avec la commande
    `pip install -r requirement.txt`

Lancer la machine virtuel python avec la commande
    `source venv/bin/activate`

### Creer la base de données
Une base de données est déjà disponible répertoire. Si ce n'est pas le cas créez un fichier **questionnaire.db** puis populez la base de données avec la commande
    `flask loaddb`

### Lancer le serveur
Allumer le serveur avec la commande
    `flask run`

### Accéder au site
Ouvrez le fichier **questionnaire.html** se trouvant dans le dossier **js**

## Ce qui à été fait
Globalement beaucoup de chose ont été faite comme l'héritage de la classe question. Il y a un crud sur toute les classes de la base de données
Actuellement il y a seulement deux type de question : SimpleQuestion et OpenQuestion

## Ce qui n'a pas été fait
Il y a un problème avec le changement de type de question du a la façon dont est fait cette dernière dans le views.py

Il n'est pas possible de faire les questionnaire. On peut juste les modifier