from django.contrib.auth.models import AbstractUser
from django.db import models

# class User(AbstractUser):
#     PROFILE_CHOICES = [
#         ('COORDENADOR', 'Coordenador'),
#         ('PROFESSOR', 'Professor'),
#         ('PAI', 'Pai'),
#     ]
#     profile = models.CharField(max_length=15, choices=PROFILE_CHOICES, default='PAI')
#     email = models.EmailField(unique=True)

#     def __str__(self):
#         return self.username
from django.contrib.auth.models import AbstractUser, Group
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)
    # Relacionamento com Escola no app 'dever'
    fk_escola = models.ForeignKey('dever.Escola', on_delete=models.CASCADE, related_name='id_escola', null=True, blank=True)

    def __str__(self):
        return self.username

