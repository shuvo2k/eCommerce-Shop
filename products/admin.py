from django.contrib import admin
from . models import product, category, publisher, writer



class productModel(admin.ModelAdmin):
    list_display = ["__str__", "writer","category", "publisher", "price"]
    search_fields = ["__str__", "category", "publisher", "writer"]
    class Meta:
        model = product

admin.site.register(product, productModel)


class categoryModel(admin.ModelAdmin):
    list_display = ["__str__"]
    search_fields = ["__str__"]
    class Meta:
        model = category

admin.site.register(category, categoryModel)



class publisherModel(admin.ModelAdmin):
    list_display = ["__str__"]
    search_fields = ["__str__"]
    class Meta:
        model = publisher

admin.site.register(publisher, publisherModel)


class writerModel(admin.ModelAdmin):
    list_display = ["__str__"]
    search_fields = ["__str__"]
    class Meta:
        model = writer

admin.site.register(writer, writerModel)