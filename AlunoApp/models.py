from django.db import models
from django.db.models.deletion import DO_NOTHING
from simple_history.models import HistoricalRecords
from django.dispatch.dispatcher import receiver
from os.path import os
import uuid

# Create your models here.
class Aluno(models.Model):
    nome = models.CharField(max_length=250)
    cpf = models.CharField(max_length=11, verbose_name='CPF')
    telefone_um = models.CharField(max_length=15, verbose_name='Telefone')
    telefone_dois = models.CharField(max_length=15, verbose_name='Outro Telefone', blank=True, null=True)
    data_nasc = models.DateField(blank=False, null=False, verbose_name='Data de Nascimento')
    logradouro = models.CharField(max_length=250, verbose_name='Endereço', blank=False, null=False)
    numero = models.CharField(max_length=20, verbose_name='Nº', blank=True, null=True)
    complemento = models.CharField(max_length=160, verbose_name='Nº', blank=True, null=True)
    cidade = models.CharField(max_length=100, verbose_name='Nº', blank=False, null=False)
    email = models.CharField(max_length=100)
    ativo = models.BooleanField()
    historico = HistoricalRecords()
    data_alteracao = models.DateTimeField(blank=True, null=True, verbose_name='Data de alteração:')
    data_cadastro = models.DateTimeField(auto_now_add=True, verbose_name='Data de cadastro:')
    #criado_por = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING, related_name='criado_por')
    

    class Meta:
        db_table = 'alunoapp_estudantes'

    def __str__(self):
        return self.nome

class Materia(models.model):
    MATERIA_LST = (
        ('1','Português'),
        ('2','Matemática'),
        ('3','Ciências'),
        ('4','Artes'),
        ('5','Educação Física'),
    )
    NIVEL_LST(
        ('1','Estágio I'),
        ('2','Estágio II'),
        ('3','1ª Série'),
        ('4','2ª Série'),
        ('5','3ª Série'),
        ('6','4ª Série'),
        ('7','5ª Série'),
    )
    nome = models.CharField(max_length=1, null=False, blank=False, choices=MATERIA_LST)
    nivel = models.CharField(max_length=1, null=False, blank=False, choices=NIVEL_LST)  
    ativo = models.BooleanField()
    data_alteracao = models.DateTimeField(blank=True, null=True, verbose_name='Data de alteração:')
    data_cadastro = models.DateTimeField(auto_now_add=True, verbose_name='Data de cadastro:')
    #criado_por = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING, related_name='criado_por')

    class Meta:
        db_table = 'alunoapp_materia'

    def __str__(self):
        return self.nome


class Turma(models.Model):
    DIA_LST = (
        ('1','Segunda'),
        ('2','Terça'),
        ('3','Quarta'),
        ('4','Quinta'),
        ('5','Sexta'),
    )
    materia = models.ForeignKey(Materia, on_delete=models.DO_NOTHING, db_column='materia')
    dia_semana = models.CharField(max_length=1, null=False, blank=False, choices=DIA_LST)
    hora_inicio = models.TimeField(blank=True, null=True)
    hora_termino = models.TimeField(blank=True, null=True)
    data_alteracao = models.DateTimeField(blank=True, null=True, verbose_name='Data de alteração:')
    data_cadastro = models.DateTimeField(auto_now_add=True, verbose_name='Data de cadastro:')
    #criado_por = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING, related_name='criado_por')

    class Meta:
        db_table = 'alunoapp_turma'

    def __str__(self):
        return self.nome

class AlunoTurma(models.Model):

    turma = models.ForeignKey(Turma, on_delete=models.DO_NOTHING, db_column='turma')
    aluno = models.ForeignKey(Aluno, on_delete=models.DO_NOTHING, db_column='aluno')
    data_cadastro = models.DateTimeField(auto_now_add=True, verbose_name='Data de cadastro:')
    #criado_por = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING, related_name='criado_por')

    class Meta:
        db_table = 'alunoapp_aluno_turma'

