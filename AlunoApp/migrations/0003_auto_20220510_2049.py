# Generated by Django 2.2.22 on 2022-05-10 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AlunoApp', '0002_auto_20220510_2014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='numero',
            field=models.IntegerField(blank=True, max_length=8, null=True, verbose_name='Nº'),
        ),
        migrations.AlterField(
            model_name='historicalaluno',
            name='numero',
            field=models.IntegerField(blank=True, max_length=8, null=True, verbose_name='Nº'),
        ),
    ]
