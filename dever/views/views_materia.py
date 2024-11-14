from django.shortcuts import render, redirect, get_object_or_404
from..forms import MateriaForm
from..models import Materia
from django.contrib.auth.models import User
from django.contrib import messages
# Views para Materia

def lista_materia(request):
    materia = Materia.objects.all()
    return render(request, 'materia/lista.html', {'materias': materia})

def cria_materia(request):
    if request.method == 'POST':
        form = MateriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dever:lista_materia')
    else:
        form = MateriaForm()
    return render(request, 'materia/form.html', {'form': form})

def atualiza_materia(request, pk):
    materia = get_object_or_404(Materia, pk=pk)
    if request.method == 'POST':
        form = MateriaForm(request.POST, instance=materia)
        if form.is_valid():
            form.save()
            return redirect('dever:lista_materia')
    else:
        form = MateriaForm(instance=materia)
    return render(request, 'materia/form.html', {'form': form})



def deleta_materia(request, pk):
    materia = get_object_or_404(Materia, pk=pk)
    try:
        materia.delete()
        messages.success(request, "Escola deletada com sucesso.")
    except Exception as e:
        messages.error(request, f"Erro ao deletar escola: {str(e)}")
    return redirect('dever:lista_materia')