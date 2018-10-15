from django.urls import path
from . import views 


app_name = 'products'


urlpatterns = [
	#class based url
	path('', views.ProductListView.as_view(), name='product_list'),
	path('book/detail/<slug:slug>', views.ProductDetailView.as_view(), name='details'),
	path('books/category/<slug:slug>', views.GetItembyCategory.as_view(), name='item_by_category'),
	path('books/popular', views.PopularBooks.as_view(), name='popular_books'),
	path('books/categories', views.BooksByCategory.as_view(), name='category'),
	path('books/category/writers', views.BooksByWriters.as_view(), name='writers'),
	path('books/category/publishers', views.BooksByPublishers.as_view(), name='publishers'),
	path('toys', views.AllToys.as_view(), name='toys'),
	path('blog', views.Blog.as_view(), name='blog'),
	



	]
