from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def telugu(request):
    return HttpResponse('This is our Telugu Movies')