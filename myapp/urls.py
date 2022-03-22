from django.urls import re_path
from .import views

urlpatterns = [
    re_path(r'^$', views.admin_log, name='admin_log'),
    re_path(r'^admin_login$', views.admin_login, name='admin_login'),
    re_path(r'^admin_dashboard$', views.admin_dashboard, name='admin_dashboard'),
]
