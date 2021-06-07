from django.db import models

# Create your models here.
from django.db import models
from django.db.models import JSONField
# Create your models here.

#Class for storing the trained model after LR has been run. 
# Uses a compound primary key of UserId and filename 
class TrainedModel(models.Model): 
    UserId = models.IntegerField(unique=False,null=False)
    filename = models.CharField(max_length=300,default="defualt")
    Trained_coefficients = JSONField(default=dict)


