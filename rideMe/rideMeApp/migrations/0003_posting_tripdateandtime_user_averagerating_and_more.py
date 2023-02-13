# Generated by Django 4.1.6 on 2023-02-11 15:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rideMeApp', '0002_remove_posting_tripdateandtime'),
    ]

    operations = [
        migrations.AddField(
            model_name='posting',
            name='tripDateAndTime',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 11, 15, 56, 39, 226664, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AddField(
            model_name='user',
            name='averageRating',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='user',
            name='registrationTime',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 11, 15, 56, 39, 223674, tzinfo=datetime.timezone.utc)),
        ),
    ]