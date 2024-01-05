# Generated by Django 5.0 on 2024-01-04 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_project_is_active_task_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='project_id',
        ),
        migrations.AlterField(
            model_name='project',
            name='tasks',
            field=models.ManyToManyField(to='projects.task'),
        ),
    ]
