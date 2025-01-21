from django.contrib import admin
from django.urls import path
from posts.views import list_view, detail_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("list/", list_view),
    path("", detail_view),
]
