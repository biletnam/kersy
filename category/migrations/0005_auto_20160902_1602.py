# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0004_auto_20160804_0539'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='categorytranslation',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='categorytranslation',
            name='master',
        ),
        migrations.AddField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=90, unique=True, null=True, blank=True),
        ),
        migrations.DeleteModel(
            name='CategoryTranslation',
        ),
    ]
