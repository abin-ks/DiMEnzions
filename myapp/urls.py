from django.urls import re_path
from .import views

urlpatterns = [
    re_path(r'^$', views.admin_dashboard, name='admin_dashboard'),
]
