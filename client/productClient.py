import requests
from django.http import HttpResponse
from django.conf import settings

class ProductClient:
    host = ""
    def __init__(self):
        global host
        if settings.PRODUCT_HOST == "":
            host = "http://google.com"
        else:
            host = settings.PRODUCT_HOST

    def getAllProducts(self):
        global host
        print("Call all products api")
        response = requests.get( host + "/productmanagement/v1/products/all")
        print(response.content)
        return response

