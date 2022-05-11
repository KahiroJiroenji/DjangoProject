import datetime

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
