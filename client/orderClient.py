import os
from django.conf import settings

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