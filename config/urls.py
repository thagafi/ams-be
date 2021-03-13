from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),
    path('api/', include('formations.urls')),
    path('api/', include('computers.urls')),
    path('api/', include('servers.urls')),
]
