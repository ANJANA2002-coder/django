from django.shortcuts import render

def student_list(request):
    students = [
        {"name": "Anu", "grade": 85, "passed": True},
        {"name": "Rahul", "grade": 40, "passed": False},
        {"name": "Meera", "grade": 72, "passed": True},
    ]

    return render(request, "students.html", {"students": students})