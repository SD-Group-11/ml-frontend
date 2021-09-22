from django.db import models

# Create your models here.
from django.db import models
from django.db.models import JSONField
# Create your models here.

#Class for storing the trained model after NB has been run. 
# Uses a compound primary key of UserId and filename 
class NaiveBayes(models.Model): 
    UserId = models.IntegerField(unique=False,null=False)
    filename = models.CharField(max_length=300)
    TrainingAccuracy = JSONField(default=dict,null=True)
    TestingAccuracy = models.DecimalField(max_digits=19,decimal_places=10,null=True)
    f1score = models.DecimalField(max_digits=19,decimal_places=10,null=True)
    AUCScore = models.DecimalField(max_digits=19,decimal_places=10,null=True)



    class Meta:
        unique_together = (('UserId', 'filename'),)

