# Generated by Django 4.2.3 on 2023-07-12 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0013_remove_dish_menus_dish_menus'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dish',
            old_name='menus',
            new_name='menu',
        ),
        migrations.AlterField(
            model_name='dish',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]