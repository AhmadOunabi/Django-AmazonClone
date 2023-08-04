from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    image= models.ImageField(upload_to='accounts')
    

PHONE_TYPES = (
    ('Primary','Primary'),
    ('Secondary','Secondary'),
)
class Phones(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_phone')
    type = models.CharField(max_length=50,choices=PHONE_TYPES)
    number = models.CharField(max_length=50)
    


ADDRESS_TYPES=(
    ('Home','Home'),
    ('Office','Office'),
    ('Academy','Academy'),
    ('Business','Business'),
    ('Other','Other'),
)
class Address(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_address')
    type= models.CharField(max_length=50,choices=ADDRESS_TYPES)
    address=models.TextField(max_length=200)