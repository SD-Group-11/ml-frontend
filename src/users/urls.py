from django.urls import path

from .views import(
    registration_view,
    login_view,
    forgot_password_view,
) 

app_name ='users'
## we're just creating the urls the data should be sent to for the respective processes in the view
urlpatterns =[
    path('register',registration_view,name='register'),
    path('login',login_view,name='login'),
    path('forgot_password',forgot_password_view,name='forgot_password'),
]