# Generated by Django 4.0.6 on 2022-07-08 12:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CST_cms', '0010_post_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='user',
        ),
    ]
