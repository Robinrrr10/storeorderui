from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
#from client.orderClient import
from . import form

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

def order(request):
    print("calling order page")
    return render(request, 'order.html')

@csrf_exempt
def createOrder(request):
    print("Creating order")
    if request.method == 'POST':
        #Save order detail in db and then give success
        orderForm = form.OrderForm(request.POST)
        if orderForm.is_valid():
            customer = orderForm.cleaned_data['cus']
            print('customer' + customer)
        else:
             print('for is not value')
        return render(request, 'orderCreateSuccess.html')
    else:
        return HttpResponse("invalid order create request")