from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def apphome(request):
  template = loader.get_template('apphome/home.html') 
  return HttpResponse(template.render())

