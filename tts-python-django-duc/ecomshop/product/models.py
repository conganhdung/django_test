from django.db import models
# Create your models here.

class Brand(models.Model):
 
    name = models.CharField(max_length=255)
    create_at =  models.DateTimeField(auto_now_add=True)
    update_at =  models.DateTimeField(auto_now_add=True)
    delete_at =  models.DateTimeField(auto_now_add=True)

class Product(models.Model):

    brand = models.ForeignKey( Brand ,on_delete=models.CASCADE )
    price = models.IntegerField()
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=255) 
    information = models.CharField(max_length=255)
    name_tag = models.FloatField(max_length=2)
    create_at =  models.DateTimeField(blank=False,null=True)
    update_at =  models.DateTimeField(blank=False,null=True)
    delete_at =  models.DateTimeField(blank=False,null=True)

class ProductInformation(models.Model):

    product = models.ForeignKey( Product,on_delete=models.CASCADE )
    total = models.IntegerField()
    cpu = models.CharField(max_length=255)
    ram = models.CharField(max_length=255) 
    os = models.CharField(max_length=255)
    weight = models.FloatField(max_length=2)
    create_at =  models.DateTimeField(blank=False,null=True)
    update_at =  models.DateTimeField(blank=False,null=True)
    delete_at =  models.DateTimeField(blank=False,null=True)

    
class Type(models.Model):
 
    name = models.CharField(max_length=255)
    create_at =  models.DateTimeField(auto_now_add=True)
    update_at =  models.DateTimeField(auto_now_add=True)
    delete_at =  models.DateTimeField(auto_now_add=True)

class ProductType(models.Model):

    type = models.ForeignKey(Type ,on_delete=models.CASCADE )
    product = models.ForeignKey(Product,on_delete=models.CASCADE )
    create_at =  models.DateTimeField(auto_now_add=True)
    update_at =  models.DateTimeField(auto_now_add=True)
    delete_at =  models.DateTimeField(auto_now_add=True)


