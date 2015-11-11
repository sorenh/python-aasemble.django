# -*- coding: utf-8 -*-
# Generated by Django 1.9b1 on 2015-11-03 07:47
from __future__ import unicode_literals

import uuid

from django.db import migrations


def gen_uuid(apps, schema_editor):
    for model_name in ('mirror', 'mirrorset', 'snapshot'):
        m = apps.get_model('mirrorsvc', model_name)
        for row in m.objects.all():
            row.uuid = uuid.uuid4()
            row.save()


class Migration(migrations.Migration):

    dependencies = [
        ('mirrorsvc', '0010_add_uuid_field'),
    ]

    operations = [
        migrations.RunPython(gen_uuid, reverse_code=migrations.RunPython.noop),
    ]
