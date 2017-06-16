from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from .models import *
from django.utils.html import format_html
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.conf.urls import url
from .views import *
from django.contrib.auth.models import User
from .forms import *
from django.template.response import TemplateResponse
# Register your models here.
AdminSite.login_template = 'admin/login_custom.html'
admin.site.register(Ferramenta)
#admin.site.register(Projeto)
admin.site.register(Credencial)
admin.site.register(Linguagem)

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
             url(
               r'^(?P<pk>.+)/atualizar_participantes$',
                self.admin_site.admin_view(self.atualizar_participantes),
                name='atualizar_participantes',
            ),

        ]
        return custom_urls + urls


    def acao(self, obj):
        return format_html(
        '<a class="button" href="{}">Cadastrar projeto</a>&nbsp'
        '<a class="button" href="{}">Atualizar participantes</a>',
                reverse('admin:cadastrar_projeto', args=[obj.pk]),
                reverse('admin:atualizar_participantes', args=[obj.pk]),
            )





    def cadastrar_projeto(self, request, pk, *args, **kwargs):
        projeto = Projeto.objects.get(pk=pk)
        ferramentas = projeto.ferramentas

        for ferramenta in list(ferramentas.all()):
            criar_projeto_ferramenta(projeto, ferramenta)


        return HttpResponseRedirect('/project_manager/projeto')

    def atualizar_participantes(self, request, pk, *args, **kwargs):
        projeto = Projeto.objects.get(pk=pk)
        ferramentas = projeto.ferramentas
        participantes_antigos = set(list(projeto.participantes.all()))
        usuario_root = User.objects.get(username='LEDS')
        if request.method == 'GET':
            form = FormProjetoParcial(instance=projeto)
            context = self.admin_site.each_context(request)
            context['opts'] = self.model._meta
            context['form'] = form
            return TemplateResponse(
                request,
                'participantes.html',
                context,
            )
        else:
            form = FormProjetoParcial(request.POST, instance=projeto)
            if form.is_valid():

                participantes_novos = set(list(form.cleaned_data['participantes'].all()))
                for ferramenta in list(ferramentas.all()):
                    atualizar_participantes_ferramenta(participantes_antigos, participantes_novos, ferramenta, projeto)

                projeto.participantes = form.cleaned_data['participantes']
                projeto.save()

        return HttpResponseRedirect('/project_manager/projeto')

admin.site.register(Projeto, ProjetoAdmin)
