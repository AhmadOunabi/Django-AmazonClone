from rest_framework import serializers
from .models import Product , Brand, Review, ProductImages
from django.db.models.aggregates import Avg




class BrandListSerializer(serializers.ModelSerializer):
    class Meta:
        model= Brand
        fields='__all__'


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model= ProductImages
        fields= ['image']


 
class ProductListSerializer(serializers.ModelSerializer):
    brand=serializers.StringRelatedField()                  # To show the brand name instead of the Brand Number 
    review_count = serializers.SerializerMethodField()
    avg_rate= serializers.SerializerMethodField()
    class Meta:
        model= Product
        fields= '__all__'
    
    
    def get_review_count(self,product):
        reviews_count=product.product_review.all().count()
        return reviews_count
    
    def get_avg_rate(self,product):
        avg=product.product_review.aggregate(rate_avg=Avg('rate'))
        return(avg['rate_avg']) if avg['rate_avg'] else 0
        


class ProductReviewSerializer(serializers.ModelSerializer):
    user=serializers.StringRelatedField()                     # To show the USER name instead of the Brand Number
    class Meta:
        model= Review
        fields=['user','review','rate']

class ProductDetailSerializer(serializers.ModelSerializer):
    image=ProductImageSerializer(source='product_images', many=True)
    reviews=ProductReviewSerializer(source='product_review', many=True)
    brand=serializers.StringRelatedField()                     # To show the brand name instead of the Brand Number 
    class Meta:
        model= Product
        fields= '__all__'




class BrandDetailSerializer(serializers.ModelSerializer):
    products=ProductListSerializer(source='product_brand',many=True)
    class Meta:
        model= Brand
        fields='__all__'