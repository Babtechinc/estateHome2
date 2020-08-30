# Generated by Django 3.0.6 on 2020-05-20 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='agent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
                ('agent_img', models.ImageField(blank=True, upload_to='media/agent_img/%Y/%m/%d/')),
                ('number', models.CharField(blank=True, max_length=200)),
                ('email', models.EmailField(blank=True, max_length=200)),
                ('tweetsm', models.CharField(blank=True, max_length=200)),
                ('fbooksm', models.CharField(blank=True, max_length=200)),
                ('linksm', models.CharField(blank=True, max_length=200)),
            ],
        ),
    ]
