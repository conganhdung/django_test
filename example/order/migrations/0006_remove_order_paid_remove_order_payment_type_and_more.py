# Generated by Django 4.0.1 on 2022-01-09 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_order_paid_order_payment_type_alter_order_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='paid',
        ),
        migrations.RemoveField(
            model_name='order',
            name='payment_type',
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('P', 'Pending'), ('DS', 'Delivered to shipper'), ('C', 'Complete')], default='P', max_length=50),
        ),
    ]
