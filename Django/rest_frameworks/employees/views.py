
from .serializers import EmployeeSerializer
from .models import Employees
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import mixins, generics, viewsets
from .pagination import CustomPageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from .filter import EmployeeFilter


# class based views
# -----------------

# class AllEmployee(APIView):
    
#     def get(self, request):
#         employee = Employees.objects.all()
#         serializer = EmployeeSerializer(employee,many=True)
#         print("serialized",serializer)
#         return Response(serializer.data,status=status.HTTP_200_OK)
        
#     def post(self, request):
#         serializer = EmployeeSerializer(data = request.data)
#         if not serializer.is_valid():
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#         serializer.save()
#         return Response(serializer.data,status=status.HTTP_201_CREATED)
    
    
# class Employee(APIView):
    
#     def get_data(self, id):
#         try:
#             return Employees.objects.get(id=id)
#         except Employees.DoesNotExist:
#             raise Http404
        
#     def get(self, request, id):
#         print(id)
#         employee = self.get_data(id)
#         print(employee)
#         serializer = EmployeeSerializer(employee)
#         return Response(serializer.data,status=status.HTTP_200_OK)
    
#     def put(self, request, id):
#         employee = self.get_data(id)
#         serializer = EmployeeSerializer(employee,data = request.data)
#         if not serializer.is_valid():
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#         serializer.save()
#         return Response(serializer.data,status=status.HTTP_200_OK)
    
#     def delete(self, request, id):
#         employee = self.get_data(id)
#         employee.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)



# Mixins based views
# -----------------


# class AllEmployee(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset = Employees.objects.all()
#     serializer_class = EmployeeSerializer
    
    
#     def get(self, request):
#         return self.list(request)
    
#     def post(self, request):
#         return self.create(request)
    

# class Employee(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
#     queryset = Employees.objects.all()
#     serializer_class = EmployeeSerializer
    
    
#     def get(self, request, pk):
#         return self.retrieve(request,pk)
    
#     def put(self, request, pk):
#         return self.update(request,pk)
    
#     def delete(self, request, pk):
#         return self.destroy(request,pk)
    
    
# Generic API based views
# -----------------


# class AllEmployee(generics.ListCreateAPIView):
#     queryset = Employees.objects.all()
#     serializer_class = EmployeeSerializer
    


# class Employee(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Employees.objects.all()
#     serializer_class = EmployeeSerializer
#     lookup_field = 'id'

# class Employee(viewsets.ViewSet):
#     def list(self, request):
#         queryset = Employees.objects.all()
#         serializer = EmployeeSerializer(queryset,many=True)
#         return Response(serializer.data,status=status.HTTP_200_OK)
        
#     def create(self, request):
#         serializer = EmployeeSerializer(data = request.data)
#         if not serializer.is_valid():
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#         serializer.save()
#         return Response(serializer.data,status=status.HTTP_201_CREATED)
    
#     def get_data(self, id):
#         try:
#             return Employees.objects.get(id=id)
#         except Employees.DoesNotExist:
#             raise Http404

#     def retrieve(self, request, pk):
#         employee = self.get_data(pk)
#         serializer = EmployeeSerializer(employee)
#         return Response(serializer.data,status=status.HTTP_200_OK)
    
#     def update(self, request, pk):
#         employee = self.get_data(pk)
#         serializer = EmployeeSerializer(employee,data = request.data)
#         if not serializer.is_valid():
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#         serializer.save()
#         return Response(serializer.data,status=status.HTTP_200_OK)
    
#     def destroy(self, request, pk):
#         employee = self.get_data(pk)
#         employee.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)



class Employee(viewsets.ModelViewSet):
    queryset = Employees.objects.all()
    serializer_class = EmployeeSerializer
    pagination_class = CustomPageNumberPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = EmployeeFilter
    
    
