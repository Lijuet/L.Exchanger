# Generated by Django 3.2.6 on 2021-10-03 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_alter_user_goal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='goal',
            field=models.CharField(choices=[('conv', 'Conversation'), ('test', 'Test')], default='conv', max_length=4, verbose_name='Goal'),
        ),
        migrations.AlterField(
            model_name='user',
            name='main_language',
            field=models.CharField(choices=[('en', 'English'), ('ko', 'Korean')], default='ko', max_length=3, verbose_name='Main Language'),
        ),
        migrations.AlterField(
            model_name='user',
            name='study_language',
            field=models.CharField(choices=[('en', 'English'), ('ko', 'Korean')], default='en', max_length=3, verbose_name='Study Language'),
        ),
    ]
