from django.db import models


class Menu(models.Model):
    """
    Model of the Menu
    has relations to Restaurant and Dishes model
    field day alow us to understand on what week day this menu is available
    """
    WEEKDAY_CHOICES = (
        (0, 'Monday'),
        (1, 'Tuesday'),
        (2, 'Wednesday'),
        (3, 'Thursday'),
        (4, 'Friday'),
        (5, 'Saturday'),
        (6, 'Sunday'),
    )

    restaurant = models.ForeignKey('restaurants.Restaurant', on_delete=models.CASCADE, null=True)
    day = models.PositiveSmallIntegerField(choices=WEEKDAY_CHOICES, default=0)
    dishes = models.ManyToManyField('dish.Dish', blank=True)

    def __str__(self):
        return f"Menu of {self.restaurant.name} | {self.day}"
