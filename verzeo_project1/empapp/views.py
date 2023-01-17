from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from empapp.models import Employee
from empapp.serializers import EmployeesSerializer

@csrf_exempt
def index(request):
    return render(request, "index.html")


def all_employee(request):
    employees = Employee.objects.all()
    context = {
        'employees': employees

    }
    return render(request, "all_employee.html", context)


@csrf_exempt
def add_employee(request):
    if request.method == 'POST':
        employee_data = Employee(First_Name=request.POST['First_Name'],
                                 Last_Name=request.POST['Last_Name'],
                                 Location=request.POST['Location'],
                                 Age=request.POST['Age'])
        # check if user is already exist or not
        employees = Employee.objects.filter(First_Name=employee_data.First_Name,
                                            Last_Name=employee_data.Last_Name)
        print(employees.count())
        # check user existence
        if employees.count() != 0:
            return JsonResponse("User is already Exist in our Application", safe=False)
        elif employee_data is not None:
            # saving the new data into database
            employee_data.save()
            return JsonResponse("User has been registered Successfully in Application", safe=False)
        return JsonResponse("Please Enter the correct Input", safe=False)
    elif request.method == 'GET':
        return render(request, "add_employee.html")
    else:
        return JsonResponse("Something Went Wrong", safe=False)


def remove_employee(request):
    if request.method == 'POST':
        # reading the data from user input
        employee_data = Employee(First_Name=request.POST['First_Name'],
                                 Last_Name=request.POST['Last_Name'])
        
        name = employee_data.First_Name
        employee = Employee.objects.filter(First_Name=name, Last_Name=employee_data.Last_Name)
        # check user existence
        if employee.count() == 0:
            return JsonResponse(name + " is not Exist in our Application")
        else:
            # delete the user
            employee.delete()
            return JsonResponse(name + " has been deleted Successfully", safe=False)
    elif request.method == 'GET':
        return render(request, "remove_employee.html")
    else:
        return JsonResponse("Something Went Wrong", safe=False)

def filter_employee(request):
    if request.method == 'POST':
        # to get all the data from database
        employees = Employee.objects.all()
        # taking the parameter to be filtered
        if 'First_Name' in request.POST:
            employees = employees.filter(First_Name=request.POST['First_Name'])
        if 'Last_Name' in request.POST:
            employees = employees.filter(Last_Name=request.POST['Last_Name'])
        # serializing the data from the database
        employees_serializer = EmployeesSerializer(employees, many=True)
        context = {
            'employees': employees_serializer.data

        }
        return render(request, "all_employee.html", context)
    elif request.method == 'GET':
        return render(request, "filter_employee.html")
    else:
        return JsonResponse("Something Went Wrong", safe=False)
