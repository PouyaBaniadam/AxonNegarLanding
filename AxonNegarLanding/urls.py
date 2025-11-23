from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    # 1. MEDIA HANDLER (Must be at the top)
    # We convert MEDIA_ROOT to str() just to be 100% safe
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': str(settings.MEDIA_ROOT)
    }),

    # 2. Admin and other apps
    path('admin/', admin.site.urls),
    path("ckeditor5/", include('django_ckeditor_5.urls')),
    path('', include('root.urls')),
]