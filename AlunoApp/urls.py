from django.urls.conf import path, re_path

from . import views


app_name = 'AlunoApp'

urlpatterns = [
    path('', views.IndexTemplateView.as_view(), name='index'),
    # re_path(r'^ajax/(?P<json>\w+|)/$', views.AjaxTemplateView.as_view(), name='ajax'),
    re_path(r'^listar/aluno/$', views.AlunoListView.as_view(), name='listar-aluno'),
    # re_path(r'^cadastrar/agenda/$', views.AgendaCreateView.as_view(), name='cadastrar-agenda'),
    # re_path(r'^alterar/agenda/(?P<pk>\w+|)/$', views.AgendaUpdateView.as_view(), name='alterar-agenda'),
    # re_path(r'^excluir/agenda/(?P<pk>\w+|)$', views.AgendaDeleteView.as_view(), name='excluir-agenda'),
    # re_path(r'^listar/aviso/$', views.AvisoListView.as_view(), name='listar-aviso'),
    # re_path(r'^listar/aviso/usuario/$', views.AvisoUsuarioListView.as_view(), name='listar-aviso-usuario'),
    # re_path(r'^cadastrar/aviso/$', views.AvisoCreateView.as_view(), name='cadastrar-aviso'),
    # re_path(r'^detalhar/aviso/(?P<pk>\w+|)/$', views.AvisoDetailView.as_view(), name='detalhar-aviso'),
    # re_path(r'^detalhar/aviso/(?P<pk>\w+|)/(?P<usuario>\w+|)/$', views.AvisoDetailView.as_view(), name='detalhar-aviso'),
    # re_path(r'^listar/canal/$', views.CanalListView.as_view(), name='listar-canal'),
    # re_path(r'^cadastrar/canal/$', views.CanalCreateView.as_view(), name='cadastrar-canal'),
    # re_path(r'^alterar/canal/(?P<pk>\w+|)/$', views.CanalUpdateView.as_view(), name='alterar-canal'),
    # re_path(r'^excluir/canal/(?P<pk>\w+|)$', views.CanalDeleteView.as_view(), name='excluir-canal'),
    # re_path(r'^listar/conteudo/$', views.ConteudoListView.as_view(), name='listar-conteudo'),
    # re_path(r'^cadastrar/conteudo/$', views.ConteudoCreateView.as_view(), name='cadastrar-conteudo'),
    # re_path(r'^alterar/conteudo/(?P<pk>\w+|)/$', views.ConteudoUpdateView.as_view(), name='alterar-conteudo'),
    # re_path(r'^excluir/conteudo/(?P<pk>\w+|)$', views.ConteudoDeleteView.as_view(), name='excluir-conteudo'),
    # re_path(r'^listar/conteudo/imagem/(?P<idconteudo>\w+|)/$', views.ConteudoImagemListView.as_view(), name='listar-conteudo-imagem'),
    # re_path(r'^cadastrar/conteudo/imagem/(?P<idconteudo>\w+|)/$', views.ConteudoImagemCreateUpdateView.as_view(), name='cadastrar-conteudo-imagem'),
    # re_path(r'^alterar/conteudo/imagem/(?P<pk>\w+|)$', views.ConteudoImagemUpdateView.as_view(), name='alterar-conteudo-imagem'),
    # re_path(r'^excluir/conteudo/imagem/(?P<pk>\w+|)$', views.ConteudoImagemDeleteView.as_view(), name='excluir-conteudo-imagem'),

]