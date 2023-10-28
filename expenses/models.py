from django.db import models

from django.contrib.auth.models import User


class AddBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    authors = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)
    published_date = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    distribution_expense = models.IntegerField(default=5)

    def __str__(self):
        return self.title
