from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    books = models.ManyToManyField("Book", related_name="users")


class Book(models.Model):
    class GenreChoices(models.TextChoices):
        FICTION = "Fiction"
        NON_FICTION = "Non-Fiction"
        MYSTERY = "Mystery"

    name = models.CharField(max_length=255)
    genre = models.CharField(max_length=24, choices=GenreChoices.choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self) -> str:
        return self.name
