from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

def about(request):
    return render(request,'about.html')

def index(request):
    return render(request,'index.html')