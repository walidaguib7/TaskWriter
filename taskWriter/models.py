from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

class FileModel(models.Model):
    path = models.CharField(max_length=200)