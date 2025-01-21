from django.shortcuts import render
from django.http import HttpResponse
from posts.models import Post


def sayhello(request):
    return HttpResponse("Hello, world.")  # pyright: ignore


def gallery(request):
    return render(request, "gallery/gallery.html")


def posts(request):
    posts = Post.objects.all()
    return render(request, "posts/posts_list.html", context={"posts": posts})


def main_view(request):
    return render(request, "base.html")
