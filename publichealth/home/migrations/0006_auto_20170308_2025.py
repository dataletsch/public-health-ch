# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-08 19:25
from __future__ import unicode_literals

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20170308_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body_de',
            field=wagtail.core.fields.RichTextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body_fr',
            field=wagtail.core.fields.RichTextField(blank=True, default=''),
        ),
    ]
