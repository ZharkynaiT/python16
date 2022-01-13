from django.contrib import admin

from product.models import Product, ProductReview

admin.site.register(Product)

admin.site.register(ProductReview)
