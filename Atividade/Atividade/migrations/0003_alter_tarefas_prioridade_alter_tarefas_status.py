# Generated by Django 5.1.2 on 2024-11-22 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Atividade', '0002_alter_tarefas_descricao_alter_tarefas_prioridade_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarefas',
            name='prioridade',
            field=models.CharField(choices=[('alta', 'Alta'), ('media', 'Média'), ('baixa', 'Baixa')], default='media', max_length=6),
        ),
        migrations.AlterField(
            model_name='tarefas',
            name='status',
            field=models.CharField(choices=[('pendente', 'Pendente'), ('em_progresso', 'Em Progresso'), ('concluida', 'Concluída')], default='pendente', max_length=15),
        ),
    ]
