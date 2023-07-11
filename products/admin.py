from django.contrib import admin
from products.models import Product,Brand,Review,ProductImages
from django_summernote.admin import SummernoteModelAdmin

class InlineProductImage(admin.TabularInline):
    model = ProductImages
    extra = 3

class ProductAdmin(SummernoteModelAdmin):
    list_display= ['name','brand','quantity','price']
    list_filter=['brand','quantity','price']
    inlines=[InlineProductImage]
    summernote_fields = '__all__'
    
# Register your models here.
admin.site.register(Product,ProductAdmin)
admin.site.register(Brand)
admin.site.register(Review)
admin.site.register(ProductImages)