# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('episodes', '0001_initial'),
        ('reactions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagereaction',
            name='enabled',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='imagereaction',
            name='episode',
            field=models.ForeignKey(to='episodes.Episode', null=True),
        ),
        migrations.AddField(
            model_name='tweetreaction',
            name='enabled',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='tweetreaction',
            name='episode',
            field=models.ForeignKey(to='episodes.Episode', null=True),
        ),
        migrations.AlterField(
            model_name='imagereaction',
            name='image',
            field=models.ImageField(upload_to='reactions/images'),
        ),
    ]
