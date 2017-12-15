# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Starship',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='StarshipModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=255)),
                ('manufacturer', models.CharField(max_length=255)),
                ('length', models.IntegerField()),
                ('hyperdrive_rating', models.FloatField()),
                ('cargo_capacity', models.IntegerField()),
                ('crew', models.IntegerField()),
                ('passengers', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='starship',
            name='model',
            field=models.ForeignKey(related_name='ships', to='shiptrader.StarshipModel'),
        ),
    ]
