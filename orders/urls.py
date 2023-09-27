from django.urls import path
from .api import CartDetailCreateAPI

urlpatterns = [
    path('api/<str:username>/cart',CartDetailCreateAPI),
]
