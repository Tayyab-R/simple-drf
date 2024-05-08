from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import viewsets
from .serializers import CustomerSerializer
from .models import Customer, Product
# Create your views here.
class CustomerViewSet(viewsets.ModelViewSet):
    """
    We are using class-based viewsSet for better convenience.
    If we use functions-based viewSet we have to define explicitly every crud operations
    using decorators.
    """
    queryset = Customer.objects.all() # query the data from the defined model
    serializer_class = CustomerSerializer # serialize data into json from our serializer


class ProductBoughtByCustomer(viewsets.ModelViewSet):
    """ Retrieve the product bought by customer """
    pass