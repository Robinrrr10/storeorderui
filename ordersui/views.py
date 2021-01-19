from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def home(request):
    return HttpResponse("Hello world")

def hm(request):
    nname = "Ram"
    return render(request, 'index.html', { 'name': nname})

def signin(request):
    return render(request, 'sign.html')

@csrf_exempt
def login(request):
    print("came inside..")
    if request.method == 'POST':
        return render(request, 'home.html')
    else:
        return HttpResponse("invalid request")