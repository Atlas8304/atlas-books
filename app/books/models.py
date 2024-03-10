from datetime import date
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    biography = models.TextField()

    def __str__(self) -> str:
        return self.full_name()

    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ManyToManyField(Author)
    cover_art = models.ImageField(default="default_cover.jpg")
    published_date = models.DateField(default=date.today)
    isbn = models.CharField(max_length=17, unique=True)
    description = models.TextField()
    genre = models.ManyToManyField(Genre)
    rating = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)],
        default=0.0
    )

    def __str__(self) -> str:
        return self.title
