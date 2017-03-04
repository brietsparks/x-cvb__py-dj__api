from django.db import models
from skills.models import Skill

class Person(models.Model):
    skills = models.ManyToManyField(Skill)
