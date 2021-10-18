from django.urls import path

from .views import(
    receiveData,
    getDatasetsInfo,
    getDatasetData,
    doLinearRegression,
    delete_dataset,
    receive_TestData,
    getTrainedDatasets,
    check_if_test_data_is_available,
    make_dataset_public,
    getPublicDatasetsInfo,
    getPublicDatasetTrainData,
    getPublicDatasetTestData,
) 

app_name ='datasets'
## we're just creating the urls the data should be sent to for the respective processes in the view
urlpatterns =[
    path('uploadData',receiveData,name='receivedata'),
    path('getDatasetsInfo',getDatasetsInfo,name='getDatasetsInfo'),
    path('getDatasetData',getDatasetData,name='getDatasetData'),
    path('doLinearRegression',doLinearRegression,name='doLinearRegression'),
    path('deleteDataset',delete_dataset,name='deleteDataset'),
    path('uploadTestData',receive_TestData,name='receiveTestData'),
    path('getTrainedDatasets',getTrainedDatasets,name='getTrainedDatasets'),
    path('checkTestData',check_if_test_data_is_available,name="checkTestData"),
    path('makeDatasetPublic',make_dataset_public,name="makeDatasetPublic"),
    path('getPublicDatasetsInfo',getPublicDatasetsInfo,name="getPublicDatasets"),
    path('getPublicDatasetTrainData',getPublicDatasetTrainData),
    path("getPublicDatasetTestData",getPublicDatasetTestData)
    
]