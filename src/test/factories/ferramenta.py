import factory
from app.models import Ferramenta

class FerramentaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ferramenta
        django_get_or_create = ('nome', 'link')

    nome = 'ferramentaTeste'
    link = 'ferramentateste.com.br'