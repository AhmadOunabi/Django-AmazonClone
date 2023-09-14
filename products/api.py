from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer
from .models import Product
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
    serializer_class = ProductSerializer
    
    



    
class ProductDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer