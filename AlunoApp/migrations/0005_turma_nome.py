# Generated by Django 2.2.22 on 2022-05-11 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AlunoApp', '0004_auto_20220510_2233'),
    ]

    operations = [
        migrations.AddField(
            model_name='turma',
            name='nome',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
    ]
