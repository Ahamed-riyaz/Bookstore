from django.urls import path, include
from .views import ProductView
urlpatterns = [
    path('product/', ProductView.as_view()),
    path('product/payment/', include('payment.urls'))
]