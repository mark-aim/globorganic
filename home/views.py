from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    param = "Hello There!"
    context = {
        'param': param,
    }
    return render(request, 'home/index.html', context)