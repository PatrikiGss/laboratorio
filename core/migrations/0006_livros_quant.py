# Generated by Django 5.2.3 on 2025-06-18 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_remove_livros_genero_livros_genero'),
    ]

    operations = [
        migrations.AddField(
            model_name='livros',
            name='quant',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
