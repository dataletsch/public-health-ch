# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-03 11:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0040_merge_20170703_1238'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raw', models.TextField(blank=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('published', models.DateTimeField(auto_now_add=True)),
                ('entry_id', models.IntegerField(blank=True)),
                ('title', models.CharField(max_length=255)),
                ('origin_title', models.CharField(blank=True, max_length=255)),
                ('link', models.URLField()),
                ('visual', models.URLField(blank=True)),
                ('content', models.TextField()),
                ('tags', models.TextField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'Entries',
            },
        ),
        migrations.CreateModel(
            name='EntryCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=255)),
                ('feedly_id', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='FeedlySettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedly_auth', models.TextField(blank=True, help_text='Your developer authorization key')),
                ('feedly_pages', models.IntegerField(blank=True, choices=[(1, '2'), (2, '5'), (3, '10'), (4, '50')], help_text='How many pages to fetch?', null=True)),
                ('feedly_stream', models.TextField(blank=True, help_text='Stream ID to fetch')),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Site')),
            ],
            options={
                'verbose_name': 'Feedly',
            },
        ),
        migrations.AddField(
            model_name='entry',
            name='categories',
            field=models.ManyToManyField(blank=True, to='feedler.EntryCategory'),
        ),
    ]
