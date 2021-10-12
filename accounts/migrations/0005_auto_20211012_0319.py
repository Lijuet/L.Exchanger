# Generated by Django 3.2.6 on 2021-10-12 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_user_main_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='goal',
            field=models.CharField(choices=[('test', 'Test'), ('conv', 'Conversation')], default='conv', max_length=4, verbose_name='Goal'),
        ),
        migrations.AddField(
            model_name='user',
            name='study_language',
            field=models.CharField(choices=[('ko', 'Korean'), ('en', 'English')], default='en', max_length=3, verbose_name='Study Language'),
        ),
        migrations.AlterField(
            model_name='user',
            name='main_language',
            field=models.CharField(choices=[('ko', 'Korean'), ('en', 'English')], default='ko', max_length=3, verbose_name='Main Language'),
        ),
    ]
