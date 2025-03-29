from django.shortcuts import render, get_object_or_404, redirect
from .models import Usuarios, Tarefas

def home(request):
    return render(request, 'home.html')

def listar_tarefas(request):
    tarefas = Tarefas.objects.all()
    return render(request, 'tarefas/listar_tarefas.html', {'tarefas': tarefas})

def listar_usuarios(request):
    usuarios = Usuarios.objects.all()
    return render(request, 'usuarios/listar_usuarios.html', {'usuarios': usuarios})

def cadastro_usuarios(request):
    if request.method == "POST":
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        usuario = Usuarios(usu_nome=nome, usu_email=email)
        usuario.save()
        return redirect('listar_usuarios')
    return render(request, 'usuarios/cadastro_usuario.html')

def cadastro_tarefas(request):
    if request.method == "POST":
        descricao = request.POST.get('descricao')
        setor = request.POST.get('setor')
        prioridade = request.POST.get('prioridade')
        status = request.POST.get('status')
        data = request.POST.get('data')
        usuario_id = request.POST.get('usuario')

        usuario = Usuarios.objects.get(usu_codigo=usuario_id)

        tarefa = Tarefas(
            tar_descricao=descricao,
            tar_setor=setor,
            tar_prioridade=prioridade,
            tar_status=status,
            tar_data=data,
            usu_codigo=usuario
        )
        tarefa.save()
        return redirect('listar_tarefas')
    usuarios = Usuarios.objects.all()
    return render(request, 'tarefas/cadastro_tarefa.html', {'usuarios': usuarios})


def edita_tarefas(request, tarefa_id):
    tarefa = get_object_or_404(Tarefas, tar_codigo=tarefa_id)

    if request.method == "POST":
        tarefa.tar_descricao = request.POST.get('descricao')
        tarefa.tar_setor = request.POST.get('setor')
        tarefa.tar_prioridade = request.POST.get('prioridade')
        tarefa.tar_status = request.POST.get('status')
        tarefa.tar_data = request.POST.get('data')
        tarefa.save()
        return redirect('listar_tarefas')

    return render(request, 'tarefas/botao/edita_tarefas.html', {'tarefa': tarefa})


def exclui_tarefas(request, tarefa_id):
    tarefa = get_object_or_404(Tarefas, tar_codigo=tarefa_id)
    tarefa.delete()
    return redirect('listar_tarefas')


def edita_usuarios(request, usu_codigo):
    usuario = get_object_or_404(Usuarios, usu_codigo=usu_codigo)

    if request.method == "POST":
        usuario.usu_nome = request.POST.get('nome')
        usuario.usu_email = request.POST.get('email')
        usuario.save()
        return redirect('listar_usuarios')

    return render(request, 'usuarios/botao/edita_usuarios.html', {'usuario': usuario})

def exclui_usuarios(request, usuario_id):
    usuario = get_object_or_404(Usuarios, usu_codigo=usuario_id)
    usuario.delete()
    return redirect('listar_usuarios')