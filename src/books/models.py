from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)

    def __str__(self) -> str:
        return self.first_name


class Book(models.Model):
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=256)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    date_published = models.DateField()

    def __str__(self) -> str:
        return self.name
