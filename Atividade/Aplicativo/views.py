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
    tarefas_list = tarefas.objects.all()  # Corrige o nome para Tarefas
    return render(request, 'lista_tarefas.html', {'tarefas': lista_tarefas})

def atualizar_usuario(request, usuario_codigo):
    usuario = get_object_or_404(usuarios, pk=usuario_codigo)  # Utilize get_object_or_404 para tratar erros
    if request.method == 'POST':
        usuario.nome = request.POST['nome']
        usuario.email = request.POST['email']
        usuario.save()
        return redirect('lista_usuarios')
    else:
        context = {'usuario': usuario}
        return render(request, 'atualizar.html', context)


def deletar_usuario(request, pk):
    usuario = get_object_or_404(usuarios, pk=pk)
    if request.method == 'POST':
        usuario.delete()
        return redirect('lista_usuarios')
    return render(request, 'deletar_usuario.html', {'usuario': usuario})

def cadastrar_tarefa(request):
    if request.method == 'POST':
        tarefa = tarefas.objects.create(
            codigo=request.POST['codigo'],
            setor=request.POST['setor'],
            usuario=usuarios.objects.get(codigo=request.POST['usuario'])
        )
        return redirect('lista_tarefas')
    else:
        form = TarefaForm()
        return render(request, 'cadastrar.html', {'form': form})

def lista_usuarios(request):
    try:
        usuario = usuarios.objects.all()
    except Exception as e:
        return render(request, 'usuarios.html', {'erro': e})  # Corrigido o caminho
    return render(request, 'usuarios.html', {'lista_usuarios': usuario})  # Corrigido o caminho