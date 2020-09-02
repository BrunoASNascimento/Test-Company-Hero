from rest_framework import serializers
from .models import Employees, Enterprises


class EmployeesSerializer(serializers.ModelSerializer):

    class Meta:

        model = Employees
        fields = fields = '__all__'


class EnterprisesSerializer(serializers.ModelSerializer):

    class Meta:

        model = Enterprises
        fields = fields = '__all__'
