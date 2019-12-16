from django.shortcuts import render
from django.http import HttpResponse


def loginView(request):
    return render(request, 'login.html')