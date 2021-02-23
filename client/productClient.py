import requests
from django.http import HttpResponse

def getAllProducts():
    print("Call all products api")
    response = requests.get("http://localhost:8080/productmanagement/v1/products/all")
    print(response.content)
    return response

