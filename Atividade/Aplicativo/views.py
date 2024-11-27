from pyexpat.errors import messages

from django.shortcuts import render
from Atividade.forms import UsuarioForm, TarefaForm
from Atividade.models import usuarios, tarefas
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse



def home(request):
    return render(request, 'home.html')

def cadastrar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_usuarios')
    else:
        form = UsuarioForm()
    return render(request, 'cadastrar_usuario.html', {'form': form})



def lista_tarefas(request):
    tarefa = tarefas.objects.all()
    return render(request, 'lista_tarefas.html', {'tarefa': tarefa})


def atualizar_usuario(request, pk):
    usuario = get_object_or_404(usuarios, codigo=pk)
    if request.method == 'POST':
        usuario.nome = request.POST.get('nome')
        usuario.email = request.POST.get('email')
        usuario.save()
        return redirect('lista_usuarios')
    return render(request, 'atualiza_usuario.html', {'usuario': usuario})


def deletar_usuario(request, pk):
    usuario = get_object_or_404(usuarios, pk=pk)
    if request.method == 'POST':
        usuario.delete()
        return redirect('lista_usuarios')
    return render(request, 'deletar_usuario.html', {'usuario': usuario})

def cadastrar_tarefa(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Tarefa cadastrada com sucesso!")
        else:
            return render(request, 'cadastrar_tarefa.html', {'form': form})
    else:
        form = TarefaForm()
    return render(request, 'cadastrar_tarefa.html', {'form': form})


def lista_usuarios(request):
    try:
        usuario = usuarios.objects.all()
    except Exception as e:
        return render(request, 'usuarios.html', {'erro': e})  # Corrigido o caminho
    return render(request, 'usuarios.html', {'lista_usuarios': usuario})  # Corrigido o caminho