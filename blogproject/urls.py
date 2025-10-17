from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("blog.urls")),  # Conecta con las rutas de la app "blog"
    path("accounts/", include("accounts.urls")),  # Enlace para el login y registro
]

# Configuración para archivos multimedia e imágenes
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



