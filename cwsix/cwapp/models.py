from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()

    def _str_(self):
        return f"{self.name} ({self.year})"