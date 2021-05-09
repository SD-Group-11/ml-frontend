from rest_framework import status
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from .models import User
import hashlib,uuid
from django.contrib.auth import authenticate,login
from django.views.decorators.csrf import csrf_exempt
from .serializers import CsrfExemptSessionAuthentication
from .serializers import (
    RegistrationSerializer,
    
    )


@api_view(['POST',])   ## ensures only POST requests can be made to the api

def registration_view(request):
    
    if request.method =='POST':
        serializer = RegistrationSerializer(data=request.data)  ## We are just passing the data into a serializer we created which will perform all the validation checks
        data={}                                                 ## such as valid email etc

        if serializer.is_valid():  ## this actually does the validation
            user = serializer.save()  ## save the user if all is good
            data['response'] = 'Successfully Registered'

        else:
            data = serializer.errors ## raise the respective error and return it 
        
        return Response(data)


@api_view(['POST',])
@csrf_exempt
def login_view(request):

    if request.method == 'POST':
        
        data={}
        Email = request.data['email']
        salt = "a12bc34de56fg"
        Password = hashlib.sha256((request.data['password']+salt).encode('utf-8')).hexdigest() ## salting and hashing the password 

        try:

            user = User.objects.get(email=Email) ##get user by the email  
            if(user):
                if(user.password==Password):  ## if passwords match , allow login
                      data['response'] ="Valid user"
                else:
                    data['response'] ='Incorrect Password'
          

        except:
            data['response']='Incorrect Email'

      
    return Response(data)

@api_view(['POST',])
@csrf_exempt
def forgot_password_view(request):
    Email = request.data['email']
    data ={}
    try:
        user = User.objects.get(email = Email) ##get the user with that respective email
        if(user):
            salt = "a12bc34de56fg"
            Password = hashlib.sha256((request.data['password']+salt).encode('utf-8')).hexdigest()  #salt and hash the password
            password  = user.password ## get the old password of the user
            if(password== Password):
                data['response'] = "New password cannot be the same as old password" ##be a troll and don't allow them to use the same password again
                return Response(data)
            else:
                user.password = Password
                user.save()  ##update the password and save it to the Database
                data['response'] = "Password Updated"
                return Response(data)
    except:
        data['response']='Incorrect email entered'  ##if we fail to retrieve a user with that email, then the email entered is incorrect 
        return Response(data)
            
