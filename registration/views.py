from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html')


def logout_page(request):
    logout(request)
    return HttpResponseRedirect("/")

