from django.http import HttpResponse
from .models import Location, Business, Item
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import LocationSerializer, BusinessSerializer, ItemSerializer

class LocationView(viewsets.ModelViewSet):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()

class BusinessView(viewsets.ModelViewSet):
    serializer_class = BusinessSerializer
    queryset = Business.objects.all()

class ItemView(viewsets.ModelViewSet):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()




def index(request):
    businesses = Business.objects.all()
    outp =  "You're at the inventory homepage. Add /admin \
    to the end of the URL to visit the admin UI or /api to visit the REST API" + '<br><br>'\
    "here is a list of current businesses<br>" + \
         '<br>'.join([b.name for b in businesses])
    return HttpResponse(outp) 
