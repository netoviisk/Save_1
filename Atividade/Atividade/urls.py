from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path, include
from Aplicativo import views

urlpatterns = [
    path('', views.home, name='home'),

    path('usuarios/cadastrar/', views.cadastrar_usuario, name='cadastrar_usuario'),

    path('usuarios/', views.lista_usuarios, name='lista_usuarios'),
    path('tarefas/', views.lista_tarefas, name='lista_tarefas'),

    path('usuarios/excluir/<int:pk>/', views.deletar_usuario, name='deletar_usuario'),

    path('usuarios/atualizar/<int:pk>/', views.atualizar_usuario, name='atualizar_usuario'),

    path('tarefas/cadastrar/', views.cadastrar_tarefa, name='cadastrar_tarefa'),
]