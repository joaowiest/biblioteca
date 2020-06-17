from django.shortcuts import render
from .models import Livro
from .models import Emprestimo
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    data = {}
    data['livros'] = Livro.objects.all()
    return render(request, 'index.html', data)

def emprestimo(request, id):
    dado={}
    print('emprestimo')
    User.is_authenticated
    livros = Livro.objects.get(id=id)
    print(livros)
    print(livros.quantia_livro)
    form = request.POST
    nome_livro = livros.nome_livro
    username = User.username
    email = User.email
    estado = ('emprestado')
    emprestimo = Emprestimo.objects.create(estado=estado, nome_livro=nome_livro, username=username, email=email)
    emprestimo.save()
    int(livros.quantia_livro)
    livros.quantia_livro -= 1
    print(livros.quantia_livro)
    livros.save()
    dado = {
        'livros':livros
        }
    return render(request,'emprestimo.html', dado)

def devolucao(request, id):
    dado={}
    print('devolver')
    livros = Livro.objects.get(id=id)
    print(livros)
    print(livros.quantia_livro)
    form = request.POST
    nome_livro = livros.nome_livro
    username = User.username
    email = User.email
    estado = ('devolvido')
    emprestimo = Emprestimo.objects.create(estado=estado, nome_livro=nome_livro, username=username, email=email)
    emprestimo.save()
    
    int(livros.quantia_livro)
    livros.quantia_livro += 1
    print(livros.quantia_livro)
    livros.save()
    dado = {
        'livros':livros
        }
    return render(request,'emprestimo.html', dado)
