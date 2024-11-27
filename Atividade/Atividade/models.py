from django.db import models

class usuarios(models.Model):
    codigo = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome

class tarefas(models.Model):
    t_codigo = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=255)
    setor = models.CharField(max_length=100)
    PRIORIDADE_CHOICES = [
        ('alta', 'Alta'),
        ('media', 'Média'),
        ('baixa', 'Baixa'),
    ]
    prioridade = models.CharField(
        max_length=6, choices=PRIORIDADE_CHOICES, default='media'
    )
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('em_progresso', 'Em Progresso'),
        ('concluida', 'Concluída'),
    ]
    status = models.CharField(
        max_length=15, choices=STATUS_CHOICES, default='pendente'
    )
    data = models.DateField()
    usu_codigo = models.ForeignKey(usuarios, on_delete=models.CASCADE)

    def __str__(self):
        return self.descricao