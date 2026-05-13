from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def rcb_captain(request):
    return HttpResponse('<h1>kohli</h1>')