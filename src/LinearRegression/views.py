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
from scipy.sparse import data
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import SGDRegressor
from sklearn.metrics import r2_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler

#from sklearn.model_selection import train_test_split

# Create your views here.

def linearRegression(userid, filename, learningrate, tolerance, datafr, datasplit,y_column_name):
    TrainX=np.array([])
    TrainY=np.array([])
    TestX=np.array([])
    TestY=np.array([])
    x=np.array([])
    y=np.array([])

    #populating x and y
    y = datafr[:][y_column_name].to_numpy()
    datafr_x = datafr.drop([y_column_name],axis=1)
    x = datafr_x.to_numpy()


    #splitting data into testing and training 
    TrainX, TestX, TrainY, TestY=train_test_split(x,y,test_size=(1-datasplit))
    #scale the data so that SDG perfoms properly
    scaler = StandardScaler()
    scaler.fit(TrainX) # (from sklearn: Don't cheat - fit only on training data)
    TrainX = scaler.transform(TrainX)
    TestX = scaler.transform(TestX)  
        
    #Train the data
    if(learningrate=='auto' and tolerance=='auto'):
        sgdr=SGDRegressor()
    else:
        sgdr=SGDRegressor(learning_rate=learningrate,tol=tolerance)
    sgdr.fit(TrainX,TrainY)
    #Lr=LinearRegression().fit(TrainX,TrainY)

    #UploadResults(id,coefficients)

    #Predict y values from training data
    Train_PredictY = sgdr.predict(TrainX)

    #Train accuracy
    Train_accuracy = r2_score(TrainY, Train_PredictY)

    #coefficient of determination
    #accuracy= sgdr.score(TrainX,TrainY)

    #intercept
    intercept=sgdr.intercept_
    print(intercept)

    #coefficients
    coefficients=sgdr.coef_

    #Prediction
    Test_PredictY = sgdr.predict(TestX)
    # print(PredictY)

    #Confusion Matrix
    #confusionMatrix = confusion_matrix(TrainY, TestY)
    
    #Mean Squared Error
    meansquared=mean_squared_error(TestY,Test_PredictY)

    #accuracy
    #accuracy=accuracy_score(TestY, PredictY)

    #Test accuracy
    accuracy = sgdr.score(TestX, TestY)
    print("accuracy",accuracy)
    Test_accuracy= r2_score(TestY, Test_PredictY)

    #parse coefficients to json
    coef_json = ArrToJson(coefficients)
    #uploading
    uploadResults(userid,filename,coef_json)
    #parse all arrats to json
    jsonFeatures=FeatToJson(datafr)
    Test_PredictY_json = ArrToJson(Test_PredictY)
    Train_PredictY_json = ArrToJson(Train_PredictY)
    TrainX_json = ArrToJson(TrainX)
    TrainY_json = ArrToJson(TrainY)
    TestX_json = ArrToJson(TestX)
    TestY_json=ArrToJson(TestY)




    return jsonFeatures, coef_json,TrainX_json,TrainY_json,TestX_json,TestY_json,Train_PredictY_json,Test_PredictY_json,Train_accuracy,Test_accuracy, meansquared

def uploadResults(id, filename,coef):
    DataInstance = TrainedModel(UserId=id,filename=filename,Trained_coefficients=coef)
    DataInstance.save()

def FeatToJson(x):
    column_names = list(x.columns)
    JSON = {}
    JSON['0'] = column_names
    for k in range(1,len(column_names)+1):
        # JSON[str(column_names)]=x[k]
        JSON[str(k)] = x[:][column_names[k-1]]

    
    return JSON
def ArrToJson(x):
    JSON = {}
    for k in range(len(x)):
        JSON[str(k)] = x[k]
    return JSON

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
        userid = request.data["id"]
        datasplit = float(request.data["datasplit"])
       
        if (request.data.get("y_column_name")!= None):
             y_column_name = request.data["y_column_name"] #let the user choose a y column if no value is given we assume that the y column is called target
        else:
            y_column_name = 'target'

        if(request.data.get("learningrate")!= None):#get learning rate if specified
            learningrate = request.data["learningrate"]
        else:
            learningrate = 'auto'
        if(request.data.get("tolerance")!= None):#get tolerance if specified
            tolerance = request.data["tolerance"]
        else:
            tolerance ='auto'
        #get
        datasetObj = Dataset.objects.get(UserId=userid, filename=filename)
        data_df= pd.read_json(datasetObj.data)#convert the json to a dataframe
        data_df = data_df.select_dtypes("number")#drop any non numeric values from the dataset
        jsonFeatures, coef_json,TrainX_json,TrainY_json,TestX_json,TestY_json,Train_PredictY_json,Test_PredictY_json,Train_accuracy,Test_accuracy, meansquared = linearRegression(userid, filename, learningrate, tolerance, data_df, datasplit,y_column_name)
        resp['jsonFeatures'] = jsonFeatures
        resp['coefficients'] = coef_json
        resp['TrainX'] = TrainX_json
        resp['TrainY'] = TrainY_json
        resp['TestX'] =TestX_json
        resp['TestY'] = TestY_json
        resp['Train_PredictY'] = Train_PredictY_json
        resp['Test_PredictY'] = Test_PredictY_json
        resp['Test_accuracy'] = Test_accuracy
        resp['Train_accuracy'] = Train_accuracy
        resp['meansquared'] = meansquared
        return Response(resp)


