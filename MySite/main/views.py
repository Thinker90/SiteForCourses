from django.shortcuts import render
from .models import *


# Create your views here.

def index(request):
    posts = Post.objects.filter(type_id=1)
    return render(request, "index.html", {'activePage': 1,
                                          'posts': posts})

def blog(request):
    return render(request, "blog.html", {'activePage': 4})

def courses(request):
    posts = Post.objects.filter(type_id=2)
    return render(request, "courses.html", {'activePage': 2,
                                            'posts': posts})

def course_detail(request,pk):
    posts = Post.objects.get(id=pk)
    return render(request, "course.html", context={'posts': posts})

def instructors(request):
    return render(request, "instructors.html", {'activePage': 3})

def contact(request):
    return render(request, "contact.html", {'activePage': 5})



