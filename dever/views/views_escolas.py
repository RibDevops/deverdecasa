from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from..forms import EscolaForm
from..models import Escola
from django.contrib.auth.models import User

# Views para Escola
def lista_escolas(request):
    escolas = Escola.objects.all()
    return render(request, 'escolas/lista.html', {'escolas': escolas})

def cria_escolas(request):
    if request.method == 'POST':
        form = EscolaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dever:lista_escolas')
    else:
        form = EscolaForm()
    return render(request, 'escolas/form.html', {'form': form})

def atualiza_escolas(request, pk):
    escola = get_object_or_404(Escola, pk=pk)
    if request.method == 'POST':
        form = EscolaForm(request.POST, instance=escola)
        if form.is_valid():
            form.save()
            return redirect('dever:lista_escolas')
    else:
        form = EscolaForm(instance=escola)
    return render(request, 'escolas/form.html', {'form': form})

# def deleta_escolas(request, pk):
#     escola = get_object_or_404(Escola, pk=pk)
#     if request.method == 'POST':
#         escola.delete()
#         messages.success(request, "Escola deletada com sucesso.")
#         return redirect('dever:lista_escolas')
#     return render(request, 'escolas/confirma_delecao.html', {'escola': escola})

from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages

def deleta_escolas(request, pk):
    escola = get_object_or_404(Escola, pk=pk)
    try:
        escola.delete()
        messages.success(request, "Escola deletada com sucesso.")
    except Exception as e:
        messages.error(request, f"Erro ao deletar escola: {str(e)}")
    return redirect('dever:lista_escolas')
