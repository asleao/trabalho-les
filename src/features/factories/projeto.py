import factory
from project_manager.models import *


class ProjetoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Projeto
        django_get_or_create = ('nome', 'ferramentas', 'participantes', 'dono', 'linguagem')
