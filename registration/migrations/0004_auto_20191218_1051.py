# Generated by Django 2.2.5 on 2019-12-18 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_delete_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(upload_to='profile_image'),
        ),
    ]