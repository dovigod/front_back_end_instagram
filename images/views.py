from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    user = request.user

    if user.is_authenticated:
        return HttpResponse('You have reached the home!')
    else:
        return HttpResponse('fuck u')


def profile(request):

    user = request.user

    if user.is_authenticated:
        return HttpResponse('Hellow Profile!!')
    else:
        return HttpResponse('fuck u')


def explore(request):

    user = request.user

    if user.is_authenticated:
        return HttpResponse('Hellow Profile!!')
    else:
        return HttpResponse('fuck u')


def feed(request):

    user = request.user

    if user.is_authenticated:
        return HttpResponse('Hellow feed!!')
    else:
        return HttpResponse('fuck u')
