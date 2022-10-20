from django.apps import AppConfig

from myproject.settings import DEFAULT_AUTO_FIELD


class MyappConfig(AppConfig):
    DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
    name = 'myapp'
