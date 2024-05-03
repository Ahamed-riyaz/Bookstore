from django.shortcuts import render
from .models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import product_serializer
from rest_framework.views import APIView
from rest_framework import status
# Create your views here.

class ProductView(APIView):
    def get(self, request):
        data = Product.objects.all()
        serializer = product_serializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = product_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def patch(self, request):
        data = request.data
        obj = Product.objects.get(id = data['id'])
        serializer = product_serializer(obj, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response("Something Went Wrong")

    def delete(self, request):
        try:
            data = request.data
            obj = Product.objects.get(id = data['id'])
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        obj.delete()
        return Response("Deleted Successfully", status=status.HTTP_200_OK)
