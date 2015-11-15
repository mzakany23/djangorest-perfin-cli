# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0002_account_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='title',
            field=models.CharField(max_length=40),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='account',
            name='type',
            field=models.CharField(blank=True, max_length=40, null=True, choices=[(b'Checking', b'checking'), (b'Credit Card', b'credit Card')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='transaction',
            name='name',
            field=models.CharField(max_length=250, null=True, blank=True),
            preserve_default=True,
        ),
    ]
