import os
import json
import requests
from django.conf import settings
from entities.order import OrderDetail

class OrderClient:
    global orderhost
    def __init__(self):
        global orderhost
        print("came to constuctor2")
        if os.getenv("ORDER_MANAGEMENT_HOST") != None and os.getenv("ORDER_MANAGEMENT_HOST") != "":
            print(os.getenv("ORDER_MANAGEMENT_HOST"))
            orderhost = os.getenv("ORDER_MANAGEMENT_HOST")
            print("111")
            print(orderhost)
        elif settings.ORDER_MANAGEMENT_HOST != None and settings.ORDER_MANAGEMENT_HOST != "":
            orderhost = settings.ORDER_MANAGEMENT_HOST
            print("112")
        else:
            orderhost = "http://google.com"
            print("113")
        print("host:" + orderhost)

    def getAllOrders(self, storeId):
        global orderhost
        print("Get all orders")
        fullUrl = orderhost + "/store/"+storeId+"/order/all"
        response = requests.get(fullUrl)
        print(response.content)
        return response
    
    def createOrder(self, storeId, orderDetail):
        global orderhost
        print("Create new order")
        jsonStr = json.dumps(orderDetail.__dict__)
        fullUrl = orderhost + "/store/"+storeId+"/order"
        print("url:" + fullUrl)
        print("body:" + jsonStr)
        response = requests.post(fullUrl, data = jsonStr)
        print(response.content)
        return response
        