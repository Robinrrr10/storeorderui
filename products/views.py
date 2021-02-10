from django.shortcuts import render
from django.http import HttpResponse
from client import allClient
import json

# Create your views here.
def product(request):
    return HttpResponse("This is product page")

def allProducts(request):
    print("came inside all product")
    apiResponse = allClient.callApi()
    jres = apiResponse.content
    values = json.loads(jres)
    va = values["data"]
    return render(request, 'product.html', { 'pro': va })


