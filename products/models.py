import os
from django.db import models
from django.template.defaultfilters import slugify
from django.db.models.signals import pre_save
from .utils import unique_slug_generator
from django.template.defaultfilters import slugify



class publisher(models.Model):
	name = models.CharField(max_length=200, unique=True)

	def __str__(self):
		return self.name



class writer(models.Model):
	name = models.CharField(max_length=200, unique=True)

	def __str__(self):
		return self.name


#imager storage structure
def upload_image_path(instance, filename):
	writer = instance.writer.name
	publisher = instance.publisher.name
	category = instance.category.name
	title = instance.title
	ext = get_filename_ext(filename)
	
	final_filename = '{publisher}-{category}-{writer}-{title}{ext}'.format(publisher=publisher, category=category, writer=writer, title=title, ext=ext)
	#print(final_filename)
	return "{final_filename}".format(publisher=publisher,final_filename=final_filename)



def get_filename_ext(filepath):
	base_name = os.path.basename(filepath)
	name, ext = os.path.splitext(base_name)
	return ext
    



class category(models.Model):
	name = models.CharField(max_length=200, unique=True)
	image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)

	def __str__(self):
		return self.name



#custom queryset manager
class ProductManager(models.Manager):
	def get_by_id(self, id):
		qs = self.get_queryset().filter(id=id)
		if qs.count() == 1:
			return qs.first()
		return None

	def popular(self):
		return self.get_queryset().filter(popular=True)



		
	

class product(models.Model):
	title = models.CharField(max_length=200, unique=True)
	slug = models.SlugField(blank=True, unique=True)
	description = models.TextField()
	previous_price = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)
	price = models.DecimalField(decimal_places=2, max_digits=10)
	image = models.ImageField(upload_to=upload_image_path)
	pdf_image1 = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
	pdf_image2 = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
	popular = models.BooleanField(default=False)
	active = models.BooleanField(default=True)
	new = models.BooleanField(default=False)


	writer = models.ForeignKey(writer, on_delete=models.CASCADE)
	publisher = models.ForeignKey(publisher, on_delete=models.CASCADE)
	category = models.ForeignKey(category, on_delete=models.CASCADE)

	objects = ProductManager()

	def get_absolute_url(self):
		return "/detail/{slug}".format(slug=self.slug)


	def __str__(self):
		return self.title 


	


'''

def product_pre_save_receiver(sender, instance, *args, **kwargs):
	gs = goslate.Goslate()
	instance.slug = slugify(gs.translate(instance.title, 'en'))
	
	print(instance.slug)

pre_save.connect(product_pre_save_receiver, sender=product)

'''


	

