# Generated by Django 5.1.3 on 2024-11-23 04:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taskWriter', '0005_remove_filemodel_image_filemodel_file_filemodel_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
        migrations.AlterModelOptions(
            name='filemodel',
            options={'verbose_name': 'media', 'verbose_name_plural': 'medias'},
        ),
        migrations.AlterModelTable(
            name='category',
            table='categories',
        ),
        migrations.AlterModelTable(
            name='filemodel',
            table='media',
        ),
    ]
