from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import DeverDeCasa

from datetime import date, timedelta
from django.shortcuts import render
from .models import DeverDeCasa

# views.py

from django.shortcuts import render
from .models import DeverDeCasa
from datetime import date

from django.views.generic import ListView

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from .models import DeverDeCasa
from .forms import DeverDeCasaForm  # Assumindo que você tenha um formulário personalizado
from datetime import date

def dever_list(request):
    deveres = DeverDeCasa.objects.all().order_by('data_entrega')
    for dever in deveres:
        dias_para_entrega = dever.dias_para_entrega()
        if dias_para_entrega == 1:
            dever.cor_fundo = "vermelho"
        elif dias_para_entrega == 2:
            dever.cor_fundo = "amarelo"
        elif dias_para_entrega == 3:
            dever.cor_fundo = "verde"
        else:
            dever.cor_fundo = "verde"
    
    return render(request, 'dever/dever_list.html', {'deveres': deveres})

def dever_detail(request, pk):
    dever = get_object_or_404(DeverDeCasa, pk=pk)
    return render(request, 'dever/dever_detail.html', {'dever': dever})

def dever_create(request):
    if request.method == 'POST':
        form = DeverDeCasaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dever_list')
    else:
        form = DeverDeCasaForm()
    
    return render(request, 'dever/dever_form.html', {'form': form})

def dever_update(request, pk):
    dever = get_object_or_404(DeverDeCasa, pk=pk)
    if request.method == 'POST':
        form = DeverDeCasaForm(request.POST, instance=dever)
        if form.is_valid():
            form.save()
            return redirect('dever_list')
    else:
        form = DeverDeCasaForm(instance=dever)
    
    return render(request, 'dever/dever_form.html', {'form': form})

def dever_delete(request, pk):
    dever = get_object_or_404(DeverDeCasa, pk=pk)
    if request.method == 'POST':
        dever.delete()
        return redirect('dever_list')
    
    return render(request, 'dever/dever_confirm_delete.html', {'dever': dever})


