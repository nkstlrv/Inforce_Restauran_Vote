# Generated by Django 4.2.3 on 2023-07-12 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0017_alter_menu_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='day',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Monday'), (1, 'Tuesday'), (2, 'Wednesday'), (3, 'Thursday'), (4, 'Friday'), (5, 'Saturday'), (6, 'Sunday')], default=0),
        ),
    ]
