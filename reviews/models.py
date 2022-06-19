from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from properties.models import Property


# def date_validation(date1, date2):
#     """
#     A validator function to check the date_rented_from
#     occurs before the date_rented_to
#     """
#     if


class Review(models.Model):
    """
    A class to represent the reviews for each proeprty
    """
    # Model fields
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    date_rented_from = models.DateField(null=True, blank=True)
    date_rented_to = models.DateField(null=True, blank=True)
    content = models.TextField(max_length=500, null=True, blank=True)
    condition_of_property = models.PositiveIntegerField(
        validators=[MaxValueValidator(5)]
    )
    quality_of_landlord = models.PositiveIntegerField(
        validators=[MaxValueValidator(5)]
    )
    rate_the_neighbourhood = models.PositiveIntegerField(
        validators=[MaxValueValidator(5)]
    )
    value_for_money = models.PositiveIntegerField(
        validators=[MaxValueValidator(5)]
    )
    standard_of_amenities_nearby = models.PositiveIntegerField(
        validators=[MaxValueValidator(5)]
    )
    date_reviewed = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    likes = models.ManyToManyField(
        User,
        related_name='review_likes',
        blank=True,
    )
    # images
