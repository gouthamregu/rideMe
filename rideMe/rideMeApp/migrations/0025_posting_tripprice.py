# Generated by Django 4.1.6 on 2023-03-07 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rideMeApp', '0024_alter_conversation_latestmessagesenttime_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='posting',
            name='tripPrice',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
            preserve_default=False,
        ),
    ]