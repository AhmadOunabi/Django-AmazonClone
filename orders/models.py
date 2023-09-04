from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from functions.code_generator import generate_code
from accounts.models import Address
from products.models import Product
import datetime

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
    product=models.ForeignKey(Product,on_delete=models.SET_NULL,related_name='orderdetail_product',null=True,blank=True)
    quantity=models.IntegerField()
    price=models.FloatField()
    def __str__(self):
        return str(self.order)


CART_STATUS=(
    ('Inprogress','Inprogress'),
    ('Completed','Completed'),
)

class Cart(models.Model):
    user=models.ForeignKey(User,related_name='cart_owner',on_delete=models.SET_NULL,null=True,blank=True)
    status=models.CharField(max_length=20,choices=CART_STATUS)
    def __str__(self):
        return str(self.user)


class CartDetail(models.Model):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE,related_name='cart_detail')
    product= models.ForeignKey(Product,related_name='cartdetail_product',on_delete=models.SET_NULL,null=True,blank=True)
    quantity=models.IntegerField()
    total=models.FloatField(null=True,blank=True)
    
    def save(self,*args,**kwargs):
        self.total=self.quantity * self.product.price
        super(CartDetail,self).save(*args,**kwargs)
        
    def __str__(self):
        return str(self.product)

class Coupons(models.Model):
    code = models.CharField(max_length=20)
    start_date=models.DateTimeField(default=timezone.now)
    end_date=models.DateTimeField(default=timezone.now, null=True,blank=True)
    discount=models.FloatField()
    quantity=models.IntegerField()
    
    def save(self,*args,**kwargs):
        self.end_date=self.start_date + datetime.timedelta(days=7)
        super(Coupons,self).save(*args,**kwargs)
    
    def __str__(self):
        return str(self.code)