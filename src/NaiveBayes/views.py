import numpy as np
import pandas as pd
import json
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from datasets.models import Dataset
from .models import NaiveBayes
from rest_framework.response import Response 
# Create your views here.

def TrainNaiveBayes(data,id,filename):
    ## fill in naive bayes training
    return

def TestNaiveBayes(data,testdata,id,filename):
    ## fill in naive bayes training
    return
@api_view(['POST',])
@csrf_exempt

def PerformNaiveBayes(request):

    UserId = request.data['UserId']
    filename = request.data['filename']
    response ={}
    try:
        ##get the respective dataset they want to train on
        dataset = Dataset.objects.get(UserId = UserId, filename=json.dumps(filename))

        ## Note that tolerance etc won't be used for Naive Bayes
        ## If test data is available, train and test together
        if(dataset.testData != {}): 
            results = TestNaiveBayes(pd.read_json(dataset.data),pd.read_json(dataset.testData),UserId,filename)
            ## add results to response and return it
        else:
            ## need to use the dataset.data to train a model.
            results = TrainNaiveBayes(pd.read_json(dataset.data),UserId,filename)
    except:
        ## if we fail to find the file and user id , return this
        ## Should almost never happen since the filename is associated with their user id.
        response['response'] = "Failed to locate file "
        return Response(response)
    
@api_view(['POST',])
@csrf_exempt
## View to check which datasets have been trained
def trained_datasets(request):
    UserId = request.data["UserID"]
    response ={}
    
    try:
        i = 1
        ##get queryset of all datasets where they occur in the TrainedModel db
        AllTrained = NaiveBayes.objects.filter(UserId=UserId)
        for Obj in AllTrained:
            response[i] = json.loads(Obj.filename)
            i+=1
        return Response(response)
    
    except:
        response['response'] = "No trained datasets"
        return Response(response)


@api_view(['POST',])
@csrf_exempt

def discard_training_results(request):
    id = request.data["UserID"]
    filename = request.data["Filename"]
    resp = {}
    try:
        ## try to locate the object and if it exists delete it
        Obj = NaiveBayes.objects.get(UserId=id,filename=json.dumps(filename))
        Obj.delete()
        resp['response'] = "Results discarded."
        return Response(resp)
    except:
        ## failing to locate object so we return a fail
        ## should never occur though
        resp['response'] = "Failed to delete results"
        return Response(resp)
