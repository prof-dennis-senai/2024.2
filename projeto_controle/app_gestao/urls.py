from django.urls import path
from . import views

app_name = 'colaboradores'

urlpatterns = [
    path('', views.listar_colaboradores, name='listar_colaboradores'),
    path('cadastrar/', views.cadastrar_colaborador, name='cadastrar_colaborador'),
    path('editar/<int:id>', views.editar_colaborador, name='editar_colaborador'),
    path('remover/<int:id>', views.remover_colaborador, name='remover_colaborador'),
]
