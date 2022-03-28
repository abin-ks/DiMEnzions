from django.urls import re_path
from .import views
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    re_path(r'^$', views.admin_log, name='admin_log'),
    re_path(r'^/admin_login$', views.admin_login, name='admin_login'),
    re_path(r'^/admin_dashboard$', views.admin_dashboard, name='admin_dashboard'),
    re_path(r'^/logout$', views.logout, name='logout'),
    
    #category
    re_path(r'^/category$', views.show_category, name="category"),
    re_path(r'^/add_category$', views.add_category, name="add_category"),
    re_path(r'^/cat_delete/(?P<cat_id>\d+)$', views.cat_delete, name="cat_delete"),
    
    #models
    re_path(r'^/admin_models$', views.admin_models, name='admin_models'),
    
    #add model
    re_path(r'^/addmodel$', views.addmodel, name="addmodel"),
    re_path(r'^/createmodel$', views.createmodel, name="createmodel"),
    
    #payment history
    re_path(r'^/admin_payment_history$', views.admin_payment_history, name='admin_payment_history'),
    re_path(r'^/payment_table$', views.payment_table, name='payment_table'),
    
    #registered users
    re_path(r'^/registeredusers$', views.registeredusers, name='registeredusers'),
    re_path(r'^/delete/(?P<reg_id>\d+)$', views.delete, name='delete'),
    
    #model edit
    re_path(r'^/adminedit/(?P<id>\d+)$', views.adminedit,name="adminedit"),
    re_path(r'^/modeledit/(?P<id>\d+)$', views.modeledit,name="modeledit"),

    #current models
    re_path(r'^/admin_current_models$', views.admin_current_models, name='admin_current_models'),
    re_path(r'^/model_delete/(?P<id>\d+)$', views.model_delete,name="model_delete")
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)