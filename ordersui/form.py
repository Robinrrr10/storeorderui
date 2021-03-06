from django import forms

class OrderForm(forms.Form):
    cus = forms.CharField(required=False)
    productName = forms.CharField(required=False)
    eachPrice = forms.CharField(required=False)
    quantity = forms.CharField(required=False)
    price = forms.CharField(required=False)