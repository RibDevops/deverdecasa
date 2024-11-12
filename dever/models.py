from django.db import models
from django.contrib.auth.models import AbstractUser

# dever/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

from django.db import models
from datetime import date
from datetime import datetime

from datetime import datetime, date
import locale



# class User(AbstractUser):
#     # Campos adicionais para seu modelo User personalizado

#     class Meta:
#         permissions = [
#             ("is_coordinator", "Can access all functionalities"),
#             ("is_teacher", "Can access assigned duties"),
#             ("is_parent", "Can only view duties"),
#         ]

#     # Defina related_name para evitar conflitos
#     groups = models.ManyToManyField(
#         'auth.Group',
#         related_name="custom_user_groups",
#         blank=True,
#         help_text="The groups this user belongs to.",
#         verbose_name="groups"
#     )
#     user_permissions = models.ManyToManyField(
#         'auth.Permission',
#         related_name="custom_user_permissions",
#         blank=True,
#         help_text="Specific permissions for this user.",
#         verbose_name="user permissions"
#     )


class Escola(models.Model):
    nome_escola = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_escola


class Materia(models.Model):
    nome_materia = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_materia


class Professor(models.Model):
    fk_escola = models.ForeignKey(Escola, on_delete=models.CASCADE, related_name="professores")
    fk_materia = models.ForeignKey(Materia, on_delete=models.CASCADE, related_name="materias_professor")
    nome_professor = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_professor


class Livro(models.Model):
    fk_materia = models.ForeignKey(Materia, on_delete=models.CASCADE, related_name="materias_livro")
    nome_livro = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_livro

class Aluno(models.Model):
    fk_escola = models.ForeignKey(Escola, on_delete=models.CASCADE, related_name="alunos")
    fk_professor = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name="alunos")
    nome_aluno = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_aluno

class DeverDeCasa(models.Model):
    fk_escola = models.ForeignKey(Escola, on_delete=models.CASCADE, related_name="deveres")
    fk_professor = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name="deveres")
    fk_materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    fk_livro = models.ForeignKey(Livro, on_delete=models.CASCADE, null=True, blank=True)
    dever = models.TextField()
    data_entrega = models.DateField() 
    data_postagem = models.DateTimeField(auto_now_add=True)

    # from datetime import datetime

    def horas_restantes(self):
        agora = datetime.now()
        # Converte `self.data_entrega` para um objeto `datetime` no mesmo horário de `agora`
        data_entrega_datetime = datetime.combine(self.data_entrega, agora.time())
        delta = data_entrega_datetime - agora
        return delta.total_seconds() // 3600  # Retorna as horas restantes

    
    def dias_para_entrega(self):
        # Retorna a quantidade de dias para o prazo de entrega
        return (self.data_entrega - date.today()).days
    
    def data_formatada(self):
        # Lista de dias da semana em inglês
        dias_da_semana_ingles = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        # Lista de dias da semana em português
        dias_da_semana_portugues = ['seg', 'ter', 'qua', 'qui', 'sex', 'sab', 'dom']
        
        # Formatar a data para o dia e o dia da semana em inglês
        dia_semana_ingles = self.data_entrega.strftime("%a")  # Exemplo: 'Mon', 'Tue', etc.
        dia_semana_portugues = dias_da_semana_portugues[dias_da_semana_ingles.index(dia_semana_ingles)]
        
        # Retornar a data no formato desejado: "08 seg"
        return self.data_entrega.strftime(f"%d {dia_semana_portugues}")


    def __str__(self):
        return f"Dever de {self.fk_materia.nome_materia} - {self.dever} - {self.dever.data_formatada()}"


    # def is_accessible_by(self, user):
    #     if user.role == User.COORDENADOR:
    #         return True
    #     elif user.role == User.PROFESSOR:
    #         return self.fk_professor.usuario == user  # Acesso apenas aos deveres cadastrados por ele
    #     elif user.role == User.PAI:
    #         return True  # Pais podem ver todos os deveres
    #     return False

