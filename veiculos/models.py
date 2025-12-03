from django.db import models

class Veiculo(models.Model):
    STATUS_CHOICES = (
        ("ATIVO", "Ativo"),
        ("MANUTENCAO", "Manutenção"),
        ("INATIVO", "Inativo"),
    )

    placa = models.CharField(max_length=10, unique=True)
    modelo = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    ano = models.IntegerField()
    cor = models.CharField(max_length=30)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="ATIVO")

    def __str__(self):
        return f"{self.modelo} - {self.placa}"
