from django.shortcuts import render
from .models import Destination


def index(request):
    decs = Destination.objects.all()

    return render(request, 'index.html', {'dest': decs})


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def elements(request):
    return render(request, 'elements.html')


def news(request):
    return render(request, 'news.html')


def destinations(request):
    return render(request, 'destinations.html')
