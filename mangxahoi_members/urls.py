from . import views
from django.urls import path
from .views import UserRegisterView
#from . import views



app_name = 'mangxahoi_members'
urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'), 
]