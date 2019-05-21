from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.response import Response
import stripe
stripe.api_key = "sk_test_4eC39HqLyjWDarjtT1zdp7dc"


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


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def doPayment(request):
	try:
		amount = request.data['amount']
		currency = request.data.get('currency','USD')
		description = request.data['description']
		tokenId = request.data['tokenId']
	except Exception as e:
		return handle_input_error('{"amount":"field_is_required","description":"field_is_required","tokenId":"field_is_required"}')
	try:
		res = stripe.Charge.create(
			amount=amount,
			currency=currency,
			source=tokenId, # obtained with Stripe.js
			description=description
		)
	except Exception as e:
		return handle_error(e)
	return Response(res, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def doSubscription(request):
	try:
		customer = request.data['customerId']
		planId = request.data['planId']
	except Exception as e:
		return handle_input_error('{"customerId":"field_is_required","planId":"field_is_required"}')
	try:
		res = stripe.Subscription.create(
			customer="cus_F6hg9lS1KHdpHr",
			items=[
				{
				"plan": planId,
				},
			]
		)
	except Exception as e:
		return handle_error(e)
	return Response(res, status=status.HTTP_200_OK)




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

