from django.urls import path
from .api import CartDetailCreateAPI, OrderListAPI

urlpatterns = [
    
    path('api/<str:username>/list', OrderListAPI.as_view()),
    
    path('api/<str:username>/cart',CartDetailCreateAPI.as_view()),
]
