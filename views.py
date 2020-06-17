from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
# Create your views here.


class Login(View):
    template_name = 'login.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        form = request.POST
        user = authenticate(
            request, username=form['username'], password=form['password'])
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, self.template_name, {
                'error': 'Credenciais Inválidas'
            })


@login_required
def logout_view(request):
    logout(request)
    return ('home')


# class Restricted(View, LoginRequiredMixin)
