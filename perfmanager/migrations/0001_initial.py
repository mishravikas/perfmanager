# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alerts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('branch', models.CharField(default=b'', max_length=128)),
                ('test', models.CharField(default=b'', max_length=128)),
                ('platform', models.CharField(default=b'', max_length=64)),
                ('percent', models.CharField(default=b'', max_length=32)),
                ('graphurl', models.CharField(default=b'', max_length=128, null=True)),
                ('changeset', models.CharField(default=b'', max_length=128)),
                ('keyrevision', models.CharField(default=b'', max_length=128)),
                ('bugcount', models.IntegerField(default=0, max_length=11)),
                ('comment', models.CharField(default=b'', max_length=1024)),
                ('bug', models.CharField(default=b'', max_length=128)),
                ('status', models.CharField(default=b'', max_length=64)),
                ('email', models.CharField(default=b'', max_length=128)),
                ('push_date', models.DateTimeField(null=True)),
                ('changesets', models.CharField(default=b'', max_length=8192)),
                ('mergedfrom', models.CharField(default=b'', max_length=128)),
                ('duplicate', models.CharField(max_length=128, null=True)),
                ('treeherderurl', models.CharField(max_length=256, null=True)),
                ('backout', models.CharField(max_length=128, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
