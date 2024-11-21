from django.db import models

class usuarios(models.Model):
    codigo = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def _str_(self):
        return self.nome

class tarefas(models.Model):
    codigo = models.AutoField(primary_key=True)
        default=0,
        null=False,
        blank=False
    )
    descricao = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )
    setor = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )
    prioridade = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )
    status = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )
    data = models.DateField()

    usu_codigo = models.ForeignKey(
        usuarios,
        on_delete=models.CASCADE
    )

