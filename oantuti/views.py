from django.shortcuts import render

# Create your views here.

def oantuti(request):
  return render(request, 'oantuti/oantuti.html', {})
