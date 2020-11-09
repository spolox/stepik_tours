from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


def custom_handler404(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена, пора попить чаёк<h1>')


def custom_handler500(request):
    return HttpResponse('<h1>Извините, сервак упал. Подождите немного...<h1>')


def main_view(request):
    return render(request, 'index.html')


def departure_view(request, departure):
    return render(request, 'departure.html')


def tour_view(request, tour_id):
    return render(request, 'tour.html')
