# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models

import jsonfield.fields


class Migration(migrations.Migration):

    """
    Current going to handle the dependency swap manually until parent_swap is more stable
    & the slideshow repo is not publicly exposed (YET).
    """

    base_class = getattr(settings, 'DEFAULT_BASE_CLASS', None)
    if base_class:

        dependencies = [
            ('content', '0001_initial'),
        ]

        operations = [
            migrations.CreateModel(
                name='Slideshow',
                fields=[(
                    'content_ptr', models.OneToOneField(
                        parent_link=True,
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        to='content.Content'
                    )
                )],
                options={
                    'abstract': False,
                },
                bases=('content.content',)
            ),
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
                ]
            )
        ]
