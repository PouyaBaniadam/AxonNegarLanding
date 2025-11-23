from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    # 1. CRITICAL: Handle Media files FIRST
    # This forces Django (Gunicorn) to serve the images from your Disk
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),

    # 2. Admin & Plugins
    path('admin/', admin.site.urls),
    path("ckeditor5/", include('django_ckeditor_5.urls')),

    # 3. Your Main App (Must be LAST)
    # If you put this first, it might steal the 'media/' request and show a 404 page.
    path('', include('root.urls')),
]