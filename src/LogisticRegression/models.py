from django.db import models

# Create your models here.

class LogisticTrainedModel(models.Model): 
    UserId = models.IntegerField(unique=False,null=False)
    filename = models.CharField(max_length=300)
    TrainingAccuracy = models.DecimalField(max_digits=19,decimal_places=10,null=True)
    f1score = models.JSONField(default=dict,null=True)
    AUCScore = models.JSONField(default=dict,null=True)
    TestingAccuracy = models.DecimalField(max_digits=19,decimal_places=10,null=True)



    class Meta:
        unique_together = (('UserId', 'filename'),)