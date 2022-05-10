from io import BytesIO
from django.conf import settings
from django.core.paginator import Paginator
from django.core.files.storage import FileSystemStorage
from django.db import connections
from django.db.models import CharField, Value as V
from django.db.models.functions import Concat
from django.db.models.query_utils import Q
from django.shortcuts import render
from django.utils.dateparse import parse_date
from django.views.generic import ListView, CreateView
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView
# from usuario.forms import UsuarioForm
# from usuario.models import Perfil, Sistema, Usuario, PerfilUsuario
# from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from . import forms
from .models import Aluno, Turma, AlunoTurma
from django.urls.base import reverse
from django.http.response import JsonResponse, HttpResponse
import json
from django.template.loader import render_to_string

# Create your views here.

class IndexTemplateView(TemplateView):
    template_name = 'AlunoApp/index.html'
    
    def get(self, request):
        
        
        return render(request, self.template_name, {'var': 'inicio'})

class AlunoListView(ListView):
    template_name = 'AlunoApp/listar-aluno.html'
    model = Aluno

    def get(self, request, **kwargs):
        aluno_lst = Aluno.objects.all().order_by('id')  
        
        return render(request, self.template_name, {'aluno_lst': aluno_lst})
        #     if request.GET.get('tipo_retorno'):
        #     return JsonResponse(list(aluno_lst.values()), safe=False)
        # else: