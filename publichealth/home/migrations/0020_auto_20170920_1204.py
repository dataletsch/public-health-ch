# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-20 10:04
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_auto_20170908_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepage',
            name='body_de',
            field=wagtail.wagtailcore.fields.StreamField((('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('section', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('info', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('photo', wagtail.wagtailimages.blocks.ImageChooserBlock(required=True)), ('summary', wagtail.wagtailcore.blocks.RichTextBlock(required=True)), ('action', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('url', wagtail.wagtailcore.blocks.URLBlock(required=False))), icon='help')), ('media', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('gallery', 'Image gallery')], icon='media'))), blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='articlepage',
            name='body_fr',
            field=wagtail.wagtailcore.fields.StreamField((('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('section', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('info', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('photo', wagtail.wagtailimages.blocks.ImageChooserBlock(required=True)), ('summary', wagtail.wagtailcore.blocks.RichTextBlock(required=True)), ('action', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('url', wagtail.wagtailcore.blocks.URLBlock(required=False))), icon='help')), ('media', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('gallery', 'Image gallery')], icon='media'))), blank=True, null=True),
        ),
    ]
