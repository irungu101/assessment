from django.db import models

# Create your models here.
class Workers(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=15)
    phone_number = models.IntegerField()
    password = models.CharField(max_length=15)

    def __str__(self):
        return self.firstname
