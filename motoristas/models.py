from django.db import models

class Motorista(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14)
    telefone = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)

    cnh_numero = models.CharField(max_length=20)
    cnh_categoria = models.CharField(max_length=5)
    cnh_validade = models.DateField()

    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome
