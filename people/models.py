from django.db import models

# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=50, unique=True)
    age = models.IntegerField()

    def __str__(self):
        return "name = " + self.name + "; age = " + str(self.age)