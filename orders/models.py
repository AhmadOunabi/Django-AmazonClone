from django.db import models
from django.contrib.auth.models import User

# Create your models here.

ORDER_STATUS=(
    ('Recieved','Recieved'),
    ('Processed','Processed'),
    ('Shipped','Shipped'),
    ('Delivered','Delivered'),
)

class Orders(models.Model):
    user=models.ForeignKey(User, related_name='order_owner',on_delete=models.SET_NULL,null=True)
    status= models.CharField(max_length=12, choices=ORDER_STATUS)
    