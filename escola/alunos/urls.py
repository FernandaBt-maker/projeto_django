from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_alunos, name='lista_alunos'),
    path('detalhe/', views.detalhe_aluno, name='detalhe_aluno'),
    path('novo/', views.cadastrar_aluno, name='cadastrar_aluno'),
]