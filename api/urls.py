from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter() # convenient and organized way to handle URL routing for views
router.register(r'customers', views.CustomerViewSet) # a raw string representing the URL pattern for the customers resource

urlpatterns = [
    path('', include(router.urls)),
    
]
