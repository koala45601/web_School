from django.shortcuts import render
from django.http import HttpResponse,request

# Create your views here.
def homepage(request):
    #return HttpResponse('<h1>Hello World</h1>')
    return render (request,"index.html")


def register(request):
    return render(request,"register.html")