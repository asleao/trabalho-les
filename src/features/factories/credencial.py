import factory
from project_manager.models import *


class CredencialFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Credencial
        django_get_or_create = ('user_name', 'token', 'agente', 'ferramenta')
