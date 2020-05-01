from django.apps import AppConfig


class JobcallConfig(AppConfig):
    name = 'apps.jobcall'

    def ready(self):
        import apps.jobcall.signals