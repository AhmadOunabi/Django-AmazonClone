from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from functions.code_generator import generate_code
from accounts.models import Address
from products.models import Product


# Create your models here.

ORDER_STATUS=(
    ('Recieved','Recieved'),
    ('Processed','Processed'),
    ('Shipped','Shipped'),
    ('Delivered','Delivered'),
)



class Order(models.Model):
    user = models.ForeignKey(User,related_name='order_owner',on_delete=models.SET_NULL,null=True,blank=True)
    status = models.CharField(max_length=12 , choices=ORDER_STATUS)
    code = models.CharField(max_length=10,default=generate_code)
    order_time = models.DateTimeField(default=timezone.now)
    delivery_time = models.DateTimeField(null=True,blank=True)
    total = models.FloatField()
    delivery_location = models.ForeignKey(Address , related_name='order_address',on_delete=models.SET_NULL,null=True,blank=True)
    
    def __str__(self):
        return str(self.user)
    

class OrderDetail(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name='order_detail')
    product=models.ForeignKey(Product,on_delete=models.SET_NULL,related_name='orderdetail_product')
    quantity=models.IntegerField()
    price=models.FloatField()

