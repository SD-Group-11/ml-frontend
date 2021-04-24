from rest_framework import serializers
import hashlib,uuid
from .models import User


class RegistrationSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(style ={'input_type':'password'},write_only=True) ##enables us to have confirm password field which won't be in the database
    class Meta:
        model = User                            ## says which model to save in the database
        fields = ['username','email','password','password2','first_name','last_name']  ## fields from the model we want , we could've said fields = '__all__'
        extra_kwargs = {
            'password':{'write_only':True}          ##again just ensuring that we can have both passwords and that they don't show in the request
        }
    
    def save(self):
        user = User(
            email = self.validated_data['email'],                   ## Here we're just creating a user with the info we received but not adding password because we 
            username = self.validated_data['username'],               ## want to check if they match
            first_name = self.validated_data['first_name'],
            last_name = self.validated_data['last_name']            
        )

        password = self.validated_data['password']  ##get both passwords
        password2 = self.validated_data['password2']
        if(password!=password2):  ##check they match and if not raise an error
            raise serializers.ValidationError({'response':'Passwords must match'})
        else:
            salt = "a12bc34de56fg"
            user.password= hashlib.sha256((password+salt).encode('utf-8')).hexdigest()  ## if passwords match, salt and hash and add to database
            user.save()
            return user

from rest_framework.authentication import SessionAuthentication, BasicAuthentication 

class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening