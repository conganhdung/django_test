# Generated by Django 4.0 on 2022-01-05 13:56

from django.db import migrations, models
import django.db.models.deletion
import home.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0008_alter_category_title_alter_product_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeatureCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transparent_image', models.ImageField(upload_to=home.models.path_and_rename)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.category')),
            ],
        ),
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_transparent_bg', models.ImageField(upload_to=home.models.path_and_rename)),
                ('short_descriptions', models.TextField(default='', max_length=300)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
    ]
