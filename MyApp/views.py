from pyexpat.errors import messages
from django.shortcuts import render
# from MyProject.MyApp.models import userdata
from . import models

# Create your views here.
def index(request):
    return render(request,'index.html')
def home(request):
    return render(request,'home.html')
def login(request):
    if models.userdata.objects.filter(
        username = request.POST['username'],password = request.POST['password']
    ).exists():
       messages.error(request,"login successful...", extra_tags="login_successful")
       return render (request,'index.html')

    else:
        return render(request,'index.html')
def home(request):
     
    return render(request, 'home.html')  
    


