# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cosplay', '0003_auto_20141010_2228'),
    ]

    operations = [
        migrations.CreateModel(
            name='JuryVote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vote_points', models.IntegerField(verbose_name='points')),
                ('vote_date', models.DateTimeField(auto_now_add=True, verbose_name='vote date')),
                ('contestant', models.ForeignKey(to='cosplay.Cosplayer')),
                ('jury_member', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'jury vote',
                'verbose_name_plural': 'jury votes',
            },
            bases=(models.Model,),
        ),
    ]
