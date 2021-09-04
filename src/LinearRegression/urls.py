from django.urls import path

from .views import(
    discard_training_results
) 

app_name ='LinearRegression'
## we're just creating the urls the data should be sent to for the respective processes in the view
urlpatterns =[
    path('discardMetrics',discard_training_results,name='discardMetrics'),
]