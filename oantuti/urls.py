from django.urls import path

from . import views

app_name = 'oantuti'
urlpatterns = [
    path('', views.oantuti, name='oantuti'),
]
