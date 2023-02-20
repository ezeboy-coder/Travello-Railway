from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


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
