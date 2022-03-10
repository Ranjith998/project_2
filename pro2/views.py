from wsgiref.handlers import read_environ
from django.http import HttpResponse
from django.shortcuts import render

def sample(request):
    fp= open(r'C:\Users\ACER\Desktop\Django\project_2\templates\sample.html','r')
    res=fp.read()
    return HttpResponse(res)

def index(request):
    return render(request,'sample.html')

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def gallery(request):
    return render(request,'gallery.html')

def contact(request):
    return render(request,'contact.html')

def feedback(request):
    return render(request,'feedback.html')