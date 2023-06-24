from django.db import models
from taggit.managers import TaggableManager
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=120,verbose_name=_('Name'))
    price= models.FloatField(_('price'))
    quantity= models.IntegerField(_('quantity'))
    description= models.TextField(_('description'),max_length=1000)
    tags = TaggableManager(_('tags'))
    brand= models.ForeignKey('Brand', related_name='product_brand',on_delete=models.SET_NULL,null=True,blank=True,verbose_name=_('brand'))
    sku=models.IntegerField(_('sku'))
    subtitle= models.TextField(_('subtitle'),max_length=500)
    def __str__(self) :
        return self.name
    
class Brand(models.Model):
    name= models.CharField(_('name'),max_length=120)
    image=models.ImageField(_('image'),upload_to='brands')
    def __str__(self) :
        return self.name
    
class Review(models.Model):
    user=models.ForeignKey(User,related_name='review_author',on_delete=models.SET_NULL,null=True,blank=True,verbose_name=_('user'))
    review=models.TextField(_('review'),max_length=500)
    rate=models.IntegerField(_('rate'))
    create_date=models.DateTimeField(_('create_date'),default=timezone.now)
    product=models.ForeignKey(Product,related_name='product_review', on_delete=models.CASCADE)
    
    def __str__(self) :
        return str(self.user)

class ProductImages(models.Model):
    Product=models.ForeignKey(Product,related_name='product_images', on_delete=models.CASCADE)
    image=models.ImageField(upload_to='product_images')