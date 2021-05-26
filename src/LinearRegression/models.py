from django.db import models

# Create your models here.
from django.db import models
from django.db.models import JSONField
# Create your models here.

class TrainedModel(models.Model): 
    UserId = models.IntegerField(unique=False,null=False)
    Trained_coefficients = JSONField(default=dict)


