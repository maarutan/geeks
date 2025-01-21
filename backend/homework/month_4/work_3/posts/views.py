from django.shortcuts import render
from posts.models import Post


def detail_view(request):
    return render(request, "detail.html")


def list_view(request):
    posts = Post.objects.all()
    return render(request, "posts/posts_list.html", context={"posts": posts})
