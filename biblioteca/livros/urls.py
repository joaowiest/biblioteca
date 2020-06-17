from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('emprestimo/<int:id>', views.emprestimo, name = 'emprestimo'),
    path('devolucao/<int:id>', views.devolucao, name = 'devolucao'),
]
