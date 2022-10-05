import os
from uuid import uuid4

from django.db import models
from django.shortcuts import reverse
from autoslug import AutoSlugField

# Create your models here.
from django.utils.safestring import mark_safe

AVAILABILITY = (
    ('IS', 'In Stock'),
    ('OS', 'Out Stock'),
)


def path_and_rename(instance, filename):
    upload_to = 'product_images'
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)


class Category(models.Model):
    title = models.CharField(default='', max_length=100, unique=True)
    slug = models.CharField(default='', max_length=100)
    description = models.TextField(default='')
    active = models.BooleanField(default=True)
    image = models.ImageField(upload_to=path_and_rename, max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title

    def get_quantity_product(self):
        return len(self.products.filter(active=True))

    @staticmethod
    def get_all_category():
        return Category.objects.filter(active=True)

    def get_absolute_url(self):
        return reverse("category", kwargs={
            'slug': self.slug
        })


class Product(models.Model):
    title = models.CharField(default='', max_length=100)
    description = models.TextField(default='')
    price = models.FloatField(default=0.0)
    status = models.CharField(choices=AVAILABILITY, max_length=30, null=True)
    active = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    slug = AutoSlugField(populate_from='title', unique=True, null=True)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.title

    def first_image(self):
        return self.images.all()[0]

    def image_tag(self):
        if self.first_image():
            return mark_safe('<img src="%s" style="width: 60px; height:60px;" />' % self.first_image().image.url)
        else:
            return 'No Image Found'

    image_tag.short_description = 'Image'

    def get_absolute_url(self):
        return reverse("product", kwargs={
            'slug': self.slug
        })

    def get_add_cart_url(self):
        return reverse("add-to-cart", kwargs={
            'slug': self.slug
        })

    @staticmethod
    def get_all_product():
        return Product.objects.filter(active=True)

    @staticmethod
    def get_product_by_category(category):
        return Product.objects.filter(category=category)


class Image(models.Model):
    product = models.ForeignKey(Product, default=None, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to=path_and_rename, max_length=255)

    def __str__(self):
        return ''

    def image_tag(self):
        if self.image:
            return mark_safe('<img src="%s" style="width: 200px; height:200px;" />' % self.image.url)
        else:
            return 'No Image Found'

# class Variation(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     title = models.CharField(default='', max_length=255)
#     price = models.FloatField(default=0.0)
#     sale_price = models.FloatField(default=0.0)
#     active = models.BooleanField(default=True)
#     inventory = models.IntegerField(default=0)
