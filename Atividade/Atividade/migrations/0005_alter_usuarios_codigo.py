# Generated by Django 5.1.2 on 2024-11-22 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Atividade', '0004_alter_usuarios_codigo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='codigo',
            field=models.BigAutoField(default=None, primary_key=True, serialize=False),
        ),
    ]
