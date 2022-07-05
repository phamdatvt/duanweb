from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

from .forms import DangkyForm

# Create your views here.

class UserRegisterView(generic.CreateView):
    form_class = DangkyForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

