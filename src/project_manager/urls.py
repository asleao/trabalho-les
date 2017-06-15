from django.conf.urls import url, include
from django.contrib import admin
from project_manager.views import *
from django.views.generic.base import RedirectView
urlpatterns = [


    url(r'^autoriza_usuario/$', autoriza_usuario, name="autoriza_usuario"),

]
