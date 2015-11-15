# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0007_transaction_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='timestamp',
            field=models.TimeField(auto_now_add=True, null=True),
            preserve_default=True,
        ),
    ]
