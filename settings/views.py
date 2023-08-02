from django.shortcuts import render
from .models import Company
# Create your views here.


def home(request):
    
    return render(request,'settings/home.html')