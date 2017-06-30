import factory
from project_manager.models import Linguagem

class LinguagemFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Linguagem
        django_get_or_create = ('nome',)

    nome = 'Python'