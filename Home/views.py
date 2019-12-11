from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def homePageView(request):
    return HttpResponse('Zdravo druže!') #kada se pozove funkcija homePageView vrati tekst
