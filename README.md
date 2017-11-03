# ScopeCreep

## Exécution dans un conteneur Docker

### Démarrage

- Compilez et démarrez le conteneur Docker pour le site Web et la base de données.

```bash
docker-compose build
docker-compose up
```

### Configuration

- Exécutez les migrations pour créer le schéma de la base de données correspondant au projet;
- Créez le premier _super user_ du site pour accéder au site d'administration.

```bash
sudo docker-compose run web python manage.py migrate
sudo docker-compose run web python manage.py createsuperuser
```

## Exécution locale

### Prérequis

En cas de soucis avec la configuration de Docker, on peut aussi simplement démarrer le site sans conteneur à l'aide du serveur de développement Django.

Avant de pouvoir le faire, repérez les paramètre liées aux base de données. Retirez des commentaires les paramètres de connexion à la BD SQLite et mettez en commentaire les paramètres de connexion de la BD PostgreSQL du conteneur. **Veuillez ne pas commit ce changement.**

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```

### Démarrage

- Démarrez le serveur de développement Django.

```bash
python manage.py runserver
```

### Configuration

Il s'agit ici des mêmes commandes que dans le cas du conteneur Docker mais sans utiliser le conteneur.

- Exécutez les migrations pour créer le schéma de la base de données correspondant au projet;
- Créez le premier _super user_ du site pour accéder au site d'administration.

```bash
python manage.py migrate
python manage.py createsuperuser
```
