from django.contrib import admin

from .models import Stock, Product, StockProduct

admin.site.register(Stock)
admin.site.register(Product)
admin.site.register(StockProduct)