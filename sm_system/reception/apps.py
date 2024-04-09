from django.apps import AppConfig


class ReceptionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sm_system.reception'

    def ready(self):
        import sm_system.reception.signals
        result = super().ready()
        return result
