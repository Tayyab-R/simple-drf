from django.urls import path, include
from .views import hello_world, send_get_data, update_customer

urlpatterns = [
    path('', hello_world, name='hello_world'),
    path('customers/',  send_get_data, name='send_get_data'),  
    path('customers/<int:pk>/', update_customer, name='update_customer'),
]
