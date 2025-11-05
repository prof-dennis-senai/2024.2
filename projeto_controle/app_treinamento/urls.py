from django.urls import path
from . import views

app_name = 'treinamentos'

urlpatterns = [
    path('', views.listar_treinamentos, name='listar_treinamentos'),
    path('cadastrar/', views.cadastrar_treinamento, name='cadastrar_treinamento'),
    path('editar/<int:id>', views.editar_treinamento, name='editar_treinamento'),
    path('remover/<int:id>', views.remover_treinamento, name='remover_treinamento'),
]
