import imp
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from accounts.views import home
urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('accounts.urls')),
    path('jobs/', include('jobs.urls')),
    path('', home, name='home')
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

