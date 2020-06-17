from django.shortcuts import render, redirect

from . import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib import auth # importando o modulo de login do django
# Create your views here.
def cadastro(request):
    if request.method == 'POST':
        form = request.POST
        password = form['password']
        password_dois = form['password_dois']
        user = User.objects.create_user( username=form['username'], email=form['email'], password=form['password'],)

        if user is not None:  
            if password == password_dois:
                print('login bem sucedido')
                user.save()
                return redirect('login')
            else:
                print('erro de login')
                return redirect('cadastro')    
        print('erro de cadastro')
           
        return render(request, 'cadastro.html')
    return render(request, 'cadastro.html')

def login(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
    
        print(username, password)
        print (user)
        if user is not None:
            
            auth.login(request, user)
            print('login realisado')
            return redirect('index')
        else:
            print('erro no login')
        return redirect('login')
    return render(request, 'login.html')
def logout(request):
    auth.logout(request)
    return redirect(inicio)
def inicio(request):
    return render(request,'inicio.html')

