from django.shortcuts import render
from django.http import HttpResponse

def home_view(request, *args, **kargs):
    return render(request, 'home.html',{})
