from django.urls import path
from . import views

app_name = 'colaboradores'

urlpatterns = [
    path('', views.listar_colaboradores, name='listar'),
]
