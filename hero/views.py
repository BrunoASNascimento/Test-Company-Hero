from rest_framework.views import APIView
from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from .models import Employees, Enterprises
from .serializers import EmployeesSerializer, EnterprisesSerializer
from rest_framework.response import Response
import json


class EmployeesCreate(generics.ListCreateAPIView):
    # Create documents with method POST and list all documents with method GET
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer


class EnterprisesCreate(generics.ListCreateAPIView):
    # Create documents with method POST and list all documents with method GET
    queryset = Enterprises.objects.all()
    serializer_class = EnterprisesSerializer


class UsernameList(APIView):
    # Get document by username
    def get(self, request, *args, **kwargs):
        question = get_object_or_404(Employees, pk=kwargs['username'])
        serializer_class = EmployeesSerializer(question)
        return Response(serializer_class.data)


class EmployeesList(APIView):
    # List documents by enterprise
    def get(self, request, *args, **kwargs):
        queryset = Employees.objects.extra(
            where=["'{}' = any (enterprise)".format(kwargs['enterprise'])])
        serialized_q = json.dumps([dict(item) for item in queryset.values()])
        return Response(json.loads(serialized_q))
