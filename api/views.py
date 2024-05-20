from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer

from .serializers import CustomerSerializer
from .models import Customer

# Create your views here.
@api_view()
def hello_world(request):
    return JsonResponse({'message': 'Hello World!!'})


@api_view(['GET', 'POST'])
def send_get_data(request):
    if request.method == 'GET':
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)
     
    elif request.method == 'POST':    
        data = request.data
        serializer = CustomerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            serializer_data = serializer.data
            return Response(serializer_data, status=status.HTTP_200_OK)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
@api_view(['PUT'])
def update_customer(request, pk):
    if request.method != 'PUT':
        return Response({'error', 'Request not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    customer = Customer.objects.get(pk=pk)
    serializer = CustomerSerializer(customer, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    else:
        return Response({'error' : 'cannot update customer'}, status=status.HTTP_400_BAD_REQUEST)
