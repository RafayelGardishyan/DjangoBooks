# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-15 17:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20171013_1701'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubmitBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submitter', models.CharField(max_length=200, verbose_name='Your name')),
                ('submitteremail', models.EmailField(max_length=200, verbose_name='Your E-mail')),
                ('booktitle', models.CharField(max_length=200, verbose_name='Book title')),
                ('bookauthor', models.CharField(max_length=200, verbose_name='Book author')),
                ('bookdescription', models.TextField(verbose_name='Book Description')),
                ('date', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Submit a book',
            },
        ),
    ]
