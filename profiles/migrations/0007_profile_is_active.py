# Generated by Django 5.0 on 2024-01-01 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_profile_email_alter_profile_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_active',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
