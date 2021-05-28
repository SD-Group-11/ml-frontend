from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from datasets.models import Dataset
from .models import TrainedModel
import json

#ml imports
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Create your views here.

def linearRegression(id, data, testdata):
    TrainX=np.array([])
    TrainY=np.array([])
    TestX=np.array([])
    TestY=np.array([])

    for x in len(data):
        TrainX[x]=data[x][0]
        TrainY[x]=data[x][1]
    
    for x in len(testdata):
        TestX[x]=data[x][0]
        TestY[x]=data[x][1]
    
    Lr = LinearRegression()
    coefficients=Lr.fit(TrainX,TrainY)
    UploadResults(id,coefficients)
    PredictY = Lr.predict(TestX)
    confusionMatrix = metrics.confusion_matrix(TestY,PredictY)
    accuracy = metrics.accuracy_score(TestY,PredictY)

    return coefficients, confusionMatrix, accuracy


def uploadResults(id,filename,coefficients):
    DataInstance = TrainedModel(UserId=id,filename=filename,Trained_Coefficients=coefficients)
    DataInstance.save()


@api_view(['POST',]) 
@csrf_exempt
#This function will be called to run the Linear Regression the request body should conatin:
#The dataset filename
#the user id 
#the name of the y column
def runLR(request): 
    resp = {}
    if request.method == "POST":
        #get request variables
        filename = request.data["filename"]
        userId = request.data["id"]
        y_column_name = request.data["y_column"]
        #get

        datasetObj = Dataset.objects.get(UserId=userId, filename=filename)
        data_df= LinearRegression2(datasetObj.data,y_column_name)

        resp['response'] ="Hello World"
        resp['data'] = data_df
        resp['dataset'] = datasetObj.data
        return Response(resp["dataset"])

def LinearRegression2(dataset, y_column_name):#this function assumes that all columns(other then taget columns) are used for multivariable LR
    df_json = json.dumps(dataset)#convert the dataset dict to a json object
    data_df = pd.read_json(df_json)#load the dataset using pandas
    data_df = data_df.T
    data_df = data_df.select_dtypes(['number']) #use only the columns with numeric values
    #data_df = data_df.drop(["No"],axis=1) #drop the column numbers column

  # x_values =data_df
    # y_values = data_df[:][""]
    # x_values =data_df
    # y_values = data_df[:][""]


    return data_df
