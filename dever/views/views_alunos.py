from django.shortcuts import render, redirect, get_object_or_404
from ..forms import AlunosForm
from ..models import Alunos
from django.contrib.auth.models import User

# Views para Alunos
def lista_alunos(request):
    alunos = Alunos.objects.all()
    return render(request, 'alunos/lista.html', {'alunos': alunos})

def cria_alunos(request):
    if request.method == 'POST':
        form = AlunosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dever:lista_alunos')
    else:
        form = AlunosForm()
    return render(request, 'alunos/form.html', {'form': form})

def atualiza_alunos(request, pk):
    alunos = get_object_or_404(Alunos, pk=pk)
    if request.method == 'POST':
        form = AlunosForm(request.POST, instance=alunos)
        if form.is_valid():
            form.save()
            return redirect('dever:lista_alunos')
    else:
        form = AlunosForm(instance=alunos)
    return render(request, 'alunos/form.html', {'form': form})

# def deleta_alunos(request, pk):
#     alunos = get_object_or_404(Alunos, pk=pk)
#     if request.method == 'POST':
#         alunos.delete()
#         return redirect('lista_alunos')
#     return render(request, 'alunos/confirma_delecao.html', {'alunos': alunos})

from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages

def deleta_alunos(request, pk):
    alunos = get_object_or_404(Alunos, pk=pk)
    try:
        alunos.delete()
        messages.success(request, "Escola deletado com sucesso.")
    except Exception as e:
        messages.error(request, f"Erro ao deletar: {str(e)}")
    return redirect('dever:lista_alunos')
