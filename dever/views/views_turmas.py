from django.shortcuts import render, redirect, get_object_or_404
from..forms import TurmaForm
from..models import Turma
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages

# Views para Turmas

@login_required
def lista_turma(request):
    turmas = Turma.objects.all()
    return render(request, 'turma/lista.html', {'turmas': turmas})

@login_required
def cria_turma(request):
    if request.method == 'POST':
        form = TurmaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dever:lista_turma')
    else:
        form = TurmaForm()
    return render(request, 'turma/form.html', {'form': form})

@login_required
def atualiza_turma(request, pk):
    turma = get_object_or_404(Turma, pk=pk)
    if request.method == 'POST':
        form = TurmaForm(request.POST, instance=turma)
        if form.is_valid():
            form.save()
            return redirect('dever:lista_turma')
    else:
        form = TurmaForm(instance=turma)
    return render(request, 'turma/form.html', {'form': form})

# def deleta_turma(request, pk):
#     turma = get_object_or_404(Turma, pk=pk)
#     if request.method == 'POST':
#         turma.delete()
#         return redirect('dever:lista_turma')
#     return render(request, 'turma/confirma_delecao.html', {'turma': turma})



@login_required
def deleta_turma(request, pk):
    turma = get_object_or_404(Turma, pk=pk)
    try:
        turma.delete()
        messages.success(request, "Escola deletada com sucesso.")
    except Exception as e:
        messages.error(request, f"Erro ao deletar escola: {str(e)}")
    return redirect('dever:lista_turma')