from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    salary = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return self.name
    
    
class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField()

    
    def __str__(self) -> str:
        return self.name
    
    
class Inventory(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()


    def __str__(self) -> str:
        return f"{self.product.name} - Quantity: {self.quantity}"
