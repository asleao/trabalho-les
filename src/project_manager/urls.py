from django.conf.urls import url, include
from django.contrib import admin
from project_manager.views import *
from django.views.generic.base import RedirectView
urlpatterns = [

    url(r'^ferramenta/$', cadastro_ferramenta, name='cadastro_ferramenta' ),
    url(r'^entrar$', login, name="login"),
    url(r'^cadastro$', cadastro_usuario, name="cadastro_usuario"),
    url(r'^autoriza_usuario/$', autoriza_usuario, name="autoriza_usuario"),
    url(r'^cria_repositorio/$', cria_repositorio, name="cria_repositorio"),

]
