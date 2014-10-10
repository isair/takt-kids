# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('cosplay', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cosplayer',
            name='costume_category',
            field=models.CharField(default='', max_length=1, null=True, choices=[('V', 'Video Game Character'), ('O', 'Original Character'), ('', 'Other')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cosplayer',
            name='email',
            field=models.EmailField(max_length=75, null=True, verbose_name='email', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cosplayer',
            name='made_own_costume',
            field=models.BooleanField(default=False, verbose_name='made own costume'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cosplayer',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, null=True, validators=[django.core.validators.RegexValidator('^\\+?1?\\d{9,15}$', "Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", 'Invalid Phone number'), django.core.validators.MaxLengthValidator(15)]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cosplayer',
            name='notes',
            field=models.CharField(max_length=512, verbose_name='notes', blank=True),
        ),
    ]
