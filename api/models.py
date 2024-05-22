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
    customer = models.ForeignKey(Customer, related_name='products', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name