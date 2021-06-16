from django.db import models
from django.db.models import JSONField
# Create your models here.

class Dataset(models.Model):
    UserId = models.IntegerField(unique=False,null=False)
    filename = models.CharField(max_length=300)
    split = models.IntegerField(null=True)
    learningRate = models.CharField(max_length = 300,null=True)
    tol = models.CharField(max_length=300,null=True)
    data = JSONField(default=dict)
    nullValues = models.IntegerField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        unique_together = (('UserId', 'filename'),)