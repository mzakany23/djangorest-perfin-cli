# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0003_auto_20151113_2006'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='slug',
            field=models.SlugField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='account',
            name='type',
            field=models.CharField(blank=True, max_length=40, null=True, choices=[(b'Checking', b'checking'), (b'Credit Card', b'credit card')]),
            preserve_default=True,
        ),
    ]
