from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404

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
        
        
@api_view(['PUT', 'DELETE'])
def update_customer(request, pk):
    customer = get_object_or_404(Customer,  pk=pk)
    if request.method == 'PUT':
        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    if request.method == 'DELETE':
        if customer:
            customer.delete()
            return Response({'messge': 'Customer deleted successfully'}, status=status.HTTP_200_OK)
        
        return Response({'error': 'Customer does not exist'}, status=status.HTTP_400_BAD_REQUEST)

    return Response({'error': 'Request method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

        