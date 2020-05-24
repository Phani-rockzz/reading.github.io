from django.urls import path, include
from django.conf.urls import url
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('reading/', views.reading, name='reading'),
    path('list/', views.datareading, name='list'),
    path('search/', views.datefilter, name='search'),
    url(r'^detail/(?P<pk>\d+)$', views.datadetails, name='detail'),
    url(r'^edit/(?P<pk>\d+)$', views.reading_update, name='edit'),
    url(r'^delete/(?P<pk>\d+)$', views.reading_delete, name='delete'),

]
