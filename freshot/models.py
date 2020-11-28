from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=30)
    ra = models.CharField(max_length=9)

    def __str__(self):
        return self.name
