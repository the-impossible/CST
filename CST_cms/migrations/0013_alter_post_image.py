# Generated by Django 4.0.6 on 2022-07-09 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CST_cms', '0012_post_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
