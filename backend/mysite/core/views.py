from django.shortcuts import render
from .models import Person
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import person_serializer
# Create your views here.

@api_view(['GET', 'POST', 'PATCH'])
def person(request):
    if request.method == 'POST':
        data = request.data
        serializer = person_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    if request.method == 'GET':
        data = Person.objects.all()
        serializer = person_serializer(data, many = True)
        return Response(serializer.data)
    if request.method == 'PATCH':
        data = request.data
        obj = Person.objects.get(id = data['id'])
        serializer = person_serializer(obj, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response("Something Went Wrong")
