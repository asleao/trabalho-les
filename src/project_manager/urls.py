from django.conf.urls import url, include
from django.contrib import admin
from project_manager.views import *

urlpatterns = [
    url(r'^$', hello_world ),
    url(r'^ferramenta/$', cadastro_ferramenta, name='cadastro_ferramenta' ),
]
