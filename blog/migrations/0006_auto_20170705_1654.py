# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20170616_1906'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='links',
            options={'ordering': ['index', '-id'], 'verbose_name': '\u53cb\u60c5\u94fe\u63a5', 'verbose_name_plural': '\u53cb\u60c5\u94fe\u63a5'},
        ),
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default=b'avatar/default.jpg', upload_to=b'avatar/%Y/%d', max_length=200, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\x9b\xbe\xe5\x83\x8f'),
        ),
    ]
