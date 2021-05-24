from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from .models import Dataset
import json
# Create your views here.

def toJSON(data):
    headers = data[0].split(",")
    JSON = {}
    length = len(data)
    features = len(headers)
    for i in range(1,length):
        row = {}
        values = data[i].split(",")
        for j in range(features):
            row[headers[j]] =  values[j]
        JSON[str(i)] = row

    return JSON

def filterData(dataset):
    newd = dataset.split(r'\n')
    data = newd[4:-7]
    dataset = toJSON(data)
    num = newd[len(newd)-3]
    id = int(num[:len(num)-2])
    filename = newd[1][newd[1].find('filename=')+9:len(newd[1])-2]

    return id,filename,dataset

@api_view(['POST',])   ## ensures only POST requests can be made to the api
@csrf_exempt

def receiveData(request):

    resp = {}
    if request.method == "POST":
        
        dataset = str(request.body)
        if(dataset != ''):
            id,filename,dataset = filterData(dataset)
            DataInstance = Dataset(UserId=id, filename=filename, data=dataset)
            DataInstance.save()
            resp['response'] ='Data Uploaded Successfully'
            return Response(resp)
        else:
            resp['response'] ='Failed to upload data'
    
    resp['response'] ='Failed to upload data'
    
        

    return Response(resp)


@api_view(['POST',])   ## ensures only POST requests can be made to the api
@csrf_exempt

def dataSummary(request):

    resp = {}
    if request.method == "POST":
        filename = request.data['filename']
        id = request.data['id']
        obj = Dataset.objects.get(UserId=id, filename=json.dumps(filename))
        datapoints = len(obj.data)
        columns  = len(obj.data['1'])
        resp['datapoints'] = datapoints
        resp['columns'] = columns
        resp['filename'] = filename
    else:
        resp['error'] = "Failed to summarise data"

    return Response(resp)