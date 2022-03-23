from django.urls import re_path
from .import views
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    re_path(r'^$', views.admin_log, name='admin_log'),
    re_path(r'^admin_login$', views.admin_login, name='admin_login'),
    re_path(r'^admin_dashboard$', views.admin_dashboard, name='admin_dashboard'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)