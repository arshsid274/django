
#from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
 #  return HttpResponse("Welcome to the Homepage!")
  return render(request,'home.html')

def aboutpage(request):
 #   return HttpResponse("This is the About Page.")
   return render(request,'about.html')