# Generated by Django 4.1.2 on 2022-11-05 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employe', '0003_feedback_userprofile_employe_role_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='last_logout',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
