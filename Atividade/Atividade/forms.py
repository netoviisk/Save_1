from django import forms
from Atividade.models import usuarios, tarefas

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = usuarios
        fields = ('nome',
                  'email')


class TarefaForm(forms.ModelForm):
    class Meta:
        model = tarefas
        fields = ('descricao',
                  'setor',
                  'prioridade',
                  'status',
                  'data')