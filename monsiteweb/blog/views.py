from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Bonjour,monde ! Ceci est ma premiere page Django")
