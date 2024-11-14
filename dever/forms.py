from django import forms
from .models import DeverDeCasa, Materia
from django import forms
from.models import Escola, Turma, Materia, Professor, Livro, Alunos
from django.contrib.auth.models import User

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
                # self.fields['fk_materia'].queryset = Materia.objects.filter(materias_professor=professor_id)
                self.fields['fk_materia'].queryset = Materia.objects.filter(professor_materias=professor_id)

            except (ValueError, TypeError):
                pass  # Se fk_professor não for válido, ignora o filtro
        else:
            self.fields['fk_materia'].queryset = Materia.objects.none()



class EscolaForm(forms.ModelForm):
    class Meta:
        model = Escola
        fields = ('nome_escola',)
        widgets = {
            'nome_escola': forms.TextInput(attrs={
                'class': 'form-control mb-3',  # Adiciona classes CSS para estilização
                'placeholder': 'Digite o nome da escola aqui',  # Define um placeholder
                'eadonly': False,  # Campo pode ser editado (se quiser somente leitura, trocar por True)
                'data-toggle': 'tooltip',  # Adiciona um atributo de dados para tooltip
                'title': 'Nome da instituição de ensino',  # Define a dica do tooltip
                'size': '50',  # Define o tamanho visível do campo
                'onblur': 'this.value=this.value.toUpperCase()',  # Converte para maiúsculas ao sair do campo
                'equired': 'equired',  # Campo é obrigatório (pode ser removido se não for necessário)
                'pattern': '[A-Za-záéíóúÁÉÍÓÚ\s]+',  # Define um padrão de entrada (letras e espaços)
                'tyle': 'border-radius: 5px; box-shadow: 0 0 5px #ccc;'  # Adiciona estilos CSS inline
            })
        }

class TurmaForm(forms.ModelForm):
    class Meta:
        model = Turma
        fields = ('fk_escola', 'turma')

class MateriaForm(forms.ModelForm):
    class Meta:
        model = Materia
        fields = ('nome_materia',)

class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ('fk_escola', 'fk_materia', 'nome_professor')

class LivrosForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ('fk_materia', 'nome_livro')

class AlunosForm(forms.ModelForm):
    class Meta:
        model = Alunos
        fields = ('fk_user', 'fk_escola', 'fk_turma', 'nome_aluno')
