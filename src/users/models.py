from django.db import models

# Create your models here.

#a model is basically a table in the database that we create and will have the fields we specify 
# we can do everything like don't allow null values etc by just adding it in the attributes, eg i use the max_length attribute

## ABSOLUTELY IMPORTANT!!
## AFter any change is made to a models.py file, run the commands python manage.py makemigrations and thereafter python manage.py migrate
## This will add changes made to the database. If you don't the program will break and throw errors 
class User(models.Model): 
    username = models.CharField(max_length=200)
    email = models.EmailField(max_length=200,unique=True)
    password = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200,default='')
    last_name = models.CharField(max_length=200,default='')
    createdat = models.DateTimeField(auto_now_add=True)