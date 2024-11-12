from django import forms
from .models import DeverDeCasa, Materia

class DeverDeCasaForm(forms.ModelForm):
    class Meta:
        model = DeverDeCasa
        fields = ['fk_escola', 'fk_materia', 'fk_livro', 'fk_professor', 'dever', 'data_entrega']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filtra as matérias se um professor foi selecionado
        if 'fk_professor' in self.data:
            try:
                professor_id = int(self.data.get('fk_professor'))
                self.fields['fk_materia'].queryset = Materia.objects.filter(materias_professor=professor_id)
            except (ValueError, TypeError):
                pass  # Se fk_professor não for válido, ignora o filtro
        else:
            self.fields['fk_materia'].queryset = Materia.objects.none()

