# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime, timedelta

class Todo(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.TextField()
    created_date = models.DateTimeField(editable=False,default=datetime.now())
