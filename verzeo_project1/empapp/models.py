import uuid

from django.db import models


# Create your models here.
class Employee(models.Model):
    Employee_ID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    First_Name = models.CharField(max_length=50)
    Last_Name = models.CharField(max_length=50)
    Location = models.CharField(max_length=50)
    Age = models.IntegerField(default=0)

