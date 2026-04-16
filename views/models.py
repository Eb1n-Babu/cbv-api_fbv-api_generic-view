from django.db import models

class Customer(models.Model):
    country = models.CharField(max_length=100)
    year = models.IntegerField(choices=[(year, year) for year in range(1948, 2015)])
    def __str__(self):
        return self.country