from django.urls import path
from .views import ProductList , ProductDetail, BrandList, BrandDetail
from .api import product_list_api,product_detail_api


urlpatterns = [
    path('brands' , BrandList.as_view()),
    path('brands/<slug:slug>' , BrandDetail.as_view()),
    path('',ProductList.as_view()),
    path('<slug:slug>', ProductDetail.as_view()),
    
    
    #api
    path('api/list',product_list_api),
    path('api/detail/<int:product_id>', product_detail_api)
    
    
    
    
    
]   
