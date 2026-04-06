from django.shortcuts import render

# Sample student data (can be from DB later)
students = [
    {'name': 'Aiswarya', 'marks': 85},
    {'name': 'Rahul', 'marks': 72},
    {'name': 'Sneha', 'marks': 90},
]

def home(request):
    return render(request, 'home.html', {'students': students})


def result(request, name):
    student_data = None

    for student in students:
        if student['name'] == name:
            student_data = student

    return render(request, 'result.html', {'student': student_data})