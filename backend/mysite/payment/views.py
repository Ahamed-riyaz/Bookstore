from django.shortcuts import render
from paypal.standard.forms import PayPalPaymentsForm
from mysite import settings
import uuid
from django.urls import reverse
from core.models import Product
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def checkout(request, product_id):
    product = Product.objects.get(id = product_id)

    host = request.get_host()

    paypal_checkout = {
     'business' : settings.PAYPAL_RECEIVER_EMAIL,
     'amount' : product.price,
     'item_name' : product.name,
     'invoice' : uuid.uuid4(),
     'currency_code' : 'INR',
     'notify_url' : f"http://{host}{reverse('paypal-ipn')}",
     'return_url' : f"http://{host}{reverse('payment_success', kwargs = {'product_id' : product.id})}",
     'cancel_url' : f"http://{host}{reverse('payment_failed', kwargs = {'product_id' : product.id})}"
    }

    paypal_payment = PayPalPaymentsForm(initial = paypal_checkout)

    product_dict = {
        'name': product.name,
        'price': product.price,
    }

    context = {
        'product': product_dict,
        'paypal': str(paypal_payment),
        'amount': product.price
    }

    return JsonResponse(context)

def payment_success(request):
    return JsonResponse({'message': 'Payment Successful'}, status=200)

def payment_failed(request):
    return JsonResponse({'message': 'Payment Failed'}, status=400)