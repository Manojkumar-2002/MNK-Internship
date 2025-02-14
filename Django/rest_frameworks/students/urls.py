from . import  views
from django.urls import path

urlpatterns = [
    path("students/",views.all_students,name="index"),
    path("students/<int:id>/",views.student,name="index"),
]
