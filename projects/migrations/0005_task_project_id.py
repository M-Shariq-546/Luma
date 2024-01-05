# Generated by Django 5.0 on 2024-01-04 12:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_remove_task_project_id_alter_project_tasks'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='project_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.project'),
        ),
    ]