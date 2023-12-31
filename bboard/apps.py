from django.apps import AppConfig


class BboardConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bboard'
    verbose_name = 'Доска объявлений'

    def ready(self):
        import bboard.signals
