from rest_framework import serializers
from .models import Category,FileModel

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name']
        
class FilesSerializer(serializers.ModelSerializer):
    file = serializers.FileField()
    class Meta:
        model = FileModel
        fields = ['id','name','file']      
        
        