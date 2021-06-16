from distutils.util import split_quoted
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from .models import Dataset
import json
from LinearRegression.views import linearRegression
from LinearRegression.models import TrainedModel
import numpy as np
import pandas as pd
import io
# Create your views here.

def filterData(dataset):
    newd = dataset.split(r'\n')  # split the string by the new line character 
    data = newd[4:-7]
    data_str = "\n".join(data)
    data_str = data_str.replace(r'\r', '')
    data_io = io.StringIO(data_str)
    df = pd.read_csv(data_io, sep=",")
    dataset = pd.DataFrame.to_json(df)

    # print(dataset)
    # print(df.head())
    result = df.to_json(orient="split")
    num = newd[len(newd)-3]
    id = int(num[:len(num)-2])
    filename = newd[1][newd[1].find('filename=')+9:len(newd[1])-2]
    nullValues =  df.isnull().sum().sum()
    return id,filename,dataset,nullValues

@api_view(['POST',])   ## ensures only POST requests can be made to the api
@csrf_exempt

def receiveData(request):

    resp = {}
    if request.method == "POST":
        
        dataset = str(request.body)
        if(dataset != ''):
            id,filename,dataset,nullValues = filterData(dataset)
            obj = None
            try:
                obj =  Dataset.objects.get(UserId = id, filename=filename)
                resp['response'] = "A dataset with that name already exists"
                return Response(resp)
            except:
                try:
                    DataInstance = Dataset(UserId=id, filename=filename, data=dataset,nullValues=nullValues)
                    DataInstance.save()
                    resp['response'] ='Data Uploaded Successfully'
                    return Response(resp)
                except:
                    resp['response'] ='Failed to upload data'
                    return Response(resp)

        else:
            resp['response'] ='The dataset is empty!'
    
    resp['response'] ='Failed to upload data'
    
        

    return Response(resp)

@api_view(['POST',])   ## ensures only POST requests can be made to the api
@csrf_exempt
def getDatasetsInfo(request):

    response ={}
    UserId = request.data['UserId']
    try:
        i =0 
        for Obj in Dataset.objects.all():
                
            dataAttributes = {}
            if(Obj.UserId ==UserId):
                dataset = pd.read_json(Obj.data)
                i+=1
                dataAttributes['id'] = Obj.id
                dataAttributes['filename'] = json.loads(Obj.filename)
                dataAttributes['datapoints'] = dataset.shape[0]
                dataAttributes['columns'] = dataset.shape[1]
                dataAttributes['featureNames'] = list(dataset.columns)
                dataAttributes['nullValues'] = Obj.nullValues
                try:
                    ModelData = TrainedModel.objects.get(UserId=Obj.UserId, filename=Obj.filename)
                    dataAttributes['MSE'] = ModelData.meanSquaredError
                    dataAttributes['TrainAccuracy'] = ModelData.TrainCoeffDetermination
                    dataAttributes['TestAccuracy'] = ModelData.TestCoeffDetermination
                except:
                    dataAttributes['Info'] = "Model not trained yet."
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

    UserId = request.data.get('UserId')
    filename = request.data.get('filename')
    resp = {}
   
    try:
        data = Dataset.objects.get(UserId=UserId, filename=json.dumps(filename))
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
    split = request.data['split']
    
    try:
        dataset = Dataset.objects.get(UserId = UserId,filename=json.dumps(filename))
        if(tol ==''):
            tol = "auto"
        if(learningRate ==''):
            learningRate = "auto"

        dataset.tol = json.dumps(tol)
        dataset.learningRate = json.dumps(learningRate)
        dataset.split = split
        dataset.save()

                    ## fill in the code that uses LR model coded by Ballim and return response provided by it 

                    ## I need to send in the dataset, learning rate, tol and split
        print("My view working")
        results  = linearRegression(dataset.UserId,dataset.filename,dataset.learningRate,dataset.tol,pd.read_json(dataset.data),int(dataset.split)/100)
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

