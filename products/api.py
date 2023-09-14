from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer
from .models import Product


@api_view(['GET'])
def product_list_api(request):
    products=Product.objects.all()         # List
    data=ProductSerializer(products,many=True).data  # json
    return Response({'products': data})






