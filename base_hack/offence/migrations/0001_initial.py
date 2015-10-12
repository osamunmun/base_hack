# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Batter',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name_text', models.CharField(max_length=200)),
                ('team_text', models.CharField(max_length=200)),
                ('ave', models.IntegerField(default=0)),
                ('game', models.IntegerField(default=0)),
                ('plate_appearance', models.IntegerField(default=0)),
                ('at_bats', models.IntegerField(default=0)),
                ('hits', models.IntegerField(default=0)),
                ('_2b', models.IntegerField(default=0)),
                ('_3b', models.IntegerField(default=0)),
                ('homerun', models.IntegerField(default=0)),
                ('total_bases', models.IntegerField(default=0)),
                ('rbi', models.IntegerField(default=0)),
                ('runs_scored', models.IntegerField(default=0)),
                ('strikeouts', models.IntegerField(default=0)),
                ('bb', models.IntegerField(default=0)),
                ('db', models.IntegerField(default=0)),
                ('sh', models.IntegerField(default=0)),
                ('sf', models.IntegerField(default=0)),
                ('sb', models.IntegerField(default=0)),
                ('obp', models.IntegerField(default=0)),
                ('slg', models.IntegerField(default=0)),
                ('risp', models.IntegerField(default=0)),
                ('double_play', models.IntegerField(default=0)),
                ('error', models.IntegerField(default=0)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
