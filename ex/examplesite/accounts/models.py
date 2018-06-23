from django.db import models

# Create your models here.

class Account(models.Model):
    first_name = models.CharField(max_length = 35)
    last_name = models.CharField(max_length = 35)
    grade = models.IntegerField()
    school = models.CharField(max_length = 150)
    phone_number = models.CharField(max_length = 12)

    def __str__(self):
        return self.first_name + " " + self.last_name
