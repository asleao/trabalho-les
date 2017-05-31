from django import forms
from django.forms import ModelForm, EmailInput, TextInput
from .models import *


class FormProjetoParcial(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = ('participantes',)
