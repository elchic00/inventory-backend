from rest_framework import serializers
from .models import Location, Business, Item

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('name', 'street', 'town', 'zip')

class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = ('idbusiness', 'name', 'loc_street_name', 'currency')

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('iditem', 'item_name', 'loc_street_name', 'idbusiness','item_count','picture','sku','expire','price')


