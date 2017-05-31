from django.db import models
from django.contrib.auth.models import User

class Ferramenta(models.Model):
    nome = models.CharField(max_length=60, blank=False, unique=True)
    link = models.URLField(max_length=200, blank=False)

    def __str__(self):
        return self.nome

class Credencial(models.Model):
    user_name =  models.CharField(max_length=60, blank=False, unique=True)
    token = models.CharField(max_length=60, blank=True, unique=True)
    agente = models.ForeignKey(User, on_delete=models.CASCADE)
    ferramenta = models.ForeignKey(Ferramenta, on_delete=models.CASCADE)

    def __str__(self):
        return self.ferramenta.nome

class Projeto(models.Model):
    nome = models.CharField(max_length=60, blank=False, unique=True)
    ferramentas = models.ManyToManyField(Ferramenta, related_name='ferramentas')
    participantes = models.ManyToManyField(User, related_name='participantes')
    dono = models.ForeignKey(User, on_delete=models.CASCADE, related_name='dono')

    def __str__(self):
        return self.nome

