from django.urls import path
from . import views 



urlpatterns = [
	#class based url
	path('', views.ProductListView.as_view(), name='product_list'),
	path('detail/<slug:slug>', views.ProductDetailView.as_view())

	]
