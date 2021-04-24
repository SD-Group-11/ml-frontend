from django.contrib import admin
from .models import User
# Register your models here.

## Just add this is the respective admin file of the app you create so we can use it 
admin.site.register(User)