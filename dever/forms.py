from django import forms
from .models import DeverDeCasa

class DeverDeCasaForm(forms.ModelForm):
    class Meta:
        model = DeverDeCasa
        fields = ['fk_escola', 'fk_materia', 'fk_livro', 'descricao']
