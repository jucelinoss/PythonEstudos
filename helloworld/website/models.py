from django.db import models

# Create your models here.
from django.db import models


class AlunoUnivesp(models.Model):
    objetos = models.Manager()
    nome = models.CharField(max_length=255, null=False, blank=False)
    sobrenome = models.CharField(max_length=255, null=False, blank=False)
    matricula = models.CharField(max_length=14, null=False, blank=False)

