from django.db import models
from django.contrib.postgres.fields import ArrayField, DateRangeField
from skills.models import Skill
from profiles.models import Profile


class Exp(models.Model):
    MAX_LENGTH_TITLE = 60
    MAX_LENGTH_SUMMARY = 255

    title = models.CharField(max_length=MAX_LENGTH_TITLE)
    summary = models.CharField(max_length=MAX_LENGTH_SUMMARY, blank=True, null=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title + ": " + self.summary


class Project(Exp):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="projects", blank=True, null=True)
    parent = models.ForeignKey("Project", on_delete=models.CASCADE, blank=True, null=True)
    date_ranges = ArrayField(DateRangeField(null=True), blank=True, null=True)


class Contribution(Exp):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="contributions", blank=True, null=True)
    parent = models.ForeignKey("Project", on_delete=models.CASCADE, blank=True, null=True)
    skills = models.ManyToManyField(Skill)


TIME_SPAN_FREQS = (
    ('F', 'Full Time'),
    ('P', 'Part Time')
)


# class TimeSpan(models.Model):
#     exp = models.ForeignKey(Exp, on_delete=models.CASCADE)
#
#     frequency = models.CharField(max_length=255, choices=TIME_SPAN_FREQS)
#
#     start_year = models.IntegerField()
#     start_month = models.IntegerField()
#     start_day = models.IntegerField(blank=True, null=True)
#
#     start_canonical = models.DateField()
#
#     end_canonical = models.DateField()
#     end_year = models.IntegerField()
#     end_month = models.IntegerField()
#     end_day = models.IntegerField(blank=True, null=True)
