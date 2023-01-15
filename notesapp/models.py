from django.db import models
from django.contrib.auth.models import User, Group

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Notes(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, blank=True, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=200)
    text = models.TextField()
    reminder = models.DateTimeField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
