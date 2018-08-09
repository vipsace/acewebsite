from django.contrib import admin
from django.urls import path, include
from website.views import index

urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
    path('s3direct/', include('s3direct.urls')),
    path('portal/', include('portalapp.urls')),
    path('', include('social_django.urls', namespace='social'))

]
admin.site.site_header = 'ACE'