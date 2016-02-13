from __future__ import unicode_literals

from django.db import models

class User(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    age = models.IntegerField()
    def __str__(self):
        return self.firstname + " " + self.lastname + " wiek: " + str(self.age)
