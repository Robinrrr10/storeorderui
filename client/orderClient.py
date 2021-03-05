import os
import requests
from django.conf import settings
from entities import order.OrderDetail

class OrderClient:
    global host
    def __int__(self):
        global host
        if os.getenv("ORDER_MANAGEMENT_HOST") != "":
            host = os.getenv("ORDER_MANAGEMENT_HOST")
        elif settings.ORDER_MANAGEMENT_HOST != "":
            host = settings.ORDER_MANAGEMENT_HOST
        else:
            host = "http://google.com"

    def getAllOrders(self, string storeId):
        global host
        print("Get all orders")
        fullUrl = host + "/store/"+storeId+"/order/all"
        response = requests.get(fullUrl)
        print(response.content)
        return response
    
    def createOrder(self, OrderDetail orderDetail):
        global host
        print("Create new order")
        fullUrl = host + "/store/"+storeId+"/order"
        