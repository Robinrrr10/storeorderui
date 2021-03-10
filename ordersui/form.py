from django import forms

class OrderForm(forms.Form):
    cus = forms.CharField(required=False)
    prd = forms.CharField(required=False)
    eachPrice = forms.CharField(required=False)
    qty = forms.CharField(required=False)
    price = forms.CharField(required=False)