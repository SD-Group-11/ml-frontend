import numpy as np
import pandas as pd
import json
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from scipy.sparse import data
from sklearn import metrics
from datasets.models import Dataset
from .models import NBTrainedModel
from rest_framework.response import Response 
from sklearn import preprocessing
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.metrics import roc_curve, auc
import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt
from sklearn.metrics import f1_score
# Create your views here.

def TrainNaiveBayes(data,id,filename):
    ## fill in naive bayes training
    ## save the results into db
    
    df_copy = data
    class_names= df_copy[df_copy.columns[-1]].unique()
    y=data.iloc[:,-1:]
    data = data.iloc[: , :-1]
    x=data
    # process data
    x = encodeFeatures(x)
    x = findAndFillNullValues(x)
    # split data
    # x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
    # create,train and test model
    model = GaussianNB()
    model.fit(x, y)
    #model.score(x_test, y_test)

    # Predicting the Test set results
    y_pred = model.predict(x)
    # Making the Confusion Matrix
    ac = accuracy_score(y,y_pred)
    cm = confusion_matrix(y, y_pred)
    f1=f1_score(y, y_pred, average=None)
    json_f1 =f1ToJSON(class_names,f1)
    # print(y_pred)
    # print(ac)
    # print(cm)
    # f1=ArrToJson(f1)
    
    y_pred_proba = model.predict_proba(x)
    fpr,tpr,roc_auc = getROCData(df_copy,y,y_pred_proba)
    json_auc = aucToJSON(class_names,roc_auc)
    ROC_curves = ROC_TO_JSON(tpr,fpr,class_names)
    
    # print(ROC_curves)
    # print("fpr: ",fpr)
    # print("tpr: ",tpr)

    # false_positive_rate, true_positive_rate, thresholds = roc_curve(y, y_pred_proba[:,1])
    # auc=metrics.auc(false_positive_rate,true_positive_rate)
    # auc=ArrToJson(auc)
    # print('false positive\n',false_positive_rate)
    # print('true positive\n',true_positive_rate)
    # print('thresholds\n',thresholds)
    # plt.plot(false_positive_rate, true_positive_rate, linestyle='-')

    json_cm=ConfusionToJson(class_names,cm)

    # print(json_cm)
    # json_fpr=ArrToJson(false_positive_rate)
    # print(json_fpr)
    # json_tpr=ArrToJson(true_positive_rate)
    
    UploadTrainingResults(id,filename,ac,json_f1,json_auc)
    
    return json_cm, json_f1,json_auc,ROC_curves

def TestNaiveBayes(data,testdata,id,filename):
    ## fill in naive bayes training and testing 
    ## will be the same as TrainNaiveBayes except we also test because we have test data
    ## remember to save the results
    # return id
    # print('testing')
    y=data.iloc[:,-1:]
    ytest=testdata.iloc[:,-1:]
    data = data.iloc[: , :-1]
    testdata=testdata.iloc[:,:-1]
    x=data
    xtest=testdata
    # process data
    x = encodeFeatures(x)
    xtest=encodeFeatures(xtest)
    x = findAndFillNullValues(x)
    xtest=findAndFillNullValues(xtest)

    model = GaussianNB()
    model.fit(x, y)
    
    # Predicting the Test set results
    y_pred = model.predict(xtest)

    # Making the Confusion Matrix
    ac = accuracy_score(ytest,y_pred)
    cm = confusion_matrix(ytest, y_pred)
    f1=f1_score(y, y_pred, average=None)

    y_pred_proba = model.predict_proba(xtest)
    # false_positive_rate, true_positive_rate, thresholds = roc_curve(ytest, y_pred_proba[:,1])
    # auc=metrics.auc(false_positive_rate,true_positive_rate)
  
    # auc=ArrToJson(auc)
    json_cm=ConfusionToJson(data,cm)
    # json_fpr=ArrToJson(false_positive_rate)
    # json_tpr=ArrToJson(true_positive_rate)
    UploadTestResults(id,filename,ac,f1,auc)
    
    # return "test success"

    return json_cm, f1,auc,json_fpr,json_tpr

def getROCData(df,y, y_pred_proba):
    y_column = df[df.columns[-1]] # get the y column so that we can 
    y_dummies = pd.get_dummies(y_column)
    n_classes = int(y.nunique())

    # Compute ROC curve and ROC area for each class
    fpr = dict()
    tpr = dict()
    roc_auc = dict()
    class_names = dict()
    for i in range(n_classes):
        fpr[i], tpr[i], _ = roc_curve(y_dummies.iloc[:, i], y_pred_proba[:, i])
        roc_auc[i] = auc(fpr[i], tpr[i])

    return fpr, tpr, roc_auc


def findCategoricalFeatures(df):
    categoricalFeatures = np.array([])
    
    # iteritems gives a tuple of column name and series
    # for each column in the dataframe
    for (columnName, columnData) in df.iteritems():
        firstValue = columnData.values[0]
        # using isinstance()
        # Check if variable is string 
        res = isinstance(firstValue, str)
        if (res):
            categoricalFeatures = np.append(categoricalFeatures, columnName)
    
    return categoricalFeatures

def encodeFeatures(x):
    categoricalFeatures = findCategoricalFeatures(x)
    for feature in categoricalFeatures:
        dummies = pd.get_dummies(x[feature])
        x = pd.concat([x, dummies], axis='columns')
        x.drop(feature, axis='columns', inplace=True)
        
    return x

def findAndFillNullValues(x):
    nullFeatures = x.columns[x.isna().any()].tolist()
    for feature in nullFeatures:
        x[feature] = x[feature].fillna(round(x[feature].mean()))
        
    return x
def ROC_TO_JSON(tpr,fpr,class_names):
    ROC_curves = []
    for i in range(0,len(class_names)):
        JSON_obj={}
        JSON_obj["class"] = str(class_names[i])
        JSON_obj["fpr_values"] = fpr[i]
        JSON_obj["tpr_values"] = tpr[i]
        ROC_curves.append(JSON_obj)
    return ROC_curves
def f1ToJSON(class_names,f1):
    f1_scores = []
    # f1_scores = {}
    for i in range(0,len(class_names)):
        JSON = {}
        JSON["class"]=str(class_names[i])
        JSON['score'] = f1[i]
        f1_scores.append(JSON)
        # f1_scores[str(i)] = JSON
    return f1_scores

def aucToJSON(class_names,auc):
    auc_values =[]
    # auc_values ={}
    for i in range(0,len(class_names)):
        JSON = {}
        JSON["class"]=str(class_names[i])
        JSON['value'] = auc[i]
        auc_values.append(JSON)
        # auc_values[str(i)] = JSON
    return auc_values

@api_view(['POST',])
@csrf_exempt

def PerformNaiveBayes(request):

    UserId = request.data['UserId']
    filename = request.data['filename']
    response ={}
    try:
        ##get the respective dataset they want to train on
        dataset = Dataset.objects.get(UserId = UserId, filename=json.dumps(filename),model = "Naive Bayes")
        print('testing')
        # response['response']="success"
        # return Response(response)
        ## Note that tolerance etc won't be used for Naive Bayes
        ## If test data is available, train and test together
        if(dataset.testData != {}): 
            # response['response'] = "testing"
            # return Response(response)
            try:
                json_cm, f1,auc,ROC_curves = TestNaiveBayes(pd.read_json(dataset.data),pd.read_json(dataset.testData),UserId,filename)
                print("json_cm",json_cm)
                print("f1",f1)
                print("auc",auc)
                print("ROC_curves",ROC_curves)
                response['cm'] = json_cm
                response['f1'] = f1
                response['auc'] =auc
                response['ROC'] =ROC_curves

                return Response(response)
            except:
                response['message'] ="testing failure"
                return Response(response)
            ## add results to response and return it
        else:
            ## need to use the dataset.data to train a model.
            # response['response'] = "training"
            # return Response(response)
            try:

                json_cm, f1,auc,ROC_curves = TrainNaiveBayes(pd.read_json(dataset.data),UserId,filename)
                # print("mark 1")
                # print("ROC_curves",ROC_curves)
                # print("auc",auc)
                # print("f1",f1)
                # print("cm",cm)
                response['cm'] = json_cm
                response['f1'] = f1
                response['auc'] =auc
                response['ROC'] = ROC_curves
                return Response(response)
            except:
                response['message'] ="training failure"
                return Response(response)
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
                ModelData = NBTrainedModel.objects.get(UserId=Obj.UserId, filename=Obj.filename)
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



def UploadTrainingResults(userid,filename,trainingacc,f1Sc,auc):
    try:
        ## create new object in db and pass it all the necessary info
        DataInstance = NBTrainedModel(UserId=userid,filename=json.dumps(filename),TrainingAccuracy=trainingacc,f1score = f1Sc,AUCScore=auc)
        print(DataInstance.UserId)
        print(DataInstance.f1score)
        print(DataInstance.filename)
        print(DataInstance.TrainingAccuracy)
        print(DataInstance.AUCScore)
        DataInstance.save()
    except:
        ## if the object already exists, get the object an update all the data. Once upated save it
        obj = NBTrainedModel.objects.get(UserId=userid, filename=json.dumps(filename))
        obj.TrainingAccuracy = trainingacc
        obj.f1score = f1Sc
        obj.AUCScore=auc
        obj.save()

def UploadTestResults(userid,filename,testingacc,f1Sc,AUC):
    try:
        ## create new object in db and pass it all the necessary info
        DataInstance = NBTrainedModel(UserId=userid,filename=filename,TestingAccuracy=testingacc,f1score = f1Sc,AUCScore=AUC)
        DataInstance.save()
    except:
        ## if the object already exists, get the object an update all the data. Once upated save it
        obj = NBTrainedModel.objects.get(UserId=userid, filename=filename)
        obj.TestingAccuracy = testingacc
        obj.f1score = f1Sc
        obj.AUCScore=AUC
        obj.save()

@api_view(['POST',])
@csrf_exempt
## View to check which datasets have been trained
def trained_datasets(request):
    UserId = request.data["UserID"]
    response ={}
    
    try:
        i = 1
        ##get queryset of all datasets where they occur in the TrainedModel db
        AllTrained = NBTrainedModel.objects.filter(UserId=UserId)
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
        Obj = NBTrainedModel.objects.get(UserId=id,filename=json.dumps(filename))
        Obj.delete()
        resp['response'] = "Results discarded."
        return Response(resp)
    except:
        ## failing to locate object so we return a fail
        ## should never occur though
        resp['response'] = "Failed to delete results"
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
            Obj = NBTrainedModel.objects.get(UserId=UserId, filename=json.dumps(filename))
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
def ConfusionToJson(class_names,cm):
    CM = []
    for k in range(0,len(class_names)):
        JSON = {}
        JSON['class']=str(class_names[k])
        JSON['predictions']=cm[:][k]
        CM.append(JSON)
    return CM


def ArrToJson(x):
    JSON = {}
    for k in range(len(x)):
        JSON[str(k)] = x[k]
    return JSON