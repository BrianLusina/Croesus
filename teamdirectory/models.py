from django.db import models


# Create your models here.
class Person(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True, unique=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    title = models.CharField(max_length=100)
    image = models.CharField(max_length=500)

    def __repr__(self):
        return "<id: %r, Name: %r, Email: %r, Title: %r>" % (self.id, self.name, self.email, self.title)

