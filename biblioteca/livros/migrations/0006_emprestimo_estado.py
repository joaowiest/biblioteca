# Generated by Django 3.0.7 on 2020-06-17 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0005_emprestimo'),
    ]

    operations = [
        migrations.AddField(
            model_name='emprestimo',
            name='estado',
            field=models.CharField(default=0, max_length=15),
            preserve_default=False,
        ),
    ]
