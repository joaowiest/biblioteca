# Generated by Django 3.0.7 on 2020-06-10 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='senha_dois',
            field=models.CharField(default=1, max_length=9),
            preserve_default=False,
        ),
    ]
