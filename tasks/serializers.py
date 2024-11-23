from .models import Tasks
from rest_framework import serializers


class TasksSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ['id','name','description','status','priority','due_date','category','user']


