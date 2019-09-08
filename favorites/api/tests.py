'''from .models import Employee

from rest_framework.test import APITestCase, APIClient
from rest_framework import status

class EmployeeTestCase(APITestCase):
    """
    Classe de testes da API.
    """

    fixtures = [
        'employee.json'
        ]

    def setUp(self):
        """
        Instancia APIClient e loga utilizando superuser.
        """
        self.client = APIClient()
        self.client.login(user='manager', password='123456')

    def test_get_api_root(self):
        """
        Testa método get em APIRoot.
        """
        response = self.client.get('http://localhost:8000/api/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_employee(self):
        """
        Testa Método get em "/api/employee/".
        """
        response = self.client.get('http://localhost:8000/api/employee/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_employee(self):
        """
        Testa Método post em "/api/employee/".
        """
        response = self.client.post('http://localhost:8000/api/employee/',
                                    {
                                    "name": "Luan teste",
                                    "email": "luan@teste.com",
                                    "department": "teste"
                                    }
                                    )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_patch_employee(self):
        """
        Testa Método patch em "/api/employee/teste/".
        """
        response = self.client.patch('http://localhost:8000/api/employee/teste/',
                                    {
                                    "name": "testado",
                                    "email": "testado@testado.com",
                                    "department": "testado"
                                    }
                                    )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'testado')
        self.assertEqual(response.data['email'], 'testado@testado.com')
        self.assertEqual(response.data['department'], 'testado')

    def test_delete_employee(self):
        """
        Testa Método delete em "/api/employee/teste/".
        """
        response = self.client.delete('http://localhost:8000/api/employee/teste/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
'''
