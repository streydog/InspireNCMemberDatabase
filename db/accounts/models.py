from django.db import models

# Create your models here.

class Account(models.Model):
    first_name = models.CharField(max_length = 25)
    last_name = models.CharField(max_length = 25)
    slug = models.SlugField()

    def __str__(self):
        return self.first_name+self.last_name
