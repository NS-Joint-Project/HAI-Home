from django.db import models
from django.utils import timezone

# Create your models here.

class TimeModel(models.Model):
    user_id = models.IntegerField(null=True, blank=True, default=0)
    departure_time = models.IntegerField(null=True, blank=True, default=0)
    return_time = models.IntegerField(null=True, blank=True, default=0)
    out_time = models.IntegerField(null=True, blank=True, default=0)