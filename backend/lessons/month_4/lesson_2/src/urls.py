from django.contrib import admin
from django.urls import path
from posts.views import gallery, sayhello, posts, main_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("gallery/", gallery),
    path("", main_view),
    path("hello", sayhello),
    path("posts", posts),
]
