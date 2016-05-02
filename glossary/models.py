from __future__ import unicode_literals

from django.db import models

class Acronym(models.Model):
    abbreviation = models.CharField(max_length=15)
    word = models.CharField(max_length=200)
