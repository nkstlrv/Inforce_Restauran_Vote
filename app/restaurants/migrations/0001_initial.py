# Generated by Django 4.2.3 on 2023-07-12 09:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('day', models.CharField(choices=[(0, 'Everyday'), (1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday'), (7, 'Sunday')], default=0, max_length=1)),
                ('price', models.DecimalField(decimal_places=2, default=None, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)])),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=500)),
                ('phone_number', models.CharField(max_length=15)),
                ('cuisine', models.CharField(default=None, max_length=100, null=True)),
                ('cost', models.CharField(choices=[(1, 'Low'), (2, 'Mid'), (3, 'High')], default=2, max_length=1)),
                ('delivery', models.BooleanField(default=False)),
                ('dish', models.ManyToManyField(to='restaurants.dish')),
            ],
        ),
    ]