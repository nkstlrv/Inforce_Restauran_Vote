# Generated by Django 4.2.3 on 2023-07-12 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dish', '0001_initial'),
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='dishes',
            field=models.ManyToManyField(blank=True, to='dish.dish'),
        ),
    ]
