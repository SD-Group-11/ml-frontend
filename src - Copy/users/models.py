from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from .managers import UserManager

# Create your models here.

#a model is basically a table in the database that we create and will have the fields we specify 
# we can do everything like don't allow null values etc by just adding it in the attributes, eg i use the max_length attribute

## ABSOLUTELY IMPORTANT!!
## AFter any change is made to a models.py file, run the commands python manage.py makemigrations and thereafter python manage.py migrate
## This will add changes made to the database. If you don't the program will break and throw errors 


class User(AbstractUser):
    email = models.EmailField(verbose_name='email address',max_length=255,unique=True,)
    username = models.CharField(max_length=200)
    first_name = models.CharField(blank=False, max_length=150, verbose_name='first name')
    last_name = models.CharField(blank=False, max_length=150, verbose_name='last name')

    # notice the absence of a "Password field", that is built in.

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name','last_name','date_joined'] # Email & Password are required by default.

    def __str__(self):
        return self.email

    objects = UserManager()