# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import plays.models


class Migration(migrations.Migration):

    dependencies = [
        ('plays', '0002_event_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=plays.models.image_upload_to)),
            ],
        ),
        migrations.RemoveField(
            model_name='playimage',
            name='play',
        ),
        migrations.RenameField(
            model_name='showing',
            old_name='play',
            new_name='event',
        ),
        migrations.AddField(
            model_name='event',
            name='type',
            field=models.CharField(blank=True, max_length=100, null=True, choices=[(b'Premium With Seating', b'Premium With Seating'), (b'Premium with No Seating', b'Premium with No Seating'), (b'Free with No Seating', b'Free with No Seating'), (b'Free with Seating', b'Free with Seating')]),
        ),
        migrations.DeleteModel(
            name='PlayImage',
        ),
        migrations.AddField(
            model_name='eventimage',
            name='event',
            field=models.ForeignKey(to='plays.Event'),
        ),
    ]
