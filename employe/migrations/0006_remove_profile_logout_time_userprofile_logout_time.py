# Generated by Django 4.1.2 on 2022-11-11 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employe', '0005_remove_userprofile_last_logout_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='logout_time',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='logout_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]