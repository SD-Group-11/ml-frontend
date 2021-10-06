from rest_framework import routers
from djoser import views

router = routers.DefaultRouter()
router.register('', views.UserViewSet)