from pyexpat.errors import messages

from django.shortcuts import render
from Atividade.forms import UsuarioForm, TarefaForm
from Atividade.models import usuarios, tarefas
from django.shortcuts import get_object_or_404, redirect



def home(request):
    return render(request, 'home.html')

def cadastrar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_usuarios')  # Corrigido o redirecionamento
    else:
        form = UsuarioForm()
    return render(request, 'cadastrar_usuario.html', {'form': form})  # Verifique se o caminho está correto

def lista_tarefas(request):
    tarefas_list = tarefas.objects.all()
    return render(request, 'lista_tarefas.html', {'tarefas': lista_tarefas})


def atualizar_usuario(request, pk):
    usuario = get_object_or_404(usuarios, pk=pk)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('lista_usuarios')
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, 'atualiza_usuario.html', {'form': form})


def deletar_usuario(request, pk):
    usuario = get_object_or_404(usuarios, pk=pk)
    if request.method == 'POST':
        usuario.delete()
        return redirect('lista_usuarios')
    return render(request, 'deletar_usuario.html', {'usuario': usuario})

def cadastrar_tarefa(request):
    if request.method == 'POST':
        descricao = request.POST['descricao']
        setor = request.POST['setor']
        prioridade = request.POST['prioridade']
        status = request.POST['status']
        data = request.POST['data']
        usu_codigo = request.POST['usu_codigo']
        usuario = usuarios.objects.get(id=usu_codigo)
        tarefas.objects.create(
            descricao=descricao,
            setor=setor,
            prioridade=prioridade,
            status=status,
            data=data,
            usu_codigo=usuario
        )
        messages.success(request, 'Tarefa cadastrada com sucesso!')
        return redirect('lista_tarefas')
    usuario = usuarios.objects.all()
    return render(request, 'cadastrar_tarefa', {'usuario': usuario})

def lista_usuarios(request):
    try:
        usuario = usuarios.objects.all()
    except Exception as e:
        return render(request, 'usuarios.html', {'erro': e})  # Corrigido o caminho
    return render(request, 'usuarios.html', {'lista_usuarios': usuario})  # Corrigido o caminho