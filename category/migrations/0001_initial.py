# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField(unique=True, null=True, blank=True)),
                ('title', models.CharField(max_length=90, unique=True, null=True, blank=True)),
                ('parent_category', models.ForeignKey(blank=True, to='category.Category', null=True)),
            ],
            options={
                'ordering': ['slug'],
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.AlterUniqueTogether(
            name='category',
            unique_together=set([('slug', 'parent_category')]),
        ),
    ]
