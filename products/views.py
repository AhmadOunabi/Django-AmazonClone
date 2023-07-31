from django.shortcuts import render
from django.views import generic
from products.models import Product,Brand
# Create your views here.

class ProductList(generic.ListView):
    model = Product
    paginate_by=15

class ProductDetail(generic.DetailView):
    model = Product


class BrandList(generic.ListView):
    model=Brand
    paginate_by=10


class BrandDetail(generic.DetailView):
    model = Brand