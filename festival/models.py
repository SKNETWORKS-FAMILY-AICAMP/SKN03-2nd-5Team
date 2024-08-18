# show_hotplace/models.py

from django.db import models

class Festival(models.Model):
    festival_name = models.CharField(max_length=255, primary_key=True)
    location = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    fee = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    parking_available = models.CharField(max_length=255)
    website_url = models.CharField(max_length=255)
    region_name = models.CharField(max_length=255)

    class Meta:
            db_table = 'festival_table'
