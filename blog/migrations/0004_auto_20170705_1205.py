# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20170705_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_Date',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 5, 12, 5, 49, 147414, tzinfo=utc)),
        ),
    ]
