# from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Employee



# Create your tests here.
class EmployeeAPITests(APITestCase):

    def setUp(self):
        # Create user
        self.user = User.objects.create_user(
            username="testpass",
            password="testpass123"
        )

        # Get JWT token
        token_url = reverse('token_obtain_pair')
        response = self.client.post(
            token_url,
            {
                "username": "testpass",
                "password": "testpass123"
            },
            format="json"
        )

        self.access_token = response.data["access"]

        # Attach token to client
        self.client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {self.access_token}"
        )

        self.employee_list_url = reverse('employee-list-create')

        def test_create_employee_success(self):
            data = {
                "name": "Ajay",
                "email": "ajay@test.com",
                "department": "IT",
                "role": "Developer"
            }

            response = self.client.post(
                self.employee_list_url,
                data,
                format="json"
            )

            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            self.assertEqual(Employee.objects.count(), 1)
            self.assertEqual(
                Employee.objects.first().email,
                "ajay@test.com"
            )
    
    def test_create_employee_duplicate_email(self):
        Employee.objects.create(
            name="First",
            email="dup@test.com"
        )

        data = {
            "name": "Second",
            "email": "dup@test.com"
        }

        response = self.client.post(
            self.employee_list_url,
            data,
            format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    def test_list_employees(self):
        Employee.objects.create(name="Emp1", email="e1@test.com")
        Employee.objects.create(name="Emp2", email="e2@test.com")

        response = self.client.get(self.employee_list_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 2)

    def test_get_employee_not_found(self):
        url = reverse('employee-detail', kwargs={"pk": 999})

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_employee(self):
        employee = Employee.objects.create(
            name="Delete Me",
            email="delete@test.com"
        )

        url = reverse(
            'employee-detail',
            kwargs={"pk": employee.id}
        )

        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Employee.objects.count(), 0)

