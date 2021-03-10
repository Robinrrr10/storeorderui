import json
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
#from client.orderClient import
from . import form
from entities.order import OrderDetail
from client.orderClient import OrderClient
from client.productClient import ProductClient

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
    or1 = OrderClient()
    if request.method == 'POST':
        #Save order detail in db and then give success
        orderForm = form.OrderForm(request.POST)
        if orderForm.is_valid():
            customer = orderForm.cleaned_data['cus']
            productname = orderForm.cleaned_data['prd']
            perPrice = orderForm.cleaned_data['eachPrice']
            noOfProduct = orderForm.cleaned_data['qty']
            value = orderForm.cleaned_data['price']
            print('customer:' + customer)
            print('productname:' + productname)
            print('perPrice:' + perPrice)
            print('noOfProduct:' + noOfProduct)
            print('value:' + value)
            store = "23"
            orderDetail = OrderDetail()
            orderDetail.storeId = store
            orderDetail.productId = 317
            orderDetail.productName = productname
            orderDetail.eachPrice = perPrice
            orderDetail.quantity = noOfProduct
            orderDetail.totalPrice = value
            print('it has all values')
            response = or1.createOrder(store, orderDetail)
            jres = response.content
            values = json.loads(jres)
            status = values["status"]
            return render(request, 'orderCreateSuccess.html', { 'status': status })
        else:
             print('for is not value')
             return HttpResponse("Something went wrong")
    else:
        return HttpResponse("invalid order create request")