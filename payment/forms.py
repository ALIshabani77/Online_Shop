from django import forms
from .models import ShippingAddress

class ShippingForm(forms.ModelForm):
    shipping_full_name=forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'نام'}),required=True)
    shipping_email=forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'ایمیل'}),required=True)
    shipping_address1=forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'آدرس'}),required=True)
    shipping_city=forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'شهر'}),required=True)
    shipping_state=forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'استان'}),required=False)
    shipping_zipcode=forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'کدپستی'}),required=False)
    shipping_country=forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'کشور'}),required=True)



    class Meta:
        model=ShippingAddress
        fields=[
            'shipping_full_name',
            'shipping_email',
            'shipping_address1',
            'shipping_city',
            'shipping_state',
            'shipping_zipcode',
            'shipping_country',
        ]

        exclude=['user',]

            
            
class PaymentForm(forms.Form):
    card_number=forms.CharField(max_length=16,label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'شماره کارت'}),required=True)
    card_exp_date=forms.CharField(max_length=4,label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'تاریخ انقضا'}),required=True)
    card_cvv_numer=forms.CharField(max_length=4,label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'(cvv2)شماره شناسایی دوم'}),required=True)
    card_password=forms.CharField(max_length=6,label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'رمز دوم'}),required=True)
    card_zipcode=forms.CharField(max_length=10,label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'آدرس کدپستی'}),required=True)

            
            
            
            