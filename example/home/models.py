import os
from uuid import uuid4

from django.db import models
from product.models import Product, Category


# Create your models here.


def path_and_rename(instance, filename):
    upload_to = 'home_images'
    ext = filename.split('.')[-1]
    # set filename as random string
    filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)


class Banner(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image_transparent_bg = models.ImageField(upload_to=path_and_rename)
    short_descriptions = models.TextField(max_length=300, default='')

    def __str__(self):
        return f'{self.product.title} Banner'

    @staticmethod
    def get_all_banner():
        return Banner.objects.all()


class FeatureCategory(models.Model):
    category = models.OneToOneField(Category, on_delete=models.CASCADE)
    transparent_image = models.ImageField(upload_to=path_and_rename)

    def __str__(self):
        return self.category.title

    @staticmethod
    def get_all_feature_cate():
        return FeatureCategory.objects.all()


class Awesome(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.title

    def number_page_awesome(self):
        return self.objects.all().length() // 8

    @staticmethod
    def get_all_awesome():
        return Awesome.objects.all()


