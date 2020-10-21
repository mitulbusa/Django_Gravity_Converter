from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('apitosg', views.apitosg, name='apitosg'),
    path('sgtoapi', views.sgtoapi, name='sgtoapi'),
    path('contact', views.contact, name='contact'),
]
