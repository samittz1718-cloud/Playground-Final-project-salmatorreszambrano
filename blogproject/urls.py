from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("blog.urls")),                 # Home/About/Pages
    path("accounts/", include("accounts.urls")),    # Auth y perfiles
    path("messages/", include("messages_app.urls")),# Mensajería
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


