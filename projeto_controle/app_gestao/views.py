from django.shortcuts import render, redirect
from django.http import HttpRequest
from .models import Gestao

# Create your views here.
def listar_colaboradores(request: HttpRequest):
    pesquisa = request.GET.get('nome', '')
    if pesquisa:
        colaboradores = Gestao.objects.filter(nome__icontains=pesquisa)
    else:
        colaboradores = Gestao.objects.all()
    return render(request, 'app_gestao/pages/listar_colaboradores.html', {"colaboradores": colaboradores, "pesquisa": pesquisa})

def remover_colaborador(request: HttpRequest, id:int):
    colaborador = Gestao.objects.get(id=id)
    colaborador.delete()
    return redirect('colaboradores:listar_colaboradores')

def cadastrar_colaborador(request: HttpRequest):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        ativo = request.POST.get('ativo', True)
        eh_terceiro = request.POST.get('eh_terceiro')
        cargo = request.POST.get('cargo')
        obj = Gestao(nome=nome, cpf=cpf, ativo=ativo, eh_terceiro=eh_terceiro, cargo=cargo)
        obj.save()
        return redirect('colaboradores:listar_colaboradores')
    return render(request, 'app_gestao/pages/cadastrar_colaborador.html')

def editar_colaborador(request: HttpRequest, id:int):
    colaborador = Gestao.objects.get(id=id)
    if request.method == 'POST':
        colaborador.nome = request.POST.get('nome')
        colaborador.cpf = request.POST.get('cpf')
        colaborador.ativo = request.POST.get('ativo')
        colaborador.eh_terceiro = request.POST.get('eh_terceiro')
        colaborador.cargo = request.POST.get('cargo')
        colaborador.save()
        return redirect('colaboradores:listar_colaboradores')
    return render(request, 'app_gestao/pages/editar_colaborador.html', {"colaborador": colaborador})
    