# Generated by Django 3.2.6 on 2021-10-08 04:16

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0004_group_study_languages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='study_languages',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(choices=[('ko', 'Korean'), ('en', 'English')], max_length=3), null=True, size=None),
        ),
    ]
