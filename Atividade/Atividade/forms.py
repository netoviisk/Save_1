from django import forms
from Atividade.models import usuarios, tarefas
from django.contrib.auth.models import User

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = usuarios
        fields = ('nome', 'email')


class TarefaForm(forms.ModelForm):
    usu_codigo = forms.ModelChoiceField(
        queryset=usuarios.objects.all(),
        empty_label="Selecione o Usuário",
        to_field_name='codigo'
    )
    class Meta:
        model = tarefas
        fields = ('descricao', 'setor', 'prioridade', 'status', 'data', 'usu_codigo')
        widgets = {
            'descricao': forms.TextInput(attrs={'class': 'form-control'}),
            'setor': forms.TextInput(attrs={'class': 'form-control'}),
            'prioridade': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'data': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['usu_codigo'].queryset = usuarios.objects.all()
