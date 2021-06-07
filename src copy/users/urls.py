from django.urls import path
from django.urls import include

app_name ='users'
## we're just creating the urls the data should be sent to for the respective processes in the view

from . import routers

urlpatterns =[
    path('users/', include(routers.router.urls)),
]