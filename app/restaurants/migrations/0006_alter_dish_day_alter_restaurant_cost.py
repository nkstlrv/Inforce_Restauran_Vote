# Generated by Django 4.2.3 on 2023-07-12 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0005_alter_dish_day_alter_restaurant_cost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='day',
            field=models.PositiveIntegerField(choices=[(0, 'Everyday'), (1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday'), (7, 'Sunday')], default=0),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='cost',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Low'), (2, 'Mid'), (3, 'High')], default=2),
        ),
    ]