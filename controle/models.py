from django.db import models


# Create your models here.
class Cidade(models.Model):
    nome = models.CharField(max_length=255)

<<<<<<< HEAD
    def __str__(self):
        return self.nome

=======
>>>>>>> 0c47fd46b6934b46aaaf3291c5edf8dde05cb55c

class Clube(models.Model):
    nome = models.CharField(max_length=255)
    dono = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    dimensao = models.CharField(max_length=255)
    preco_hora = models.FloatField(max_length=255)
<<<<<<< HEAD
    cidade = models.ForeignKey(
        Cidade, related_name='clube_cidade', null=True, on_delete=models.DO_NOTHING)
=======
    cidade = models.ForeignKey(Cidade, on_delete=models.DO_NOTHING)
>>>>>>> 0c47fd46b6934b46aaaf3291c5edf8dde05cb55c

    def __str__(self):
        return self.nome
