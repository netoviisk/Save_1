# Generated by Django 4.2.16 on 2024-11-21 22:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="usuarios",
            fields=[
                ("codigo", models.AutoField(primary_key=True, serialize=False)),
                ("nome", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="tarefas",
            fields=[
                ("t_codigo", models.AutoField(primary_key=True, serialize=False)),
                ("descricao", models.CharField(max_length=100)),
                ("setor", models.CharField(max_length=100)),
                ("prioridade", models.CharField(max_length=100)),
                ("status", models.CharField(max_length=100)),
                ("data", models.DateField()),
                (
                    "usu_codigo",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Atividade.usuarios",
                    ),
                ),
            ],
        ),
    ]
