import requests
import os
from django.http import HttpResponse
from django.conf import settings

class ProductClient:
    global host
    def __init__(self):
        global host
        if os.getenv("PRODUCT_HOST") != "":
            host = os.getenv("PRODUCT_HOST")
        elif settings.PRODUCT_HOST == "":
            host = "http://google.com"
        else:
            host = settings.PRODUCT_HOST

    def getAllProducts(self):
        global host
        print("Call all products api")
        fullUrl =  host + "/productmanagement/v1/products/all"
        print("url is:" + fullUrl)
        response = requests.get(fullUrl)
        print(response.content)
        return response

