import os , django
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from faker import Faker
from products.models import Product, Brand, ProductImages
import random

def seed_brand(n):
    fake= Faker()
    images= ['1.png', '2.png', '3.png', '4.png','5.jpg','6.png','7.jpg']
    for i in range(n):
        Brand.objects.create(
            name= fake.name(),
            image= f"brands/{images[random.randint(0,6)]}"
        )
        

def seed_products(n):
    fake=Faker()
    flags=['New','Sale','Feature']
    images=['1.png','2.webp','3.jpg','4.jpg','5.png','6.png','7.webp','8.avif','9.avif']
    for i in range(n):
        Product.objects.create(
            name=fake.name(),
            price=round(random.uniform(20.99,999.99),2),
            quantity=random.randint(1,100),
            description=fake.text(max_nb_chars=1000),
            subtitle=fake.text(max_nb_chars=500),
            sku=random.randint(100,100000),
            brand=Brand.objects.get(id=random.randint(104,202)),
            image=f'products/{images[random.randint(0,8)]}',
            flag= flags[random.randint(0,len(flags)-1)],
        )

def seed_product_images():
    images=['1.jpg', '2.jpg', '3.jpg', '4.png', '5.webp', '6.avif','7.avif','8.png','9.webp','10.jpg','11.jpg','12.png']
    for i in range(2006,4570):
        for j in range(3):
            ProductImages.objects.create(
                product= Product.objects.get(id=i),
                image= f'product_images/{images[random.randint(0,11)]}'
            )
#seed_brand(100)
#seed_products(2000)
seed_product_images()