from django.urls import path
from . import views

urlpatterns = [path('checkout/<int:product_id>', views.checkout, name='checkout'),
               path('payment-success/<int:product_id>', views.payment_success, name='payment_success'),
               path('payment-failed/<int:product_id>', views.payment_failed, name='payment_failed')
               ]