from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('root.urls')),
    path("ckeditor5/", include('django_ckeditor_5.urls')),
    
    # This forces Django to serve media files from your mounted Disk
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]