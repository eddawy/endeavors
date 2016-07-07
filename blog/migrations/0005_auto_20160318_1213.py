# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-18 12:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20160302_0540'),
    ]

    operations = [
        migrations.CreateModel(
            name='TopicVisit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=40)),
                ('session_key', models.CharField(max_length=40)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topic_visits', to='blog.Topic')),
            ],
        ),
        migrations.RemoveField(
            model_name='topicview',
            name='topic',
        ),
        migrations.DeleteModel(
            name='TopicView',
        ),
    ]
