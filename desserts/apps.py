from django.apps import AppConfig


class DessertsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "desserts"

    def ready(self):
        import my_auth.signals
