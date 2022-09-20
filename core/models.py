from enum import unique
from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    description = models.TextField(blank=False)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.name
