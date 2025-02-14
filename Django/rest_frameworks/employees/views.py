
from .serializers import EmployeeSerializer
from .models import Employees
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404


class AllEmployee(APIView):
    
    def get(self, request):
        employee = Employees.objects.all()
        serializer = EmployeeSerializer(employee,many=True)
        print("serialized",serializer)
        return Response(serializer.data,status=status.HTTP_200_OK)
        
    def post(self, request):
        serializer = EmployeeSerializer(data = request.data)
        if not serializer.is_valid():
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    
    
class Employee(APIView):
    
    def get_data(self, id):
        try:
            return Employees.objects.get(id=id)
        except Employees.DoesNotExist:
            raise Http404
        
    def get(self, request, id):
        print(id)
        employee = self.get_data(id)
        print(employee)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def put(self, request, id):
        employee = self.get_data(id)
        serializer = EmployeeSerializer(employee,data = request.data)
        if not serializer.is_valid():
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def delete(self, request, id):
        employee = self.get_data(id)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)