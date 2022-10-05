from django.db import models

class Payment(models.Model):
    name = models.CharField(max_length=255)
    create_at =  models.DateTimeField(auto_now_add=True)
    update_at =  models.DateTimeField(auto_now_add=True)
    delete_at =  models.DateTimeField(auto_now_add=True)

