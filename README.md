# ScopeCreep

## Exécution dans un conteneur Docker

### Déploiement et démarrage

1. Compiler et démarrer le conteneur Docker pour le site Web et la base de données.

		sudo docker-compose build
		sudo docker-compose up

### Configuration

1. Exécuter les migrations pour créer le schéma de la base de données correspondant au projet;

2. Créer le premier _super user_ du site pour accéder au site d'administration.

		sudo docker-compose run web python manage.py migrate
		sudo docker-compose run web python manage.py createsuperuser

3. Naviguer à l'adresse <http://localhost:80>

