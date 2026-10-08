from django.test import TestCase
from .models import Aluno
from django.urls import reverse
from .forms import AlunoForm



class AlunoViewsTests(TestCase):
	def setUp(self):
		self.aluno = Aluno.objects.create(
			nome='Ana',
			email='ana@example.com',
			idade=20,
			matriculado=True,
		)

	def test_lista_exibe_situacao_da_matricula(self):
		response = self.client.get(reverse('lista_alunos'))

		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Ana')
		self.assertContains(response, 'Sim')

	def test_detalhe_exibe_apenas_nome_do_aluno(self):
		response = self.client.get(reverse('detalhe_aluno'))

		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Ana')
		self.assertNotContains(response, 'ana@example.com')
		self.assertNotContains(response, '20')

	def test_pagina_de_cadastro_esta_disponivel(self):
		response = self.client.get(reverse('cadastrar_aluno'))

		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'alunos/form_aluno.html')

	def test_pagina_de_login_esta_disponivel(self):
		response = self.client.get(reverse('login_direto'))

		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'registration/login.html')

	def test_pagina_inicial_abre_o_login(self):
		response = self.client.get(reverse('inicio'), follow=True)

		self.assertRedirects(response, reverse('login_direto'))
		self.assertTemplateUsed(response, 'registration/login.html')

	def test_formulario_exige_email(self):
		form = AlunoForm(data={
			'nome': 'Bruno',
			'idade': 18,
			'email': '',
			'matriculado': True,
		})

		self.assertFalse(form.is_valid())
		self.assertIn('email', form.errors)

	def test_lista_alunos_status(self):
			response = self.client.get('/alunos/')
			self.assertEqual(response.status_code, 200)

class AlunoModelTest(TestCase):

    def test_criar_aluno(self):
        aluno = Aluno.objects.create(
            nome="Teste",
            idade=20,
            email="teste@email.com"
        )

        self.assertEqual(aluno.nome, "Teste")
        self.assertTrue(aluno.matriculado)