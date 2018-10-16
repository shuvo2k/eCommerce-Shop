from django.shortcuts import render
from . models import Cart 

'''
def cart_create(user=None):
	cart_obj = Cart.objects.create(user=None)
	print('New cart creted')
	return cart_obj
'''


def cart_home(request):
	cart_obj = Cart.objects.new_or_get(request)
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

	}

	return render(request, 'carts/cart_home.html', context)