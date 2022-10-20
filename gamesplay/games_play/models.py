from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class ProfileModel(models.Model):
    email = models.EmailField()
    MIN_AGE = 12
    age = models.IntegerField(
        validators= [MinValueValidator(MIN_AGE)],
    )
    MAX_PASSWORD_LENGTH = 30
    password = models.CharField(
        max_length=MAX_PASSWORD_LENGTH,
    )
    MAX_NAME_LENGTH = 30
    first_name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        null=True,
        blank=True,
    )

    last_name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        blank=True,
        null=True,
    )

    profile_picture = models.URLField(
        blank=True,
        null=True,
    )


class GameModel(models.Model):
    MAX_TITLE_LENGTH = 30
    title = models.CharField(
        max_length=MAX_TITLE_LENGTH,
        unique=True,
    )
    MAX_CATEGORY_LENGTH = 30
    CATEGORY_CHOICES = (
        ("ACTION", 'Action'),
        ("ADVENTURE", "Adventure"),
        ('PUZZLE', "Puzzle"),
        ("STRATEGY", 'Strategy'),
        ('SPORTS', 'Sports'),
        ('BOARD/CARD GAME', 'Board/Card Game'),
        ("OTHER", 'Other')
    )
    category = models.CharField(
        max_length=MAX_CATEGORY_LENGTH,
        choices=CATEGORY_CHOICES,
    )
    rating = models.FloatField(
        validators=[MinValueValidator(0.1), MaxValueValidator(5)],
    )
    max_level = models.IntegerField(
        validators=[MinValueValidator(1)],
        null=True,
    )
    image_url = models.URLField()
    summary = models.TextField(
        null=True,
    )

