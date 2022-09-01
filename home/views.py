
from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
# Create your views here.
def index(request):
    context = {
        'variable':'This is sent'
    }
    return render(request,'index.html',context)

    
    
def about(request):
    return render(request,'about.html',)
   

def services(request):
    return render(request,'services.html',)
    

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        contact = Contact(name=name,email=email,phone=phone,date=datetime.today())
        contact.save()
        messages.success(request, 'Your massage has been send')
    return render(request,'contact.html')
   
