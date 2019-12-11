from django.urls import path
from .views import homePageView

urlpatterns = [
    path('',homePageView, name='home') #ako user requesta homepage (''), onda koristi view koji se zove homePageView
]