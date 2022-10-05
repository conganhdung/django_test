from ast import Delete
from turtle import update
from venv import create
from django.db import models
from accounts.models import User
from payment.models import Payment
from product.models import ProductInformation

class Order(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    total = models.IntegerField()
    discount = models.CharField(max_length=10,null=True)
    oreder_status = models.CharField(max_length=10) 
    payment_id = models.ForeignKey(Payment,on_delete=models.CASCADE)
    create_at =  models.DateTimeField(auto_now_add=True)
    update_at =  models.DateTimeField(auto_now_add=True)
    delete_at =  models.DateTimeField(auto_now_add=True)

class OrderItem(models.Model):

    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    product = models.ForeignKey(ProductInformation,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    create_at = models.DateField(auto_now_add=True) 
    update_at =  models.DateTimeField(auto_now_add=True)
    delete_at =  models.DateTimeField(auto_now_add=True)

