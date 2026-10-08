from django import forms

from .models import Aluno


class AlunoForm(forms.ModelForm):
    email = forms.EmailField(required=True, label='E-mail')

    class Meta:
        model = Aluno
        fields = ['nome', 'idade', 'email', 'matriculado']