# Generated by Django 3.0.7 on 2020-06-16 18:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0005_auto_20200616_1504'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Cliente',
        ),
    ]
