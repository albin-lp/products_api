from django.db import models
from django.contrib.auth.models import User

class Products(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product_name=models.CharField(max_length=100)
    price=models.PositiveIntegerField()
    brand=models.CharField(max_length=200)

    def __str__(self):
        return self.product_name





# Create your models here.
