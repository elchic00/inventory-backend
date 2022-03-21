from django.contrib import admin

from .models import Location, Business, Item

admin.site.register(Location)
admin.site.register(Business)
admin.site.register(Item)