# Generated by Django 3.1.3 on 2022-05-26 10:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('career', '0003_auto_20220526_1858'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carrerusers',
            name='profile_pic',
        ),
    ]
