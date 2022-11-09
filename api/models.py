from django.db import models
from django.contrib.auth.models import User



class Catagories(models.Model):

    catagory_name=models.CharField(max_length=100)
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return self.catagory_name

class Products(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product_name=models.CharField(max_length=100)
    price=models.PositiveIntegerField()
    brand=models.CharField(max_length=200)
    cat=models.ForeignKey(Catagories,on_delete=models.CASCADE,default="1")

    def __str__(self):
        return self.product_name





# Create your models here.
