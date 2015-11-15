# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='type',
            field=models.TextField(blank=True, max_length=40, null=True, choices=[(b'Checking', b'checking'), (b'Credit Card', b'credit Card')]),
            preserve_default=True,
        ),
    ]
