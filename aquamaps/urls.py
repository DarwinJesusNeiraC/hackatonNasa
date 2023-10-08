from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from usuarios.views import register_request, home, login_request, logout_request
from animales.views import mapa

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='homepage'),
    path('register/', register_request, name='register'),
    path('login/', login_request, name='login'),
    path('logout/', logout_request, name='logout'),
    path('mapa/', mapa, name='mapa'),
]

# Añade estas líneas para servir archivos multimedia durante el desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
