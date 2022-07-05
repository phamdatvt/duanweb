from django.shortcuts import render

from .models import *
# Create your views here.

def appquiziq(request):
  quiz = Quiz.objects.all()
  context = {'quiz': quiz}
  return render(request, 'appquiziq/testIQ.html', context)
  #template = loader.get_template('appquizenglish/testENG.html') 
  #return HttpResponse(template.render())

def quiz(request, myid):
    quiz = Quiz.objects.get(id=myid)
    return render(request, "appquiziq/quiz.html", {'quiz':quiz})