# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import plays.models


class Migration(migrations.Migration):

    dependencies = [
        ('theaters', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('start_date', models.DateField(null=True, blank=True)),
                ('end_date', models.DateField(null=True, blank=True)),
                ('slug', models.SlugField(null=True, blank=True)),
                ('info', models.TextField(null=True, blank=True)),
                ('organizer', models.ForeignKey(blank=True, to='theaters.Organizer', null=True)),
                ('theater', models.ForeignKey(blank=True, to='theaters.Venue', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PlayImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=plays.models.image_upload_to)),
                ('play', models.ForeignKey(to='plays.Event')),
            ],
        ),
        migrations.CreateModel(
            name='Showing',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('hour', models.CharField(default=b'First Showing', max_length=20)),
                ('slug', models.SlugField(null=True, blank=True)),
                ('no_of_seats', models.IntegerField(null=True, blank=True)),
                ('price', models.DecimalField(null=True, max_digits=20, decimal_places=2, blank=True)),
                ('sale_price', models.DecimalField(null=True, max_digits=20, decimal_places=2, blank=True)),
                ('play', models.ForeignKey(to='plays.Event')),
            ],
        ),
    ]
