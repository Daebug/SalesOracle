from django.urls import path
from . import views

app_name = 'salesoracle'

urlpatterns = [
    path('predict/', views.predict_success, name='predict'),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('loading/', views.loading, name='loading'),

]
