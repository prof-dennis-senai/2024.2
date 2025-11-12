from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def criar_usuario(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        User.objects.create_user(username=username, password=password, email=email)
        return redirect('accounts:login')
    return render(request, 'app_login/pages/criar_conta.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('colaboradores:listar_colaboradores')
    return render(request, 'app_login/pages/login.html')

def logout(request):
    auth.logout(request)
    return redirect('colaboradores:listar_colaboradores')