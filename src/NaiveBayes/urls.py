from django.urls import path

from .views import(
    trained_datasets,
    discard_training_results
) 

app_name ='NaiveBayes'
## we're just creating the urls the data should be sent to for the respective processes in the view
urlpatterns =[
    path('trainedDatasets',trained_datasets),
    path("discardResults",discard_training_results),
]