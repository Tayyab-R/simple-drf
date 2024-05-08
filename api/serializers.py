from rest_framework import serializers
from .models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    """
    Serializer is used to serialize complex data from models or python objects
    into convinient form like json to read.
    
    We can say serializer is a bridge between python objects and the outside world.

    Here we are using model 'Customer' and 'all fields' of our model to serialize
    into readable form.
    """
    class Meta:
        model = Customer
        fields = '__all__'