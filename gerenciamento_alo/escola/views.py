from django.shortcuts import render, redirect
from .forms import AlunoForm, ProfessorForm, DisciplinaForm, TutoriaForm
from .models import Aluno  # adicione essa linha


def cadastrar_aluno(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirecionar para a lista de alunos
            return redirect('listar_alunos')
    else:
        form = AlunoForm()
    return render(request, 'escola/cadastrar_aluno.html', {'form': form})


def listar_alunos(request):
    alunos = Aluno.objects.all()
    return render(request, 'escola/listar_alunos.html', {'alunos': alunos})


def cadastrar_professor(request):
    if request.method == 'POST':
        form = ProfessorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('escola/listar_professores')
    else:
        form = ProfessorForm()
    return render(request, 'escola/cadastrar_professor.html', {'form': form})


def listar_professores(request):
    professores = Professor.objects.all()
    return render(request, 'escola/listar_professores.html', {'professores': professores})


def cadastrar_disciplina(request):
    if request.method == 'POST':
        form = DisciplinaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('escola/listar_disciplinas')
    else:
        form = DisciplinaForm()
    return render(request, 'escola/cadastrar_disciplina.html', {'form': form})


def listar_disciplinas(request):
    disciplinas = Disciplina.objects.all()
    return render(request, 'escola/listar_disciplinas.html', {'disciplinas': disciplinas})


def cadastrar_tutoria(request):
    if request.method == 'POST':
        form = TutoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_tutorias')
    else:
        form = TutoriaForm()
    return render(request, 'escola/cadastrar_tutoria.html', {'form': form})


def listar_tutorias(request):
    tutorias = Tutoria.objects.all()
    return render(request, 'escola/listar_tutorias.html', {'tutorias': tutorias})
