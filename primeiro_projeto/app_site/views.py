from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'app_site/pages/index.html', {"nome_teste": "Guilherme"})

def sobre(request):
    return render(request, 'app_site/pages/sobre.html', {"nome_teste": "Joao"})