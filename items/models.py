from django.db import models
import datetime as dt
from django.contrib.postgres.fields import ArrayField, DateRangeField


class Item(models.Model):
    name = models.CharField(max_length=60)
    weight = models.FloatField()
    ints = ArrayField(models.IntegerField(default=0), blank=True, null=True)
    daterange = DateRangeField(null=True)
    dateranges = ArrayField(DateRangeField(null=True), blank=True, null=True)

    def __str__(self):
        return self.name
