from django.db import models

# Create your models here.


class Festival(models.Model):
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_parking = models.BooleanField()
    street_address = models.CharField(max_length=255)
    link = models.URLField()

    def __str__(self):
        return self.title
