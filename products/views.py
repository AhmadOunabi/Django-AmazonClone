from django.shortcuts import render
from django.views import generic
from products.models import Product,Brand,ProductImages,Review
# Create your views here.

class ProductList(generic.ListView):
    model = Product
    paginate_by=15

class ProductDetail(generic.DetailView):
    model = Product