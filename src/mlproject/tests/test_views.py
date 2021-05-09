from django.test import TestCase, Client
from django.urls import reverse
from users.models import User
import json
import hashlib

class TestViews(TestCase):
    
    def setUp(self):
        #create url variables
        self.client = Client()
        self.register_url = reverse('users:register')
        self.login_url = reverse('users:login')
        self.forgot_password_url = reverse('users:forgot_password')
        
        #create password variables
        self.salt = "a12bc34de56fg"
        self.password = hashlib.sha256(('test_pass'+self.salt).encode('utf-8')).hexdigest()  

#tests for the registration view
        
    #test that a user can be added
    def test_user_registration_POST_adds_new_user(self):
        #create a post request to server with the new users details and save the response
        request_body ={
            'username' : 'test',
            'email': 'test@email.com',
            'password' : 'test_pass',
            'password2' : 'test_pass',
            'first_name':' test_name',
            'last_name': 'test_last_name'

        }
        response = self.client.post(self.register_url,request_body)
        #check wether the view returns a message saying that the user has been registered
        self.assertEquals(response.data['response'],'Successfully Registered')
        #check whether the new user has been added to the databases
        self.assertEquals(User.objects.get(username='test').username, '')

    #test that a user is not added if no user data is given
    def test_user_registration_POST_no_data(self):  
        
        #create a post request with no data
        response = self.client.post(self.register_url)
        #check that the a new user has not beeen added to the database
        self.assertEquals(User.objects.count(), 0)
    
    
    
    #test that a user cannot be added if their email address is already registered to another user
    def test_user_registration_POST_already_exists(self):
        # add a User to the database
        User.objects.create(
            username = 'test',
            email = 'test@email.com',
            password = 'test_pass',
            first_name =' test_name',
            last_name =  'test_last_name' 
        )
        #send a request to create the same user
        request_body ={
            'username' : 'test',
            'email': 'test@email.com',
            'password' : 'test_pass',
            'password2' : 'test_pass',
            'first_name':' test_name',
            'last_name': 'test_last_name'

        }

        response = self.client.post(self.register_url,request_body)
        #check that the duplicate user is rejected

        self.assertEquals(str(response.data['email'][0]), "user with this email already exists.")
        
        #delete the user that was added
        user = User.objects.get(username='test')
        user.delete()

    #test that the passwords validation is working
    def test_user_registration_POST_passwords_dont_match(self):
        #create a post request to server with the new users details and save the response
        request_body ={
            'username' : 'test',
            'email': 'test@email.com',
            'password' : 'test_pass',
            'password2' : 'tet_pass',
            'first_name':' test_name',
            'last_name': 'test_last_name'

        }
        response = self.client.post(self.register_url,request_body)
        #check wether the view returns a message saying that the passwords dont match
        self.assertEquals(str(response.data['response']),'Passwords must match')
        #check whether that the new user has not been to the database
        self.assertEquals(User.objects.count(),0)

    
#tests for the login view
    #test that a user can login
    def test_user_login_POST_logs_in(self):
   
        #add a user to the database

        User.objects.create(
            username = 'test',
            email = 'test@email.com',
            password = self.password,
            first_name ='test_name',
            last_name =  'test_last_name' 
        )
        #send a login request and save the response
        request_body ={
            'email': 'test@email.com',
            'password' : 'test_pass'
        }
        response = self.client.post(self.login_url,request_body)
        #check if the user returns as valid
        self.assertEquals(response.data['response'], 'Valid user')

        #delete the user that was added
        user = User.objects.get(username='test')
        user.delete()

#test the forgot_password view
    #test that an existing user can change thier password
    def test_user_login_POST_logs_in(self):
   
        #add a user to the database
        
       
        ## salting and hashing the password
        User.objects.create(
            username = 'test',
            email = 'test@email.com',
            password = self.password,
            first_name ='test_name',
            last_name =  'test_last_name' 
        )
        #send a login request and save the response
        #salt and hash the new password
        new_password = hashlib.sha256(('test_new_pass'+self.salt).encode('utf-8')).hexdigest()  
        request_body ={
            'email': 'test@email.com',
            'password' : 'test_new_pass'
        }
        response = self.client.post(self.forgot_password_url,request_body)
        #check if the view returns a password updated message
        self.assertEquals(response.data['response'], 'Password Updated')
        #check if the password has been updated in the database
        self.assertEquals(User.objects.get(username='test').password,new_password)

        #delete the user that was added
        user = User.objects.get(username='test')
        user.delete()

