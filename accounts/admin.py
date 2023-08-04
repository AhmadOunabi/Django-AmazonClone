from django.contrib import admin
from .models import User, Profile, Phones, Address
# Register your models here.
admin.site.register(Profile)
admin.site.register(Phones)
admin.site.register(Address)