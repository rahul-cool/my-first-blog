# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_Date',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 30, 7, 9, 54, 571719, tzinfo=utc)),
        ),
    ]
