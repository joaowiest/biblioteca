# Generated by Django 3.0.7 on 2020-06-10 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0002_livro_quntia_livro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livro',
            name='quntia_livro',
            field=models.IntegerField(),
        ),
    ]