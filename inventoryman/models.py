# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Business(models.Model):
    idbusiness = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    loc_street_name = models.ForeignKey('Location', default ='None', on_delete = models.DO_NOTHING, db_column='loc_street_name')
    currency = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'business'
        unique_together = (('name','idbusiness'),)

    def __str__(self):
        return f"ID: {self.idbusiness} | Name: {self.name}"


class Item(models.Model):
    iditem = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=45)
    loc_street_name = models.ForeignKey('Location', models.DO_NOTHING, db_column='loc_street_name', blank=True, null=True)
    idbusiness = models.ForeignKey('Business', models.DO_NOTHING, db_column='idbusiness', blank=True, null=True)
    item_count = models.IntegerField()
    picture = models.CharField(max_length=45, blank=True, null=True)
    sku = models.CharField(unique=True, max_length=45, blank=True, null=True)
    expire = models.DateField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'item'

    def __str__(self):
        return f"ID:{self.iditem} | Name: {self.item_name}"


class Location(models.Model):
    name = models.CharField(max_length=45)
    street = models.CharField(primary_key=True, max_length=120)
    town = models.CharField(max_length=45, blank=True, null=True)
    zip = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'location'
        unique_together = (('street', 'name'),)

    def __str__(self):
        return f"Nickname: {self.name} | Street: {self.street}"