from django.apps import AppConfig

# Se usa la ubicacion de esta clase para registrar la aplicacion en el proyecto (settings.py)
class EncuestasConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'encuestas'
