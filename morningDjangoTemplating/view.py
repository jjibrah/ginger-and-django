from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def gallery(request):
    return render(request, 'gallery.html')


courses = [
    {"name": "Python", "duration": "2 months", "cost": "KSH 25k "},
    {"name": "Android", "duration": "2 months", "cost": "KSH 35k "},
    {"name": "Data science", "duration": "4 months", "cost": "KSH 60k "},
]


def courses(request):
    context = {"Courses": courses}
    return render(request, 'courses.html', context)
