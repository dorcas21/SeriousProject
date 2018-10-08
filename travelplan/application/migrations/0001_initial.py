# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Travel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('travel_name', models.CharField(max_length=50)),
                ('travel_meeting', models.CharField(max_length=50)),
                ('travel_venue', models.CharField(max_length=50)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('travel_days', models.IntegerField()),
                ('user', models.CharField(max_length=30, null=True)),
                ('status', models.CharField(default=0, max_length=100, choices=[(0, b'pending'), (1, b'confirmed')])),
                ('status_report', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=12)),
                ('last_name', models.CharField(max_length=12)),
                ('email', models.CharField(max_length=30)),
                ('password', models.TextField()),
                ('username', models.CharField(max_length=20)),
                ('phone_number', models.CharField(max_length=12)),
                ('user_level', models.CharField(default=3, help_text=b'1 == admin, 2 == finance office, 3 == public', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('travel', models.OneToOneField(primary_key=True, serialize=False, to='application.Travel')),
                ('budget_line', models.IntegerField()),
                ('budget_cost', models.IntegerField()),
                ('additional_cost', models.IntegerField()),
                ('budget_spent', models.IntegerField(null=True)),
                ('budget_quarter', models.IntegerField(null=True)),
                ('budget', models.IntegerField()),
                ('budget_balance', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Details',
            fields=[
                ('travel', models.OneToOneField(primary_key=True, serialize=False, to='application.Travel')),
                ('justification', models.TextField()),
                ('project_details', models.CharField(max_length=30)),
                ('region', models.CharField(max_length=30)),
                ('communication_details', models.TextField()),
                ('date', models.DateField()),
                ('department', models.CharField(max_length=30)),
                ('report', models.TextField()),
            ],
        ),
    ]
