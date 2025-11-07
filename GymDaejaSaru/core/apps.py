from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'
    verbose_name = 'Gestión de Gimnasio'
    
    def ready(self):
        import core.signals  # Importar señales para que se registren

