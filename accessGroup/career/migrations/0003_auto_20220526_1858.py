# Generated by Django 3.1.3 on 2022-05-26 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('career', '0002_user_age'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='CarrerUsers',
        ),
    ]
