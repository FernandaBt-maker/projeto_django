from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Aluno
from .forms import AlunoForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

def lista_alunos(request):
    alunos = Aluno.objects.all()
    return render(request, 'alunos/lista_alunos.html', {'alunos': alunos})


def detalhe_aluno(request):
    aluno = Aluno.objects.first()
    return render(request, 'alunos/detalhe_aluno.html', {'aluno': aluno})

@login_required

def cadastrar_aluno(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/alunos/')
    else:
        form = AlunoForm()

    return render(request, 'alunos/form_aluno.html', {'form': form})


def cadastrar_aluno(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/alunos/')
    else:
        form = AlunoForm()

    return render(request, 'alunos/form_aluno.html', {'form': form})