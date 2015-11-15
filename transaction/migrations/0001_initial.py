# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.TextField(max_length=40)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(null=True, blank=True)),
                ('name', models.TextField(max_length=250, null=True, blank=True)),
                ('amount', models.DecimalField(default=0.0, max_digits=6, decimal_places=2)),
                ('account', models.ForeignKey(to='transaction.Account')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
