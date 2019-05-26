from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.response import Response
from .models import Plan,User,SubscribeTransaction,Transaction
from .serializers import SubscribeSerializer
import stripe
from django.shortcuts import get_object_or_404
stripe.api_key = "sk_test_gCC3ppShZfCsyYgOHZ2L22iN"


def handle_error(e):
	error_text = ""
	if(type(e) == stripe.error.CardError):
		error_text =  "Strip Card Error"
	elif(type(e) == stripe.error.StripeError ):
		error_text =  "Strip InvalidRequestError"
	elif(type(e) == stripe.error.InvalidRequestError ):
		error_text =  "Strip InvalidRequestError"
	elif(type(e) == stripe.error.AuthenticationError ):
		error_text =  "Strip InvalidRequestError"
	elif(type(e) == stripe.error.APIConnectionError ):
		error_text =  "Strip InvalidRequestError"
	elif(type(e) == stripe.error.InvalidRequestError ):
		error_text =  "Strip InvalidRequestError"
	else:
		error_text =  str(type(e))
	return Response(error_text,status=status.HTTP_400_BAD_REQUEST)


def handle_input_error(err_description):
	return Response(err_description,status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def getCustomer(request):
	try:
		email = request.data['email']
	except Exception as e:
		return handle_input_error('{"email":"field_is_required"}')
	res = stripe.Customer.list(email=email)
	print(res)
	return Response(res, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def createCustomer(request):
	try:
		email = request.data['email']
		source = request.data['source']
	except Exception as e:
		return handle_input_error('{"email":"field_is_required","source":"field_is_required"}')
	try:
		res = stripe.Customer.create(email=email,source=source)
	except Exception as e:
		return handle_error(e)
	return Response(res, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def addCardToCustomer(request):
	try:
		customerId = request.data['customerId']
		cardToken = request.data['cardToken']
	except Exception as e:
		return handle_input_error('{"customerId":"field_is_required","cardToken":"field_is_required"}')
	try:
		res = stripe.Customer.create_source(customerId,source=cardToken)
	except Exception as e:
		return handle_error(e)
	return Response(res, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def createCustomerKey(request):
	try:
		customerId = request.data['customerId']
		api_version = request.data['api_version']
	except Exception as e:
		return handle_input_error('{"customerId":"field_is_required","api_version":"field_is_required"}')
	try:
		res = stripe.EphemeralKey.create(customer=customerId, stripe_version=api_version)    	
	except Exception as e:
		return handle_error(e)
	return Response(res, status=status.HTTP_200_OK)

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def doPayment(request):
	try:
		# amount = request.data['amount']
		plan_id = request.data['plan']
		currency = request.data.get('currency','USD')
		description = request.data['description']
		tokenId = request.data['tokenId']
		mobile_number = request.data['mobile_number']
		name = request.data['name']
		shipping_address = request.data['shipping_address']
		country = request.data['country']
		state = request.data['state']
		zip_code = request.data['zip_code']

		
	except Exception as e:
		return handle_input_error('{"plan":"field_is_required","description":"field_is_required","tokenId":"field_is_required"}')
	# try:
	print("===============")
	plan = get_object_or_404(Plan, pk=plan_id)
	print(plan)
	user = request.user
	if(plan.plan_name !='Free'):
		amount = int(plan.price * 100)
		res = stripe.Charge.create(
			amount=amount,
			currency=currency,
			source=tokenId, # obtained with Stripe.js
			description=description
		)
		transaction = Transaction.objects.create(plan=plan,user=user,pay_amount=amount)
		transaction.plan_name = plan.plan_name
		transaction.currency = currency
		transaction.name = name
		transaction.shipping_address = shipping_address
		transaction.country = country
		transaction.state = state
		transaction.zip_code = zip_code
		transaction.token_id = tokenId
		transaction.mobile_number = mobile_number
		transaction.ip_address = get_client_ip(request)
		transaction.payment_status = res.status
		transaction.save()
	else:
		transaction = Transaction.objects.create(plan=plan,user=user,pay_amount = plan.price*100)
		transaction.plan_name= plan.plan_name
		transaction.save()
	
	user.label_in_use = user.label_in_use + plan.label_count
	user.photo_in_use = user.label_in_use + plan.photo_count
	user.save()

	# except Exception as e:
		# return handle_error(e)
	return Response('success', status=status.HTTP_200_OK)


# @api_view(['POST'])
# @permission_classes((IsAuthenticated,))
# def doSubscription(request):
# 	try:
# 		customer = request.data['customerId']
# 		planId = request.data['planId']
# 	except Exception as e:
# 		return handle_input_error('{"customerId":"field_is_required","planId":"field_is_required"}')
# 	try:
# 		res = stripe.Subscription.create(
# 			customer="cus_F6hg9lS1KHdpHr",
# 			items=[
# 				{
# 				"plan": planId,
# 				},
# 			]
# 		)
# 	except Exception as e:
# 		return handle_error(e)
# 	return Response(res, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def doSubscription(request):
	serializer = SubscribeSerializer(data=request.data)
	serializer.is_valid(raise_exception = True)
	customerId = request.user.subscribed_customer_id
	plan = serializer.validated_data['plan']
	if plan.is_free:
		request.user.subscribed_plan = plan
		request.user.save()
		transaction = SubscribeTransaction.objects.create(plan=plan,user=request.user)
		transaction.plan_name = plan.name
		transaction.plan_price = plan.price
		transaction.plan_product_id = plan.product_id
		transaction.save()
		
		return Response('success')
	# email = 
	print(serializer.validated_data)
	if not serializer.validated_data['email'] or not serializer.validated_data['tokenId']:	# If email or tokenId is not present, use the already existing cusmoter.		
		if not customerId:
			return Response({'email':'required','tokenId':'required'},status = status.HTTP_400_BAD_REQUEST)

	try:
		if not customerId:
			res = stripe.Customer.create(email=serializer.validated_data['email'],source=serializer.validated_data['tokenId'])
			customerId = res['id']
		subscription_id = request.user.subscription_id
		if not subscription_id:
			print('create')
			res = stripe.Subscription.create(
				customer=customerId,
				items = [{"plan":plan.product_id}])
			request.user.subscription_id = res.id
			request.user.subscribed_plan = plan
			request.user.subscribed_token_id = serializer.validated_data['tokenId']
			request.user.subscribed_customer_id = customerId
			request.user.subscribed_email = serializer.validated_data['email']

		else:
			print('modify')
			# res = stripe.Subscription.modify(
			# 	subscription_id,
			# 	items = [{"plan":plan.product_id}])

			subscription = stripe.Subscription.retrieve('sub_F90njAzkpg0qab')
			res = stripe.Subscription.modify(
			  'sub_F90njAzkpg0qab',
			  cancel_at_period_end=False,
			  items=[{
			    'id': subscription['items']['data'][0].id,
			    'plan': 'plan_EwPdwJ4bIkLgWD',
			  }]
			)
			request.user.subscription_id = res.id
			request.user.subscribed_plan = plan 
		request.user.save()
		transaction = SubscribeTransaction.objects.create(plan=plan,user=request.user)
		transaction.subscribe_email = request.user.subscribed_email
		transaction.subscribed_token_id = request.user.subscribed_token_id
		transaction.subscription_id = request.user.subscription_id
		transaction.plan_name = plan.name
		transaction.plan_price = plan.price
		transaction.plan_product_id = plan.product_id
		transaction.save()

	except Exception as e:
		return handle_error(e)		
	return Response('success')		


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def deleteSubscription(request):
	try:
		sub_id = request.data['sub_id']
	except Exception as e:
		return handle_input_error('{"sub_id":"field_is_required"}')
	try:
		res = stripe.Subscription.delete(sub_id)
	except Exception as e:
		return handle_error(e)
	return Response(res, status=status.HTTP_200_OK)


