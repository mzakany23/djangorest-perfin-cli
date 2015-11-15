# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0005_account_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='category',
            field=models.CharField(blank=True, max_length=40, null=True, choices=[(b'Fixed', b'fixed'), (b'Variable', b'variable'), (b'Income', b'income')]),
            preserve_default=True,
        ),
    ]
