# Generated by Django 3.0.6 on 2020-05-30 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0009_listi_ng_deal'),
    ]

    operations = [
        migrations.AddField(
            model_name='listi_ng',
            name='location',
            field=models.CharField(default='Epe', max_length=2000),
        ),
    ]
