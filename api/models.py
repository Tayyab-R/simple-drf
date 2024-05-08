from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    salary = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return self.name
    
    