from django.db import models
from django.contrib.auth.models import User
from shop.models import Product
from django.db.models.signals import post_save
# Create your models here.


class ShippingAddress(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    shipping_full_name=models.CharField(max_length=250)
    shipping_email=models.CharField(max_length=300)
    shipping_address1=models.CharField(max_length=250,blank=True)
    shipping_city=models.CharField(max_length=25,blank=True)
    shipping_state=models.CharField(max_length=25,blank=True,null=True)
    shipping_zipcode=models.CharField(max_length=25,blank=True,null=True)
    shipping_country=models.CharField(max_length=25,default="IRAN")

    class Meta:
        verbose_name_plural='Shipping Address'

    def __str__(self):
        return f'Shipping Address From - {str(self.shipping_full_name)}'
    
def create_shipping(sender,instance,created,**kwargs):
    if created:
        user_shipping=ShippingAddress(user=instance)
        user_shipping.save()
post_save.connect(create_shipping,sender=User)


    



class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    full_name=models.CharField(max_length=250)
    email=models.EmailField(max_length=300)
    shipping_address=models.TextField(max_length=150000)
    amount_paid=models.DecimalField(decimal_places=0,max_digits=12)
    date_ordered=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Order - {str(self.id)}'


class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE,null=True)
    Products=models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    quantity=models.PositiveIntegerField(default=1)
    price=models.DecimalField(decimal_places=0,max_digits=12)


    def __str__(self):
        return f'Order Item -{str(self.id)}'
