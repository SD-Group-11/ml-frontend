from distutils.util import split_quoted
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from .models import Dataset
import pandas as pd
import io
import json
from LinearRegression.views import linearRegression
import re
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

<<<<<<< HEAD
    # print(dataset)
    # print(df.head())
=======
    print(dataset)
    print(df.head())
 #   dataset = toJSON(data)
>>>>>>> ad44e4240a17fb3928ba25cc7e886d46d0a8674c
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
        print(dataset)
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

        userObj = Dataset.objects.get(UserId=UserId)
        if(userObj):
            i =0 
            for Obj in Dataset.objects.all():
                
                dataAttributes = {}
                if(Obj.UserId ==UserId):
                    dataset = pd.read_json(Obj.data)
                    i+=1
                    dataAttributes['id'] = Obj.id
                    dataAttributes['filename'] = Obj.filename
                    dataAttributes['datapoints'] = dataset.shape[0]
                    dataAttributes['columns'] = dataset.shape[1]
                    dataAttributes['featureNames'] = list(dataset.columns)
                    dataAttributes['null'] = Obj.nullValues
                    response[i] = dataAttributes
            
            return Response(response)


    except:

        response['error'] = "No datasets have been uploaded."


@api_view(['POST',])   ## ensures only POST requests can be made to the api
@csrf_exempt

def getDatasetData(request):

    UserId = request.data.get('UserId')
    filename = request.data.get('filename')
    resp = {}
<<<<<<< HEAD
    try:
        data = Dataset.objects.get(UserId=UserId, filename=filename)
        resp['data'] = data.data
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
    fileid = request.data['id']
    learningRate = request.data['learningRate']
    tol = request.data['tol']
    split = request.data['split']

    try:
        dataset = Dataset.objects.get(UserId = UserId,filename=json.dumps(filename))

        dataset.split = split
        dataset.learningRate = learningRate
        dataset.tol = tol
        dataset.save()

        ## fill in the code that uses LR model coded by Ballim and return response provided by it 

        ## I need to send in the dataset, learning rate, tol and split

        results  = linearRegression(dataset.UserId,dataset.filename,dataset.learningRate,dataset.tol,pd.read_json(dataset.data),dataset.split/100)

        resp['results'] = results
        return Response(resp)

    except:

        resp['error'] = 'Failed to find dataset associated with your account. Please try again'

        return Response(resp)

=======
    if request.method == "POST":
        filename = request.data['filename']
        id = request.data['id']
        obj = Dataset.objects.get(UserId=id, filename=json.dumps(filename))
        df = pd.read_json(obj.data)
        datapoints = len(df)
        columns  = len(df.columns)
        resp['datapoints'] = datapoints
        resp['columns'] = columns
        resp['filename'] = filename
    else:
        resp['error'] = "Failed to summarise data"

    return Response(resp)
>>>>>>> ad44e4240a17fb3928ba25cc7e886d46d0a8674c
