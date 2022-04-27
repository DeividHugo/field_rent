from django.db import models


# Create your models here.
class Cidade(models.Model):
    nome = models.CharField(max_length=255)


class Clube(models.Model):
    nome = models.CharField(max_length=255)
    dono = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    dimensao = models.CharField(max_length=255)
    preco_hora = models.FloatField(max_length=255)
    cidade = models.ForeignKey(Cidade, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.nome
