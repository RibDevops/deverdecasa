from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    PROFILE_CHOICES = [
        ('COORDENADOR', 'Coordenador'),
        ('PROFESSOR', 'Professor'),
        ('PAI', 'Pai'),
    ]

    profile = models.CharField(max_length=15, choices=PROFILE_CHOICES, default='PAI')
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username
    