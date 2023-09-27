from rest_framework import serializers
from .models import Cart,CartDetail,Order,OrderDetail,Coupons


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model=CartDetail
        fields='__all__'

class OrderListSerializer(serializers.ModelSerializer):
    user=serializers.StringRelatedField()     # to show users name instead of ID
    class Meta:
        model = Order
        fields= '__all__'

class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=OrderDetail
        fields='__all__'


