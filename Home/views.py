from django.shortcuts import render
from django.views.generic import TemplateView #built-in TemplateView kako bi prikazali template

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'