from datetime import datetime

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Field, Submit, Row, HTML, Fieldset, ButtonHolder
from crispy_forms.templatetags.crispy_forms_field import css_class
from django import forms
from django.db.models import Q
from django.forms.widgets import Select, CheckboxSelectMultiple, SelectMultiple, RadioSelect, ClearableFileInput
from django_summernote.widgets import SummernoteWidget
# from usuario.models import Usuario

from .models import Aluno, Turma, AlunoTurma

    
class AlunoForm(forms.ModelForm):

    class Meta:
        model = Aluno
        fields = '__all__'
        exclude = ['data_alteracao',]

    def __init__(self, *args, **kwargs):
        super(AlunoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'GET'
        self.helper.layout = Layout(
            Row(
                Div(Field('nome'), css_class="col-md-8"),
                Div(Field('email'), css_class="col-md-4"),
            ),
            Row(
                Div(Field('cpf'), css_class="col-md-6"),
                Div(Field('telefone_um'), css_class="col-md-3"),
                Div(Field('telefone_dois'), css_class="col-md-3"),     
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
            Row(
                    Div(
                    Field(Submit('submit', 'Salvar', css_class='btn btn-primary botao pull-right has-value', data_acao_btn="salvar")), css_class="col-md-12"
                    )
                )
        )


class TurmaForm(forms.ModelForm):
    
    class Meta:
        model = Turma
        fields = '__all__'
        exclude = ['data_alteracao',]

    def __init__(self, *args, **kwargs):
        super(TurmaForm, self).__init__(*args, **kwargs)



class AlunoTurmaForm(forms.ModelForm):
    
    class Meta:
        model = AlunoTurma
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(AlunoTurmaForm, self).__init__(*args, **kwargs)
