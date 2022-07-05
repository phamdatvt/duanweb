from django.urls import path

from . import views

app_name = 'appquizenglish'
urlpatterns = [
    path('', views.appquizenglish, name='appquizenglish'),
    
]
