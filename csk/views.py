from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def csk_captain(request):
    return HttpResponse('<h1>ms dhoni</h1>')
