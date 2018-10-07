import random
import string
from django.utils.text import slugify
import goslate

def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))




def unique_slug_generator(instance, new_slug=None):
	gs = goslate.Goslate()
	slug = slugify(gs.translate(instance.title, 'en'))
	
	print('slug' + slug)


	Klass = instance.__class__
	qs_exists = Klass.objects.filter(slug=slug).exists()
	#print(qs_exists)
	if qs_exists:
		new_slug = "{slug}-{randstr}".nnformat(
			slug=slug, 
			randstr=random_string_generator(size=4)
			)
		return unique_slug_generator(instance, new_slug=new_slug)
	return slug


