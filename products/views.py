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
    template_name = 'products/brand_list.html'

class BrandDetail(generic.ListView):
    model = Product
    paginate_by=10
    template_name = 'products/brand_detail.html'
    
    
    #To get the List of the Products that have this Brand name 
    def get_queryset(self,*args,**kwargs):
        brand  = Brand.objects.get(slug=self.kwargs['slug'])
        queryset = Product.objects.filter(brand=brand)
        return queryset
    
    
    #To get the Brand Infos 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["brand"] = Brand.objects.get(slug=self.kwargs['slug'])
        return context