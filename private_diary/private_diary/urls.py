from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.contrib.staticfiles.urls import static
from .import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('diary.urls')),
    path('accounts/' ,include('allauth.urls')),
]

urlpatterns += static(settings.MEDIA_URL,
document_root=settings.MEDIA_ROOT)
