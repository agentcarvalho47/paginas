from django.db import models
from django.urls import reverse

# Create your models here.
# Create your models here.
class Aluno(models.Model):
    nome = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
    email = models.CharField(
        max_length=50,
        null=False,
        blank=False
    )
    senha = models.CharField(
        max_length=14,
        null=False,
        blank=False
    )
    matricula = models.CharField(
        max_length=15,
        null=False,
        blank=False
    )
    def get_absolute_url(self): # Insira no final do model
        return reverse('sucessfull')
    