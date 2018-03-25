from django.shortcuts import render

from posts.models import Posts


# Create your views here.


def index(request):
    context = {
        'title': 'Hello',
        'posts': Posts.objects.all()
    }
    return render(request, 'posts/index.html', context)


def details(request, id):
    context = {
        'post': Posts.objects.get(id=id)
    }
    return render(request, 'posts/details.html', context)
