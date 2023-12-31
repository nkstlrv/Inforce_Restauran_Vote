# Generated by Django 4.2.3 on 2023-07-12 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0006_alter_dish_day_alter_restaurant_cost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dish',
            name='day',
        ),
        migrations.RemoveField(
            model_name='dish',
            name='price',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='cost',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='cuisine',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='dish',
        ),
        migrations.AlterField(
            model_name='dish',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='address',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='phone_number',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.PositiveSmallIntegerField(choices=[(0, 'Everyday'), (1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday'), (7, 'Sunday')], default=0)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurants.restaurant')),
            ],
        ),
        migrations.AddField(
            model_name='dish',
            name='menu',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='restaurants.menu'),
        ),
    ]
