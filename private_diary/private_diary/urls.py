
from django.contrib import admin
from django.urls import path, path
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('diary.urls')),
    path('accounts/', include('allauth.urls')),
]
