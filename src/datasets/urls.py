from django.urls import path

from .views import(
    receiveData,
    getDatasetsInfo,
    getDatasetData,
    doLinearRegression
) 

app_name ='datasets'
## we're just creating the urls the data should be sent to for the respective processes in the view
urlpatterns =[
    path('uploadData',receiveData,name='receivedata'),
    path('getDatasetsInfo',getDatasetsInfo,name='getDatasetsInfo'),
    path('getDatasetData',getDatasetData,name='getDatasetData'),
    path('doLinearRegression',doLinearRegression,name='doLinearRegression')
    
]