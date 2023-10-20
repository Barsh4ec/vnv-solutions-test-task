from django.contrib.auth.models import AbstractUser
from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=63)
    description = models.TextField()

    def __str__(self) -> str:
        return self.name


class User(AbstractUser):
    groups = models.ManyToManyField(to=Group, related_name="users", blank=True)

    def __str__(self) -> str:
        return self.username
