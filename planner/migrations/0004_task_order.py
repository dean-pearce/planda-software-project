# Generated by Django 2.2.5 on 2019-12-15 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0003_project_private'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='order',
            field=models.IntegerField(default=1),
        ),
    ]
