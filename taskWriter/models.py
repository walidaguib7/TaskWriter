from django.db import models
from django.utils.translation import gettext_lazy as _

def upload_to(instance , filename):
    return '/media/{filename}'.format(filename=filename)

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'categories'
        verbose_name = 'category'
        verbose_name_plural = 'categories'

class FileModel(models.Model):
    name = models.CharField(max_length=255,default="Untitled")
    file = models.FileField(upload_to='media/', default='/media/image.png')
    class Meta:
        db_table = 'media'
        verbose_name = 'media'
        verbose_name_plural = 'medias'