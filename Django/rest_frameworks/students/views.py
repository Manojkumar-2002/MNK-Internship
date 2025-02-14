
from .serializers import StudentSerializer
from .models import Students
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Students
# Create your views here.

@api_view(['GET','POST'])
def all_students(request):
    if request.method == "GET":
        
        students = Students.objects.all()
        serializer = StudentSerializer(students,many=True)
        print("serialized",serializer)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    elif request.method == "POST":
        serializer = StudentSerializer(data = request.data)
        if not serializer.is_valid():
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
        
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    
@api_view(['GET','PUT','DELETE'])
def student(request,id):
    try:
        print(type(id))
        student = Students.objects.get(id=id)
    except Students.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        serializer = StudentSerializer(student,request.data)
        if not serializer.is_valid():
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    

        