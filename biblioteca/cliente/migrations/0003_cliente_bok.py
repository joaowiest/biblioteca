# Generated by Django 3.0.7 on 2020-06-10 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0002_cliente_senha_dois'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='bok',
            field=models.CharField(default=-1, max_length=100),
            preserve_default=False,
        ),
    ]