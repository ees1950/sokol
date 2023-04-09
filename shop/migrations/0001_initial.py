# Generated by Django 3.2.18 on 2023-04-08 08:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=128, verbose_name='E-mail')),
                ('first_name', models.CharField(max_length=128, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=128, verbose_name='Last Name')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=128, verbose_name='Product')),
                ('order_date', models.DateField(verbose_name='Order Date')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shop.customer')),
            ],
        ),
    ]
