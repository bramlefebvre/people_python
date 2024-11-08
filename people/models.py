from django.db import models

# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self):
        return "name = " + self.name + "; age = " + str(self.age)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(models.functions.Lower("name"), name= "unique_lower_name")
        ]