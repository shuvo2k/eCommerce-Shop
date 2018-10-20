from django.shortcuts import render, get_object_or_404
from django.views import View
from . models import product, writer, publisher, category 
from django.http import Http404

from carts.models import Cart

#CLASS based product view 
class ProductListView(View):

	template_name = 'product/list.html'
	
	def get(self, request):
		queryset_all = product.objects.all()
		queryset_popular = product.objects.popular()
		
		writer_query = writer.objects.all()
		publisher_query = publisher.objects.all()
		category_query = category.objects.all()


		context = {
			'products':queryset_all,
			'popular':queryset_popular,
			'writer_query':writer_query,
			'publisher_query':publisher_query,
			'category_query':category_query
		}
		return render(request, self.template_name, context)
	
	
	'''
	def get_context_data(self, *args, **kwargs):
		context = super(ProductListView, self).get_context_data(*args, **kwargs)
		print(context)
		return context

	'''

'''
#function based product view 
def product_list(request):
	queryset = product.objects.all()
	context = {
		'products':queryset,
	}
	return render(request, 'product/list.html', context)


#function based detail view
def product_detail(request, id):
	queryset = get_object_or_404(id=id)
	context = {

	}
	return render(request, 'product/product_detail.html', context)
 '''
class ProductPopularListView(View):
	template_name = 'product/list.html'



class ProductPopularDetailView(View):
	template_name = 'product/list.html'





#class based detail view
class ProductDetailView(View):
	template_name = 'product/detail.html'
	def get(self, request, slug):
		#queryset = get_object_or_404(product, id=id)
		queryset = product.objects.get(slug=slug)
		print(queryset)
		print("slug" + slug)
		if queryset is None:
			raise Http404("Product Does Not Exists.")

		#cart 
		cart_obj, new_obj = Cart.objects.new_or_get(request)

		context = {
			'query':queryset,
			'cart_obj':cart_obj,
		}
		return render(request, self.template_name, context)

'''
	def get_object(self, *args, **kwargs):
		request = self.request
		pk = self.kwargs.get('id')
		queryset = product.objects.get_by_id(id)
		if queryset is None:
			raise Http404('Product Does not Exists.')
		return None

'''


class GetItembyCategory(View):
	def get(self, request, slug):
		pass



class BooksByCategory(View):
	def get(self, request):
		pass


class BooksByWriters(View):
	def get(self, request):
		pass


class BooksByPublishers(View):
	def get(self, request):
		pass







class PopularBooks(View):
	def get(self, request):
		pass


class AllToys(View):
	def get(self, request):
		pass

class Blog(View):
	def get(self, request):
		pass
"""
class Login(View):
	def get(self, request):
		pass

class Logout(View):
	def get(self, request):
		pass

"""