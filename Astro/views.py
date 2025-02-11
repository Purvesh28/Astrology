from django.shortcuts import render
from django.http import HttpResponse,HttpResponseBadRequest
from django.template import loader
import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
# from Astro.forms import AstroClientPayent
from Astro.models import *
from django.http import HttpResponseRedirect
from django.conf import settings
from django.urls import reverse
from django.contrib.auth.models import User 
from django.shortcuts import get_object_or_404
from twilio.rest import Client as Twillio_Client
# import keys

# Create your views here.
razorpay_client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

###### SMS Section

account_sid = 'AC962b6e50d427771f3cae1716a5f6b660'
auth_token = 'f11c43b84cd1c2c0d8f4adea568e0bad'
CC='+91'
client_number = ''
twilio_number = '+18183517905'
target_number = CC+client_number

twilio_client = Twillio_Client(account_sid,auth_token)
# message = twilio_client.messages.create(body="This is a new message from Code", from_=twilio_number, to=target_number)


# print("message::::",message)
# print("message::::",message.body)


##### Product_1 = "Persional Kundali"
booking_slot = ''

amount = 0 
Product_ID = ''

Product_1 = "299"+"00" 
Product_1 = int(Product_1)
Product_1_ID = "P_KUNDALI"

Product_2 = "4001"+"00" 
Product_2 = int(Product_2)
Product_2_ID = "BOOK_CALL"

Product_3 = "6001"+"00" 
Product_3 = int(Product_3)
Product_3_ID = "BOOK_VIDEO_CALL"

Product_4 = "10101"+"00" 
Product_4 = int(Product_4)
Product_4_ID = "BOOK_LIVE_CONSULTATION"

Product_5 = "401"+"00" 
Product_5 = int(Product_5)
Product_5_ID = "P_KUNDALI_2"

Product_6 = "801"+"00" 
Product_6 = int(Product_6)
Product_6_ID = "P_KUNDALI_3"

display_amount = amount/100

applied_GST = 0
gst__ = display_amount*applied_GST
gst = gst__/100

currency = 'INR'

Payment_Success = 0
User_Name = ''

Alert_Message = ''


total_payment = display_amount + gst
print("**********************************")

# table_obj = AstroClient.objects.all
# print("table_obj is ::",table_obj)



def index(request):
	global amount
	global Product_1
	global Product_1_ID
	global Alert_Message
	global display_amount
	global Payment_Success

	context = {}
	# context['razorpay_order_id'] = razorpay_order_id
	context['amount'] = amount
	context['Product_1'] = Product_1
	context['Product_5'] = Product_5
	context['Product_6'] = Product_6
	context['Product_1_ID'] = Product_1_ID
	context['Product_5_ID'] = Product_5_ID
	context['Product_6_ID'] = Product_6_ID
	context['Alert_Message'] = Alert_Message
	context['display_amount'] = display_amount
	context['Payment_Success'] = Payment_Success
	
	
	return render(request, 'index.html',context=context)



def Book_Consultation(request):
	global Product_1
	global Product_2
	global Product_3
	global Product_4
	global Product_5
	global Product_6
	global Product_1_ID
	global Product_2_ID
	global Product_3_ID
	global Product_4_ID
	global Product_5_ID
	global Product_6_ID

	context = {}
	context['Product_1'] = Product_1
	context['Product_2'] = Product_2
	context['Product_3'] = Product_3
	context['Product_4'] = Product_4
	context['Product_5'] = Product_5
	context['Product_6'] = Product_6
	context['Product_1_ID'] = Product_1_ID
	context['Product_2_ID'] = Product_2_ID
	context['Product_3_ID'] = Product_3_ID
	context['Product_4_ID'] = Product_4_ID
	context['Product_5_ID'] = Product_5_ID
	context['Product_6_ID'] = Product_6_ID
	return render(request, 'Book_Consultation.html',context=context)
	




@csrf_exempt
def Get_booking(request):
	global amount
	global gst
	global display_amount
	global Product_ID
	global Product_2_ID
	global Product_3_ID
	global Product_4_ID
	global Product_5_ID
	global Product_6_ID
	global target_number


	if request.method == 'POST':
		print("In payment_capture Function")
		print("payment_details :::::::::: ",request.POST)
		amount = int(request.POST['Product_Price'])
		Product_ID = request.POST['Product_ID']

		display_amount = amount/100
		gst__ = display_amount*applied_GST
		gst = gst__/100



		print("Selected Amount is ::::::",amount)
		print("Selected Product is ::::::",Product_ID)


		if Product_ID == Product_1_ID:
			print("We've Got A Purchasing For Persionalized Kundali ..")
			return HttpResponseRedirect("/Buying_page/")

		if Product_ID == Product_2_ID:
			print("We've Got A Booking For Call Consultation ..")
			return HttpResponseRedirect("/Booking_Page/")

		if Product_ID == Product_3_ID:
			print("We've Got A Booking For Video Call Consultation ..")
			return HttpResponseRedirect("/Booking_Page/")
		
		if Product_ID == Product_4_ID:
			print("We've Got A Booking For Live Consultation ..")
			return HttpResponseRedirect("/Booking_Page/")
		
		if Product_ID == Product_5_ID:
			print("We've Got A Booking For Persionalized Kundali 2 ..")
			return HttpResponseRedirect("/Buying_page/")
		
		if Product_ID == Product_6_ID:
			print("We've Got A Booking For Persionalized Kundali 3 ..")
			return HttpResponseRedirect("/Buying_page/")

		# message = twilio_client.messages.create(body="This is a new message from Code", from_=twilio_number, to=target_number)





def Buying_page(request):
	global amount
	global display_amount
	global gst
	global Alert_Message
	global Initial_order_id
	global Product_ID
	
	print("amount-----",amount)	
	# Create a Razorpay Order
	if request.method == "POST":
		print("request.method::::::::;",request.method)

	print("Landing on Buying_page")
	table_obj=AstroClient()
	razorpay_order = razorpay_client.order.create(dict(amount=amount,currency=currency,payment_capture='0'))

	# order id of newly created order.
	Initial_order_id = razorpay_order['id']
	print("Initial_order_id 1",Initial_order_id)
	callback_url = '/paymenthandler/'

	# # we need to pass these details to frontend.
	context = {}
	context['razorpay_order_id'] = Initial_order_id
	context['callback_url'] = callback_url
	context['razorpay_merchant_key'] = settings.RAZORPAY_KEY_ID
	context['razorpay_amount'] = amount
	context['currency'] = currency
	context['display_amount'] = display_amount
	context['applied_GST'] = applied_GST
	context['gst'] = gst
	context['total_payment'] = int(amount)/100 + int(gst)
	context['Product_ID'] = Product_ID
	amount = amount
	
	# table_obj.product_id = Product_ID
	table_obj.order_id = Initial_order_id
	table_obj.save()

	print("table_obj saved Initial_order_id",Initial_order_id)
	print("Leaving From Buying_page")

	return render(request, 'Buying_Page.html', context=context)



@csrf_exempt
def user_details(request):
	global User_Name
	global db_serial_no
	global Alert_Message
	global Initial_order_id
	global Product_ID
	global target_number

	table_obj=AstroClient()
	if request.method == "POST":
		print("user_details ::::::: ",request.POST)

		try:
			User_Name = request.POST['name']
			mobile_no = request.POST['mobile_no']
			email_id = request.POST['email_id']
			gender = request.POST['gender']
			birth_date = str(request.POST['birth_date'])
			birth_time = request.POST['birth_time']
			birth_place = request.POST['birth_city']
			birth_state = request.POST['birth_state']
			birth_country = request.POST['birth_country']
			language = request.POST['language']
			notes = request.POST['notes']
			target_number = CC+mobile_no
			print("User Details Saved In DataBase : ||| ")


			all_clients = AstroClient.objects.all()
			print("all_clients:::::",all_clients)


			# Edit the payment_id for the last client
			if all_clients:
				last_client = all_clients.last()
				print("last_client id is ::::::::::::::::::::::",last_client,last_client.order_id)
				if Initial_order_id == last_client.order_id:
					last_client.name = User_Name
					last_client.mobile_no = mobile_no
					last_client.email_id = email_id
					last_client.gender = gender
					last_client.birth_date = birth_date
					last_client.birth_time = birth_time
					last_client.birth_place = birth_place
					last_client.birth_state = birth_state
					last_client.birth_country = birth_country
					last_client.language = language
					last_client.notes = notes
					last_client.save()
					print("last_client id is ::::::::::::::::::::::",last_client.pk)
					print("last_client id type::::::::::::::::::::::",type(last_client.pk))
					db_serial_no = last_client.pk						

					print("User info saved to table:::")

					return HttpResponseRedirect("/Payment/")
				else:					
					Alert_Message = 'Different Order Id Detected : ///'	
					return HttpResponseRedirect("/Buying_page/")
			else:
				Alert_Message = 'Client Not Found : ///'	
				return HttpResponseRedirect("/Buying_page/")
		except Exception as e:
			print("actully aama naa aayu",e)
	else:
		Alert_Message = 'Invalid request Method : ///'	
		print("------------HttpResponseBadRequest get")
		return HttpResponseRedirect("/")




def Payment(request):
	global amount
	global Alert_Message
	global Product_ID
	print("Landing on Payment_page")
	if request.method == "POST":
		print("request.method::::::::;",request.method)

	table_obj=AstroClient()
	razorpay_order = razorpay_client.order.create(dict(amount=amount,currency=currency,payment_capture='0'))

	# order id of newly created order.

	razorpay_order_id = razorpay_order['id']
	callback_url = '/paymenthandler/'

	# we need to pass these details to frontend.
	context = {}
	context['razorpay_order_id'] = razorpay_order_id
	context['callback_url'] = callback_url
	context['razorpay_merchant_key'] = settings.RAZORPAY_KEY_ID
	context['razorpay_amount'] = amount
	context['currency'] = currency
	context['display_amount'] = display_amount
	context['applied_GST'] = applied_GST
	context['gst'] = gst
	context['total_payment'] = int(amount)/100 + int(gst)
	print("Leaving From Payment_page")

	return render(request, 'Payment_page.html', context=context)




# we need to csrf_exempt this url as
# POST request will be made by Razorpay
# and it won't have the csrf token.
@csrf_exempt
def paymenthandler(request):
	global amount
	global Payment_Success
	global db_serial_no
	global User_Name
	global Alert_Message
	global Product_ID
	global booking_slot

	

	if request.method == "POST":
		print("In paymenthandler -------->")
		print("paymenthandler::::::::;",request.POST)

		print("Product_ID is ::::::",Product_ID)
		
		# only accept POST request.
		razorpay_order = razorpay_client.order.create(dict(amount=amount,currency=currency,payment_capture='0'))
		Payment_Success = 0

		# order id of newly created order.
		razorpay_order_id = razorpay_order['id']
		callback_url = '/paymenthandler/'

		client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID,settings.RAZORPAY_KEY_SECRET))
		# print("client keys == ",client)

		payment = client.order.create({'amount': amount, 'currency':'INR', 'payment_capture' : 1})
		print("payment:::::",payment)
		total_payment = int(payment['amount'])/100
		print("total_payment:++++++++++++++++::",total_payment)

		try:
		
			# get the required parameters from post request.
			payment_id = request.POST.get('razorpay_payment_id', '')
			razorpay_order_id = request.POST.get('razorpay_order_id', '')
			payment_signature = request.POST.get('razorpay_signature', '')
			payment_status_code = request.POST.get('status_code', '')

			print("payment_id::::::; ",payment_id)
			print("razorpay_order_id::::::; ",razorpay_order_id)
			print("signature::::::; ",payment_signature)
			params_dict = {
				'razorpay_order_id': razorpay_order_id,
				'razorpay_payment_id': payment_id,
				'razorpay_signature': payment_signature
			}

			# verify the payment signature.
			result = razorpay_client.utility.verify_payment_signature(
				params_dict)
			if result is not None and Payment_Success == 0:
				try:

					# capture the payemt
					razorpay_client.payment.capture(payment_id, amount)

					print("--------paymentsuccess")
					print("AstroClient.objects.get(id=db_serial_no))")
					if Product_ID == Product_1_ID:
						table_obj = AstroClient

					else:
						table_obj = Astro_Booking_Client

					################################################

					Paid_Client = table_obj.objects.get(id=int(db_serial_no))
					print("xxxxxxxxxxxxxxxxx",Paid_Client.pk)
					print("xxxxxxxxxxxxxxxxx",Paid_Client.name)
					print("db_serial_no ::::::",db_serial_no)
					print("User_Name ::::::",User_Name)

					# Edit the payment_id for the last client
					if Paid_Client:
						if db_serial_no == Paid_Client.pk and User_Name == Paid_Client.name:
							print("Paid_Client id is ::::::::::::::::::::::",Paid_Client.pk)
							print("Paid_Client name is ::::::::::::::::::::::",Paid_Client.name)
							
							# Edit the payment_id for the last client
							Paid_Client.order_id = razorpay_order_id
							Paid_Client.payment_id = payment_id
							Paid_Client.payment_signature = payment_signature
							Paid_Client.payment_amount = total_payment
							Paid_Client.paid = True
							Paid_Client.save()

							Payment_Success = 1 

							print("Payment_Success :: ",Payment_Success)
							print("After Edit:", Paid_Client.name, Paid_Client.order_id, Paid_Client.payment_id, Paid_Client.paid)
							print("Conf message created------------------------------")
							print("Conf message created------------------------------",Product_ID,booking_slot,target_number)
							# message = twilio_client.messages.create(body="Hello User, Your Order Has been Confirmed of Persionalized Kundali ", from_=twilio_number, to=target_number)
							

							if Product_ID == Product_1_ID:
								try:
									message = twilio_client.messages.create(body="Hello User, Your Order Has been Confirmed of" + Product_ID +" Your Order Will be deliver to your Registered Email-id Shortly Thank You.", from_=twilio_number, to=target_number)
									print("Conf message Sent |||||||||||",message)
								except:
									print("Conf message Could not Sent /////////////",message)
									return render(request, 'paymentsuccess.html')


							else:
								try:
									message = twilio_client.messages.create(body="Hello User, Your Booking Has been Confirmed of" + Product_ID +" Your Consultation is Sceduled on Tomorrow" + booking_slot + "Your Google Meet Link Will be Delivered Thank You.", from_=twilio_number, to=target_number)
									print("Conf message Sent |||||||||||",message)
								except:
									print("Conf message Could not Sent /////////////",message)
									return render(request, 'paymentsuccess.html')



							return render(request, 'paymentsuccess.html')
						else:
							Alert_Message = "Payment Failed, Retry Payment"
							return render(request, 'Buying_Page.html',{"Payment_Success":Payment_Success,"Alert_Message":Alert_Message})
					else:
						Alert_Message = "User Module Error, Retry."
						return render(request, 'paymentfail.html')
				except:
					print("------------paymentfail 1")
					return HttpResponseRedirect("/")
			else:
				print("------------paymentfail 2")
				# if signature verification fails.
				return render(request, 'paymentfail.html')
		except:
			print("------------HttpResponseBadRequest 1")
			# if we don't find the required parameters in POST data
			return HttpResponseBadRequest()
	else:
		print("------------HttpResponseBadRequest 2")
	# if other than POST request is made.
		return HttpResponseBadRequest()


def ex(request):
	template = loader.get_template('ex.html')
	return HttpResponse(template.render())








def Booking_Page(request):

	global amount
	global display_amount
	global gst
	global Alert_Message
	global Initial_order_id
	global Product_ID

	# Create a Razorpay Order
	if request.method == "POST":
		print("request.method::::::::;",request.method)

	print("Landing on Booking_Page")
	table_obj=Astro_Booking_Client()
	razorpay_order = razorpay_client.order.create(dict(amount=amount,currency=currency,payment_capture='0'))

	# order id of newly created order.
	Initial_order_id = razorpay_order['id']
	print("Initial_order_id 1",Initial_order_id)
	callback_url = '/paymenthandler/'

	# # we need to pass these details to frontend.
	context = {}
	context['razorpay_order_id'] = Initial_order_id
	context['callback_url'] = callback_url
	context['razorpay_merchant_key'] = settings.RAZORPAY_KEY_ID
	context['razorpay_amount'] = amount
	context['currency'] = currency
	context['display_amount'] = display_amount
	context['applied_GST'] = applied_GST
	context['gst'] = gst
	context['total_payment'] = int(amount)/100 + int(gst)
	context['Product_ID'] = Product_ID
	amount = amount
	
	# table_obj.product_id = Product_ID
	table_obj.order_id = Initial_order_id
	table_obj.save()

	print("table_obj saved Initial_order_id",Initial_order_id)
	print("Leaving From Booking_Page")

	return render(request, 'Booking_Page.html', context=context)	



@csrf_exempt
def Booking_User(request):
	global User_Name
	global Product_ID
	global db_serial_no
	global Alert_Message
	global Initial_order_id
	global booking_slot
	global target_number

	if request.method == "POST":
		print("Booking_User_details ::::::: ",request.POST)

		try:
			User_Name = request.POST['name']
			mobile_no = request.POST['mobile_no']
			email_id = request.POST['email_id']
			gender = request.POST['gender']
			birth_date = str(request.POST['birth_date'])
			birth_time = request.POST['birth_time']
			birth_place = request.POST['birth_city']
			birth_state = request.POST['birth_state']
			birth_country = request.POST['birth_country']
			language = request.POST['language']
			booking_slot = request.POST['booking_slot']
			notes = request.POST['notes']
			target_number = CC+mobile_no
			print("User Details Saved In DataBase : ||| ")

			all_clients = Astro_Booking_Client.objects.all()
			print("all_clients:::::",all_clients)

			# Edit the payment_id for the last client
			if all_clients:
				last_client = all_clients.last()
				print("last_client id is ::::::::::::::::::::::",last_client,last_client.order_id)
				if Initial_order_id == last_client.order_id:
					last_client.name = User_Name
					last_client.mobile_no = mobile_no
					last_client.email_id = email_id
					last_client.gender = gender
					last_client.birth_date = birth_date
					last_client.birth_time = birth_time
					last_client.birth_place = birth_place
					last_client.birth_state = birth_state
					last_client.birth_country = birth_country
					last_client.language = language
					last_client.booking_slot = booking_slot
					last_client.product_id = Product_ID
					last_client.notes = notes
					last_client.save()
					print("Booking_User last_client id is ::::::::::::::::::::::",last_client.pk)
					print("Booking_User last_client id type::::::::::::::::::::::",type(last_client.pk))
					db_serial_no = last_client.pk						

					print("Booking_User info saved to table:::")

					return HttpResponseRedirect("/Payment/")
				else:					
					Alert_Message = 'Different Order Id Detected : ///'	
					print("Alert_Message :::: ",Alert_Message)
					return HttpResponseRedirect("/Buying_page/")
			else:
				Alert_Message = 'Client Not Found : ///'	
				return HttpResponseRedirect("/Buying_page/")
		except:
			print("actully aama naa aayu")
			return HttpResponseRedirect("/Buying_page/")
	else:
		Alert_Message = 'Invalid request Method : ///'	
		print("------------HttpResponseBadRequest get")
		return HttpResponseRedirect("/")



