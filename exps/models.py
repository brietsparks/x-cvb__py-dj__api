from django.db import models
from django.contrib.postgres.fields import ArrayField, DateRangeField
from skills.models import Skill
from profiles.models import Profile


class Exp(models.Model):
    MAX_LENGTH_TITLE = 60
    MAX_LENGTH_SUMMARY = 255

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    parent = models.ForeignKey("Project", on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=MAX_LENGTH_TITLE)
    summary = models.CharField(max_length=MAX_LENGTH_SUMMARY, blank=True, null=True)

    def __str__(self):
        return self.title + ": " + self.summary


class Project(Exp):
    date_ranges = ArrayField(DateRangeField(null=True), blank=True, null=True)


class Contribution(Exp):
    skills = models.ManyToManyField(Skill)
