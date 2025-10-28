from django.shortcuts import render

# Create your views here.
def home(request):
    nome = request.GET.get('nome')
    return render(request, 'app_site/pages/index.html', {"nome_cliente": nome})

def sobre(request):
    return render(request, 'app_site/pages/sobre.html', {"nome_teste": "Joao"})