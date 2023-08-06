from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.

class Profile(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    image= models.ImageField(upload_to='accounts', default='user-icon-human-person-sign-vector-20444565.jpg')
    
    def __str__(self):
        return str(self.user)
    
    # Create new Profile for each new User using Signals.
    @receiver(post_save, sender=User)
    def create_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
    

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