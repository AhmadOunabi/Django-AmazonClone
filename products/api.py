from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import ProductListSerializer, ProductDetailSerializer, BrandListSerializer, BrandDetailSerializer
from .models import Product, Brand
from rest_framework import generics


# @api_view(['GET'])
# def product_list_api(request):
#     products=Product.objects.all()         # List
#     data=ProductSerializer(products,many=True,context={'request':request}).data  #json     context is to return the URL of Media 'Images'
#     return Response({'products': data})


# @api_view(['GET'])
# def product_detail_api(request, product_id):
#     product=Product.objects.get(id=product_id)
#     data=ProductSerializer(product,context={'request':request}).data            #json     context is to return the URL of Media 'Images'
#     return Response({'product': data})


class ProductListAPI(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    permission_classes = [IsAuthenticated]
    
    



    
class ProductDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    permission_classes = [IsAuthenticated]




class BrandListAPI(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandListSerializer



class BrandDetailAPI(generics.RetrieveAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandDetailSerializer