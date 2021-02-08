from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def product(request):
    return HttpResponse("This is product page")

def allProducts(request):
    return render(request, 'product.html')


