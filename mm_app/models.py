# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Mood(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    mood = models.CharField(max_length=250)
    reason = models.CharField(max_length=250)
    date_feedback = models.DateTimeField(auto_now_add=True, auto_now=False)
    update_date = models.DateTimeField(auto_now_add=False, auto_now=True)

