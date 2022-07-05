from datetime import datetime
from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from .models import *
# Create your views here.

def appquizenglish(request):
  question = Question.objects.all()
  context = {'question': question}
  return render(request, 'appquizenglish/testENG.html', context)
  #template = loader.get_template('appquizenglish/testENG.html') 
  #return HttpResponse(template.render())


  