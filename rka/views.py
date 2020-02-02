from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def prodView(request):
    return render(request, 'prview.html')


def search(request):
    return render(request, 'search.html')


def sale(request):
    return render(request, 'sale.html')
    