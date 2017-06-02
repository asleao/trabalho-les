from django.conf.urls import url, include
from django.contrib import admin
from project_manager.views import *
from django.views.generic.base import RedirectView
urlpatterns = [


    url(r'^autoriza_usuario/$', autoriza_usuario, name="autoriza_usuario"),
    url(r'^taiga/$', taiga, name="taiga"),
    #url(r'^cria_repositorio/$', cria_repositorio, name="cria_repositorio"),
    #url(r'^adiciona_colaboradores/$', adiciona_colaboradores, name="adiciona_colaboradores"),
    #url(r'^remove_colaboradores/$', remove_colaboradores, name="remove_colaboradores"),

]
