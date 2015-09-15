# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drip', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='drip',
            name='msg_type',
            field=models.CharField(default=b'email', max_length=5, choices=[(b'email', b'Email'), (b'sms', b'Text Message')]),
            preserve_default=True,
        ),
    ]
