# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Event(models.Model):
    """docstring for Event."""
    types = (
        ('s','Self'),
        ('g','Group'),
        ('c','Cooperate'),
        ('o','Others')
    )
    full_name = models.CharField(max_length=100, blank=False, null=False)
    mobile = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(max_length=100, blank=False, null=False)
    idCard = models.ImageField(blank=False, null=False)
    type = models.CharField(choices=types, default='s', max_length=2)
    tickets = models.FloatField(default=1)
    created_at = models.DateTimeField(blank=False, null=False, auto_now=True)

    def __init__(self, arg):
        super(Event, self).__init__()
        self.arg = arg
