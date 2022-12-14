# Generated by Django 4.0.1 on 2022-01-10 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0010_alter_order_order_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='time_create',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('p', 'Pending'), ('ds', 'Delivered to shipper'), ('c', 'Complete'), ('cc', 'Cancel')], default='P', max_length=50),
        ),
    ]
