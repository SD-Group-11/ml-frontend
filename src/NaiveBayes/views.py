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
    ## save the results into db
    return

def TestNaiveBayes(data,testdata,id,filename):
    ## fill in naive bayes training and testing 
    ## will be the same as TrainNaiveBayes except we also test because we have test data
    ## remember to save the results
    return
@api_view(['POST',])
@csrf_exempt

def PerformNaiveBayes(request):

    UserId = request.data['UserId']
    filename = request.data['filename']
    response ={}
    try:
        ##get the respective dataset they want to train on
        dataset = Dataset.objects.get(UserId = UserId, filename=json.dumps(filename),model = "Naive Bayes")

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

@api_view(['POST',])   ## ensures only POST requests can be made to the api
@csrf_exempt
## view to get meta data about each dataset
def getDatasetsInfo(request):

    response ={}
    UserId = request.data['UserId']
    try:
        i =0 
        ## filter for all the datasets associated with a User and linear regression
        AllDatasets = Dataset.objects.filter(UserId=UserId,model = "Naive Bayes")
        ## loop through the returned set and get the respective info
        for Obj in AllDatasets:
                
            dataAttributes = {}
           
            dataset = pd.read_json(Obj.data)
            i+=1
            dataAttributes['id'] = Obj.id
            dataAttributes['filename'] = json.loads(Obj.filename)
            dataAttributes['datapoints'] = dataset.shape[0] ## get the number of rows
            dataAttributes['columns'] = dataset.shape[1] ## number of columns/features
            dataAttributes['featureNames'] = list(dataset.columns)
            dataAttributes['nullValues'] = Obj.nullValues
            dataAttributes['created'] = Obj.created ## date created which automatically filled when object is created
            try:
                ## if we succed in finding the dataset, check if it was trained and return metrics from database
                ModelData = NaiveBayes.objects.get(UserId=Obj.UserId, filename=Obj.filename)
                dataAttributes['f1'] = ModelData.f1score
                dataAttributes['AUC'] = ModelData.AUCScore
                dataAttributes['TrainingAccuracy'] = ModelData.TrainingAccuracy
                dataAttributes['TestingAccuracy'] = ModelData.TestingAccuracy
            except:
                dataAttributes['Info'] = "Model not trained yet."
                ## if the model is not trained then just return the general info about the dataset
            response[i] = dataAttributes
            
        if( not response):
             response['error'] = "No datasets have been uploaded."
             return Response(response)

        return Response(response)

    except:

        response['error'] = "No datasets have been uploaded."
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
