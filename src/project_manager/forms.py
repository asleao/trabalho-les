from django import forms
from django.forms import ModelForm, EmailInput, TextInput
from .models import *

class FormCadastroUsuario(forms.ModelForm):     
    class Meta:
        model = User
        fields = ('first_name','last_name','username','email','password')
        widgets = {
            'first_name': TextInput(attrs={'name':'first_name','class':'form-control'}),
            'last_name': TextInput(attrs={'name':'last_name','class':'form-control'}),
            'username': TextInput(attrs={'name':'last_name','class':'form-control'}),
            'email': EmailInput(attrs={'name':'email','class':'form-control'}),            
            'password': TextInput(attrs={'type':'password','name':'password','class':'form-control'}),
                  } 
        labels ={
            'first_name': 'Nome:',
            'last_name': 'Sobrenome:',
            'username': 'Matrícula:',
            'email': 'E-mail:',
            'password': 'Senha:',
        }       
