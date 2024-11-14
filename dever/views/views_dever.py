from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from ..models import DeverDeCasa, Escola
from ..forms import DeverDeCasaForm  # Assumindo que você tenha um formulário personalizado
from datetime import date

def dever_list(request):
    deveres = DeverDeCasa.objects.all().order_by('data_entrega')
    for dever in deveres:
        dias_para_entrega = dever.dias_para_entrega()
        # horas_restantes = dever.horas_restantes()
        if dias_para_entrega <= 1:
            dever.cor_fundo = "vermelho"
        elif dias_para_entrega == 2:
            dever.cor_fundo = "amarelo"
        else:
            dever.cor_fundo = "verde"
    
    return render(request, 'dever/dever_list.html', {'deveres': deveres})

def dever_detail(request, pk):
    dever = get_object_or_404(DeverDeCasa, pk=pk)
    return render(request, 'dever/dever_detail.html', {'dever': dever})

@login_required(login_url='/login/')
def dever_create(request):
    if request.method == 'POST':
        form = DeverDeCasaForm(request.POST)
        print("Dados do POST:", request.POST) 
        if form.is_valid():
            form.save()
            return redirect('dever:dever_list')
        else:
            print(form.errors)  # Isso ajudará a ver os erros no console
    else:
        form = DeverDeCasaForm()

    escolas = Escola.objects.all()
    return render(request, 'dever/dever_form.html', {'form': form, 'escolas': escolas})

@login_required
def dever_update(request, pk):
    dever = get_object_or_404(DeverDeCasa, pk=pk)
    if request.method == 'POST':
        form = DeverDeCasaForm(request.POST, instance=dever)
        if form.is_valid():
            form.save()
            return redirect('dever:dever_list')
    else:
        form = DeverDeCasaForm(instance=dever)
    
    return render(request, 'dever/dever_form.html', {'form': form})

@login_required
def dever_delete(request, pk):
    dever = get_object_or_404(DeverDeCasa, pk=pk)
    try:
        dever.delete()
        messages.success(request, "Dever deletado com sucesso.")
    except Exception as e:
        messages.error(request, f"Erro ao deletar: {str(e)}")
    return redirect('dever:dever_list')
