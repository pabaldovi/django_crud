# Generated by Django 4.0.5 on 2022-06-13 15:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 13, 15, 46, 47, 295262, tzinfo=utc), verbose_name='date'),
            preserve_default=False,
        ),
    ]
