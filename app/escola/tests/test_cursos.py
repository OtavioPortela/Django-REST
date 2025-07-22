from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from escola.models import Curso
from django.contrib.auth.models import User 

class CursoApiTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='otavio', password='123456')
        self.client.force_authenticate(user=self.user)  # 👈 autentica o teste

    def test_criar_curso(self):
        url = reverse('cursos-list')
        data = {
            "codigo": "PY101",
            "descricao": "Curso de Python para iniciantes",
            "nivel": "B"
        }
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Curso.objects.count(), 1)
        self.assertEqual(Curso.objects.get().codigo, "PY101")
