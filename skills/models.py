from django.db import models


class Skill(models.Model):
    title = models.CharField(max_length=60, unique=True)

    def __str__(self):
        return self.title
