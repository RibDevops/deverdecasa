from django.db import models
from django.contrib.auth.models import AbstractUser

# dever/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

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

class Materia(models.Model):
    nome_materia = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_materia

class Escola(models.Model):
    nome_escola = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_escola


class Professor(models.Model):
    fk_escola = models.ForeignKey(Escola, on_delete=models.CASCADE, related_name="Professores")
    fk_materia = models.ForeignKey(Materia, on_delete=models.CASCADE, related_name="Materia")
    nome_professor = models.CharField(max_length=100)
    # usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_professor


class Aluno(models.Model):
    fk_escola = models.ForeignKey(Escola, on_delete=models.CASCADE, related_name="alunos")
    fk_professor = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name="alunos")
    nome_aluno = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_aluno





class Livro(models.Model):
    nome_livro = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_livro


class DeverDeCasa(models.Model):
    fk_escola = models.ForeignKey(Escola, on_delete=models.CASCADE, related_name="deveres")
    fk_professor = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name="deveres")
    fk_materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    fk_livro = models.ForeignKey(Livro, on_delete=models.CASCADE, null=True, blank=True)
    descricao = models.TextField()
    data_postagem = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Dever de {self.fk_materia.nome_materia} - {self.descricao} - {self.data_postagem.date()}"

    # def is_accessible_by(self, user):
    #     if user.role == User.COORDENADOR:
    #         return True
    #     elif user.role == User.PROFESSOR:
    #         return self.fk_professor.usuario == user  # Acesso apenas aos deveres cadastrados por ele
    #     elif user.role == User.PAI:
    #         return True  # Pais podem ver todos os deveres
    #     return False
