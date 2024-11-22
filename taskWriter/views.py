from rest_framework.response import Response
from .models import Category

from .serializers import CategorySerializer
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET','POST']) 
def  getAllCategories(request):
    if request.method == 'GET':
            categories = Category.objects.all()
            serializer = CategorySerializer(categories , many=True)
            return Response(serializer.data)
    if request.method == 'POST':
            category = CategorySerializer(data=request.data)
            if category.is_valid():
                category.save()
                return Response(status=status.HTTP_201_CREATED)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PATCH','DELETE'])
def getbyId(request,id):
    
    try:
        category = Category.objects.get(pk=id)
    except category.DoesNotExists:
        return Response(status=status.HTTP_404_NOT_FOUND)    
    
    if request.method == 'GET':
        serializer = CategorySerializer(category)
        return Response(serializer.data)
    elif request.method == 'PATCH':
        serializer = CategorySerializer(category , data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        category.delete()
        return Response(status=status.HTTP_200_OK)







        
       
        
    