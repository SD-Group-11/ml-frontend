"""mlproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
    # Use RedirectView to  takes the new relative URL to redirect to (/users/) as its first argument when
    # the URL pattern specified in the path() function is matched (the root URL, in this case).
from django.views.generic import RedirectView 


urlpatterns = [
    path('admin/', admin.site.urls),
    #path("", RedirectView.as_view(url='users/', permanent=True)), #Tal: redirect empty url to users application urls

    path('api/v1/', include('users.urls')),
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken')),
    path('datasets/',include('datasets.urls')),
    path('LinearRegression/', include('LinearRegression.urls')),
    path('NaiveBayes/',include('NaiveBayes.urls')),
    path('LogisticRegression/',include('LogisticRegression.urls')),


]

