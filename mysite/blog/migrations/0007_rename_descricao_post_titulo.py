# Generated by Django 4.1.7 on 2023-03-30 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_rename_titulo_post_descricao'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='descricao',
            new_name='titulo',
        ),
    ]
