# Generated by Django 5.0 on 2023-12-28 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0003_members_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='is_invited',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='members',
            name='is_member',
            field=models.BooleanField(default=False),
        ),
    ]
