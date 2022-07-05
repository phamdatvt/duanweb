from django.urls import path

from . import views

app_name = 'appre'
urlpatterns = [
    path('', views.appre, name='appre'),
]
