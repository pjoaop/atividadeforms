from django.db import models

# Create your models here.

LISTA_CURSO= [
    ('Informatica', 'Informatica'),
    ('Apicultura', 'Apicultura'),
    ('Alimentos', 'Alimentos'),
]

class Pessoa(models.Model):
    nome = models.CharField(max_length=150)
    cpf = models.CharField(max_length=30)
    nascimento =models.DateField()
    email = models.EmailField()
    endereco = models.CharField(max_length=300)
    curso = models.CharField(max_length=150, choices=LISTA_CURSO)

    def __str__(self) -> str:
        return self.nome