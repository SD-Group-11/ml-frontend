import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import SGDRegressor
from sklearn.metrics import r2_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import mean_squared_error
from .models import TrainedModel
#from sklearn.model_selection import train_test_split

# Create your views here.

def linearRegression(userid, filename, learningrate, tolerance, datafr, datasplit):
    TrainX=np.array([])
    TrainY=np.array([])
    TestX=np.array([])
    TestY=np.array([])
    x=np.array([])
    y=np.array([])
    
    data = datafr.to_numpy()
    data=data.transpose()
    
    #populating x and y
    x=np.array(data[0:len(data)-1])
    y=np.array(data[len(data)-1])
    x = np.transpose(x)
    #splitting data into testing and training 
    TrainX, TestX, TrainY, TestY=train_test_split(x,y,test_size=(1-datasplit))

    #Train the data
    sgdr =None
    if(learningrate=='auto' and tolerance=='auto'):
        print("inside")
        sgdr=SGDRegressor()
    else:
        sgdr=SGDRegressor(learning_rate=learningrate,tol=tolerance)
    sgdr.fit(TrainX,TrainY)
    #Lr=LinearRegression().fit(TrainX,TrainY)

    #UploadResults(id,coefficients)


    #coefficient of determination
    accuracy= sgdr.score(TrainX,TrainY)
    # print(score)

    #intercept
    intercept=sgdr.intercept_
    print(intercept)

    #coefficients
    coefficients=sgdr.coef_

    #Prediction
    PredictY = sgdr.predict(TestX)
    print(PredictY)

    #Confusion Matrix
    #confusionMatrix = confusion_matrix(TrainY, TestY)
    
    #Mean Squared Error
    meansquared=mean_squared_error(TestY,PredictY)

    #accuracy
    #accuracy=accuracy_score(TestY, PredictY)

    #uploading
    uploadresults(userid,filename,coefficients)

    jsonFeatures=FeatToJson(x)
    Test_PredictY_json = ArrToJson(Test_PredictY)
    Train_PredictY_json = ArrToJson(Train_PredictY)
    TrainX_json = ArrToJson(TrainX)
    TrainY_json = ArrToJson(TrainY)
    TestX_json = ArrToJson(TestX)
    TestY_json=ArrToJson(TestY)




    return jsonFeatures, coef_json,TrainX_json,TrainY_json,TestX_json,TestY_json,Train_PredictY_json,Test_PredictY_json,Train_accuracy,Test_accuracy, meansquared

    # return jsonFeatures, coefficients, accuracy, meansquared, x, y, PredictY


def uploadresults(id, filename,coef):
    DataInstance = TrainedModel(UserId=id,filename=filename,Trained_Coefficients=coef)
    DataInstance.save()

def FeatToJson(x):
    JSON = {}
    for k in range(len(x)):
        JSON[str(k)]=x[k]
    
    return JSON
def ArrToJson(x):
    JSON = {}
    for k in range(len(x)):
        JSON[str(k)] = x[k]
    return JSON