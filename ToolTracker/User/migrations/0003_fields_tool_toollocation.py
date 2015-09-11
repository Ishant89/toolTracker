# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('User', '0002_auto_20150910_2322'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fields',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('description', models.TextField()),
                ('type', models.CharField(max_length=500, verbose_name=b'Type of argument', choices=[(b'FT', b'File Type'), (b'INT', b'Integer Type'), (b'FLT', b'Float Type'), (b'STR', b'String Type')])),
                ('env', models.CharField(help_text=b'Specify env var as name=$value', max_length=100000, verbose_name=b'Env variables')),
            ],
        ),
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('description', models.TextField()),
                ('usage', models.TextField()),
                ('file', models.FileField(upload_to=b'', verbose_name=b'Upload the file of the tool')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ToolLocation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('location', models.TextField()),
                ('tool', models.ForeignKey(to='User.Tool')),
            ],
        ),
    ]
