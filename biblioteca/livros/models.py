from django.db import models
from datetime import datetime
# Create your models here.
class Livro(models.Model):
    nome_livro = models.CharField(max_length=200)
    altor_livro = models.CharField(max_length=200)
    ano_livro = models.DateTimeField(default=datetime.now, blank=True)
    resumo_livro =  models.TextField()
    quantia_livro = models.IntegerField()
    
class Emprestimo(models.Model):
    estado = models.CharField(max_length=15)
    nome_livro = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    email = models.CharField(max_length=200)