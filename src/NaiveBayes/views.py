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
            response['confusionMatrix'] = [
                {
                    "class":'Class 1',
                    "predictions": [12,23,21] #array must be in same order as classes 
                    #i.e preditctions[0] is the is the number of Class 1 datapoints that were identified as class 1 
                    #and predictions[1] is the number of class 2 datapoints that were identified as class 2


                },
                {
                    "class":'Class 2',
                    "predictions": [53,20,10]

                    
                },
                {
                    "class":'Class 3',
                    "predictions": [34,28,40]

                    
                } 
            ]
            response['f1Score'] = 0.1
            response['AUC'] = 0.3  
            #x and y points for the ROC curve
            response['ROC'] = [
                {
                "class":"class 1",
                "fpr_values":[0.0 ,0.0 ,0.0 ,0.0196078431372549 ,0.0196078431372549 ,0.0784313725490196 ,0.0784313725490196 ,0.09803921568627451 ,0.09803921568627451 ,0.11764705882352941 ,0.11764705882352941 ,0.13725490196078433 ,0.13725490196078433 ,0.1568627450980392 ,0.1568627450980392 ,0.17647058823529413 ,0.17647058823529413 ,0.3137254901960784 ,0.3137254901960784 ,0.3333333333333333 ,0.3333333333333333 ,0.35294117647058826 ,0.35294117647058826 ,0.4117647058823529 ,0.4117647058823529 ,0.45098039215686275 ,0.45098039215686275 ,0.47058823529411764 ,0.47058823529411764 ,0.5098039215686274 ,0.5098039215686274 ,0.5686274509803921 ,0.5686274509803921 ,1.0],
                "tpr_values":[0.0 ,0.041666666666666664 ,0.125 ,0.125 ,0.25 ,0.25 ,0.2916666666666667 ,0.2916666666666667 ,0.3333333333333333 ,0.3333333333333333 ,0.4166666666666667 ,0.4166666666666667 ,0.5 ,0.5 ,0.5416666666666666 ,0.5416666666666666 ,0.5833333333333334 ,0.5833333333333334 ,0.7083333333333334 ,0.7083333333333334 ,0.75 ,0.75 ,0.7916666666666666 ,0.7916666666666666 ,0.8333333333333334 ,0.8333333333333334 ,0.875 ,0.875 ,0.9166666666666666 ,0.9166666666666666 ,0.9583333333333334 ,0.9583333333333334 ,1.0 ,1.0 ]
                },
                {
                "class":"class 1",
                "fpr_values":[0.0 ,0.0 ,0.0 ,0.022222222222222223 ,0.022222222222222223 ,0.1111111111111111 ,0.1111111111111111 ,0.17777777777777778 ,0.17777777777777778 ,0.2 ,0.2 ,0.24444444444444444 ,0.24444444444444444 ,0.26666666666666666 ,0.26666666666666666 ,0.37777777777777777 ,0.37777777777777777 ,0.4222222222222222 ,0.4222222222222222 ,0.4888888888888889 ,0.4888888888888889 ,0.5555555555555556 ,0.5555555555555556 ,0.6222222222222222 ,0.6222222222222222 ,0.6444444444444445 ,0.6444444444444445 ,0.6666666666666666 ,0.6666666666666666 ,0.7333333333333333 ,0.7333333333333333 ,0.7555555555555555 ,0.7555555555555555 ,0.8888888888888888 ,0.8888888888888888 ,1.0],
                "tpr_values":[0.0 ,0.03333333333333333 ,0.13333333333333333 ,0.13333333333333333 ,0.16666666666666666 ,0.16666666666666666 ,0.2 ,0.2 ,0.26666666666666666 ,0.26666666666666666 ,0.3333333333333333 ,0.3333333333333333 ,0.4 ,0.4 ,0.43333333333333335 ,0.43333333333333335 ,0.5 ,0.5 ,0.5666666666666667 ,0.5666666666666667 ,0.6 ,0.6 ,0.6333333333333333 ,0.6333333333333333 ,0.7 ,0.7 ,0.7333333333333333 ,0.7333333333333333 ,0.9 ,0.9 ,0.9333333333333333 ,0.9333333333333333 ,0.9666666666666667 ,0.9666666666666667 ,1.0 ,1.0]
                }
            ]
            
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
