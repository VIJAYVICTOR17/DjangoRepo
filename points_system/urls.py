from django.contrib import admin
from django.urls import path, include
from apps.views import home
from django.conf import settings
from django.conf.urls.static import static

# Ensure this line is correct

urlpatterns = [
    path('', home, name='home'),  # Home URL
    path('admin/', admin.site.urls),  # Admin URL
    path('api/', include('apps.urls')),  # Include API URLs
    path('auth/', include('djoser.urls')),  # User authentication
    path('auth/', include('djoser.urls.authtoken')),  # Token authentication
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
