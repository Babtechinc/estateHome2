# Generated by Django 3.0.6 on 2020-05-21 10:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0001_initial'),
        ('listing', '0002_auto_20200521_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listi_ng',
            name='agent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agent.agent'),
        ),
    ]
