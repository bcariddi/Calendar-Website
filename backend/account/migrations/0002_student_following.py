# Generated by Django 2.2.7 on 2019-12-30 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0001_initial'),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='following',
            field=models.ManyToManyField(to='organization.Organization'),
        ),
    ]