from django.conf.urls import url, include
from django.contrib import admin
from project_manager.views import *

urlpatterns = [

    url(r'^ferramenta/$', cadastro_ferramenta, name='cadastro_ferramenta' ),
    url(r'^$', login, name="login"),
    url(r'^cadastro$', cadastro_usuario, name="cadastro_usuario"),
]
