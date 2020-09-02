from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.postgres.fields import JSONField
from django.core.validators import MaxValueValidator, MinValueValidator


class Enterprises(models.Model):

    class Meta:
        # Table name
        db_table = 'enterprises'

    """     
    name: Name and primary key
    country: Country name    

    """

    name = models.CharField(max_length=200, primary_key=True)
    country = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Employees(models.Model):

    class Meta:
        # Table name
        db_table = 'employees'

    """     
    username: Username and primary key
    name: Employee name
    age: Employee age
    enterprise: List with the names of the employees' companies

    """
    username = models.CharField(max_length=32, primary_key=True)
    name = models.CharField(max_length=200)
    age = models.IntegerField(validators=[
        MaxValueValidator(120),
        MinValueValidator(10)
    ])
    enterprise = ArrayField(models.CharField(max_length=200), default=list)

    def __str__(self):
        return self.name
