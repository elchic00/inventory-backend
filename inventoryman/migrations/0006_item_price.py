# Generated by Django 4.0.3 on 2022-03-21 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventoryman', '0005_remove_item_location_name_alter_item_business_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='price',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
