from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.db.models import Q

from app_gestao.models import Gestao
from .models import Treinamento, TreinamentoColaborador

from utils.send_email_utils.bem_vindo.bem_vindo import enviar_email_bem_vindo_basico,enviar_email_bem_vindo_avancado

# Create your views here.
def listar_treinamentos(request: HttpRequest):
    enviar_email_bem_vindo_avancado('caldana.gabriel@hotmail.com', 'Dennis')
    pesquisa = request.GET.get('titulo', '')
    if pesquisa:
        treinamentos = Treinamento.objects.filter(nome__icontains=pesquisa)
    else:
        treinamentos = Treinamento.objects.all()
    return render(request, 'app_treinamento/pages/listar_treinamentos.html', {"treinamentos": treinamentos, "pesquisa": pesquisa})

def remover_treinamento(request: HttpRequest, id:int):
    treinamento = Treinamento.objects.get(id=id)
    treinamento.delete()
    return redirect('treinamentos:listar_treinamentos')

def cadastrar_treinamento(request: HttpRequest):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        validade_em_meses = request.POST.get('validade')
        quantidade_horas = request.POST.get('quantidade_horas')
        obj = Treinamento(titulo=titulo, descricao=descricao, validade_em_meses=validade_em_meses, quantidade_horas=quantidade_horas)
        obj.save()
        return redirect('treinamentos:listar_treinamentos')
    return render(request, 'app_treinamento/pages/cadastrar_treinamento.html')

def editar_treinamento(request: HttpRequest, id:int):
    treinamento = Treinamento.objects.get(id=id)
    if request.method == 'POST':
        treinamento.titulo = request.POST.get('titulo')
        treinamento.descricao = request.POST.get('descricao')
        treinamento.validade_em_meses = request.POST.get('validade')
        treinamento.quantidade_horas = request.POST.get('quantidade_horas')
        treinamento.save()
        return redirect('treinamentos:listar_treinamentos')
    return render(request, 'app_treinamento/pages/editar_treinamento.html', {"treinamento": treinamento})
    

def listar_cursos(request: HttpRequest):
    nome_colaborador = request.GET.get('nome', '')
    titulo_curso = request.GET.get('titulo', '')
    if nome_colaborador or titulo_curso:
        cursos = TreinamentoColaborador.objects.filter(Q(colaborador__nome__icontains=nome_colaborador) or Q(treinamento__titulo__icontains=titulo_curso)).select_related('colaborador', 'treinamento')
    else:
        cursos = TreinamentoColaborador.objects.all()
    return render(request, 'app_treinamento/pages/listar_cursos.html', {"treinamentos": cursos})

def cadastrar_cursos(request: HttpRequest):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        validade_em_meses = request.POST.get('validade')
        quantidade_horas = request.POST.get('quantidade_horas')
        obj = Treinamento(titulo=titulo, descricao=descricao, validade_em_meses=validade_em_meses, quantidade_horas=quantidade_horas)
        obj.save()
        return redirect('treinamentos:listar_treinamentos')
    
    cursos = Treinamento.objects.all()
    colaboradores = Gestao.objects.all()
    return render(request, 'app_treinamento/pages/cadastrar_curso.html', {"cursos": cursos, "colaboradores": colaboradores}) 
