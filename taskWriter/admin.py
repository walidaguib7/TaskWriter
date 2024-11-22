from django.contrib import admin

from .models import Category, FileModel

admin.site.register([Category , FileModel])