import factory
from django.contrib.auth.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ('username', 'email', 'password')

    username = 'asleao'
    email = 'andre.sp.leao@gmail.com'
    password = '41251e4c06395df825477f646d5bc612bb7ea8db'
