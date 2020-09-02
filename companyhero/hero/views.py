from rest_framework.views import APIView
from django.shortcuts import render
from rest_framework import generics
from .models import Employees
from .serializers import EmployeesSerializer

# Create your views here.
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status


class EmployeesList(generics.ListCreateAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer


class UsernameList(APIView):
    def get(self, request, *args, **kwargs):
        question = get_object_or_404(Employees, pk=kwargs['username'])
        serializer = EmployeesSerializer(question)
        return Response(serializer.data)
