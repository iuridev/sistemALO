from django import forms
from .models import Aluno, Professor, Disciplina, Tutoria


class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = '__all__'


class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = '__all__'


class DisciplinaForm(forms.ModelForm):
    class Meta:
        model = Disciplina
        fields = '__all__'


class TutoriaForm(forms.ModelForm):
    class Meta:
        model = Tutoria
        fields = '__all__'
