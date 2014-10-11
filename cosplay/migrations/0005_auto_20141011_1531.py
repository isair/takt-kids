# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cosplay', '0004_juryvote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cosplayer',
            name='costume_category',
            field=models.CharField(default='X', max_length=1, null=True, choices=[('V', 'Video Game Character'), ('O', 'Original Character'), ('X', 'Other')]),
        ),
    ]
