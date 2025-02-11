from django.db import models

# Create your models here.
class AstroClient(models.Model):
	name = models.CharField(max_length=100)	
	email_id = models.CharField(max_length=100)	
	mobile_no = models.CharField(max_length=100)	
	gender = models.CharField(max_length=100)	
	birth_date = models.CharField(max_length=100)	
	birth_time = models.CharField(max_length=100)	
	birth_place = models.CharField(max_length=100)	
	birth_state = models.CharField(max_length=100)	
	birth_country = models.CharField(max_length=100)	
	language = models.CharField(max_length=100)	
	notes = models.CharField(max_length=300)	
	order_id = models.CharField(max_length=100, blank=True)	
	payment_id = models.CharField(max_length=100, blank=True)
	product_id = models.CharField(max_length=100, blank=True)
	payment_amount = models.CharField(max_length=100, blank=True)	
	payment_signature = models.CharField(max_length=100, blank=True)
	paid = models.BooleanField(default=False)

	# def __str__(self):
	# 	return self.name + ' ' + self.mobile_no + ' ' + self.email_id + ' ' + self.order_id + ' ' + self.payment_id + ' ' + self.payment_amount + ' ' + self.payment_signature 


# Create your models here.
class Astro_Booking_Client(models.Model):
	name = models.CharField(max_length=100)	
	email_id = models.CharField(max_length=100)	
	mobile_no = models.CharField(max_length=100)	
	gender = models.CharField(max_length=100)	
	birth_date = models.CharField(max_length=100)	
	birth_time = models.CharField(max_length=100)	
	birth_place = models.CharField(max_length=100)	
	birth_state = models.CharField(max_length=100)	
	birth_country = models.CharField(max_length=100)	
	language = models.CharField(max_length=100)	
	booking_slot = models.CharField(max_length=300)	
	notes = models.CharField(max_length=300)	
	order_id = models.CharField(max_length=100, blank=True)	
	payment_id = models.CharField(max_length=100, blank=True)
	product_id = models.CharField(max_length=100, blank=True)
	payment_amount = models.CharField(max_length=100, blank=True)	
	payment_signature = models.CharField(max_length=100, blank=True)
	paid = models.BooleanField(default=False)

	# def __str__(self):
	# 	return self.name + ' ' + self.mobile_no + ' ' + self.email_id + ' ' + self.order_id + ' ' + self.payment_id + ' ' + self.payment_amount + ' ' + self.payment_signature 
