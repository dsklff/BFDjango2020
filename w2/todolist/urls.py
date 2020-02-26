from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('polls/', include('api.urls')),
    path('admin/', admin.site.urls),
]
