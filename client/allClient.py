import requests
from django.http import HttpResponse

def callApi():
    print("came inside client call api")
    response = requests.get("https://reqres.in/api/users?page=2")
    print(response.content)
    return response