from rest_framework import serializers
from empapp.models import Employee


class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('Employee_ID', 'First_Name', 'Last_Name', 'Location', 'Age')