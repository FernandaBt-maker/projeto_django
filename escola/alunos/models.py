from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    email = models.EmailField(default="sememail@gmail.com",max_length=150)
    matriculado = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

    def __str__(self):
        return self.nome
