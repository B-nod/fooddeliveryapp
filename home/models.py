from unicodedata import category
from django.contrib.auth.models import User
from django.core.validators import *
from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.category_name

class FoodProduct(models.Model):
    food_name = models.CharField(max_length=250)
    food_price = models.FloatField()
    stock = models.IntegerField()
    image = models.FileField(upload_to='static/uploads', null=True)
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.food_name

class Order(models.Model):
    PAYMENT = (
        ('Cash on Delivery','Cash on Deliver'),
        ('Esewa','Esewa'),
        ('Khalti','Khalti')
    )
    foodproduct=models.ForeignKey(FoodProduct,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total_price = models.IntegerField(null=True)
    status = models.CharField(default='Pending', max_length=200)
    payment_method = models.CharField(max_length=200, choices=PAYMENT)
    payment_status = models.BooleanField(default=False,null=True,blank=True)
    contact_no = models.CharField(validators=[MinLengthValidator(9),MaxLengthValidator(10)], max_length=10)
    address = models.CharField(max_length=200, null=True)
    created_date = models.DateTimeField(auto_now_add=True)

