from django.urls import path
from .views import person
urlpatterns = [
    path('', person),
]