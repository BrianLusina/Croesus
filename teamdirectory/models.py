from django.db import models


# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    title = models.CharField(max_length=100)
    image = models.CharField(max_length=500)

    def __repr__(self):
        return "<Name: % name>" % (self.name)