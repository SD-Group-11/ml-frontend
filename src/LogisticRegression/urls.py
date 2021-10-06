from django.urls import path

from .views import(
    trained_datasets,
    discard_training_results,
    getDatasetsInfo,
    PerformLogisticRegression,
    delete_dataset
) 

app_name ='LogisticRegression'
## we're just creating the urls the data should be sent to for the respective processes in the view
urlpatterns =[
    path('trainedDatasets',trained_datasets),
    path('discardResults',discard_training_results),
    path('getDatasetsInfo',getDatasetsInfo),
    path('PerformLogisticRegression',PerformLogisticRegression),
    path('deleteDataset',delete_dataset)
]