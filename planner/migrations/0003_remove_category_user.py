# Generated by Django 2.2.3 on 2019-11-02 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0002_auto_20191102_0818'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='user',
        ),
    ]