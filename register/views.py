from django.shortcuts import render
from django.http import HttpResponse

def registerView(request):
    return render(request, 'register.html')