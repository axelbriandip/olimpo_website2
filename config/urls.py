# config/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static # Necesario para servir media en desarrollo

urlpatterns = [
    path('admin/', admin.site.urls),
    # ⚠️ Root path points to the 'core' app
    path('', include('core.urls')), 
    
    # Paths for MVP apps
    path('news/', include('news.urls')), 
    path('club/', include('club.urls')),
]

# Configuración para servir archivos multimedia (imágenes) durante el desarrollo.
# NO usar en producción.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)