from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    user = request.user

    if user.is_authenticated:
        return render(
            request,
            'base.html',
            context={
                'title': 'Feed',
                'message': 'hellow dude~~'
            })
    else:
        return render(
            request,
            'base.html',
            context={
                'title': 'Log in',
                'message': 'fuck u'
            })


def profile(request):

    user = request.user

    if user.is_authenticated:
        return render(
            request,
            'base.html',
            context={
                'title': 'Profile',
                'message': 'This is profile html'
            })
    else:
        return render(
            request,
            'base.html',
            context={
                'title': 'Log in',
                'message': ' fuck u'
            })


def explore(request):

    user = request.user

    if user.is_authenticated:
        return render(
            request,
            'base.html',
            context={
                'title': 'Explore',
                'message': 'hellow dude~~'
            })
    else:
        return render(
            request,
            'base.html',
            context={
                'title': 'Log in',
                'message': 'fuck u'
            })
