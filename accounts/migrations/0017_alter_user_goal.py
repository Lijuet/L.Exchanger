# Generated by Django 3.2.6 on 2021-10-05 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_auto_20211005_0556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='goal',
            field=models.CharField(choices=[('test', 'Test'), ('conv', 'Conversation')], default='conv', max_length=4, verbose_name='Goal'),
        ),
    ]
