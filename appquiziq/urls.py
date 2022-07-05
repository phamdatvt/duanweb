from django.urls import path

from . import views

app_name = 'appquiziq'
urlpatterns = [
    path('', views.appquiziq, name='appquiziq'),
    path("<int:myid>/", views.quiz, name="quiz"),
]
