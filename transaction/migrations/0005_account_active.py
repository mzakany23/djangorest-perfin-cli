# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0004_auto_20151113_2012'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='active',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
