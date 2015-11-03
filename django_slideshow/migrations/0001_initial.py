# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models

import jsonfield.fields


class Migration(migrations.Migration):

    is_bulbs_content = getattr(settings, 'IS_BULBS_CONTENT', False)

    if is_bulbs_content:

        dependencies = [
            ('content', '0001_initial')
        ]

        operations = [
            migrations.CreateModel(
                name='Slideshow',
                fields=[
                    (
                        'content_ptr',
                        models.OneToOneField(
                            parent_link=True,
                            auto_created=True,
                            primary_key=True,
                            serialize=False,
                            to='content.Content'
                        )
                    ),
                    ('slides', jsonfield.fields.JSONField(default=[], blank=True))
                ]
            )
        ]

    else:

        dependencies = [

        ]

        operations = [
            migrations.CreateModel(
                name='Slideshow',
                fields=[
                    (
                        'id',
                        models.AutoField(
                            verbose_name='ID',
                            serialize=False,
                            auto_created=True,
                            primary_key=True
                        )
                    ),
                    ('slides', jsonfield.fields.JSONField(default=[], blank=True)),
                ],
            ),
        ]
