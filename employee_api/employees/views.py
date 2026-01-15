# from django.shortcuts import render

from rest_framework import permissions , generics
from .models import Employee
from .serializers import EmployeeSerializer


# Create your views here.


class EmployeeListCreateView(generics.ListCreateAPIView):
    # queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]


    def get_queryset(self):
        queryset = Employee.objects.all()
        department = self.request.query_params.get('department')
        role = self.request.query_params.get('role')

        if department:
            queryset = queryset.filter(department=department)

        if role:
            queryset = queryset.filter(role=role)
        
        return queryset


class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]