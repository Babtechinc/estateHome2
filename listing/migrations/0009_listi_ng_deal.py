# Generated by Django 3.0.6 on 2020-05-30 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0008_auto_20200528_1607'),
    ]

    operations = [
        migrations.AddField(
            model_name='listi_ng',
            name='deal',
            field=models.CharField(choices=[('sale', 'sale'), ('rent', 'rent')], default='rent', max_length=45),
        ),
    ]
