from django.db import models

class Activity(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    place = models.CharField(max_length=100)

    class Meta:
        db_table = 'activity'
