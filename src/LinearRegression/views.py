import numpy as np
import pandas as pd
import json
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import SGDRegressor
from sklearn.metrics import r2_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import mean_squared_error
from .models import TrainedModel
from sklearn.preprocessing import StandardScaler
import time
#from sklearn.model_selection import train_test_split

# Create your views here.

def linearRegression(userid, filename, learningrate, tolerance, datafr, datasplit):
    TrainX=np.array([])
    TrainY=np.array([])
    TestX=np.array([])
    TestY=np.array([])
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
    #splitting data into testing and training 
    TrainX, TestX, TrainY, TestY=train_test_split(x,y,test_size=(1-datasplit))
    #scale the data so that SDG perfoms properly
    scaler = StandardScaler()
    scaler.fit(TrainX) # (from sklearn: Don't cheat - fit only on training data)
    TrainX = scaler.transform(TrainX)
    TestX = scaler.transform(TestX)  
    #Train the 
    
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
    print(Intercept)
    #coefficients
    coefficients=sgdr.coef_

    #Prediction
    Test_PredictY = sgdr.predict(TestX)
  
   
    
    #Mean Squared Error
    meansquared=mean_squared_error(TestY,Test_PredictY)
  
    #accuracy
    #accuracy=accuracy_score(TestY, PredictY)

    #Test accuracy
    accuracy = sgdr.score(TestX, TestY)
    # print("accuracy",accuracy)
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




    return jsonFeatures, coef_json,TrainX_json,TrainY_json,TestX_json,TestY_json,Train_PredictY_json,Test_PredictY_json,Train_accuracy,Test_accuracy, meansquared, Intercept

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