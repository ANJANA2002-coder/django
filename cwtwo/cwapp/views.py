from django.shortcuts import render

def employee_list(request):
    employees = [
        {"name": "Anjana", "job": "Data Analyst", "salary": 50000, "full_time": True},
        {"name": "Rahul", "job": "Developer", "salary": 60000, "full_time": False},
        {"name": "Meera", "job": "Designer", "salary": 45000, "full_time": True},
    ]

    return render(request, "employees.html", {"employees": employees})


