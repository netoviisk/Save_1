# Generated by Django 5.1.2 on 2024-11-22 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Atividade', '0003_alter_tarefas_prioridade_alter_tarefas_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='codigo',
            field=models.AutoField(default=None, primary_key=True, serialize=False),
        ),
    ]
