from django.shortcuts import render
from products.models import product, writer
from django.db.models import Q
from django.views.generic import ListView

# Create your views here.

def test(request):
	
	query = request.GET.get('q')
	'''
	#queryset from ProductModelManager [products.models]
	if query:
		return product.objects.search(query)
	'''
	#manual quey set 
	all_products = product.objects.all()
	if query:
		all_products = all_products.filter(
			Q(title__icontains=query) |
            Q(writer__name__icontains=query)
              )
            
	context = {
		"all":all_products
	}
	return render(request, 'product_books.html', context)

'''
class SearchProduct(ListView):
	template_name = "product_books.html"

	def get_queryset(self, *args, **kwargs):
		request = self.request
		print(request.GET.get('q'))
		return product.objects.filter(slug__icontains='books')
'''