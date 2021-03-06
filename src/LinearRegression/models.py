from django.db import models

# Create your models here.
from django.db import models
from django.db.models import JSONField
# Create your models here.

#Class for storing the trained model after LR has been run. 
# Uses a compound primary key of UserId and filename 
class TrainedModel(models.Model): 
    UserId = models.IntegerField(unique=False,null=False)
    filename = models.CharField(max_length=300)
    Trained_coefficients = JSONField(default=dict,null=True)
    meanSquaredError = models.DecimalField(max_digits=19,decimal_places=10,null=True)
    TrainCoeffDetermination = models.DecimalField(max_digits=19,decimal_places=10,null=True)
    TestCoeffDetermination = models.DecimalField(max_digits=19,decimal_places=10,null=True)


    class Meta:
        unique_together = (('UserId', 'filename'),)

