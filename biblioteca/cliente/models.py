from django.db import models
from datetime import datetime
# Create your models here.
class Emprestimo(models.Model):
    username = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    nome_livro = models.CharField(max_length=9)
    data = models.DateTimeField(default=datetime.now, blank=True)
    # python manage.py makemigrations
    # python manage.py migrate