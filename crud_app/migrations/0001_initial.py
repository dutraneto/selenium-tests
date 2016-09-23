# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-13 23:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pertence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_pertence', models.CharField(max_length=45)),
                ('descricao', models.TextField()),
                ('data_criacao', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_pessoa', models.CharField(max_length=45)),
                ('endereco', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=15)),
            ],
        ),
        migrations.AddField(
            model_name='pertence',
            name='pessoa_fk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud_app.Pessoa'),
        ),
    ]