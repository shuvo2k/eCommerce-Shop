from django.shortcuts import render, redirect
from . models import Cart 
from products.models import product 

'''
def cart_create(user=None):
	cart_obj = Cart.objects.create(user=None)
	print('New cart creted')
	return cart_obj
'''


def cart_home(request):
	cart_obj, new_obj = Cart.objects.new_or_get(request)

	#product = cart_obj.products.all()
	#cart_id = request.session.get('cart_id', None)
	'''
	#print(request.session)
	#print(dir(request.session))
	#key = request.session.session_key
	#print(key)
	#we can access this session dictionary in any page like localhost:8000
	#request.session['first_name'] = "shuvo"
	#del request.session['cart_id']
	#cart_id = request.session.get('cart_id', None)

	#if cart_id is None: #and isinstance(cart_id, int):
		#print('create new cart')
		#cart_obj = Cart.objects.create(user=None)
		#request.session['cart_id'] = cart_obj.id
		#print('New cart created')
	qs = Cart.objects.filter(id=cart_id)
	if qs.count() == 1:
		print('cart id exists')
		cart_obj = qs.first()
		if request.user.is_authenticated and cart_obj.user is None:
			cart_obj.user = request.user
			cart_obj.save()
	else:
		#cart_obj=cart_create(request.user)
		cart_obj = Cart.objects.new(user=request.user)
		request.session['cart_id'] = cart_obj.id
	'''


	context = {
		'cart':cart_obj
	}

	return render(request, 'carts/cart_home.html', context)


def cart_update(request):
	print(request.POST)
	product_id = request.POST.get('product_id')
	if product_id is not None:
		try:
			product_obj = product.objects.get(id=product_id)
		except product.DoesNotExist:
			print("show message to usr, product is gone")
			return redirect("cart:home")

		cart_obj, new_obj = Cart.objects.new_or_get(request)
		#print('cart')
		#print(cart_obj.products.all())
		if product_obj in cart_obj.products.all():
		#print('products removes')
			cart_obj.products.remove(product_obj)
		else:
			#print('product added')
			cart_obj.products.add(product_obj)
		request.session['cart_items'] = cart_obj.products.count()
		request.session['cart_total'] = int(cart_obj.total)
	#cart_obj.products.add(product_id)
	#cart_obj.products.remove(obj)
	#return redirect(product_obj.get_absolute_url())

	return redirect("cart:home")

