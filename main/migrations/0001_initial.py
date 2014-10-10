# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import main.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('description', models.CharField(max_length=255, verbose_name='description', blank=True)),
            ],
            options={
                'verbose_name': 'achievement',
                'verbose_name_plural': 'achievements',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255, verbose_name='name')),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'event',
                'verbose_name_plural': 'events',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Freeloader',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=60, verbose_name='name')),
                ('gender', models.CharField(max_length=1, verbose_name='gender', choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')])),
                ('year_of_birth', models.PositiveIntegerField(verbose_name='year of birth')),
                ('notes', models.CharField(max_length=255, verbose_name='notes', blank=True)),
                ('register_date', models.DateTimeField(auto_now_add=True, verbose_name='register date')),
                ('event', models.ForeignKey(default=main.models.get_current_event, to='main.Event')),
            ],
            options={
                'verbose_name': 'freeloader',
                'verbose_name_plural': 'freeloaders',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('owner_name', models.CharField(max_length=60, verbose_name='owner name')),
                ('owner_gender', models.CharField(max_length=1, verbose_name='owner gender', choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')])),
                ('owner_year_of_birth', models.PositiveIntegerField(verbose_name='year of birth')),
                ('ticket_number', models.PositiveIntegerField(verbose_name='ticket number')),
                ('free', models.BooleanField(default=False, verbose_name='free')),
                ('voucher_number', models.IntegerField(null=True, verbose_name='voucher number', blank=True)),
                ('notes', models.CharField(max_length=255, verbose_name='notes', blank=True)),
                ('register_date', models.DateTimeField(auto_now_add=True, verbose_name='register date')),
                ('achievements', models.ManyToManyField(to='main.Achievement', verbose_name='achievements', blank=True)),
                ('cards', models.ManyToManyField(related_name='cards', verbose_name='cards', to='main.Achievement', blank=True)),
                ('event', models.ForeignKey(default=main.models.get_current_event, to='main.Event')),
            ],
            options={
                'verbose_name': 'ticket',
                'verbose_name_plural': 'tickets',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='ticket',
            unique_together=set([('event', 'ticket_number')]),
        ),
        migrations.AddField(
            model_name='achievement',
            name='event',
            field=models.ForeignKey(to='main.Event'),
            preserve_default=True,
        ),
    ]
