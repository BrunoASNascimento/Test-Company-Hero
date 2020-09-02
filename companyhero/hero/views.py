from rest_framework.views import APIView
from django.shortcuts import render
from rest_framework import generics
from .models import Employees
from .serializers import EmployeesSerializer

# Create your views here.
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
import json
from django.core.serializers.json import DjangoJSONEncoder


class EmployeesCreate(generics.ListCreateAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer


class UsernameList(APIView):
    def get(self, request, *args, **kwargs):
        question = get_object_or_404(Employees, pk=kwargs['username'])
        serializer_class = EmployeesSerializer(question)
        return Response(serializer_class.data)


class EmployeesList(generics.ListCreateAPIView):
    def get(self, request, *args, **kwargs):
        queryset = Employees.objects.extra(
            where=["'{}' = any (enterprise)".format(kwargs['enterprise'])])
        serialized_q = json.dumps([dict(item) for item in queryset.values()])
        return Response(json.loads(serialized_q))
