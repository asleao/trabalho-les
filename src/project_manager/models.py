from django.db import models
from django.contrib.auth.models import User

class Ferramenta(models.Model):
    nome = models.CharField(max_length=60, blank=False, unique=True)
    link = models.URLField(max_length=200, blank=False)

    def __str__(self):
        return self.nome