import imp
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from accounts.views import home
from jobs.views import TnC
urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('accounts.urls')),
    path('jobs/', include('jobs.urls')),
    path('', home, name='home'),
    path('T&Cs/', TnC, name='terms')
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Distinct Writers Hub Admin"
admin.site.site_title = "Distinct Writers Hub Admin"
admin.site.index_title = "Distinct Writers Hub Admin"