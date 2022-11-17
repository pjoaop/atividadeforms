from django.db import models
# Create your models here.

LISTA_CURSO= [
    ('Informatica', 'Informatica'),
    ('Apicultura', 'Apicultura'),
    ('Alimentos', 'Alimentos'),
]

LISTA_SEXO = [
        ('masculino','masculino'),
        ('feminino','feminino'),
    ]

class MiniCurso(models.Model):
    nome = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.nome

class Pessoa(models.Model):
    nome = models.CharField(max_length=150)
    cpf = models.CharField(max_length=30)
    nascimento =models.DateField()
    email = models.EmailField()
    endereco = models.CharField(max_length=300)
    sexo = models.CharField(max_length=150,choices=LISTA_SEXO,default='Feminino')
    curso = models.CharField(max_length=150, choices=LISTA_CURSO)
    minicursos = models.ManyToManyField(MiniCurso)

    def __str__(self) -> str:
        return self.nome