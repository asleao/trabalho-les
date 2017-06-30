import factory
from project_manager.models import *


class FerramentaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ferramenta
        django_get_or_create = ('nome', 'link')

    nome = 'Github'
    link = 'www.github.com'
