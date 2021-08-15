from django.shortcuts import *
from django.http import HttpResponse,request
from .models import *

# Create your views here.
def homepage(request):
    #return HttpResponse('<h1>Hello World</h1>')
    return render (request,"index.html")

def register(request):
    if request.method == 'POST':
        data = request.POST.copy()
        name = data.get('name')
        lastname = data.get('Lastname')
        id_card = data.get('ID_number')
        date = data.get('B_date')
        gender = data.get('gender')
        Email = data.get('email')
        address = data.get('address')
        passcode = data.get('passcode')

        datanew = register_students()
        datanew.name = name
        datanew.lastname = lastname
        datanew.ID_card = id_card
        datanew.birthdate = date
        datanew.gender = gender
        datanew.email = Email
        datanew.address = address
        datanew.passcode = passcode

        datanew.save()

        return redirect('home')

    return render(request,"register.html")

def login_backend(request):
    return render(request,"Loginback.html")