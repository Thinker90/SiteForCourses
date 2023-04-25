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

def news_detail(request,pk):
    posts = Post.objects.get(id=pk)
    return render(request, "course.html", context={'posts': posts})

def instructors(request):
    posts = Post.objects.get(type_id=3)
    return render(request, "instructors.html", {'activePage': 3,
                                                'posts': posts})

def contact(request):
    return render(request, "contact.html", {'activePage': 5})

#async def send_message_to_telegram(message):
    # создаем бота
#    API_TOKEN = '6287877530:AAEGHSuJgsvNzP2p3m6L7LD071p9cBw49hY'
#    bot = Bot(token=API_TOKEN)
    # создаем диспетчер
#    dp = Dispatcher(bot)
    # отправляем сообщение
#    await bot.send_message(text=message)

