from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def panda(request):
    return HttpResponse(�"Nastya Sonzeva - Zayka")
