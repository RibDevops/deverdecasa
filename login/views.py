# from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth import logout
# from django.shortcuts import redirect
# # Create your views here.

# from django.contrib.auth.models import AbstractUser
# from django.db import models

# class User(AbstractUser):
#     PROFILE_CHOICES = [
#         ('COORDENADOR', 'Coordenador'),
#         ('PROFESSOR', 'Professor'),
#         ('PAI', 'Pai'),
#     ]

#     profile = models.CharField(max_length=15, choices=PROFILE_CHOICES, default='PAI')
#     email = models.EmailField(unique=True)

#     def __str__(self):
#         return self.username

# def cadastrar_usuario(request):
#     if request.method == "POST":
#         form_usuario = UserCreationForm(request.POST)
#         if form_usuario.is_valid():
#             form_usuario.save()
#             return redirect('index')
#     else:
#         form_usuario = UserCreationForm()
#     return render(request, 'cadastro.html', {'form_usuario': form_usuario})

# def logar_usuario(request):
#     if request.method == "POST":
#         username = request.POST["username"]
#         password = request.POST["password"]
#         usuario = authenticate(request, username=username, password=password)
#         if usuario is not None:
#             login(request, usuario)
#             return redirect('index')
#         else:
#             form_login = AuthenticationForm()
#     else:
#         form_login = AuthenticationForm()
#     return render(request, 'login.html', {'form_login': form_login})

# def index(request):
#     return render(request, 'index.html')

# def logout_view(request):
#     logout(request)
#     return redirect('logar_usuario')  # Redireciona para a página de login ou outra página desejada após o logout


from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from.forms import RegistroUsuarioForm, LoginForm
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

@login_required
def registro_view(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'accounts/registro.html', {'form': form})

# def login_view(request):
#     if request.method == 'POST':
#         form = LoginForm(data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect('/')
#     else:
#         form = LoginForm()
#     return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('/')

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')  # Altere para o template correto

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import redirect, render

def login_view(request):
    # Instancia o formulário de autenticação
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                
                # Crie a sessão com o ID da escola do usuário, caso o usuário tenha o campo 'escola'
                if hasattr(user, 'escola'):
                    request.session['escola_id'] = user.escola.id
                return redirect('login:home')

            else:
                messages.error(request, 'Credenciais inválidas.')
    
    # Renderiza a página de login para GET ou se a autenticação falhar
    return render(request, 'login.html', {'form_login': form})

