from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TasksSerializers
from .models import Tasks
from rest_framework import status
from .filters import TaskFilter
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

@api_view(['GET','POST'])
def getTasks(request):
    if request.method == 'GET':
         tasks = Tasks.objects.all()
         serializer = TasksSerializers(tasks,many=True)  
         return Response(serializer.data)
    elif request.method == 'POST':
        task = TasksSerializers(data=request.data)
        if task.is_valid():
            task.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(task.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PATCH','DELETE'])
def getById(request,id):
    
    try:
        task = Tasks.objects.get(pk=id)
    except task.DoesNotExists:
        return Response(status=status.HTTP_404_NOT_FOUND) 
    
    if request.method == 'GET':
        serializer = TasksSerializers(task)
        return Response(serializer.data)
    elif request.method == 'PATCH':
        serializer = TasksSerializers(task , data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_200_OK)
