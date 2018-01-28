from django.shortcuts import render
from django.http import HttpResponse
from .models import Image, Comment, Like

# Create your views here.


def index(request):
    user = request.user

    if user.is_authenticated:
        all_images = Image.objects.all()
        all_comments = Comment.objects.all()
        all_likes = Like.objects.all()

        return render(
            request,
            'feed.html',
            context={
                'images': all_images,
                'comments': all_comments,
                'likes': all_likes
            })
    else:
        return render(request, 'login.html')


def profile(request):

    user = request.user

    if user.is_authenticated:
        return render(request, 'profile.html')
    else:
        return render(request, 'login.html')


def explore(request):

    user = request.user

    if user.is_authenticated:
        all_images = Image.objects.all()
        all_comments = Comment.objects.all()
        all_likes = Like.objects.all()

        return render(request, 'explore.html', context={'images': all_images})
    else:
        return render(request, 'login.html')
