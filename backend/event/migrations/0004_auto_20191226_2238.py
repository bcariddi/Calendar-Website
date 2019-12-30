# Generated by Django 2.2.7 on 2019-12-27 04:38

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_auto_20191226_2205'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='eventDescription',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='event',
            name='eventTags',
        ),
        migrations.AddField(
            model_name='event',
            name='tags',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), default=list, size=None),
        ),
    ]