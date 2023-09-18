from django.urls import path
from .views import ProductList , ProductDetail, BrandList, BrandDetail
from .api import ProductListAPI,ProductDetailAPI, BrandListAPI, BrandDetailAPI


urlpatterns = [
    path('brands' , BrandList.as_view()),
    path('brands/<slug:slug>' , BrandDetail.as_view()),
    path('',ProductList.as_view()),
    path('<slug:slug>', ProductDetail.as_view()),
    
    
    #api
    path('api/list',ProductListAPI.as_view()),
    path('api/detail/<int:pk>', ProductDetailAPI.as_view()),
    
    
    path('brands/api/list',BrandListAPI.as_view()),
    path('brands/api/detail/<int:pk>', BrandDetailAPI.as_view()),
    
]   
