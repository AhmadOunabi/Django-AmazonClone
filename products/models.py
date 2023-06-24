from django.db import models
from taggit.managers import TaggableManager
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=120)
    price= models.FloatField()
    quantity= models.IntegerField()
    description= models.TextField(max_length=1000)
    tags = TaggableManager()
    brand= models.ForeignKey('Brand', related_name='product_brand',on_delete=models.SET_NULL,null=True,blank=True)
    sku=models.IntegerField()
    subtitle= models.TextField(max_length=500)
    
    def __str__(self) :
        return self.name
    
class Brand(models.Model):
    name= models.CharField(max_length=120)
    image=models.ImageField(upload_to='brands')

    def __str__(self) :
        return self.name
    
class Review(models.Model):
    user=models.ForeignKey(User,related_name='review_author',on_delete=models.SET_NULL,null=True,blank=True)
    review=models.TextField(max_length=500)
    rate=models.IntegerField()
    create_date=models.DateTimeField(default=timezone.now)
    product=models.ForeignKey(Product,related_name='product_review', on_delete=models.CASCADE)
    
    def __str__(self) :
        return self.user