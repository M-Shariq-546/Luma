# Generated by Django 5.0 on 2023-12-28 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0002_remove_group_is_invited_remove_group_is_member_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
