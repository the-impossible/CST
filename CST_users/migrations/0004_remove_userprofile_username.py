# Generated by Django 4.0.6 on 2022-07-08 10:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CST_users', '0003_remove_userprofile_email_remove_userprofile_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='username',
        ),
    ]
