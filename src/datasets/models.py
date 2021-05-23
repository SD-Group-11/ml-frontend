from django.db import models
from django.db.models import JSONField
# Create your models here.

class Dataset(models.Model):
    UserId = models.IntegerField(unique=False,null=False)
    filename = models.CharField(max_length=300)
    data = JSONField(default=dict)
   