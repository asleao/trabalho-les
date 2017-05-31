from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from .models import *
from django.utils.html import format_html
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.conf.urls import url
from .views import *
from django.contrib.auth.models import User
# Register your models here.
AdminSite.login_template = 'admin/login_custom.html'
admin.site.register(Ferramenta)
#admin.site.register(Projeto)
admin.site.register(Credencial)


class ProjetoAdmin(admin.ModelAdmin):

    list_display = ('nome', 'dono', 'acao')

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            url(
               r'^(?P<pk>.+)/cadastrar_projeto$',
                self.admin_site.admin_view(self.cadastrar_projeto),
                name='cadastrar_projeto',
            ),

        ]
        return custom_urls + urls


    def acao(self, obj):
        return format_html(
        '<a class="button" href="{}">Cadastrar projeto</a>',
                reverse('admin:cadastrar_projeto', args=[obj.pk]),
            )

    def cadastrar_projeto(self, request, pk, *args, **kwargs):
        projeto = Projeto.objects.get(pk=pk)
        nome_projeto = projeto.nome
        participantes = projeto.participantes
        usuario_root = User.objects.get(username='gabriellmb05')

        cria_repositorio(projeto.pk, usuario_root)
        adiciona_colaboradores(projeto.pk, usuario_root)
        return HttpResponseRedirect('/project_manager/projeto')





#    def save_model(self, request, obj, form, change):

#       obj.save()
admin.site.register(Projeto, ProjetoAdmin)




