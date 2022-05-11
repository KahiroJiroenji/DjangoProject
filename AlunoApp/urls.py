from django.urls.conf import path, re_path

from . import views


app_name = 'AlunoApp'

urlpatterns = [
    path('', views.IndexTemplateView.as_view(), name='index'),
    re_path(r'^ajax/(?P<json>\w+|)/$', views.AjaxTemplateView.as_view(), name='ajax'),

    re_path(r'^listar/aluno/$', views.AlunoListView.as_view(), name='listar-aluno'),
    re_path(r'^cadastrar/aluno/$', views.AlunoCreateView.as_view(), name='cadastrar-aluno'),
    re_path(r'^alterar/aluno/(?P<pk>\w+|)/$', views.AlunoUpdateView.as_view(), name='alterar-aluno'),
    re_path(r'^excluir/aluno/(?P<pk>\w+|)$', views.AlunoDeleteView.as_view(), name='excluir-aluno'),

    re_path(r'^listar/turma/$', views.TurmaListView.as_view(), name='listar-turma'),
    re_path(r'^cadastrar/turma/$', views.TurmaCreateView.as_view(), name='cadastrar-turma'),
    re_path(r'^alterar/turma/(?P<pk>\w+|)/$', views.TurmaUpdateView.as_view(), name='alterar-turma'),
    re_path(r'^excluir/turma/(?P<pk>\w+|)/$', views.TurmaDeleteView.as_view(), name='excluir-turma'),

    re_path(r'^listar/aluno/turma/$', views.AlunoTurmaListView.as_view(), name='listar-aluno-turma'),
    re_path(r'^cadastrar/aluno/turma/$', views.AlunoTurmaCreateView.as_view(), name='cadastrar-aluno-turma'),
    re_path(r'^excluir/aluno/turma/(?P<pk>\w+|)$', views.AlunoTurmaDeleteView.as_view(), name='excluir-aluno-turma'),

]