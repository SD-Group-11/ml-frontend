from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from .models import Dataset
import json

#ml imports
import numpy as np
from sklearn.linear_model import LinearRegression

# Create your views here.
