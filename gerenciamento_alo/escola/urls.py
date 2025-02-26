from django.urls import path
from . import views

urlpatterns = [
    path('alunos/cadastrar/', views.cadastrar_aluno, name='cadastrar_aluno'),
    path('alunos/', views.listar_alunos, name='listar_alunos'),
    path('professores/cadastrar/', views.cadastrar_professor,
         name='cadastrar_professor'),
    path('professores/', views.listar_professores, name='listar_professores'),
    path('disciplinas/cadastrar/', views.cadastrar_disciplina,
         name='cadastrar_disciplina'),
    path('disciplinas/', views.listar_disciplinas, name='listar_disciplinas'),
    path('tutorias/cadastrar/', views.cadastrar_tutoria, name='cadastrar_tutoria'),
    path('tutorias/', views.listar_tutorias, name='listar_tutorias'),
]
