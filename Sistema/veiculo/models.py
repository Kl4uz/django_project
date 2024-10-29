from django.db import models
from .consts import OPCOES_COMBUSTIVEIS, OPCOES_CORES, OPCOES_MARCAS

class Veiculo(models.Model):
    marca = models.SmallIntegerField(choices =  OPCOES_MARCAS)
    modelo = models.CharField(max_length=100)
    ano = models.IntegerField()
    cor = models.SmallIntegerField(choices= OPCOES_CORES)
    foto = models.ImageField(blank = True, null = True, upload_to = '')
    combustivel = models.SmallIntegerField(choices= OPCOES_COMBUSTIVEIS)

