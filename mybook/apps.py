from django.apps import AppConfig


class MybookConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mybook'


    def ready(self):
        import mybook.signals