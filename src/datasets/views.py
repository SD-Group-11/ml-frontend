from distutils.util import split_quoted
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from .models import Dataset
import json
from LinearRegression.views import linearRegression,TrainingLinearRegression
from LinearRegression.models import TrainedModel
import numpy as np
import pandas as pd
import io
# Create your views here.

def filterData(dataset):
    newd = dataset.split(r'\n')  # split the string by the new line character 
    data = newd[4:-11]
    data_str = "\n".join(data)
    data_str = data_str.replace(r'\r', '')
    data_io = io.StringIO(data_str)
    df = pd.read_csv(data_io, sep=",")
    dataset = pd.DataFrame.to_json(df)

    num = newd[len(newd)-7]
    id = int(num[:len(num)-2])
    filename = newd[1][newd[1].find('filename=')+9:len(newd[1])-2]
    nullValues =  df.isnull().sum().sum()
    model =  newd[len(newd) - 3].replace(r'\r', '')
    return id,filename,dataset,nullValues,model

## same as filterData just adjusted indices to account for the appended filename 
def filterTestData(dataset):
    newd = dataset.split(r'\n')  # split the string by the new line character 
    data = newd[4:-15]
    data_str = "\n".join(data)
    data_str = data_str.replace(r'\r', '')
    ##print(data_str)
    data_io = io.StringIO(data_str)
    df = pd.read_csv(data_io, sep=",")
    dataset = pd.DataFrame.to_json(df)
    print(newd)
    num = newd[len(newd)-11]
    id = int(num[:len(num)-2])
    filename = newd[len(newd)-7].replace(r'\r', '')
    nullValues =  df.isnull().sum().sum()
    model = newd[len(newd)-3].replace(r'\r', '')
    return id,filename,dataset,nullValues,model


@api_view(['POST',])   ## ensures only POST requests can be made to the api
@csrf_exempt

def receiveData(request):

    resp = {}
    if request.method == "POST":
        
        dataset = str(request.body)
        ## check dataset is not empty
        if(dataset != ''):
            ## filter the data and get these values from the string
            id,filename,dataset,nullValues,ModelName = filterData(dataset)
            obj = None
            try:
                ## check if user already has a file with that name, if so then return it
                obj =  Dataset.objects.get(UserId = id, filename=filename,model =ModelName)
                resp['response'] = "A dataset with that name already exists"
                return Response(resp)
            except:
                ##if no dataset with the name , then try to create the dataset
                try:
                    DataInstance = Dataset(UserId=id, filename=filename,model=ModelName, data=dataset,nullValues=nullValues)
                    DataInstance.save()
                    resp['response'] ='Data Uploaded Successfully'
                    return Response(resp)
                except:
                    ##failure to upload. Should never occur unless data is in the incorrect format
                    resp['response'] ='Failed to upload data'
                    return Response(resp)

        else:
            resp['response'] ='The dataset is empty!'
    
    resp['response'] ='Failed to upload data'
    
        

    return Response(resp)

@api_view(['POST',])   ## ensures only POST requests can be made to the api
@csrf_exempt
def receive_TestData(request):
    ## same as receive data just that the string coming in has some extra info we need to filter for
    dataset = str(request.body)
    response = {}
    if(dataset != ''):
        
        id,filename,testData,nullValues,ModelName = filterTestData(dataset)
        try:
            ## find inital dataset and this new data to the test field
            Obj = Dataset.objects.get(UserId=id, filename=json.dumps(filename),model=ModelName)
            Obj.testData = testData
            Obj.save()
            response['response'] = "Successfully uploaded test data."
            return Response(response)
        except:
            response['response'] = "Failed to locate corresponding training dataset."
            return Response(response)

##json.dumps adds "" to a string
@api_view(['POST',])   ## ensures only POST requests can be made to the api
@csrf_exempt
## view to get meta data about each dataset
def getDatasetsInfo(request):

    response ={}
    UserId = request.data['UserId']
    try:
        i =0 
        ## filter for all the datasets associated with a User and linear regression
        AllDatasets = Dataset.objects.filter(UserId=UserId,model = "Linear Regression")
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
                ModelData = TrainedModel.objects.get(UserId=Obj.UserId, filename=Obj.filename)
                dataAttributes['MSE'] = ModelData.meanSquaredError
                dataAttributes['TrainAccuracy'] = ModelData.TrainCoeffDetermination
                dataAttributes['TestAccuracy'] = ModelData.TestCoeffDetermination
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


@api_view(['POST',])   ## ensures only POST requests can be made to the api
@csrf_exempt

def getDatasetData(request):

    ## just a view that gets the data in the dataset and returns in a specific format, to populate search table in frontend 
    UserId = request.data.get('UserId')
    filename = request.data.get('filename')
    ModelName = request.data.get('ModelName')
    resp = {}
   
    try:
        data = Dataset.objects.get(UserId=UserId, filename=json.dumps(filename),model =ModelName)
        dataframe = pd.read_json(data.data)
        dataframe =  dataframe.dropna()
        jsonRowData = dataframe.to_dict(orient='records')
        # print(json.dumps(jsonRowData))
        resp['data'] = jsonRowData
        return Response(resp)

    except:
        resp['error'] = "Failed to load dataset. Please try again"
        return Response(resp)



@api_view(['POST',])   ## ensures only POST requests can be made to the api
@csrf_exempt

def doLinearRegression(request):
    
    resp ={}
    UserId = request.data['UserId']
    filename = request.data['filename']
    learningRate = request.data['learningRate']
    tol = request.data['tol']
    
    try:
        ## locate dataset object and if the tolerance and learning rate are empty strings then set them to auto in the db and use general in regression function
        dataset = Dataset.objects.get(UserId = UserId,filename=json.dumps(filename),model = "Linear Regression")
        if(tol ==''):
            tol = "auto"
        if(learningRate ==''):
            learningRate = "auto"

        dataset.tol = json.dumps(tol)
        dataset.learningRate = json.dumps(learningRate)
        dataset.save()

                    ## fill in the code that uses LR model coded by Ballim and return response provided by it 

                    ## I need to send in the dataset, learning rate, tol and split
        results =[]
        ## when no test data has been uploaded train on full training data
        if(dataset.testData == {}): 
            results = TrainingLinearRegression(dataset.UserId,dataset.filename,dataset.learningRate,dataset.tol,pd.read_json(dataset.data))
            ## below is everything returned for training data . Metrics etc
            resp['jsonFeatures'] = results[0]
            resp['coefficients'] = results[1]
            resp['TrainX'] = results[2]
            resp['TrainY'] = results[3]
            resp['Train_PredictY'] = results[4]
            resp['Train_accuracy'] = results[5]
            resp["Intercept"] = results[6]

        else:
            ## test data uploaded, then train again and test this time 
            results  = linearRegression(dataset.UserId,dataset.filename,dataset.learningRate,dataset.tol,pd.read_json(dataset.data),pd.read_json(dataset.testData))
            ##results for training and testing used in front end for the reports etc
            resp['jsonFeatures'] = results[0]
            resp['coefficients'] = results[1]
            resp['TrainX'] = results[2]
            resp['TrainY'] = results[3]
            resp['TestX'] = results[4]
            resp['TestY'] = results[5]
            resp['Train_PredictY'] = results[6]
            resp['Test_PredictY'] = results[7]
            resp['Test_accuracy'] = results[8]
            resp['Train_accuracy'] = results[9]
            resp['meansquared'] = results[10]
            resp["Intercept"] = results[11]

        return Response(resp)

    except:

        resp['error'] = 'Failed to perform Training.'

        return Response(resp)


@api_view(['POST',])   ## ensures only POST requests can be made to the api
@csrf_exempt

def delete_dataset(request):

    UserId = request.data["UserID"]
    filename = request.data["Filename"]
    ModelName = request.data["ModelName"]
    response ={}
    try:
        ## get dataset to be deleted in the db
        dataset = Dataset.objects.get(UserId = UserId, filename=json.dumps(filename),model =ModelName)
        try:
            ## if model was trained on , get that data as well and delete it
            Obj = TrainedModel.objects.get(UserId=UserId, filename=json.dumps(filename))
            Obj.delete()
        except:
            pass
        ##delete dataset
        dataset.delete()
        response['success'] = "Dataset Successfully deleted."

        return Response(response)
    except:
        response['error'] = "Failed to delete dataset."
        return Response(response)


@api_view(['POST',])   ## ensures only POST requests can be made to the api
@csrf_exempt

def getTrainedDatasets(request):
## View to return all the datasets that training has been performed on
    UserId = request.data["UserID"]
    response ={}
    
    try:
        i = 1
        ##get queryset of all datasets where they occur in the TrainedModel db
        AllTrained = TrainedModel.objects.filter(UserId=UserId)
        for Obj in AllTrained:
            response[i] = json.loads(Obj.filename)
            i+=1
        return Response(response)
    
    except:
        response['response'] = "No trained datasets"
        return Response(response)

@api_view(['POST',])   ## ensures only POST requests can be made to the api
@csrf_exempt

def check_if_test_data_is_available(request):
## given the composite PK, check if the user has uploaded test data
    UserId = request.data["UserID"]
    filename = request.data["Filename"]
    ModelName = request.data["ModelName"]
    response = {}
    try:
        ## get dataset object
        Obj = Dataset.objects.get(UserId=UserId, filename=json.dumps(filename),model = ModelName)
        ## if test data field is empty dict then return no test data
        if(Obj.testData != {}): 
            response['response'] = "Test Data exists"
        else:
            response['response'] = "Test Data does not exist"

        return Response(response)
    
    except:
        response['response'] = "Failed"
        return Response(response)