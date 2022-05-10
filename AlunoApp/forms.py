from datetime import datetime

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Field, Submit, Row, HTML
from crispy_forms.templatetags.crispy_forms_field import css_class
from django import forms
from django.db.models import Q
from django.forms.widgets import Select, CheckboxSelectMultiple, SelectMultiple, RadioSelect, ClearableFileInput
from django_summernote.widgets import SummernoteWidget
# from usuario.models import Usuario

from .models import Aluno, Materia, Turma, AlunoTurma

    
class AlunoForm(forms.ModelForm):

    class Meta:
        model = Aluno
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        self.espaco_id = kwargs.pop('espaco_id', None)
        super(AlunoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'GET'
        self.helper.layout = Layout(
            Row(
                Div(Field('nome'), css_class="col-md-8"),
                Div(Field('data_nasc'), css_class="col-md-4"),
            )
            Div(Field('email', css_class="email"), css_class="col-md-12 email"),
                Row(
                    Div(Field('cpf', css_class="cpf"), css_class="col-md-6"),
                    Div(Field('telefone_um', css_class="sp_celphones"), css_class="col-md-3"),
                    Div(Field('telefone_dois', css_class="sp_celphones"), css_class="col-md-3"),
                    
                ),
                Fieldset(
                   "Dados Residenciais", 

                    Row(
                        
                        Div(Field('logradouro'), css_class="col-md-6"), 
                        Div(Field('numero'), css_class="col-md-1"), 
                        Div(Field('complemento'), css_class="col-md-5"), 
                        Div(css_class="col-md-12", style="height:25px;"),
                        Div(Field('cidade'), css_class="col-md-4"), 
                        
                    ),
                ),
                Div(Field('ativo'), css_class="col-md-12"),
        )



class DevolutivaForm(forms.ModelForm):
    
    class Meta:
        model = Devolutiva
        fields = '__all__'


class SolicitacaoForm(forms.ModelForm):

    class Meta:
        model = Solicitacao
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        self.usuario = kwargs.pop('usuario', None)
        super(SolicitacaoForm, self).__init__(*args, **kwargs)
        solicitante =  Usuario.objects.filter(pk=self.usuario.pk)
        self.fields['solicitante'].queryset = solicitante
        # self.fields['solicitante'].initial = solicitante[0]
        self.fields['solicitante'].widget = forms.HiddenInput()
        self.fields['tematica'].queryset = Tematica.objects.all()
        self.fields['modalidade'].queryset = Modalidade.objects.none()
        self.fields['rascunho'].widget = forms.HiddenInput()
        self.fields['fluxo_solicitacao'].widget = forms.HiddenInput()

class SolicitacaoEspacoForm(forms.ModelForm):
    
    class Meta:
        model = SolicitacaoEspaco
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(SolicitacaoEspacoForm, self).__init__(*args, **kwargs)

        self.fields['solicitacao'].queryset = Solicitacao.objects.none()

        if 'solicitacao' in self.data:
            try:
                solicitacao = int(self.data.get('solicitacao'))
                self.fields['solicitacao'].queryset = Solicitacao.objects.filter(pk=solicitacao)
                
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['solicitacao'].queryset = self.instance.solicitacao



class LocalForm(forms.ModelForm):
    
    class Meta:
        model = Local
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(LocalForm, self).__init__(*args, **kwargs)

