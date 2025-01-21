from django.contrib import admin
from django.db.utils import settings
from django.forms.widgets import static
from django.urls import path
from posts.views import list_view, detail_view
from django.conf.urls.static import static  # pyright: ignore

urlpatterns = [
    path("admin/", admin.site.urls),
    path("list/", list_view),
    path("", detail_view),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
