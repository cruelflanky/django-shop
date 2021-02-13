from django import forms
from .models import *

class CheckoutForm(forms.Form):
	name = forms.CharField(required=True)
	email = forms.EmailField(required=False)
	phone = forms.CharField(required=True)
	address = forms.CharField(required=False)
	comment = forms.CharField(required=False)
