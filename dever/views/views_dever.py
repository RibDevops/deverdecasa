from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from ..models import DeverDeCasa

from datetime import date, timedelta
from django.shortcuts import render
from ..models import DeverDeCasa

from django.shortcuts import render
from ..models import DeverDeCasa
from datetime import date

from django.views.generic import ListView

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from ..models import DeverDeCasa
from ..forms import DeverDeCasaForm  # Assumindo que você tenha um formulário personalizado
from datetime import date

def dever_list(request):
    deveres = DeverDeCasa.objects.all().order_by('data_entrega')
    for dever in deveres:
        dias_para_entrega = dever.dias_para_entrega()
        horas_restantes = dever.horas_restantes()
        print(f'data_entrega - {dever.data_entrega}')
        print(f'dias_para_entrega - {dias_para_entrega}')
        print(f'horas_restantes - {horas_restantes}')
        if dias_para_entrega <= 1:
            dever.cor_fundo = "vermelho"
        # elif dias_para_entrega == 1:
        #     dever.cor_fundo = "vermelho"
        elif dias_para_entrega == 2:
            dever.cor_fundo = "amarelo"
        else:
            dever.cor_fundo = "verde"
    
    return render(request, 'dever/dever_list.html', {'deveres': deveres})

def dever_detail(request, pk):
    dever = get_object_or_404(DeverDeCasa, pk=pk)
    return render(request, 'dever/dever_detail.html', {'dever': dever})

from ..models import Escola  # Certifique-se de importar o modelo Escola

from django.shortcuts import render, redirect
from ..forms import DeverDeCasaForm
from ..models import Escola

def dever_create(request):
    if request.method == 'POST':
        form = DeverDeCasaForm(request.POST)
        print("Dados do POST:", request.POST) 
        if form.is_valid():
            print("Escola selecionada:", form.cleaned_data.get('fk_escola'))
            print("Professor selecionado:", form.cleaned_data.get('fk_professor'))
            print("Matéria selecionada:", form.cleaned_data.get('fk_materia'))
            print("Livro selecionado:", form.cleaned_data.get('fk_livro'))
            print("Descrição do dever:", form.cleaned_data.get('dever'))
            print("Data de entrega:", form.cleaned_data.get('data_entrega'))



            form.save()
            return redirect('dever_list')
        else:
            print(form.errors)  # Isso ajudará a ver os erros no console
    else:
        form = DeverDeCasaForm()

    escolas = Escola.objects.all()
    return render(request, 'dever/dever_form.html', {'form': form, 'escolas': escolas})



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


