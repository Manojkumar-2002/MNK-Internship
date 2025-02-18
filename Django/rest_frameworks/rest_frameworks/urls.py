
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/",include('students.urls')),
    path("api/v1/employees/",include('employees.urls')),
    path("api/v1/blog-app/",include('blogs.urls')),
]
