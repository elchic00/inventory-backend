# Generated by Django 4.0.3 on 2022-03-25 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventoryman', '0008_alter_business_location_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='location_name',
            field=models.ForeignKey(db_column='location_name', default='None', on_delete=django.db.models.deletion.DO_NOTHING, to='inventoryman.location'),
        ),
        migrations.AlterField(
            model_name='item',
            name='idbusiness',
            field=models.ForeignKey(blank=True, db_column='idbusiness', null=True, on_delete=django.db.models.deletion.CASCADE, to='inventoryman.business'),
        ),
    ]
