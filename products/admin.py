from django.contrib import admin
from . models import product



class productModel(admin.ModelAdmin):
    list_display = ["__str__", "price"]
    search_fields = ["__str__",]
    class Meta:
        model = product

admin.site.register(product, productModel)
