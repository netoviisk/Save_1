# Generated by Django 5.1.2 on 2024-11-22 05:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Atividade', '0006_alter_usuarios_codigo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarefas',
            name='usu_codigo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Atividade.usuarios'),
        ),
    ]
