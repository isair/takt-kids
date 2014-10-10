# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields
import cosplay.models
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('main', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cosplayer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('character_name', models.CharField(max_length=100, verbose_name='character name')),
                ('costume_category', models.CharField(default='', max_length=1, null=True, choices=[('V', 'Video Game Character'), ('O', 'Original Character'), ('', 'Other')])),
                ('made_own_costume', models.BooleanField(default=False, verbose_name='made own costume')),
                ('email', models.EmailField(max_length=75, verbose_name='email', blank=True)),
                ('phone_number', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator('^\\+?1?\\d{9,15}$', "Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", 'Invalid Phone number'), django.core.validators.MaxLengthValidator(15)])),
                ('picture', sorl.thumbnail.fields.ImageField(upload_to=cosplay.models.u_file_rename, blank=True)),
                ('contest_number', models.IntegerField(null=True, blank=True)),
                ('notes', models.CharField(max_length=512, verbose_name='notes', blank=True)),
                ('register_date', models.DateTimeField(auto_now_add=True, verbose_name='register date')),
                ('ticket', models.OneToOneField(to='main.Ticket')),
            ],
            options={
                'verbose_name': 'cosplayer',
                'verbose_name_plural': 'cosplayers',
            },
            bases=(models.Model,),
        ),
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
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vote_date', models.DateTimeField(auto_now_add=True, verbose_name='vote date')),
                ('contestant', models.ForeignKey(to='cosplay.Cosplayer')),
                ('voter', models.ForeignKey(to='main.Ticket')),
            ],
            options={
                'verbose_name': 'vote',
                'verbose_name_plural': 'votes',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='vote',
            unique_together=set([('voter', 'contestant')]),
        ),
    ]
