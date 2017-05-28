from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from .models import *
# Register your models here.
AdminSite.login_template = 'admin/login_custom.html'
admin.site.register(Ferramenta)
admin.site.register(Projeto)
admin.site.register(Credencial)





