# Generated by Django 5.0 on 2024-01-02 10:57

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0006_members_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='group_id',
            field=models.UUIDField(default=uuid.uuid4, unique=True),
        ),
    ]