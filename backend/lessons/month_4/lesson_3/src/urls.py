from django.contrib import admin
from django.urls import path
from posts.views import gallery, sayhello, posts, main_view
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("gallery/", gallery),
    path("", main_view),
    path("hello", sayhello),
    path("posts", posts),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
