from django.urls import path

from .views import(
    receiveData,
    dataSummary
) 

app_name ='datasets'
## we're just creating the urls the data should be sent to for the respective processes in the view
urlpatterns =[
    path('uploadData',receiveData,name='receivedata'),
    path('dataSummary',dataSummary,name='datasummary')
]