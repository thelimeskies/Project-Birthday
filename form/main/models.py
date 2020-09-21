from django.db import models

# Create your models here.


class Index(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    dob = models.DateField()
    phone_number = models.CharField(max_length=14)
    email = models.CharField(max_length=255)

    class Meta:
        ordering = ['-dob']
