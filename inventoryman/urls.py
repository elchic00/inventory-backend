from django.urls import path, include
from . import views
from rest_framework import routers

# route urls for the api/{route}
router = routers.DefaultRouter()
router.register(r'locations', views.LocationView, 'location')
router.register(r'businesses', views.BusinessView, 'business')
router.register(r'items', views.ItemView, 'item')

urlpatterns = [
    path('', include(router.urls)),
]