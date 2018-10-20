from django.contrib import admin
from . models import Order, OrderItem




class OrderItemInlineModel(admin.TabularInline):
	model = OrderItem
	raw_id_fields = ['product']
    #search_fields = ["__str__",]
    

class OrderModel(admin.ModelAdmin):
    list_display = ["__str__","status", "shipping_total", "total"]
    search_fields = ["__str__",]
    inlines = [OrderItemInlineModel]

   
    class Meta:
        model = Order

admin.site.register(Order, OrderModel)

