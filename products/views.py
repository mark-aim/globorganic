from django.shortcuts import render

# Create your views here.
def index(request):
    param = "Hello There!"
    context = {
        'param': param,
    }
    return render(request, 'products/index.html', context);