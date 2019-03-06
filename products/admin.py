from django.contrib import admin
from .models import product
from .models import offer

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


admin.site.register(product, ProductAdmin)


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')


admin.site.register(offer, OfferAdmin)