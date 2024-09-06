from django.db import models
import uuid

class Users(models.Model):
    id = models.AutoField(primary_key=True,)
    name = models.CharField(blank=True, max_length=20)
    password = models.CharField(blank=True, max_length=200)
