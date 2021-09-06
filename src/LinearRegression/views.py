import numpy as np
import pandas as pd
import json
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response 
from sklearn.linear_model import SGDRegressor
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
from .models import TrainedModel
from sklearn.preprocessing import StandardScaler


# Create your views here.
def TrainingLinearRegression(userid, filename, learningrate, tolerance, datafr):
    TrainX=np.array([])
    TrainY=np.array([])
    x=np.array([])
    y=np.array([])
    datafr =  datafr.dropna()
    print(np.shape(datafr))
    data = datafr.to_numpy()
    data=data.transpose()
    #populating x and y
    x=np.array(data[0:len(data)-1])
    y=np.array(data[len(data)-1])
    x = np.transpose(x)
    TrainX = x
    TrainY = y
    #scale the data so that SDG perfoms properly
    scaler = StandardScaler()
    scaler.fit(TrainX) # (from sklearn: Don't cheat - fit only on training data)
    TrainX = scaler.transform(TrainX)
    
    if(json.loads(learningrate)=='auto' and json.loads(tolerance)=='auto'):
        sgdr=SGDRegressor()
    else:
        sgdr=SGDRegressor(alpha=float(json.loads(learningrate)),tol=float(json.loads(tolerance)))

    sgdr.fit(TrainX,TrainY)
    # Predict y values from training data
    Train_PredictY = sgdr.predict(TrainX)
   
    #Train accuracy
    Train_accuracy = r2_score(TrainY, Train_PredictY)
  


    #intercept
    intercept=sgdr.intercept_
  
    Intercept = ArrToJson(intercept)
    #coefficients
    coefficients=sgdr.coef_
     #parse coefficients to json
    coef_json = ArrToJson(coefficients)
    jsonFeatures=FeatToJson(datafr)
    Train_PredictY_json = ArrToJson(Train_PredictY)
    TrainX_json = ArrToJson(TrainX)
    TrainY_json = ArrToJson(TrainY)
    UploadTrainingResults(userid,filename,coef_json,Train_accuracy)
    return jsonFeatures, coef_json,TrainX_json,TrainY_json,Train_PredictY_json,Train_accuracy, Intercept


def linearRegression(userid, filename, learningrate, tolerance, datafr,testdata):
    TrainX=np.array([])
    TrainY=np.array([])
    TestX=np.array([])
    TestY=np.array([])
    x=np.array([])
    y=np.array([])
    datafr =  datafr.dropna()
    ##testdata = testdata.dropna()
    print(np.shape(datafr))
    data = datafr.to_numpy()
    data=data.transpose()
    
    #populating x and y
    x=np.array(data[0:len(data)-1])
    y=np.array(data[len(data)-1])
    x = np.transpose(x)
    TrainX = x
    TrainY = y
    #scale the data so that SDG perfoms properly
    scaler = StandardScaler()
    scaler.fit(TrainX) # (from sklearn: Don't cheat - fit only on training data)
    TrainX = scaler.transform(TrainX)
    # TestX = scaler.transform(TestX)  
    
    if(json.loads(learningrate)=='auto' and json.loads(tolerance)=='auto'):
        sgdr=SGDRegressor()
    else:
        sgdr=SGDRegressor(alpha=float(json.loads(learningrate)),tol=float(json.loads(tolerance)))

    sgdr.fit(TrainX,TrainY)
    # Predict y values from training data
    Train_PredictY = sgdr.predict(TrainX)
   
    #Train accuracy
    Train_accuracy = r2_score(TrainY, Train_PredictY)
  


    #intercept
    intercept=sgdr.intercept_
  
    Intercept = ArrToJson(intercept)
    #coefficients
    coefficients=sgdr.coef_
     #parse coefficients to json
    coef_json = ArrToJson(coefficients)
    jsonFeatures=FeatToJson(datafr)
    Train_PredictY_json = ArrToJson(Train_PredictY)
    TrainX_json = ArrToJson(TrainX)
    TrainY_json = ArrToJson(TrainY)
    ## The User has not uploaded test data
    

    testdata.dropna()
    Test = testdata.to_numpy()
    Test = Test.transpose()
    TestX=np.array(Test[0:len(Test)-1])
    TestY=np.array(Test[len(Test)-1])
    TestX = np.transpose(TestX)
    TestX = scaler.transform(TestX)  
    #Prediction
    Test_PredictY = sgdr.predict(TestX)
    #Mean Squared Error
    meansquared=mean_squared_error(TestY,Test_PredictY)
    #Test accuracy
    Test_accuracy= r2_score(TestY, Test_PredictY)
    Test_PredictY_json = ArrToJson(Test_PredictY)
    TestX_json = ArrToJson(TestX)
    TestY_json=ArrToJson(TestY)
    #uploading
    uploadResults(userid,filename,coef_json,Train_accuracy,Test_accuracy,meansquared)
    return jsonFeatures, coef_json,TrainX_json,TrainY_json,TestX_json,TestY_json,Train_PredictY_json,Test_PredictY_json,Train_accuracy,Test_accuracy, meansquared, Intercept

##View to discard results
@api_view(['POST',])
@csrf_exempt
def discard_training_results(request):
    id = request.data["UserID"]
    filename = request.data["Filename"]
    resp = {}
    try:
        Obj = TrainedModel.objects.get(UserId=id,filename=json.dumps(filename))
        Obj.delete()
        resp['response'] = "Results discarded."
        return Response(resp)
    except:
        resp['response'] = "Failed to delete results"
        return Response(resp)

    
def UploadTrainingResults(userid,filename,coef,TrainAcc):
    try:
        DataInstance = TrainedModel(UserId=userid,filename=filename,Trained_coefficients=coef,TrainCoeffDetermination = TrainAcc)
        DataInstance.save()
    except:
        obj = TrainedModel.objects.get(UserId=userid, filename=filename)
        obj.Trained_coefficients = coef
        obj.TrainCoeffDetermination = TrainAcc
        obj.save()

def uploadResults(id, filename,coef,TrainAcc,TestAcc,MSE):
    try:
        DataInstance = TrainedModel(UserId=id,filename=filename,Trained_coefficients=coef,TrainCoeffDetermination = TrainAcc,TestCoeffDetermination=TestAcc,meanSquaredError = MSE)
        DataInstance.save()
    except:
        obj = TrainedModel.objects.get(UserId=id, filename=filename)
        obj.Trained_coefficients = coef
        obj.TrainCoeffDetermination = TrainAcc
        obj.TestCoeffDetermination = TestAcc
        obj.meanSquaredError = MSE
        obj.save()

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
