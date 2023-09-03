from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='company',null=True,blank=True)
    call_us = models.CharField(max_length=20,blank=True,null=True)
    email_us = models.EmailField(null=True,blank=True)
    address = models.CharField(max_length=200 , null=True,blank=True)
    subtitle = models.CharField(max_length=200,null=True,blank=True)
    emails = models.TextField(max_length=200, null=True,blank=True)
    phones = models.TextField(max_length=200, null=True,blank=True)
    fb_link = models.URLField(null=True,blank=True)
    twitter_link = models.URLField(null=True,blank=True)
    youtube_link = models.URLField(null=True,blank=True)
    android_app = models.URLField(null=True,blank=True)
    ios_app = models.URLField(null=True,blank=True)
    
    
    
    def __str__(self):
        return self.name
    
    class DeliveryFee(models.Model):
        fee=models.FloatField()
        
        def __str__(self):
            return self.fee