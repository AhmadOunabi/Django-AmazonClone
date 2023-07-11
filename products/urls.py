from django.urls import path
from products.views import ProductList , ProductDetail


urlpatterns = [
    path('',ProductList.as_view()),
    path('<slug:slug>',ProductDetail.as_view()),
]
