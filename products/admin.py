from django.contrib import admin
from products.models import Product,Brand,Review,ProductImages


class InlineProductImage(admin.TabularInline):
    model = ProductImages

class ProductAdmin(admin.ModelAdmin):
    list_display= ['name','brand','quantity','price']
    list_filter=['brand','quantity','price']
    inlines=[InlineProductImage]
    
# Register your models here.
admin.site.register(Product,ProductAdmin)
admin.site.register(Brand)
admin.site.register(Review)
admin.site.register(ProductImages)