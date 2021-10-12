# Generated by Django 3.2.6 on 2021-10-05 05:59

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0003_auto_20211005_0554'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='study_languages',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(choices=[('en', 'English'), ('ko', 'Korean')], max_length=3), null=True, size=None),
        ),
    ]
