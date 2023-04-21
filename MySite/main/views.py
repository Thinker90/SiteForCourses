from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, "index.html", {'activePage': 1})

def blog(request):
    return render(request, "blog.html", {'activePage': 4})

def courses(request):
    return render(request, "courses.html", {'activePage': 2})

def instructors(request):
    return render(request, "instructors.html", {'activePage': 3})

def contact(request):
    return render(request, "contact.html", {'activePage': 5})

