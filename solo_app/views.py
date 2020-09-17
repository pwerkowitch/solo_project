from django.shortcuts import render, HttpResponse
from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages
import bcrypt
def index(request):
    
    return render(request,'home.html')

# Create your views here.
def review(request):
    return render (request,'review.html')

def travel(request):
    request.session['place'] = request.POST['address']
    return redirect('/')