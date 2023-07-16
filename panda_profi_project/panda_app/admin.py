from django.contrib import admin

# Register your models here.
from .models import Category, Product, PaintingChamber, Vimes, ProductPhoto

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(PaintingChamber)
admin.site.register(Vimes)
admin.site.register(ProductPhoto)
