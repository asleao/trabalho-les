from django.db import models
from django.contrib.auth.models import User

class Pessoa(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)    
    matricula = models.CharField(max_length=14, null=False, blank=False)    

    def __str__(self):
        return self.user.first_name
