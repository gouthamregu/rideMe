# Generated by Django 4.1.6 on 2023-02-11 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rideMeApp', '0007_alter_posting_tripdateandtime_alter_user_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='password123', max_length=256),
        ),
        migrations.AlterField(
            model_name='user',
            name='averageRating',
            field=models.FloatField(),
        ),
    ]