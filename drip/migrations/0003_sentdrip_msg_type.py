# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drip', '0002_drip_msg_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='sentdrip',
            name='msg_type',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
    ]
