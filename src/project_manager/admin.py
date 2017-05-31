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
        nome_projeto = projeto.nome
        participantes = list(projeto.participantes.all())
        nomes_participantes = []
        for participante in participantes:
            nomes_participantes.append(participante.username)
        usuario_root = User.objects.get(username='gabriellmb05')

        cria_repositorio(projeto.pk, usuario_root)
        adiciona_colaboradores(projeto.pk, usuario_root, nomes_participantes)
        return HttpResponseRedirect('/project_manager/projeto')



    def atualizar_participantes(self, request, pk, *args, **kwargs):
        projeto = Projeto.objects.get(pk=pk)
        participantes_antigos = set(list(projeto.participantes.all()))
        nomes_participantes_antigos = set()
        for participante in participantes_antigos:
            nomes_participantes_antigos.add(participante.username)
        usuario_root = User.objects.get(username='gabriellmb05')
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
                nomes_participantes_novos = set()
                for participante in participantes_novos:
                    nomes_participantes_novos.add(participante.username)
                lista_remocao = nomes_participantes_antigos.difference(nomes_participantes_novos)
                lista_adicao = nomes_participantes_novos.difference(nomes_participantes_antigos)
                print(nomes_participantes_antigos)
                print(nomes_participantes_novos)
                if lista_remocao != set():
                    remove_colaboradores(projeto.pk,usuario_root, lista_remocao)
                if lista_adicao != set():
                    adiciona_colaboradores(projeto.pk, usuario_root, lista_adicao)
                projeto.participantes = form.cleaned_data['participantes']
                projeto.save()

        return HttpResponseRedirect('/project_manager/projeto')


#    def save_model(self, request, obj, form, change):

#       obj.save()
admin.site.register(Projeto, ProjetoAdmin)




