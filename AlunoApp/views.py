from io import BytesIO
from django.conf import settings
from django.core.paginator import Paginator
from django.core.files.storage import FileSystemStorage
from django.db import connections
from django.db.models import CharField, Value as V
from django.db.models.functions import Concat
from django.db.models.query_utils import Q
from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.utils.dateparse import parse_date
from django.views.generic import ListView, CreateView
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView
from django.urls import reverse_lazy
import datetime
 
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

class AjaxTemplateView(TemplateView):
    template_name = 'AlunoApp/ajax.html'

    def post(self, request, **kwargs):
        result = [{'foo': 1, 'bar': 2}]         
        return render(request, self.template_name, {'json': json.dumps(kwargs)})


class IndexTemplateView(TemplateView):
    template_name = 'AlunoApp/index.html'
    
    def get(self, request):
        
        
        return render(request, self.template_name, {'base': 'inicio'})

class AlunoListView(ListView):
    template_name = 'AlunoApp/listar-aluno.html'
    model = Aluno

    def get(self, request, **kwargs):
        aluno_lst = Aluno.objects.all().order_by('id')  
        
        return render(request, self.template_name, {'aluno_lst': aluno_lst})

class AlunoCreateView(CreateView):
    template_name = 'AlunoApp/cadastrar-aluno.html'

    def get(self, request):
        form = forms.AlunoForm
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = forms.AlunoForm(request.POST)
        if form.is_valid():
            formAluno = form.save(commit=False)
            # formAluno.criado_por = request.user            
            formAluno.save()
            form.save_m2m()
            
            success_url = reverse_lazy('AlunoApp:listar-aluno')
            return JsonResponse({'success': formAluno.id})
        else:
            return JsonResponse({'error': form.errors})

    def get_success_url(self):
        return reverse('AlunoApp:listar-aluno')

class AlunoUpdateView(UpdateView):
    model = Aluno
    form_class = forms.AlunoForm
    template_name = 'AlunoApp/alterar-aluno.html'
    context_object_name = 'aluno'

    def get(self, request, **kwargs):
        obj = get_object_or_404(Aluno, pk=kwargs.get('pk'))
        form = forms.AlunoForm(request.POST or None, instance = obj)
        this_aluno = Aluno.objects.get(pk=kwargs.get('pk'))
        return render(request, self.template_name, {'form': form, 'this_aluno': this_aluno})

    def get_success_url(self):
        return reverse('AlunoApp:ajax', kwargs={'json': 1})

    def post(self, request, *args, **kwargs):
        instance = get_object_or_404(Aluno, pk=kwargs.get('pk'))
        form = self.form_class(request.POST, instance = instance)
        if form.is_valid():
            formAluno = form.save(commit=False)
            formAluno.data_alteracao = datetime.datetime.now()  
            formAluno.save()
            return JsonResponse({'success': formAluno.pk})
        
    def get_context_data(self, **kwargs):
        context = super(AlunoUpdateView, self).get_context_data()
        return context

        
class AlunoDeleteView(DeleteView):
    model = Aluno
    success_url = reverse_lazy('AlunoApp:listar-aluno')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

class TurmaListView(ListView):
    template_name = 'AlunoApp/listar-turma.html'
    model = Turma

    def get(self, request, **kwargs):
        turma_lst = Turma.objects.all().order_by('id')  
        
        return render(request, self.template_name, {'turma_lst': turma_lst})

class TurmaCreateView(CreateView):
    template_name = 'AlunoApp/cadastrar-turma.html'

    def get(self, request):
        form = forms.TurmaForm
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = forms.TurmaForm(request.POST)
        if form.is_valid():
            formTurma = form.save(commit=False)       
            formTurma.save()
            form.save_m2m()
            
            success_url = reverse_lazy('AlunoApp:listar-turma')
            return JsonResponse({'success': formTurma.id})
        else:
            return JsonResponse({'error': form.errors})

    def get_success_url(self):
        return reverse('AlunoApp:listar-aluno')

class TurmaUpdateView(UpdateView):
    model = Turma
    form_class = forms.TurmaForm
    template_name = 'AlunoApp/alterar-turma.html'
    context_object_name = 'aluno'

    def get(self, request, **kwargs):
        obj = get_object_or_404(Turma, pk=kwargs.get('pk'))
        form = forms.TurmaForm(request.POST or None, instance = obj)
        this_turma = Turma.objects.get(pk=kwargs.get('pk'))
        return render(request, self.template_name, {'form': form, 'this_turma': this_turma})

    def get_success_url(self):
        return reverse('AlunoApp:ajax', kwargs={'json': 1})

    def post(self, request, *args, **kwargs):
        instance = get_object_or_404(Turma, pk=kwargs.get('pk'))
        form = self.form_class(request.POST, instance = instance)
        if form.is_valid():
            formTurma = form.save(commit=False)
            formTurma.data_alteracao = datetime.datetime.now()  
            formTurma.save()
            return JsonResponse({'success': formTurma.pk})
        
    def get_context_data(self, **kwargs):
        context = super(TurmaUpdateView, self).get_context_data()
        return context


class TurmaDeleteView(DeleteView):
    model = Turma
    success_url = reverse_lazy('AlunoApp:listar-turma')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class AlunoTurmaListView(ListView):
    template_name = 'AlunoApp/listar-aluno-turma.html'
    model = AlunoTurma

    def get(self, request, **kwargs):
        alunoturma_lst = AlunoTurma.objects.all().order_by('id')  
        
        return render(request, self.template_name, {'alunoturma_lst': alunoturma_lst})

class AlunoTurmaCreateView(CreateView):
    template_name = 'AlunoApp/cadastrar-aluno-turma.html'

    def get(self, request):
        form = forms.AlunoTurmaForm
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = forms.AlunoTurmaForm(request.POST)
        if form.is_valid():
            formAlunoTurma = form.save(commit=False)       
            formAlunoTurma.save()
            form.save_m2m()
            
            return JsonResponse({'success': formAlunoTurma.id})
        else:
            return JsonResponse({'error': form.errors})

    def get_success_url(self):
        return reverse('AlunoApp:listar-aluno')

class AlunoTurmaDeleteView(DeleteView):
    model = AlunoTurma
    success_url = reverse_lazy('AlunoApp:listar-aluno-turma')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
