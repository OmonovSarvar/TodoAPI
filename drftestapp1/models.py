from django.db import models
from django.utils import timezone


# Create your models here.


class TodoModel(models.Model):
    title = models.CharField(max_length=60)
    description = models.CharField(max_length=222)
    date = models.DateField(default=timezone.datetime.now())

    def __str__(self):
        return f'{self.title}'
