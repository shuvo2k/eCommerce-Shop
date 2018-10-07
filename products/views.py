from django.shortcuts import render, get_object_or_404
from django.views import View
from . models import product 
from django.http import Http404



#CLASS based product view 
class ProductListView(View):

	template_name = 'product/list.html'
	
	def get(self, request):
		queryset_all = product.objects.all()
		queryset_popular = product.objects.popular()

		context = {
			'products':queryset_all,
			'popular':queryset_popular,
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

		context = {
			'detail':queryset,
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