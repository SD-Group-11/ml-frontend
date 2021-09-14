import numpy as np
import pandas as pd
import json
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from datasets.models import Dataset
from rest_framework.response import Response 
# Create your views here.

@api_view(['POST',])
@csrf_exempt

def PerformNaiveBayes(request):

    UserId = request.data['UserId']
    filename = request.data['filename']
    response ={}
    try:
        ##get the respective dataset they want to train on
        dataset = Dataset.objects.get(UserId = UserId, filename=json.dumps(filename))

        ## need to use the dataset.data to train a model. Note that tolerance etc won't be used for Naive Bayes
    except:
        ## if we fail to find the file and user id , return this
        ## Should almost never happen since the filename is associated with their user id.
        response['response'] = "Failed to locate file "
        return Response(response)