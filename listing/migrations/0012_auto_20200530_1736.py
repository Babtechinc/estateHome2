# Generated by Django 3.0.6 on 2020-05-30 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0011_auto_20200530_1735'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listi_ng',
            old_name='type',
            new_name='type_listing',
        ),
        migrations.AlterField(
            model_name='listi_ng',
            name='deal',
            field=models.CharField(choices=[('rent', 'rent'), ('sale', 'sale')], default='rent', max_length=45),
        ),
    ]
