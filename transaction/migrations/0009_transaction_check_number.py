# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0008_auto_20151114_0416'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='check_number',
            field=models.CharField(max_length=40, null=True, blank=True),
            preserve_default=True,
        ),
    ]
