# Generated by Django 5.1.3 on 2024-11-23 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskWriter', '0004_alter_filemodel_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='filemodel',
            name='Image',
        ),
        migrations.AddField(
            model_name='filemodel',
            name='file',
            field=models.FileField(default='/media/image.png', upload_to='media/'),
        ),
        migrations.AddField(
            model_name='filemodel',
            name='name',
            field=models.CharField(default='Untitled', max_length=255),
        ),
    ]
