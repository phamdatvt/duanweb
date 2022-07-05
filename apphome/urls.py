from django.urls import path

from . import views

app_name = 'apphome'
urlpatterns = [
    path('', views.apphome, name='apphome'),
]
