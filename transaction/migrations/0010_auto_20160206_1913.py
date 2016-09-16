# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0009_transaction_check_number'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='transaction',
            unique_together=set([('date', 'check_number', 'name', 'amount')]),
        ),
    ]
