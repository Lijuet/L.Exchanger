# Generated by Django 3.2.6 on 2021-10-03 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='group_name',
            field=models.CharField(default='study group', max_length=30),
        ),
    ]
