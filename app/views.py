from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Naveen(request):
    return HttpResponse('<marquee><h2>Naveen is good boy</h2></marquee>')