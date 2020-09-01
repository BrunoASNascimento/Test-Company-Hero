from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.postgres.fields import JSONField

# Create your models here.


class Employees(models.Model):

    class Meta:

        db_table = 'employees'

    name = models.CharField(max_length=200)
    age = models.IntegerField()
    enterprise = ArrayField(models.CharField(max_length=200), default=list)

    def __str__(self):
        return self.name
