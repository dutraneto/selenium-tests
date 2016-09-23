from django.db import models
from django.utils import timezone


class Pessoa(models.Model):

    nome_pessoa = models.CharField(max_length=45)
    endereco = models.CharField(max_length=100)
    cpf = models.CharField(max_length=15)

    def __str__(self):

        return self.nome_pessoa


class Pertence(models.Model):

    nome_pertence = models.CharField(max_length=45)
    descricao = models.TextField()
    data_criacao = models.DateField(default=timezone.now)
    pessoa_fk = models.ForeignKey(Pessoa, on_delete=models.CASCADE)

    def __str__(self):

        return self.nome_pertence
