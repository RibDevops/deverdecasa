from django.shortcuts import render, redirect, get_object_or_404
from..forms import ProfessorForm
from..models import Professor
from django.contrib.auth.models import User
from django.contrib import messages

# Views para Professor

def lista_professor(request):
    professor = Professor.objects.all()
    return render(request, 'professor/lista.html', {'professores': professor})

def cria_professor(request):
    if request.method == 'POST':
        form = ProfessorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dever:lista_professor')
    else:
        form = ProfessorForm()
    return render(request, 'professor/form.html', {'form': form})

def atualiza_professor(request, pk):
    professor = get_object_or_404(Professor, pk=pk)
    if request.method == 'POST':
        form = ProfessorForm(request.POST, instance=professor)
        if form.is_valid():
            form.save()
            return redirect('dever:lista_professor')
    else:
        form = ProfessorForm(instance=professor)
    return render(request, 'professor/form.html', {'form': form})

# def (request, pk):
#     professor = get_object_or_404(Professor, pk=pk)
#     if request.method == 'POST':
#         professor.delete()
#         return redirect('dever:lista_professor')
#     return render(request, 'professor/confirma_delecao.html', {'professor': professor})

def deleta_professor(request, pk):
    professor = get_object_or_404(Professor, pk=pk)
    try:
        professor.delete()
        messages.success(request, "Escola deletada com sucesso.")
    except Exception as e:
        messages.error(request, f"Erro ao deletar escola: {str(e)}")
    return redirect('dever:lista_professor')