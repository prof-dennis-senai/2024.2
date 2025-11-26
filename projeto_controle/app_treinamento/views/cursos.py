from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.db.models import Q

from app_gestao.models import Gestao
from app_treinamento.models import Treinamento, TreinamentoColaborador

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
