from django.apps import AppConfig


def create_app():
    class HeroConfig(AppConfig):
        name = 'hero'


my_app = create_app()
